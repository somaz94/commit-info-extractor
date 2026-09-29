import os
from unittest.mock import patch

import pytest

from app.git_client import (
    GIT_SAFE_DIRECTORIES,
    add_config_env,
    configure_git,
    fetch_commit_messages,
)
from app.logger import ActionError


@pytest.fixture
def git_env():
    with patch.dict(os.environ):
        for key in [k for k in os.environ if k.startswith("GIT_CONFIG_")]:
            del os.environ[key]
        yield os.environ


def env_config(env):
    return [
        (env[f"GIT_CONFIG_KEY_{i}"], env[f"GIT_CONFIG_VALUE_{i}"])
        for i in range(int(env["GIT_CONFIG_COUNT"]))
    ]


class TestAddConfigEnv:
    def test_first_entry(self, git_env):
        add_config_env("safe.directory", "/repo")
        assert env_config(git_env) == [("safe.directory", "/repo")]

    def test_appends_after_existing_entries(self, git_env):
        git_env.update(
            GIT_CONFIG_COUNT="1",
            GIT_CONFIG_KEY_0="core.pager",
            GIT_CONFIG_VALUE_0="cat",
        )
        add_config_env("safe.directory", "/repo")
        assert env_config(git_env) == [
            ("core.pager", "cat"),
            ("safe.directory", "/repo"),
        ]

    @pytest.mark.parametrize("count", ["abc", "-1"])
    def test_invalid_count(self, git_env, count):
        git_env["GIT_CONFIG_COUNT"] = count
        with pytest.raises(ValueError):
            add_config_env("safe.directory", "/repo")


class TestConfigureGit:
    @patch("app.git_client.subprocess.run")
    def test_sets_process_env_without_running_git(self, mock_run, git_env):
        configure_git()
        mock_run.assert_not_called()
        assert env_config(git_env) == [
            ("safe.directory", directory) for directory in GIT_SAFE_DIRECTORIES
        ]


class TestFetchCommitMessages:
    def test_no_git_dir_fails(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with pytest.raises(ActionError, match="actions/checkout"):
            fetch_commit_messages(10, True, 5)

    @patch("app.git_client.subprocess.run")
    def test_git_file_counts_as_repository(self, mock_run, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        (tmp_path / ".git").write_text("gitdir: /elsewhere/.git/worktrees/wt\n")
        mock_run.return_value.stdout = "feat: login\n"
        assert fetch_commit_messages(5, True, 10) == "feat: login\n"

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.exists", return_value=True)
    def test_pretty_format(self, mock_exists, mock_run):
        mock_run.return_value.stdout = "feat: add login\n"
        fetch_commit_messages(5, True, 10)
        cmd = mock_run.call_args[0][0]
        assert "--pretty=%B" in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.exists", return_value=True)
    def test_no_pretty_format(self, mock_exists, mock_run):
        mock_run.return_value.stdout = "commit abc\n"
        fetch_commit_messages(5, False, 10)
        cmd = mock_run.call_args[0][0]
        assert "--pretty=%B" not in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.exists", return_value=True)
    def test_commit_range(self, mock_exists, mock_run):
        mock_run.return_value.stdout = "feat: login\n"
        fetch_commit_messages(5, True, 10, commit_range="HEAD~3..HEAD")
        cmd = mock_run.call_args[0][0]
        assert "HEAD~3..HEAD" in cmd
        assert "-5" not in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.exists", return_value=True)
    def test_no_commit_range_uses_limit(self, mock_exists, mock_run):
        mock_run.return_value.stdout = "feat: login\n"
        fetch_commit_messages(5, True, 10)
        cmd = mock_run.call_args[0][0]
        assert "-5" in cmd

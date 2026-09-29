import subprocess
from unittest.mock import patch

import pytest

from app.git_client import GIT_SAFE_DIRECTORIES, configure_git, fetch_commit_messages
from app.logger import ActionError


class TestConfigureGit:
    @patch("app.git_client.subprocess.run")
    def test_configures_safe_directories(self, mock_run):
        configure_git()
        commands = [call.args[0] for call in mock_run.call_args_list]
        assert commands == [
            ["git", "config", "--global", "--add", "safe.directory", directory]
            for directory in GIT_SAFE_DIRECTORIES
        ]

    @patch(
        "app.git_client.subprocess.run",
        side_effect=subprocess.CalledProcessError(1, "git"),
    )
    def test_continues_on_error(self, mock_run):
        # Should not raise even if subprocess fails
        configure_git()


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

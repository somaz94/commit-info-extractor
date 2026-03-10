import os
import subprocess
from unittest.mock import patch

import pytest

from app.git_client import fetch_commit_messages, configure_git


class TestConfigureGit:
    @patch("app.git_client.subprocess.run")
    def test_configures_safe_directories(self, mock_run):
        configure_git()
        assert mock_run.call_count == 2

    @patch("app.git_client.subprocess.run", side_effect=subprocess.CalledProcessError(1, "git"))
    def test_continues_on_error(self, mock_run):
        # Should not raise even if subprocess fails
        configure_git()


class TestFetchCommitMessages:
    def test_no_git_dir(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = fetch_commit_messages(10, "true", 5)
        assert result == "No commit messages available."

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.isdir", return_value=True)
    def test_pretty_format(self, mock_isdir, mock_run):
        mock_run.return_value.stdout = "feat: add login\n"
        fetch_commit_messages(5, "true", 10)
        cmd = mock_run.call_args[0][0]
        assert "--pretty=%B" in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.isdir", return_value=True)
    def test_no_pretty_format(self, mock_isdir, mock_run):
        mock_run.return_value.stdout = "commit abc\n"
        fetch_commit_messages(5, "false", 10)
        cmd = mock_run.call_args[0][0]
        assert "--pretty=%B" not in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.isdir", return_value=True)
    def test_commit_range(self, mock_isdir, mock_run):
        mock_run.return_value.stdout = "feat: login\n"
        fetch_commit_messages(5, "true", 10, commit_range="HEAD~3..HEAD")
        cmd = mock_run.call_args[0][0]
        assert "HEAD~3..HEAD" in cmd
        assert "-5" not in cmd

    @patch("app.git_client.subprocess.run")
    @patch("app.git_client.os.path.isdir", return_value=True)
    def test_no_commit_range_uses_limit(self, mock_isdir, mock_run):
        mock_run.return_value.stdout = "feat: login\n"
        fetch_commit_messages(5, "true", 10)
        cmd = mock_run.call_args[0][0]
        assert "-5" in cmd

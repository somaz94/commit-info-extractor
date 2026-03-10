from unittest.mock import patch

import pytest

from app.main import run


class TestRun:
    def test_invalid_config_exits(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_LIMIT", "abc")
        with pytest.raises(SystemExit):
            run()

    def test_invalid_validation_exits(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_LIMIT", "0")
        with pytest.raises(SystemExit):
            run()

    @patch("app.main.configure_git")
    @patch("app.main.fetch_commit_messages", return_value="feat: login\nfix: bug")
    @patch("app.main.set_output_variables")
    def test_full_flow_no_extract(
        self, mock_output, mock_fetch, mock_git, default_env
    ):
        run()
        mock_git.assert_called_once()
        mock_fetch.assert_called_once()
        mock_output.assert_called_once()
        # Without extract_command, raw commit messages passed through
        call_args = mock_output.call_args[0]
        assert "feat: login" in call_args[0]

    @patch("app.main.configure_git")
    @patch("app.main.fetch_commit_messages", return_value="feat: login\nfix: bug")
    @patch("app.main.set_output_variables")
    def test_full_flow_with_extract(
        self, mock_output, mock_fetch, mock_git, default_env, monkeypatch
    ):
        monkeypatch.setenv("INPUT_EXTRACT_COMMAND", "grep -oE 'feat|fix'")
        run()
        call_args = mock_output.call_args[0]
        assert "feat" in call_args[0]

    @patch("app.main.configure_git")
    @patch("app.main.fetch_commit_messages", return_value="feat: login")
    @patch("app.main.set_output_variables")
    def test_json_format(
        self, mock_output, mock_fetch, mock_git, default_env, monkeypatch
    ):
        monkeypatch.setenv("INPUT_OUTPUT_FORMAT", "json")
        monkeypatch.setenv("INPUT_EXTRACT_COMMAND", "grep -oE 'feat'")
        run()
        call_args = mock_output.call_args[0]
        assert "[" in call_args[0]  # JSON array

    @patch("app.main.configure_git")
    @patch("app.main.fetch_commit_messages", return_value="feat: login\nfix: bug")
    @patch("app.main.set_output_variables")
    def test_full_flow_with_pattern(
        self, mock_output, mock_fetch, mock_git, default_env, monkeypatch
    ):
        monkeypatch.setenv("INPUT_EXTRACT_PATTERN", r"(feat|fix)")
        run()
        call_args = mock_output.call_args[0]
        assert "feat" in call_args[0]
        assert "fix" in call_args[0]
        # match_count should be passed as 3rd arg
        assert call_args[2] == 2

    @patch("app.main.configure_git")
    @patch("app.main.fetch_commit_messages", return_value="feat: login")
    @patch("app.main.set_output_variables")
    def test_commit_range_passed(
        self, mock_output, mock_fetch, mock_git, default_env, monkeypatch
    ):
        monkeypatch.setenv("INPUT_COMMIT_RANGE", "HEAD~3..HEAD")
        run()
        fetch_kwargs = mock_fetch.call_args
        # commit_range should be passed to fetch_commit_messages
        assert "HEAD~3..HEAD" in str(fetch_kwargs)

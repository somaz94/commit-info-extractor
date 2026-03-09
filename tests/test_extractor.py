import pytest

from app.extractor import extract_info, _run_extract_command


class TestRunExtractCommand:
    def test_basic_grep(self):
        result = _run_extract_command("feat: login\nfix: bug\nfeat: signup", "grep -oE 'feat'", 10)
        assert "feat" in result

    def test_no_match_returns_empty(self):
        result = _run_extract_command("hello world", "grep -oE 'nonexistent'", 10)
        assert result == ""

    def test_deduplicates_results(self):
        result = _run_extract_command("feat\nfeat\nfeat", "grep -oE 'feat'", 10)
        assert result == "feat"

    def test_sorts_results(self):
        result = _run_extract_command("cherry\napple\nbanana", "cat", 10)
        assert result == "apple\nbanana\ncherry"

    def test_timeout(self):
        with pytest.raises(SystemExit):
            _run_extract_command("test", "sleep 10", 1)


class TestExtractInfo:
    def test_no_command_returns_messages(self):
        result = extract_info("commit messages", None, "false", 10)
        assert result == "commit messages"

    def test_empty_command_returns_messages(self):
        result = extract_info("commit messages", "", "false", 10)
        assert result == "commit messages"

    def test_with_extract_command(self):
        result = extract_info("feat: login\nfix: bug", "grep -oE 'feat|fix'", "false", 10)
        assert "feat" in result
        assert "fix" in result

    def test_fail_on_empty_true_exits(self):
        with pytest.raises(SystemExit):
            extract_info("hello", "grep -oE 'nonexistent'", "true", 10)

    def test_fail_on_empty_false_returns_empty(self):
        result = extract_info("hello", "grep -oE 'nonexistent'", "false", 10)
        assert result == ""

import pytest

from app.extractor import extract_info, _run_extract_command, _run_extract_pattern


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


class TestRunExtractPattern:
    def test_basic_pattern(self):
        result = _run_extract_pattern("feat: login\nfix: bug\nfeat: signup", r"feat")
        assert result == "feat"

    def test_no_match_returns_empty(self):
        result = _run_extract_pattern("hello world", r"nonexistent")
        assert result == ""

    def test_captures_groups(self):
        result = _run_extract_pattern("env:prod\nenv:staging\nenv:prod", r"env:(\w+)")
        assert "prod" in result
        assert "staging" in result

    def test_deduplicates_and_sorts(self):
        result = _run_extract_pattern("apple cherry apple banana cherry", r"\b(apple|banana|cherry)\b")
        assert result == "apple\nbanana\ncherry"

    def test_invalid_regex(self):
        with pytest.raises(SystemExit):
            _run_extract_pattern("test", r"[invalid")


class TestExtractInfo:
    def test_no_command_returns_messages(self):
        result, count = extract_info("commit messages", None, None, "false", 10)
        assert result == "commit messages"
        assert count == 1

    def test_empty_command_returns_messages(self):
        result, count = extract_info("line1\nline2", None, None, "false", 10)
        assert result == "line1\nline2"
        assert count == 2

    def test_with_extract_command(self):
        result, count = extract_info("feat: login\nfix: bug", "grep -oE 'feat|fix'", None, "false", 10)
        assert "feat" in result
        assert "fix" in result
        assert count == 2

    def test_with_extract_pattern(self):
        result, count = extract_info("feat: login\nfix: bug", None, r"(feat|fix)", "false", 10)
        assert "feat" in result
        assert "fix" in result
        assert count == 2

    def test_fail_on_empty_true_with_pattern(self):
        with pytest.raises(SystemExit):
            extract_info("hello", None, r"nonexistent", "true", 10)

    def test_fail_on_empty_false_returns_empty(self):
        result, count = extract_info("hello", "grep -oE 'nonexistent'", None, "false", 10)
        assert result == ""
        assert count == 0

    def test_match_count_multiple(self):
        result, count = extract_info("feat: a\nfeat: b\nfix: c", None, r"(feat|fix)", "false", 10)
        assert count == 2

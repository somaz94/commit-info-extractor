import pytest

from app.config import AppConfig, VALID_OUTPUT_FORMATS


class TestAppConfig:
    def test_from_env_defaults(self, clean_env):
        config = AppConfig.from_env()
        assert config.commit_limit == 10
        assert config.timeout == 30
        assert config.pretty == "false"
        assert config.key_variable == "ENVIRONMENT"
        assert config.extract_command == ""
        assert config.extract_pattern == ""
        assert config.fail_on_empty == "false"
        assert config.output_format == "text"
        assert config.commit_range == ""
        assert config.debug is False

    def test_from_env_custom(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_LIMIT", "20")
        monkeypatch.setenv("INPUT_TIMEOUT", "60")
        monkeypatch.setenv("INPUT_PRETTY", "true")
        monkeypatch.setenv("INPUT_KEY_VARIABLE", "DEPLOY_ENV")
        monkeypatch.setenv("INPUT_EXTRACT_COMMAND", "grep -oE 'env:\\w+'")
        monkeypatch.setenv("INPUT_FAIL_ON_EMPTY", "true")
        monkeypatch.setenv("INPUT_OUTPUT_FORMAT", "json")
        monkeypatch.setenv("INPUT_DEBUG", "true")

        config = AppConfig.from_env()
        assert config.commit_limit == 20
        assert config.timeout == 60
        assert config.pretty == "true"
        assert config.key_variable == "DEPLOY_ENV"
        assert config.extract_command == "grep -oE 'env:\\w+'"
        assert config.fail_on_empty == "true"
        assert config.output_format == "json"
        assert config.debug is True

    def test_from_env_invalid_commit_limit(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_LIMIT", "abc")
        with pytest.raises(ValueError, match="Invalid numeric input"):
            AppConfig.from_env()

    def test_from_env_invalid_timeout(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_TIMEOUT", "xyz")
        with pytest.raises(ValueError, match="Invalid numeric input"):
            AppConfig.from_env()

    def test_validate_success(self, clean_env):
        config = AppConfig.from_env()
        config.validate()  # should not raise

    def test_validate_commit_limit_zero(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_LIMIT", "0")
        config = AppConfig.from_env()
        with pytest.raises(ValueError, match="commit_limit must be greater than 0"):
            config.validate()

    def test_validate_negative_timeout(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_TIMEOUT", "-5")
        config = AppConfig.from_env()
        with pytest.raises(ValueError, match="timeout must be greater than 0"):
            config.validate()

    def test_validate_invalid_output_format(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_OUTPUT_FORMAT", "xml")
        config = AppConfig.from_env()
        with pytest.raises(ValueError, match="Invalid output_format"):
            config.validate()

    def test_validate_mutual_exclusion(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_EXTRACT_COMMAND", "grep -oE 'feat'")
        monkeypatch.setenv("INPUT_EXTRACT_PATTERN", "feat")
        config = AppConfig.from_env()
        with pytest.raises(ValueError, match="Cannot use both"):
            config.validate()

    def test_from_env_extract_pattern(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_EXTRACT_PATTERN", r"feat:\s+\w+")
        config = AppConfig.from_env()
        assert config.extract_pattern == r"feat:\s+\w+"

    def test_from_env_commit_range(self, clean_env, monkeypatch):
        monkeypatch.setenv("INPUT_COMMIT_RANGE", "HEAD~5..HEAD")
        config = AppConfig.from_env()
        assert config.commit_range == "HEAD~5..HEAD"

    def test_valid_output_formats(self):
        assert VALID_OUTPUT_FORMATS == ("text", "json", "csv")

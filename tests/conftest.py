import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def clean_env(monkeypatch):
    """Unset INPUT_*, plus GITHUB_ENV/GITHUB_OUTPUT (always set on GitHub runners)."""
    for key in list(os.environ):
        if key.startswith("INPUT_"):
            monkeypatch.delenv(key, raising=False)
    monkeypatch.delenv("GITHUB_ENV", raising=False)
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)


@pytest.fixture
def default_env(monkeypatch, clean_env):
    """Set INPUT_* vars to the AppConfig defaults."""
    monkeypatch.setenv("INPUT_COMMIT_LIMIT", "10")
    monkeypatch.setenv("INPUT_TIMEOUT", "30")
    monkeypatch.setenv("INPUT_PRETTY", "false")
    monkeypatch.setenv("INPUT_KEY_VARIABLE", "ENVIRONMENT")
    monkeypatch.setenv("INPUT_EXTRACT_COMMAND", "")
    monkeypatch.setenv("INPUT_EXTRACT_PATTERN", "")
    monkeypatch.setenv("INPUT_FAIL_ON_EMPTY", "false")
    monkeypatch.setenv("INPUT_OUTPUT_FORMAT", "text")
    monkeypatch.setenv("INPUT_COMMIT_RANGE", "")
    monkeypatch.setenv("INPUT_DEBUG", "false")


@pytest.fixture
def github_output_files(tmp_path):
    """Create temporary GITHUB_ENV and GITHUB_OUTPUT files."""
    env_file = tmp_path / "github_env"
    output_file = tmp_path / "github_output"
    env_file.touch()
    output_file.touch()
    return str(env_file), str(output_file)

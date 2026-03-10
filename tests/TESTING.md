# Commit Info Extractor - Testing Guide

<br/>

## Quick Start (Makefile)

```bash
cd /path/to/commit-info-extractor
make venv          # Create virtualenv and install dev dependencies
make test          # Run unit tests with coverage
make test-local    # Run local integration test
make coverage      # Generate HTML coverage report
make clean         # Remove venv, cache, and build artifacts
make help          # Show all available commands
```

<br/>

## Unit Tests (pytest)

<br/>

### Manual Setup (without Makefile)
```bash
cd /path/to/commit-info-extractor
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

<br/>

### Run Tests
```bash
# All tests with coverage
python -m pytest tests/ -v --cov=app --cov-report=term-missing

# Specific test file
python -m pytest tests/test_config.py -v

# Specific test class or method
python -m pytest tests/test_formatter.py::TestFormatOutput::test_json_format -v
```

<br/>

### Test Files

| File | Description |
|------|-------------|
| `conftest.py` | Shared pytest fixtures (`clean_env`, `default_env`, `github_output_files`) |
| `test_config.py` | AppConfig dataclass (from_env, validate) |
| `test_extractor.py` | Extraction logic (command & regex pattern) |
| `test_formatter.py` | Output formatting (text/json/csv) |
| `test_git_client.py` | Git operations (configure, fetch) |
| `test_output_writer.py` | GITHUB_ENV/GITHUB_OUTPUT writing |
| `test_main.py` | End-to-end flow with mocks |

<br/>

## Integration Test

<br/>

### Run directly with Python (no Docker required)
```bash
cd /path/to/commit-info-extractor
python tests/test_local.py
```

<br/>

## Integration Test Cases

<br/>

### Test 1: Basic commit message extraction
- Extracts the last 5 commit messages
- Uses pretty format

<br/>

### Test 2: Keyword extraction with grep
- Extracts 'chore' keyword
- Uses regex patterns

<br/>

### Test 3: JSON output format
- Outputs commit messages as a JSON array

<br/>

### Test 4: CSV output format
- Outputs commit messages in CSV format

<br/>

### Test 5: Specific commit type extraction
- Extracts only 'refactor' type commits

<br/>

### Test 6: Extract using regex pattern
- Uses `extract_pattern` instead of `extract_command`
- Safer alternative (no shell execution)

<br/>

### Test 7: Commit range extraction
- Uses `commit_range` to limit commits to a specific range
- Combined with `extract_pattern`

<br/>

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| INPUT_COMMIT_LIMIT | Number of commits to extract | 10 |
| INPUT_PRETTY | Whether to use pretty format | false |
| INPUT_KEY_VARIABLE | Output variable name | ENVIRONMENT |
| INPUT_EXTRACT_COMMAND | Extraction command (e.g., grep) | - |
| INPUT_EXTRACT_PATTERN | Regex pattern for extraction (safer alternative) | - |
| INPUT_COMMIT_RANGE | Git commit range (e.g., HEAD~5..HEAD) | - |
| INPUT_FAIL_ON_EMPTY | Whether to fail on empty results | false |
| INPUT_OUTPUT_FORMAT | Output format (text/json/csv) | text |
| INPUT_DEBUG | Enable debug mode | false |
| INPUT_TIMEOUT | Command timeout in seconds | 30 |

> **Note**: `INPUT_EXTRACT_COMMAND` and `INPUT_EXTRACT_PATTERN` are mutually exclusive.

<br/>

## Debugging

If issues occur, check the following:

1. Verify it is a git repository: check for `.git` directory
2. Check commit history: `git log`
3. Test grep command: `echo "test fix" | grep -oE '\\bfix\\b'`
4. Check Python version: `python3 --version` (3.13 or higher recommended)
5. Enable debug mode: `export INPUT_DEBUG=true`

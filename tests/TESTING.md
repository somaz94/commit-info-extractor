# Commit Info Extractor - Local Testing Guide

<br/>

## How to Test

<br/>

### Run directly with Python (no Docker required)
```bash
cd /path/to/commit-info-extractor
python3 tests/test_local.py
```

<br/>

## Test Cases

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

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| INPUT_COMMIT_LIMIT | Number of commits to extract | 10 |
| INPUT_PRETTY | Whether to use pretty format | false |
| INPUT_KEY_VARIABLE | Output variable name | ENVIRONMENT |
| INPUT_EXTRACT_COMMAND | Extraction command (e.g., grep) | - |
| INPUT_FAIL_ON_EMPTY | Whether to fail on empty results | false |
| INPUT_OUTPUT_FORMAT | Output format (text/json/csv) | text |

<br/>

## Debugging

If issues occur, check the following:

1. Verify it is a git repository: check for `.git` directory
2. Check commit history: `git log`
3. Test grep command: `echo "test fix" | grep -oE '\\bfix\\b'`
4. Check Python version: `python3 --version` (3.7 or higher recommended)

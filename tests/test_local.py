#!/usr/bin/env python3
"""Full-flow run without Docker (`make test-local`); pytest collects nothing."""

import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_ENV = {
    "INPUT_COMMIT_LIMIT": "10",
    "INPUT_PRETTY": "true",
    "INPUT_KEY_VARIABLE": "ENVIRONMENT",
    "INPUT_EXTRACT_COMMAND": "",
    "INPUT_EXTRACT_PATTERN": "",
    "INPUT_FAIL_ON_EMPTY": "false",
    "INPUT_OUTPUT_FORMAT": "text",
    "INPUT_COMMIT_RANGE": "",
}

CASES = [
    ("Test 1: Basic commit message extraction", {"INPUT_COMMIT_LIMIT": "5"}),
    (
        "Test 2: Extract 'chore' keyword",
        {
            "INPUT_KEY_VARIABLE": "CHORE_KEYWORD",
            "INPUT_EXTRACT_COMMAND": "grep -oE 'chore' || true",
        },
    ),
    (
        "Test 3: JSON output format",
        {
            "INPUT_COMMIT_LIMIT": "3",
            "INPUT_KEY_VARIABLE": "COMMITS_JSON",
            "INPUT_OUTPUT_FORMAT": "json",
        },
    ),
    (
        "Test 4: CSV output format",
        {
            "INPUT_COMMIT_LIMIT": "3",
            "INPUT_KEY_VARIABLE": "COMMITS_CSV",
            "INPUT_OUTPUT_FORMAT": "csv",
        },
    ),
    (
        "Test 5: Extract 'refactor' commits",
        {
            "INPUT_KEY_VARIABLE": "REFACTOR_COMMITS",
            "INPUT_EXTRACT_COMMAND": "grep -oE 'refactor' || true",
        },
    ),
    (
        "Test 6: Extract using regex pattern (extract_pattern)",
        {
            "INPUT_KEY_VARIABLE": "PATTERN_RESULT",
            "INPUT_EXTRACT_PATTERN": r"(feat|fix|chore|refactor|docs|ci|test)",
        },
    ),
    (
        "Test 7: Extract with commit range",
        {
            "INPUT_KEY_VARIABLE": "RANGE_RESULT",
            "INPUT_EXTRACT_PATTERN": r"(feat|fix|chore|refactor)",
            "INPUT_COMMIT_RANGE": "HEAD~3..HEAD",
        },
    ),
]


def run_test(test_name: str, overrides: dict) -> bool:
    """Run a single test case and report whether it passed."""
    print("\n" + "=" * 50)
    print(f"{test_name}")
    print("=" * 50)

    from app.main import run

    with patch.dict(os.environ, {**BASE_ENV, **overrides}):
        try:
            run()
        except Exception as e:  # noqa: BLE001
            print(f"[FAIL] Test failed: {e}")
            return False
    print("[PASS] Test completed successfully")
    return True


def main() -> int:
    """Run all test cases and return the process exit code."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}\n")

    print("=" * 50)
    print("Local Integration Test Suite")
    print("=" * 50)

    # configure_git() appends GIT_CONFIG_* entries to os.environ on every run.
    with patch.dict(os.environ):
        results = [run_test(name, overrides) for name, overrides in CASES]

    failed = results.count(False)
    print("\n" + "=" * 50)
    if failed:
        print(f"[FAIL] {failed} of {len(results)} integration tests failed")
    else:
        print("[PASS] All integration tests completed!")
    print("=" * 50)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

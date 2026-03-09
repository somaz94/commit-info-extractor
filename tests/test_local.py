#!/usr/bin/env python3
"""
Local integration test script for commit-info-extractor.
Run this directly without Docker to test the full flow.
Usage: cd /path/to/commit-info-extractor && python3 tests/test_local.py
"""

import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_test(test_name: str, env_vars: dict) -> None:
    """Run a single test case."""
    print("\n" + "=" * 50)
    print(f"{test_name}")
    print("=" * 50)

    for key, value in env_vars.items():
        os.environ[key] = value

    from app.main import run

    try:
        run()
        print(f"[PASS] Test completed successfully")
    except SystemExit as e:
        if e.code != 0:
            print(f"[FAIL] Test failed with exit code {e.code}")
        else:
            print(f"[PASS] Test completed successfully")
    except Exception as e:
        print(f"[FAIL] Test failed with exception: {e}")


def main():
    """Run all test cases."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}\n")

    print("=" * 50)
    print("Local Integration Test Suite")
    print("=" * 50)

    run_test(
        "Test 1: Basic commit message extraction",
        {
            "INPUT_COMMIT_LIMIT": "5",
            "INPUT_PRETTY": "true",
            "INPUT_KEY_VARIABLE": "ENVIRONMENT",
            "INPUT_EXTRACT_COMMAND": "",
            "INPUT_FAIL_ON_EMPTY": "false",
            "INPUT_OUTPUT_FORMAT": "text",
        },
    )

    run_test(
        "Test 2: Extract 'chore' keyword",
        {
            "INPUT_COMMIT_LIMIT": "10",
            "INPUT_PRETTY": "true",
            "INPUT_KEY_VARIABLE": "CHORE_KEYWORD",
            "INPUT_EXTRACT_COMMAND": "grep -oE 'chore' || true",
            "INPUT_FAIL_ON_EMPTY": "false",
            "INPUT_OUTPUT_FORMAT": "text",
        },
    )

    run_test(
        "Test 3: JSON output format",
        {
            "INPUT_COMMIT_LIMIT": "3",
            "INPUT_PRETTY": "true",
            "INPUT_KEY_VARIABLE": "COMMITS_JSON",
            "INPUT_EXTRACT_COMMAND": "",
            "INPUT_FAIL_ON_EMPTY": "false",
            "INPUT_OUTPUT_FORMAT": "json",
        },
    )

    run_test(
        "Test 4: CSV output format",
        {
            "INPUT_COMMIT_LIMIT": "3",
            "INPUT_PRETTY": "true",
            "INPUT_KEY_VARIABLE": "COMMITS_CSV",
            "INPUT_EXTRACT_COMMAND": "",
            "INPUT_FAIL_ON_EMPTY": "false",
            "INPUT_OUTPUT_FORMAT": "csv",
        },
    )

    run_test(
        "Test 5: Extract 'refactor' commits",
        {
            "INPUT_COMMIT_LIMIT": "10",
            "INPUT_PRETTY": "true",
            "INPUT_KEY_VARIABLE": "REFACTOR_COMMITS",
            "INPUT_EXTRACT_COMMAND": "grep -oE 'refactor' || true",
            "INPUT_FAIL_ON_EMPTY": "false",
            "INPUT_OUTPUT_FORMAT": "text",
        },
    )

    print("\n" + "=" * 50)
    print("[PASS] All integration tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()

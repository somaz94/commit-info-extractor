"""Extract information from commit messages using shell commands or regex patterns."""

import re
import subprocess

from app.logger import print_debug, print_error, print_section


def extract_info(
    commit_messages: str,
    extract_command: str | None,
    extract_pattern: str | None,
    fail_on_empty: str,
    timeout: int,
) -> tuple[str, int]:
    """Extract information from commit messages.

    Args:
        commit_messages: Input commit messages.
        extract_command: Shell command to extract info.
        extract_pattern: Regex pattern to extract info (safer alternative).
        fail_on_empty: Whether to fail on empty results.
        timeout: Command timeout in seconds.

    Returns:
        Tuple of (extracted information, match count).
    """
    print_section("Extracting Environment Information")

    if not extract_command and not extract_pattern:
        lines = [line for line in commit_messages.strip().split("\n") if line.strip()]
        return commit_messages, len(lines)

    if extract_pattern:
        print(f"  - Using extract pattern: {extract_pattern}")
        environment = _run_extract_pattern(commit_messages, extract_pattern)
    else:
        print(f"  - Using extract command: {extract_command}")
        environment = _run_extract_command(commit_messages, extract_command, timeout)

    print_debug(f"Input length: {len(commit_messages)} characters")

    match_count = len([line for line in environment.split("\n") if line.strip()]) if environment.strip() else 0

    if not environment.strip() and fail_on_empty.lower() == "true":
        print_error(
            "No environment information extracted and fail_on_empty is set to true"
        )

    if environment.strip():
        if match_count > 1:
            print(f"  - Found {match_count} unique matches")
        print(f"  - Extracted value: {environment}")

    return environment, match_count


def _run_extract_pattern(commit_messages: str, pattern: str) -> str:
    """Extract matches using Python regex pattern.

    Args:
        commit_messages: Input text.
        pattern: Regex pattern to match.

    Returns:
        Deduplicated, sorted extraction result.
    """
    try:
        compiled = re.compile(pattern)
    except re.error as e:
        print_error(f"Invalid regex pattern '{pattern}': {e}")
        return ""

    matches = compiled.findall(commit_messages)
    print_debug(f"Pattern matched {len(matches)} times")

    unique = sorted(set(matches))
    return "\n".join(unique) if unique else ""


def _run_extract_command(
    commit_messages: str, extract_command: str, timeout: int
) -> str:
    """Run extraction command on commit messages.

    Args:
        commit_messages: Input text.
        extract_command: Shell command to run.
        timeout: Command timeout in seconds.

    Returns:
        Deduplicated, sorted extraction result.
    """
    try:
        result = subprocess.run(
            extract_command,
            shell=True,
            input=commit_messages,
            capture_output=True,
            text=True,
            check=False,
            executable="/bin/bash",
            timeout=timeout,
        )

        print_debug(f"Command exit code: {result.returncode}")
        print_debug(f"Output length: {len(result.stdout)} characters")

        lines = [line for line in result.stdout.strip().split("\n") if line.strip()]
        environment = "\n".join(sorted(set(lines))) if lines else ""

        if result.returncode > 1 and result.stderr:
            print_debug(
                f"Command warning (exit {result.returncode}): {result.stderr}"
            )

        return environment

    except subprocess.TimeoutExpired:
        print_error(f"Extract command timed out after {timeout} seconds")
    except Exception as e:
        print_debug(f"Exception type: {type(e).__name__}")
        print_error(f"Failed to extract environment information: {e}")

    return ""

"""Extract information from commit messages using shell commands."""

import subprocess

from app.logger import print_debug, print_error, print_section


def extract_info(
    commit_messages: str,
    extract_command: str | None,
    fail_on_empty: str,
    timeout: int,
) -> str:
    """Extract information from commit messages.

    Args:
        commit_messages: Input commit messages.
        extract_command: Shell command to extract info.
        fail_on_empty: Whether to fail on empty results.
        timeout: Command timeout in seconds.

    Returns:
        Extracted information as string.
    """
    print_section("Extracting Environment Information")

    if not extract_command:
        return commit_messages

    print(f"  - Using extract command: {extract_command}")
    print_debug(f"Input length: {len(commit_messages)} characters")

    environment = _run_extract_command(commit_messages, extract_command, timeout)

    if not environment.strip() and fail_on_empty.lower() == "true":
        print_error(
            "No environment information extracted and fail_on_empty is set to true"
        )

    if environment.strip():
        lines = [line for line in environment.split("\n") if line]
        if len(lines) > 1:
            print(f"  - Found {len(lines)} unique matches")
        print(f"  - Extracted value: {environment}")

    return environment


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

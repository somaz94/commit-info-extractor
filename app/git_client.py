"""Git operations for fetching commit messages."""

import os
import subprocess

from app.logger import print_debug, print_error, print_section, print_success

GIT_SAFE_DIRECTORIES = ["/usr/src", "/github/workspace"]


def configure_git() -> None:
    """Configure git safe directories."""
    print_section("Configuring Git")

    for directory in GIT_SAFE_DIRECTORIES:
        try:
            subprocess.run(
                ["git", "config", "--global", "--add", "safe.directory", directory],
                check=True,
                capture_output=True,
                timeout=5,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print_debug(f"Failed to configure {directory}: {e}")

    print_success("Git configuration completed")


def fetch_commit_messages(
    commit_limit: int, pretty: str, timeout: int, commit_range: str = ""
) -> str:
    """Fetch commit messages from git repository.

    Args:
        commit_limit: Number of commits to retrieve.
        pretty: Whether to use pretty format.
        timeout: Command timeout in seconds.
        commit_range: Git commit range (e.g., "HEAD~5..HEAD", "v1.0.0..v1.1.0").

    Returns:
        Commit messages as string.
    """
    print_section("Fetching Commit Messages")

    if not os.path.isdir(".git"):
        print("  - No git repository available")
        return "No commit messages available."

    cmd = ["git", "log"]

    if commit_range:
        cmd.append(commit_range)
        print_debug(f"Using commit range: {commit_range}")
    else:
        cmd.append(f"-{commit_limit}")

    if pretty and pretty.lower() != "false":
        cmd.append("--pretty=%B")

    print_debug(f"Executing: {' '.join(cmd)} (timeout: {timeout}s)")

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        commit_messages = result.stdout
        if commit_messages:
            label = f"range {commit_range}" if commit_range else f"last {commit_limit} commits"
            print(f"  - {label}:")
            for line in commit_messages.split("\n"):
                if line:
                    print(f"    {line}")

        return commit_messages

    except subprocess.TimeoutExpired:
        print_error(f"Git command timed out after {timeout} seconds")
    except subprocess.CalledProcessError as e:
        print_debug(f"Git command failed with exit code {e.returncode}")
        if e.stderr:
            stderr = e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr
            print_debug(f"Git stderr: {stderr}")
        print_error("Failed to fetch commit messages")

    return ""

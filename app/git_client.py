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


def fetch_commit_messages(commit_limit: int, pretty: str, timeout: int) -> str:
    """Fetch commit messages from git repository.

    Args:
        commit_limit: Number of commits to retrieve.
        pretty: Whether to use pretty format.
        timeout: Command timeout in seconds.

    Returns:
        Commit messages as string.
    """
    print_section("Fetching Commit Messages")

    if not os.path.isdir(".git"):
        print("  - No git repository available")
        return "No commit messages available."

    cmd = ["git", "log", f"-{commit_limit}"]
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
            print(f"  - Last {commit_limit} commits:")
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

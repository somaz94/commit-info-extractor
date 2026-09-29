"""Git operations for fetching commit messages."""

import os
import subprocess

from app.logger import fail, print_debug, print_section, print_success

GIT_SAFE_DIRECTORIES = ["/usr/src", "/github/workspace"]


def add_config_env(key: str, value: str) -> None:
    """Append key=value to the git config that child git processes read from the environment.

    Git treats GIT_CONFIG_COUNT/KEY/VALUE as command-scope config, so safe.directory
    is honoured and ~/.gitconfig is never touched.
    """
    count = int(os.environ.get("GIT_CONFIG_COUNT", "0"))
    if count < 0:
        raise ValueError(f"Invalid GIT_CONFIG_COUNT: {count}")
    os.environ[f"GIT_CONFIG_KEY_{count}"] = key
    os.environ[f"GIT_CONFIG_VALUE_{count}"] = value
    os.environ["GIT_CONFIG_COUNT"] = str(count + 1)


def configure_git() -> None:
    """Trust the checkout directories for this process only; no git config file is written."""
    print_section("Configuring Git")

    for directory in GIT_SAFE_DIRECTORIES:
        add_config_env("safe.directory", directory)
        print_debug(f"safe.directory={directory}")

    print_success("Git configuration completed")


def fetch_commit_messages(
    commit_limit: int, pretty: bool, timeout: int, commit_range: str = ""
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

    # .git is a file, not a directory, in worktrees and submodules.
    if not os.path.exists(".git"):
        fail(
            "No git repository in the workspace root. Check out the repository "
            "with actions/checkout (default path) before this action."
        )

    cmd = ["git", "log"]

    if commit_range:
        cmd.append(commit_range)
        print_debug(f"Using commit range: {commit_range}")
    else:
        cmd.append(f"-{commit_limit}")

    if pretty:
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
            label = (
                f"range {commit_range}"
                if commit_range
                else f"last {commit_limit} commits"
            )
            print(f"  - {label}:")
            for line in commit_messages.split("\n"):
                if line:
                    print(f"    {line}")

        return commit_messages

    except subprocess.TimeoutExpired:
        fail(f"Git command timed out after {timeout} seconds")
    except subprocess.CalledProcessError as e:
        print_debug(f"Git command failed with exit code {e.returncode}")
        if e.stderr:
            print_debug(f"Git stderr: {e.stderr}")
        fail("Failed to fetch commit messages")

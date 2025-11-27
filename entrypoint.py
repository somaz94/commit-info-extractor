#!/usr/bin/env python3

import os
import sys
import subprocess
import json
from datetime import datetime
from typing import Optional, List

# Global debug flag
DEBUG = False


def print_header(message: str) -> None:
    """Print formatted header."""
    print("\n" + "=" * 50)
    print(f"▶️ {message}")
    print("=" * 50 + "\n")


def print_section(message: str) -> None:
    """Print formatted section."""
    print(f"\n{message}:")


def print_debug(message: str) -> None:
    """Print debug message if debug mode is enabled."""
    if DEBUG:
        print(f"[DEBUG] {message}")


def print_success(message: str) -> None:
    """Print success message."""
    print(f"✅ {message}")


def print_error(message: str) -> None:
    """Print error message and exit."""
    print(f"❌ {message}", file=sys.stderr)
    sys.exit(1)


def configure_git() -> None:
    """Configure git safe directories."""
    print_section("Configuring Git")
    
    directories = ["/usr/src", "/github/workspace"]
    for directory in directories:
        try:
            subprocess.run(
                ["git", "config", "--global", "--add", "safe.directory", directory],
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError:
            print_error(f"Failed to set safe.directory {directory}")
    
    print_success("Git configuration completed")


def fetch_commit_messages(commit_limit: int, pretty: str, timeout: int = 30) -> str:
    """Fetch commit messages from git repository."""
    print_section("Fetching Commit Messages")
    
    if not os.path.isdir(".git"):
        print("  • No git repository available")
        return "No commit messages available."
    
    try:
        cmd = ["git", "log", f"-{commit_limit}"]
        if pretty and pretty.lower() != "false":
            cmd.append("--pretty=%B")
        
        print_debug(f"Executing: {' '.join(cmd)} (timeout: {timeout}s)")
        
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        commit_messages = result.stdout
        print(f"  • Last {commit_limit} commits:")
        for line in commit_messages.split('\n'):
            if line:
                print(f"    {line}")
        
        return commit_messages
    
    except subprocess.TimeoutExpired:
        print_error(f"Git command timed out after {timeout} seconds")
    except subprocess.CalledProcessError as e:
        print_debug(f"Git command failed with exit code {e.returncode}")
        print_error("Failed to fetch commit messages")


def extract_environment(commit_messages: str, extract_command: Optional[str], fail_on_empty: str, timeout: int = 30) -> str:
    """Extract environment information from commit messages."""
    print_section("Extracting Environment Information")
    
    if extract_command:
        print(f"  • Using extract command: {extract_command}")
        print_debug(f"Input length: {len(commit_messages)} characters")
        try:
            # Execute the extract command with commit messages as input
            result = subprocess.run(
                extract_command,
                shell=True,
                input=commit_messages,
                capture_output=True,
                text=True,
                check=False,  # Don't raise exception on non-zero exit
                executable='/bin/bash',
                timeout=timeout
            )
            
            print_debug(f"Command exit code: {result.returncode}")
            print_debug(f"Output length: {len(result.stdout)} characters")
            
            # Get unique values and sort, filtering out empty lines
            lines = [line for line in result.stdout.strip().split('\n') if line.strip()]
            environment = '\n'.join(sorted(set(lines))) if lines else ""
            
            # Only error if stderr is present AND returncode is not 0 or 1 (grep returns 1 when no match)
            if result.returncode > 1 and result.stderr:
                print(f"  • Command warning (exit {result.returncode}): {result.stderr}", file=sys.stderr)
        except subprocess.TimeoutExpired:
            print_error(f"Extract command timed out after {timeout} seconds")
        except Exception as e:
            print_debug(f"Exception type: {type(e).__name__}")
            print_error(f"Failed to extract environment information: {e}")
    else:
        environment = commit_messages
    
    # Handle empty environment information
    if not environment.strip() and fail_on_empty.lower() == "true":
        print_error("No environment information extracted and fail_on_empty is set to true")
    
    # Count unique matches
    if environment.strip():
        environment_lines = [line for line in environment.split('\n') if line]
        environment_count = len(environment_lines)
        if environment_count > 1:
            print(f"  • Found {environment_count} unique matches")
        print(f"  • Extracted value: {environment}")
    
    return environment


def format_output(value: str, output_format: str) -> str:
    """Format output based on specified format."""
    print_section("Formatting Output")
    print(f"  • Output format: {output_format}")
    
    if output_format == "json":
        # Convert to JSON array
        lines = [line for line in value.split('\n') if line]
        return json.dumps(lines, ensure_ascii=False)
    
    elif output_format == "csv":
        # Convert to CSV with proper escaping
        lines = [line for line in value.split('\n') if line]
        # Escape commas and quotes
        escaped_lines = []
        for line in lines:
            # Escape quotes by doubling them
            escaped = line.replace('"', '""')
            # If the line contains comma or quote, wrap in quotes
            if ',' in escaped or '"' in line:
                escaped = f'"{escaped}"'
            escaped_lines.append(escaped)
        return ','.join(escaped_lines)
    
    else:  # text (default)
        return value


def set_output_variables(environment: str, key_variable: str) -> None:
    """Set output variables for GitHub Actions."""
    print_section("Setting Output Variables")
    
    output_var = key_variable or "ENVIRONMENT"
    print(f"  • Key Variable: {output_var}")
    
    github_env = os.getenv("GITHUB_ENV")
    github_output = os.getenv("GITHUB_OUTPUT")
    
    if github_env and github_output:
        # GitHub Actions environment
        delimiter = f"EOF_{int(datetime.now().timestamp())}"
        
        # Write to GITHUB_ENV
        with open(github_env, "a") as f:
            f.write(f"value_variable<<{delimiter}\n")
            f.write(f"{environment}\n")
            f.write(f"{delimiter}\n")
            f.write(f"key_variable={output_var}\n")
        
        # Write to GITHUB_OUTPUT
        with open(github_output, "a") as f:
            f.write(f"value_variable<<{delimiter}\n")
            f.write(f"{environment}\n")
            f.write(f"{delimiter}\n")
            f.write(f"key_variable={output_var}\n")
        
        print_success("Variables set in GitHub Actions environment")
    else:
        # Local execution
        print_success("Local execution - variables would be set as:")
        print(f"  • {output_var}={environment}")


def main() -> None:
    """Main execution function."""
    global DEBUG
    
    # Get input parameters from environment variables
    DEBUG = os.getenv("INPUT_DEBUG", "false").lower() == "true"
    commit_limit = int(os.getenv("INPUT_COMMIT_LIMIT", "10"))
    pretty = os.getenv("INPUT_PRETTY", "false")
    key_variable = os.getenv("INPUT_KEY_VARIABLE", "ENVIRONMENT")
    extract_command = os.getenv("INPUT_EXTRACT_COMMAND", "")
    fail_on_empty = os.getenv("INPUT_FAIL_ON_EMPTY", "false")
    output_format = os.getenv("INPUT_OUTPUT_FORMAT", "text")
    timeout = int(os.getenv("INPUT_TIMEOUT", "30"))
    
    print_header("Environment Variable Extractor")
    print_debug(f"Debug mode: {DEBUG}")
    print_debug(f"Timeout: {timeout}s")
    
    # Execute workflow
    configure_git()
    commit_messages = fetch_commit_messages(commit_limit, pretty, timeout)
    environment = extract_environment(commit_messages, extract_command or None, fail_on_empty, timeout)
    
    # Format output if environment is not empty
    if environment.strip():
        environment = format_output(environment, output_format)
    
    set_output_variables(environment, key_variable)
    
    print_header("Process Completed Successfully")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("Process interrupted by user")
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")

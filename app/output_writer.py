"""Write output variables for GitHub Actions."""

import os
from datetime import datetime

from app.logger import print_error, print_section, print_success


def set_output_variables(environment: str, key_variable: str) -> None:
    """Set output variables for GitHub Actions.

    Args:
        environment: The value to set.
        key_variable: The name of the key variable.
    """
    print_section("Setting Output Variables")

    output_var = key_variable or "ENVIRONMENT"
    print(f"  - Key Variable: {output_var}")

    github_env = os.getenv("GITHUB_ENV")
    github_output = os.getenv("GITHUB_OUTPUT")

    if github_env and github_output:
        _write_github_outputs(environment, output_var, github_env, github_output)
    else:
        print_success("Local execution - variables would be set as:")
        print(f"  - {output_var}={environment}")


def _write_github_outputs(
    environment: str, output_var: str, github_env: str, github_output: str
) -> None:
    """Write values to GITHUB_ENV and GITHUB_OUTPUT files.

    Args:
        environment: The value to write.
        output_var: Variable name.
        github_env: Path to GITHUB_ENV file.
        github_output: Path to GITHUB_OUTPUT file.
    """
    delimiter = f"EOF_{int(datetime.now().timestamp())}"

    try:
        for filepath in (github_env, github_output):
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(f"value_variable<<{delimiter}\n")
                f.write(f"{environment}\n")
                f.write(f"{delimiter}\n")
                f.write(f"key_variable={output_var}\n")

        print_success("Variables set in GitHub Actions environment")
    except IOError as e:
        print_error(f"Failed to write output files: {e}")

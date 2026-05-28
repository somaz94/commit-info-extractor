"""Write output variables for GitHub Actions."""

import os
import uuid

from app.logger import fail, print_section, print_success


def set_output_variables(
    environment: str, key_variable: str, match_count: int = 0
) -> None:
    """Set output variables for GitHub Actions.

    Args:
        environment: The value to set.
        key_variable: The name of the key variable.
        match_count: Number of extracted matches.
    """
    print_section("Setting Output Variables")

    output_var = key_variable or "ENVIRONMENT"
    print(f"  - Key Variable: {output_var}")
    print(f"  - Match Count: {match_count}")

    github_env = os.getenv("GITHUB_ENV")
    github_output = os.getenv("GITHUB_OUTPUT")

    if github_env and github_output:
        _write_github_outputs(
            environment, output_var, match_count, github_env, github_output
        )
    else:
        print_success("Local execution - variables would be set as:")
        print(f"  - {output_var}={environment}")
        print(f"  - match_count={match_count}")


def _write_github_outputs(
    environment: str,
    output_var: str,
    match_count: int,
    github_env: str,
    github_output: str,
) -> None:
    """Write values to GITHUB_ENV and GITHUB_OUTPUT files.

    GITHUB_ENV receives an env var named after the user-chosen key (e.g. DEPLOY_ENV),
    consumable by subsequent steps via ${{ env.DEPLOY_ENV }}.
    GITHUB_OUTPUT receives the three action.yml-declared outputs
    (key_variable, value_variable, match_count).

    Args:
        environment: The value to write.
        output_var: Variable name to expose as env var in GITHUB_ENV.
        match_count: Number of extracted matches.
        github_env: Path to GITHUB_ENV file.
        github_output: Path to GITHUB_OUTPUT file.
    """
    delimiter = f"EOF_{uuid.uuid4().hex}"

    try:
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"{output_var}<<{delimiter}\n")
            f.write(f"{environment}\n")
            f.write(f"{delimiter}\n")

        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"value_variable<<{delimiter}\n")
            f.write(f"{environment}\n")
            f.write(f"{delimiter}\n")
            f.write(f"key_variable={output_var}\n")
            f.write(f"match_count={match_count}\n")

        print_success("Variables set in GitHub Actions environment")
    except IOError as e:
        fail(f"Failed to write output files: {e}")

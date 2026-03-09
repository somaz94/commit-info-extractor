"""Main orchestration for commit-info-extractor."""

from app.config import AppConfig
from app.extractor import extract_info
from app.formatter import format_output
from app.git_client import configure_git, fetch_commit_messages
from app.logger import print_debug, print_error, print_header, set_debug
from app.output_writer import set_output_variables


def run() -> None:
    """Main execution flow."""
    try:
        config = AppConfig.from_env()
    except ValueError as e:
        print_error(str(e))
        return

    set_debug(config.debug)

    try:
        config.validate()
    except ValueError as e:
        print_error(str(e))
        return

    print_header("Environment Variable Extractor")
    print_debug(f"Debug mode: {config.debug}")
    print_debug(f"Commit limit: {config.commit_limit}")
    print_debug(f"Timeout: {config.timeout}s")
    print_debug(f"Output format: {config.output_format}")

    configure_git()

    commit_messages = fetch_commit_messages(
        config.commit_limit, config.pretty, config.timeout
    )

    environment = extract_info(
        commit_messages,
        config.extract_command or None,
        config.fail_on_empty,
        config.timeout,
    )

    if environment.strip():
        environment = format_output(environment, config.output_format)

    set_output_variables(environment, config.key_variable)

    print_header("Process Completed Successfully")

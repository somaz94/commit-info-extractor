"""Input configuration parsing and validation."""

import os
from dataclasses import dataclass

DEFAULT_TIMEOUT = 30
DEFAULT_COMMIT_LIMIT = 10
VALID_OUTPUT_FORMATS = ("text", "json", "csv")


@dataclass
class AppConfig:
    """Configuration loaded from environment variables."""

    commit_limit: int
    timeout: int
    pretty: str
    key_variable: str
    extract_command: str
    extract_pattern: str
    fail_on_empty: str
    output_format: str
    commit_range: str
    debug: bool

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Create configuration from environment variables."""
        debug = os.getenv("INPUT_DEBUG", "false").lower() == "true"

        try:
            commit_limit = int(os.getenv("INPUT_COMMIT_LIMIT", str(DEFAULT_COMMIT_LIMIT)))
            timeout = int(os.getenv("INPUT_TIMEOUT", str(DEFAULT_TIMEOUT)))
        except ValueError as e:
            raise ValueError(f"Invalid numeric input: {e}") from e

        return cls(
            commit_limit=commit_limit,
            timeout=timeout,
            pretty=os.getenv("INPUT_PRETTY", "false"),
            key_variable=os.getenv("INPUT_KEY_VARIABLE", "ENVIRONMENT"),
            extract_command=os.getenv("INPUT_EXTRACT_COMMAND", ""),
            extract_pattern=os.getenv("INPUT_EXTRACT_PATTERN", ""),
            fail_on_empty=os.getenv("INPUT_FAIL_ON_EMPTY", "false"),
            output_format=os.getenv("INPUT_OUTPUT_FORMAT", "text").lower(),
            commit_range=os.getenv("INPUT_COMMIT_RANGE", ""),
            debug=debug,
        )

    def validate(self) -> None:
        """Validate configuration values.

        Raises:
            ValueError: If any configuration value is invalid.
        """
        if self.commit_limit <= 0:
            raise ValueError("commit_limit must be greater than 0")
        if self.timeout <= 0:
            raise ValueError("timeout must be greater than 0")
        if self.output_format not in VALID_OUTPUT_FORMATS:
            raise ValueError(
                f"Invalid output_format: {self.output_format}. "
                f"Must be {', '.join(VALID_OUTPUT_FORMATS)}"
            )
        if self.extract_command and self.extract_pattern:
            raise ValueError(
                "Cannot use both extract_command and extract_pattern. Choose one."
            )

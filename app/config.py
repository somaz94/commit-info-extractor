"""Input configuration parsing and validation."""

import os
import re
from dataclasses import dataclass

DEFAULT_TIMEOUT = 30
DEFAULT_COMMIT_LIMIT = 10
VALID_OUTPUT_FORMATS = ("text", "json", "csv")

# Best-effort denylist, not a sandbox; | and || stay allowed on purpose
DANGEROUS_PATTERNS = re.compile(
    r"[;&`]"          # shell chaining (;, &), backticks
    r"|\$[\({']"      # $() substitution, ${} expansion, $'' escapes
    r"|>\s*/"         # redirect to absolute path
    r"|\brm\b"
    r"|\bcurl\b"     # network access
    r"|\bwget\b"
    r"|\bnc\b"
    r"|\bchmod\b"
    r"|\bchown\b"
    r"|\bmkdir\b"
    r"|\bsudo\b"
    r"|\beval\b"
    r"|\bexec\b"
    r"|\bsource\b"
    r"|\bdd\b"
    r"|(?<![\w.-])(?:ba|z|da|k)?sh\b"  # shell interpreters, not a .sh suffix
)
# Outside single quotes these expand to the running shell's binary.
SHELL_BINARY_VARIABLES = re.compile(r"\$(?:0|BASH|SHELL)\b")


def _scan_command(command: str) -> tuple[str, str, bool]:
    """Read extract_command the way bash splits it.

    Returns:
        The text with quotes and escapes removed (bash joins r''m into rm), the
        part outside single quotes (where $ still expands), and whether a
        newline outside quotes and comments starts another command, as ; does.
        A newline right after | or a backslash continues the line instead.
    """
    joined: list[str] = []
    expandable: list[str] = []
    quote = prev = last = ""
    escaped = comment = chained = False
    for ch in command.strip():
        if comment and ch != "\n":
            continue
        comment = False
        if escaped:
            escaped = False
            if ch != "\n":
                joined.append(ch)
                last = "\\"
        elif quote:
            if ch == quote:
                quote = ""
            elif ch == "\\" and quote == '"':
                escaped = True
            else:
                joined.append(ch)
                if quote == '"':
                    expandable.append(ch)
        elif ch == "\\":
            escaped = True
        elif ch in "'\"":
            quote = last = ch
        elif ch == "#" and prev in ("", " ", "\t", "\n", "|"):
            comment = True
        else:
            if ch == "\n":
                chained = chained or last != "|"
            elif ch not in " \t":
                last = ch
            joined.append(ch)
            expandable.append(ch)
        prev = ch
    return "".join(joined), "".join(expandable), chained


def _is_blocked_command(command: str) -> bool:
    """Check extract_command against the denylist as written and as bash reads it."""
    joined, expandable, chained = _scan_command(command)
    return (
        chained
        or bool(DANGEROUS_PATTERNS.search(command))
        or bool(DANGEROUS_PATTERNS.search(joined))
        or bool(SHELL_BINARY_VARIABLES.search(expandable))
    )


def _bool_env(name: str, default: str = "false") -> bool:
    """Parse a GitHub Actions string-typed boolean input into a real bool."""
    return os.getenv(name, default).lower() == "true"


@dataclass
class AppConfig:
    """Configuration loaded from environment variables."""

    commit_limit: int
    timeout: int
    pretty: bool
    key_variable: str
    extract_command: str
    extract_pattern: str
    fail_on_empty: bool
    output_format: str
    commit_range: str
    debug: bool

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Create configuration from environment variables."""
        try:
            commit_limit = int(os.getenv("INPUT_COMMIT_LIMIT", str(DEFAULT_COMMIT_LIMIT)))
            timeout = int(os.getenv("INPUT_TIMEOUT", str(DEFAULT_TIMEOUT)))
        except ValueError as e:
            raise ValueError(f"Invalid numeric input: {e}") from e

        return cls(
            commit_limit=commit_limit,
            timeout=timeout,
            pretty=_bool_env("INPUT_PRETTY"),
            key_variable=os.getenv("INPUT_KEY_VARIABLE", "ENVIRONMENT"),
            extract_command=os.getenv("INPUT_EXTRACT_COMMAND", ""),
            extract_pattern=os.getenv("INPUT_EXTRACT_PATTERN", ""),
            fail_on_empty=_bool_env("INPUT_FAIL_ON_EMPTY"),
            output_format=os.getenv("INPUT_OUTPUT_FORMAT", "text").lower(),
            commit_range=os.getenv("INPUT_COMMIT_RANGE", ""),
            debug=_bool_env("INPUT_DEBUG"),
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
        if self.extract_command and _is_blocked_command(self.extract_command):
            raise ValueError(
                f"extract_command contains blocked shell operators or commands: "
                f"'{self.extract_command}'. Use extract_pattern for safer extraction."
            )

"""Logging and output formatting utilities."""

import sys

# Global debug flag
_debug = False


def set_debug(enabled: bool) -> None:
    """Enable or disable debug mode."""
    global _debug
    _debug = enabled


def is_debug() -> bool:
    """Return current debug mode state."""
    return _debug


def print_header(message: str) -> None:
    """Print formatted header."""
    print("\n" + "=" * 50)
    print(f">> {message}")
    print("=" * 50 + "\n")


def print_section(message: str) -> None:
    """Print formatted section."""
    print(f"\n{message}:")


def print_debug(message: str) -> None:
    """Print debug message if debug mode is enabled."""
    if _debug:
        print(f"[DEBUG] {message}")


def print_success(message: str) -> None:
    """Print success message."""
    print(f"[OK] {message}")


def print_error(message: str) -> None:
    """Print error message and exit."""
    print(f"[ERROR] {message}", file=sys.stderr)
    sys.exit(1)

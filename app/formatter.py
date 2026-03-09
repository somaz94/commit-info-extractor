"""Output formatting for extracted values."""

import json

from app.logger import print_section


def format_output(value: str, output_format: str) -> str:
    """Format output based on specified format.

    Args:
        value: Input value to format.
        output_format: Desired output format (json, csv, text).

    Returns:
        Formatted output string.
    """
    print_section("Formatting Output")
    print(f"  - Output format: {output_format}")

    if not value.strip():
        return value

    if output_format == "json":
        return _format_json(value)
    if output_format == "csv":
        return _format_csv(value)
    return value


def _format_json(value: str) -> str:
    """Format value as JSON array."""
    lines = [line for line in value.split("\n") if line]
    return json.dumps(lines, ensure_ascii=False)


def _format_csv(value: str) -> str:
    """Format value as CSV string."""
    lines = [line for line in value.split("\n") if line]
    escaped_lines = []
    for line in lines:
        escaped = line.replace('"', '""')
        if "," in escaped or '"' in line:
            escaped = f'"{escaped}"'
        escaped_lines.append(escaped)
    return ",".join(escaped_lines)

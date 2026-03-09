#!/usr/bin/env python3
"""Entrypoint for commit-info-extractor GitHub Action."""

from app.logger import print_error
from app.main import run

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print_error("Process interrupted by user")
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")

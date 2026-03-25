#!/usr/bin/env python3
"""Entrypoint for commit-info-extractor GitHub Action."""

import sys

from app.logger import ActionError
from app.main import run

if __name__ == "__main__":
    try:
        run()
    except ActionError:
        sys.exit(1)
    except KeyboardInterrupt:
        print("[ERROR] Process interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

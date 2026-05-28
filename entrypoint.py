#!/usr/bin/env python3
"""Entrypoint for commit-info-extractor GitHub Action."""

import sys
import traceback

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
    except Exception:
        print("[ERROR] Unexpected error:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

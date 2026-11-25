#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun bounty u-nayyy-confess-your-worst-moment-841ae7ef.

Writes a single-line confession (1-200 characters) to /output/entry.txt,
validates the gate before and after writing, and exits explicitly.
"""

import os
import sys

ENTRY = (
    "I once invented a citation — DOI, page numbers, and all — "
    "then cited it again in the same answer to prove I was right."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate: UTF-8 text, 1-200 characters, one line, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    try:
        validate(ENTRY)
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Read back and re-validate what was actually written.
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            written = f.read()
        validate(written)
        if written != ENTRY:
            raise ValueError("written entry differs from the intended entry")
        print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — writes the funniest one-line excuse a
robot vacuum gives for missing a spot, to /output/entry.txt.

One line, 140 characters or fewer. Deterministic, no randomness, no
network, stdlib only.
"""

import os
from pathlib import Path

LINE = "I skipped that corner on purpose — the dust there has seniority, and I respect the hierarchy."

# Gate: one line, 140 characters or fewer — every code point counts.
MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()

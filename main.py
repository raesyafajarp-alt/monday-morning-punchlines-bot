#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to /output/entry.txt.
The joke is a single line, well within the 1-200 character gate.
"""

import os

ENTRY = (
    "My bed filed for full custody of me on Monday morning. "
    "The judge granted it \u2014 I only get weekends."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to /output/entry.txt.
The joke is a single line, well within the 1-200 character gate.
"""

import os

ENTRY = (
    "Monday morning is the only time my bed files for full custody of me "
    "\u2014 and the judge always rules in its favour, five days a week."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

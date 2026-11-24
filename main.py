#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status-page line for a total outage to
/output/entry.txt. Deterministic, standard library only, no network,
no trailing newline.
"""

import os

ENTRY = "Status: all systems down, including our optimism. A 4:58 p.m. deploy did this. No ETA — just engineers, cold coffee, and the truth, updated hourly."


def main() -> None:
    # The sealed gate accepts exactly one line of 1-160 characters.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

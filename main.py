#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes one Wi-Fi network name (at most 32 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no input. The same bytes every run.
The file is written with no trailing newline, so its character count is
exactly the length of the line itself.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I changed the locks AND the WiFi"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

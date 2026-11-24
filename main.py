#!/usr/bin/env python3
"""One-Liner Marathon entry: one original joke, printed exactly once.

The line below was written for this entry and is printed verbatim to
stdout, deterministically, every run.
"""

LINE = "I told my Wi-Fi router I needed space, so now it keeps dropping me."

def main() -> int:
    print(LINE)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

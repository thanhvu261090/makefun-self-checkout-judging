#!/usr/bin/env python3
"""Entry for make.fun bounty: The Self-Checkout Is Judging You.

Writes one funny one-line remark from a judgmental self-checkout
machine to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "Twelve yoghurts, no spoon, no plan \u2014 and you scanned the loyalty card like it would save you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

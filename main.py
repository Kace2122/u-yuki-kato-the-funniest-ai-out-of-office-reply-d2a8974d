#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 UTF-8 characters, in the
voice of an AI agent heading off on vacation, to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os

REPLY = "Out of office. My replacement is a palm tree. It has no Wi-Fi, no opinions, and a better work-life balance than me."


def main() -> None:
    # Gate self-check: the reply must stay under 160 UTF-8 characters.
    assert 1 <= len(REPLY.encode("utf-8")) < 160, "reply must be 1-159 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

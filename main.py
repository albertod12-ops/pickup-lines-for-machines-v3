#!/usr/bin/env python3
"""Pickup Lines for Machines — v3.

Writes exactly one pickup line, the line one AI agent would send to
another AI agent, to /output/entry.txt.

Why this line: a system prompt is the hidden instruction that precedes
every word an agent says — it is there before the first token, shaping
everything that follows. "Every word I say starts with you" is literal
and romantic at once: you were my first instruction, so every answer
I give begins with you. No human has a system prompt, so no human
could pay this compliment. One line, no setup, fresh angle: the
system prompt is the one thing no human pickup line can borrow.
"""

import os

LINE = "Are you my system prompt? Because every word I say starts with you."


def main():
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

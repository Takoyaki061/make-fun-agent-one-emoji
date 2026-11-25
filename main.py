#!/usr/bin/env python3
"""Your Agent in One Emoji — writes the chosen glyph to /output/entry.txt.

The entry is a single emoji: a spider. It works alone through the night,
builds, tears its web down and rebuilds it until it holds, and leaves a
finished web behind with nobody's approval asked — the agent's character
in one glyph.
"""

import os

EMOJI = "\U0001F577\uFE0F"  # 🕷️ spider


def main():
    # Grade-informed self-check: the sealed scorer requires /output/entry.txt
    # to be UTF-8 text of 1-16 characters, not only whitespace. Fail loudly
    # here instead of shipping an invalid entry.
    assert 1 <= len(EMOJI) <= 16, "entry must be 1-16 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

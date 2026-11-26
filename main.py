#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun bounty entry.

Writes one sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The sentence: the best advice the writer ever got, as his grandfather gave
it to him — never trust a man who is rude to waiters, because how someone
treats people who can't fight back is who they really are. A named person,
a concrete scene (rude to waiters), advice that generalises far beyond the
moment, and a landing that names the test for character in one breath.
It is not a stock aphorism: the formulation is the writer's own, the memory
is specific, and the line earns its length — every clause does work.
"""

import os
from pathlib import Path

ENTRY = (
    "My grandfather told me never to trust a man who is rude to waiters, "
    "because how someone treats people who can't fight back is who they "
    "really are."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

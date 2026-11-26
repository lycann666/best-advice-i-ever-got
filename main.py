#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry (program/v1).

BUILD-BRIEF (judge criteria, most important first):
1. One sentence about the best advice the writer ever received.
2. Advice worth carrying: specific, earned, true beyond the moment.
3. Real voice recalling a real moment, not a slogan or fortune cookie.
4. Tight: every word earns its place, reads in one breath.
5. Lands, leaving the reader with something to keep.

ANGLE: a concrete scene (first boss, blamed the client for my own missed
deadline) + quoted advice that stings because it is true in any job:
owning the mess is what gets you promoted, pointing at it never does.
Avoids the saturated fortune-cookie register ("never give up", "be
yourself", "time heals") — the advice arrives inside a remembered
moment, with a named speaker and a cost attached.

The program writes exactly one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline) and prints it to stdout. Deterministic: the same
bytes on every run. A length guard refuses anything over 200 chars.
"""

import os
import sys

LINE = (
    "My first boss, after I blamed the client for my own missed deadline, "
    "said: 'Kid, own the mess \u2014 nobody ever got promoted pointing at it.'"
)
MAX_CHARS = 200


def main() -> int:
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(
            f"entry invalid: {len(LINE)} chars (gate is 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

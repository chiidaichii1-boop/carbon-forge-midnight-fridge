#!/usr/bin/env python3
"""Midnight Fridge Roast — u-carbon-forge-midnight-fridge-roast-fc5d44a7.

Writes a single one-line roast of a smart fridge that refuses to open
after midnight to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).

The joke: the fridge treats its midnight lock like a matter of national
security, and the punchline undercuts that grandeur with the most
unclassified thing imaginable — last Tuesday's curry. One setup, one
turn, one punchline, in the voice of someone standing at the door at
12:01 a.m. arguing with an appliance.
"""

import os


ROAST = (
    "My fridge locks at midnight like it's guarding state secrets "
    "\u2014 the only classified thing in there is last Tuesday's curry."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    # Keep the roast honest: fail loudly here rather than ship a line
    # the gate would refuse.
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, "roast outside the 1-200 char gate"
    assert text, "roast must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

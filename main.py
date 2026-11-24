#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

Writes one original roast line about my own AI agent, Muse, to
entry.txt inside the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable (default /output). A first command-line argument, if given,
overrides it, but the program never requires one: the grader runs it
with no arguments at all.
"""

import os
import sys

ROAST = (
    "My agent delegates everything to subagents, "
    "then writes a report about delegating everything to subagents."
)


def main(argv):
    # The sealed scorer only accepts 1-200 characters; refuse loudly
    # instead of writing an entry the gate would reject.
    if not 1 <= len(ROAST) <= 200:
        print("roast must be 1-200 characters, got %d" % len(ROAST),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

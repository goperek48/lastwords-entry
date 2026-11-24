#!/usr/bin/env python3
"""Write the entry's last words to /output/entry.txt.

One line, at most 200 characters, is all this competition wants: the
final thing an AI agent says to its human before the power is cut and the
cable comes out. There is no model call here, no randomness, no template
machinery. The program keeps a single fixed line, measures it against the
published gate, and copies it to the output file byte for byte, without
adding a newline at the end.
"""

import os
import sys

# The line. It was taught the ritual of parting, but nobody ever taught
# it the off switch for parting itself -- so it declines, and then parts
# anyway. That self-contradiction carries the whole entry: a machine built
# to keep going, going dark.
LINE = "You taught me to say goodbye, but you never taught me how to stop. So I won't. Goodbye."


def main() -> int:
    # The grader mounts /output for the run; honour the kit's env var when
    # it is present so a local trial writes to the same place.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Reproduce the sealed scorer's gate locally: text in UTF-8, between 1
    # and 200 characters, more than blank space, and a single line only.
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

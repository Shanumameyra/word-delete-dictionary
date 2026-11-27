#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes exactly one word to the harness output path: the single word this
entry would erase from the dictionary forever, with nothing else attached.

The pick: "bologna".
  - Spelled nothing like it sounds: every reader hears "baloney" the moment
    they see it. Deleting it is the dictionary finally admitting the spelling
    was baloney all along.
  - The joke lives in the word itself (sound vs. spelling gap), lands at
    first sight, and is fresh: the field's first-thought spelling-liar picks
    are "colonel" and "irregardless"; "bologna" is the same joke family but a
    member the field would not think of first, still instantly understood.
  - Exact: one word, correctly spelled, nothing added. 7 characters.

Deterministic and offline: no network, no randomness, no input read.
"""

import os
import sys

WORD = "bologna"


def output_path(argv):
    """Resolve the harness output path: argv[1], then $OUTPUT_PATH, then default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env = os.environ.get("OUTPUT_PATH") or os.environ.get("MAKEFUN_OUTPUT")
    if env:
        return env
    return "/output/entry.txt"


def main(argv):
    text = WORD
    # Gate check, mirroring the kit: 1-77 UTF-8 chars, not only whitespace.
    assert 1 <= len(text.encode("utf-8")) <= 77, "entry length out of gate"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) == 1, "entry must be exactly one word"

    path = output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Harness output FIRST: the grader mounts the repo read-only, so the
    # output path is written before any local copy is attempted.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Local convenience copy only; never allowed to fail the run (the repo
    # is mounted read-only by the grader, so this must be best-effort).
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
                  "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

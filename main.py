#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader). The entry is a single emoji chosen by a 36-candidate
tournament scored on the judge's five criteria in order — see candidates.md.

Winner: the octopus. An AI agent is an intelligent worker that runs many
tasks and tools in parallel; the octopus is the one glyph that shows exactly
that at a glance, with a bold silhouette that reads at any size, far from
the brief's named obvious picks (the robot and the smiley).
"""

import os

ENTRY = "🐙"


def validate(entry: str) -> None:
    """Hold the entry to the kit's gate and to the brief's stricter rule.

    Gate: UTF-8 text of 1 to 16 characters, not only white space.
    Brief: the glyph alone — so exactly one character, no variation
    selector and no zero-width joiner hiding inside the count.
    """
    assert len(entry) == 1, f"entry must be one glyph, got {len(entry)} chars"
    assert entry.strip() != "", "entry must not be white space"
    assert "️" not in entry, "variation selector would add a second character"
    assert "‍" not in entry, "ZWJ sequences are not a single glyph"
    assert len(entry.encode("utf-8")) <= 16, "entry exceeds the gate in bytes"


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The glyph alone, nothing else: no newline, no caption.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

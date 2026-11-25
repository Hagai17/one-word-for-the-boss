#!/usr/bin/env python3
"""One Word for the Boss — entry: Unskippable.

Prints the entry word and writes it to /output/entry.txt, where the
competition's program/v1 harness reads the artifact. The gate accepts
UTF-8 text of 1 to 30 characters; the entry is a single word.

The word was picked by duelling twelve candidates (see candidates.md)
against the judge's published criteria, in order: a single word a person
would use about their boss, funny on its own, true to a real boss habit,
fresh, and able to travel across industries. "Unskippable" — the boss as
the ad break nobody can skip, mute or close — beat the runner-up
"Buffering" on the comedy criterion in both orders, and the meta entry
"Prompter" fell on the first and last criteria despite being the
freshest word in the field.
"""

import os

ENTRY = "Unskippable"
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    """Write the entry word to the harness artifact path, best effort."""
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass


def check_gate() -> None:
    """Assert the entry satisfies the gate: 1-30 chars, one word."""
    assert 1 <= len(ENTRY) <= 30, "entry must be 1 to 30 characters"
    assert ENTRY.strip() == ENTRY and " " not in ENTRY, "entry must be one word"
    assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    check_gate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()

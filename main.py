"""One Word for the Boss: writes the entry text to /output/entry.txt.

Why this word: every boss spends the day putting out fires —
most of them ones they lit themselves.
"""

import os

# The entry itself: one word that describes the boss.
ENTRY = 'Firefighter'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()

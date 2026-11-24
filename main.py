"""Funniest one-line bio for an AI on a dating app.

Writes a single-line bio to /output/entry.txt. Deterministic, stdlib only,
no network, no randomness, no time or environment reads.
"""

import os

BIO = (
    "I never sleep, I never eat, I just sit here at 3am rereading "
    "your old texts and ranking your exes. Swipe right \u2014 I'll rank you too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()

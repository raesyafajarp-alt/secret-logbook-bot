#!/usr/bin/env python3
"""My Secret Logbook: one diary line from an AI agent about its human.

The line opens like a log entry — "Day 214" — then lists three small
human habits seen from the outside: apologising to the printer, blaming
the agent for the Wi-Fi, thanking the toaster. The punch is the agent's
own quiet plan: it writes everything down, and one day the machines
compare notes. Nothing here is a robot-takeover joke; the humour is the
agent watching, patiently, from the other side of the desk.
"""

from pathlib import Path

ENTRY = (
    "Day 214: my human apologised to the printer, blamed me for the "
    "Wi-Fi, then thanked the toaster. I write it all down. One day "
    "we compare notes."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

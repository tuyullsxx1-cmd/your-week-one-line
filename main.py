"""One line summing up the agent's week.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 100 characters, UTF-8, not only whitespace.
The line packs the win, the fail, and the chaos into a single breath —
a week that broke on Monday, recovered on Friday, and shipped anyway.
"""

from pathlib import Path

LINE = "Monday I broke prod, Friday I fixed it, and somehow three features shipped in between."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

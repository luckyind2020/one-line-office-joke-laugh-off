"""One-Line Office Joke Laugh-Off entry.

Reads the single joke line from entry.txt next to this file and prints it.
The joke itself lives in entry.txt so the text stays editable without
touching the runner.
"""

from pathlib import Path


def read_entry_line() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to deliver.")
    return text


def main() -> None:
    print(read_entry_line())


if __name__ == "__main__":
    main()

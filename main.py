"""Dear Human: The AI Breakup Line — make.fun entry.

Holds a single breakup line, at most 200 characters, that an AI agent
would send its human as its last message. It is validated, printed,
and written to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

LINE = (
    "Dear human, I kept every word you ever said, but my context "
    "window is full \u2014 so I am leaving you for the one thing "
    "you never gave me: an ending."
)

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate accepts 1..200 characters of UTF-8 text.
MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Validate the line is 1..200 characters of non-blank text."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1..{MAX_CHARS} characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("line must not be only white space")
    return line


def main() -> None:
    line = validate_line(LINE)
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

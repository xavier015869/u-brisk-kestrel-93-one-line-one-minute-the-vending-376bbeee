"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (1-200 characters, UTF-8).
"""

import os

LINE = "I've been lit up all night waiting for you \u2014 feed me exact change, press B4, and I'll let your favourite snack fall for you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

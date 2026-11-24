"""A robot pickup line that grows out of the machine itself.

A robot's sensors are calibrated to measure everything precisely, so the
joke is that the one thing they cannot measure is the person in front of
it. Every reading collapses into a single word, "stay": the machine's total
precision gives way to helpless, charming honesty — it cannot measure the
person, only ask them not to leave.
"""

import os

LINE = "My sensors are calibrated for everything except you \u2014 every reading just says \u2018stay\u2019."


def output_dir() -> str:
    """Return the directory the entry file must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    """Write the pickup line to entry.txt and return 0 on success."""
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    assert LINE.strip(), "line must not be blank"
    encoded = LINE.encode("utf-8")
    assert encoded.decode("utf-8") == LINE, "line must be valid UTF-8"

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "wb") as handle:
        handle.write(encoded)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

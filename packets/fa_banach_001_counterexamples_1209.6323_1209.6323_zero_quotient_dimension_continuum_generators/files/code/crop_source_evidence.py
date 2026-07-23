#!/usr/bin/env python3
"""Crop the full Questions section from page 9 of the source-paper render."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page-9.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as page:
        # Preserve the full readable text width and the complete Questions
        # section, including Question 5 and its continuation line.
        crop = page.crop((100, 425, 1430, 935))
        crop.save(OUTPUT)
        print(f"saved {OUTPUT} at {crop.width}x{crop.height}")


if __name__ == "__main__":
    main()

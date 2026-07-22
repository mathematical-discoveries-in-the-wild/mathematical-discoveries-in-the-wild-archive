#!/usr/bin/env python3
"""Crop Conjecture 6.2 and its simplest-unknown-case note from page 25."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source-page-25.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Full readable text width; includes the preamble, complete conjecture,
        # displayed form, conclusion, and the explicitly simplest unknown case.
        crop = image.crop((170, 1382, 1485, 2260))
        crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

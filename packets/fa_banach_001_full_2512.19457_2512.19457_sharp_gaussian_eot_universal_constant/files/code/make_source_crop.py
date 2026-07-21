#!/usr/bin/env python3
"""Crop source page 19 to the complete Conjecture 3.1 statement."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source-page-19.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Full readable text width, with both margins and the complete conjecture.
    crop = image.crop((90, 110, 1400, 650))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

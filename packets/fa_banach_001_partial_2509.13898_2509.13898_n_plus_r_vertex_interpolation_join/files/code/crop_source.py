#!/usr/bin/env python3
"""Crop the full-width Remark 2 source evidence from rendered PDF page 2."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page-02.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Retain both text margins and the complete vertex-interpolation remark.
        crop = image.crop((100, 585, 1600, 1080))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

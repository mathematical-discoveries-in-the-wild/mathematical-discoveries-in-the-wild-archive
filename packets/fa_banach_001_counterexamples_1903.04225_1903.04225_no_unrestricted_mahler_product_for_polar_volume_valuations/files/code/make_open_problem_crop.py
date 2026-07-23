#!/usr/bin/env python3
"""Crop the source-paper page containing the open question.

Run from the packet directory:

    python code/make_open_problem_crop.py

The input page is rendered at 180 dpi from PDF page 4 and stored in
tmp/pdfs/source_page_4.png.  The crop retains the full text width, the
classification hypothesis on zeta_2, and the complete question.
"""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page_4.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    if image.size != (1530, 1980):
        raise RuntimeError(f"expected a 1530x1980 page render, got {image.size}")

    # Full readable text width; from Theorem 1.3* through the entire remark.
    crop = image.crop((125, 285, 1415, 1435))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Crop Theorem 2.12 and Remark 2.13 from page 9 of the source PDF."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source-09.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    width, height = image.size
    # Keep the complete page width. Vertically retain Theorem 2.12, both
    # displayed formulas, and all of Remark 2.13, without clipping the next
    # paragraph at the lower edge.
    box = (0, round(0.125 * height), width, round(0.295 * height))
    crop = image.crop(box)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)
    print(f"source={image.size}, box={box}, result={crop.size}, output={OUTPUT}")


if __name__ == "__main__":
    main()

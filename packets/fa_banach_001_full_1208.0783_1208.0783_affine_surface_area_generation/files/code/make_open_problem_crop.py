#!/usr/bin/env python3
"""Crop the closure conjecture from page 12 of the source PDF."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page_12.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    width, height = image.size
    # Retain the full readable text width and the final lines of Theorem 3.2,
    # followed by the entire conjecture paragraph at the foot of page 12.
    box = (round(0.055 * width), round(0.765 * height),
           round(0.945 * width), round(0.940 * height))
    crop = image.crop(box)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)
    print(f"source={image.size}, box={box}, result={crop.size}, output={OUTPUT}")


if __name__ == "__main__":
    main()

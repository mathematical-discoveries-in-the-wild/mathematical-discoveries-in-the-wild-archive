#!/usr/bin/env python3
"""Crop Remark 3 from page 11 of the rendered source PDF."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source-11.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    width, height = image.size
    # Retain the complete page width and all of Remark 3, including the
    # definition of alpha_n, the conjectured order, and the cube example.
    box = (0, round(0.505 * height), width, round(0.915 * height))
    crop = image.crop(box)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)
    print(f"source={image.size}, box={box}, result={crop.size}, output={OUTPUT}")


if __name__ == "__main__":
    main()

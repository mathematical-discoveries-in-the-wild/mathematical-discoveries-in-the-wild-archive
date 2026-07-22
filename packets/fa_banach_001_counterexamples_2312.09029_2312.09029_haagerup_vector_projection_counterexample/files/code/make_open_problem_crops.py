#!/usr/bin/env python3
"""Crop the two-page open-problem passage from rendered source pages.

The input pages are 1530 x 1980 PNG renders of pages 11 and 12 of the
arXiv PDF at 180 dpi.  The crops retain the full page width so no part of the
statement is clipped horizontally.
"""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
RENDER_DIR = PACKET / "tmp" / "pdfs"
FIGURE_DIR = PACKET / "figures"


def crop(source: str, output: str, top_fraction: float, bottom_fraction: float) -> None:
    image = Image.open(RENDER_DIR / source)
    width, height = image.size
    box = (0, round(top_fraction * height), width, round(bottom_fraction * height))
    result = image.crop(box)
    result.save(FIGURE_DIR / output, optimize=True)
    print(f"{output}: source={image.size}, box={box}, result={result.size}")


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    # Page 11 ends with the first line of the question.
    crop("source-11.png", "open_problem_crop_page11.png", 0.845, 0.985)
    # Page 12 completes the question and states that no definite result is known.
    crop("source-12.png", "open_problem_crop_page12.png", 0.000, 0.305)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render and crop PDF page 22 around Question 6.15 and Theorem 6.16."""

from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    pdf = pdfium.PdfDocument(str(SOURCE))
    page = pdf[21]  # one-based PDF page 22
    image: Image.Image = page.render(scale=180 / 72).to_pil()
    left = round(image.width * 0.075)
    right = round(image.width * 0.925)
    top = round(image.height * 0.595)
    bottom = round(image.height * 0.925)
    crop = image.crop((left, top, right, bottom))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

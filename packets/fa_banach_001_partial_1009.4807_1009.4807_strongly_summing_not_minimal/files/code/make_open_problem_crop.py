#!/usr/bin/env python3
"""Render and crop PDF page 25 around Problems 7.1--7.3."""

from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    pdf = pdfium.PdfDocument(str(SOURCE))
    page = pdf[24]  # one-based PDF page 25
    scale = 180 / 72
    image: Image.Image = page.render(scale=scale).to_pil()

    # Keep the full readable text width and all of the Open Problems heading,
    # Problems 7.1--7.3, and the prose around Problem 7.2.
    left = round(image.width * 0.075)
    right = round(image.width * 0.925)
    top = round(image.height * 0.625)
    bottom = round(image.height * 0.965)
    crop = image.crop((left, top, right, bottom))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

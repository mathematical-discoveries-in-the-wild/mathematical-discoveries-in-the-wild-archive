#!/usr/bin/env python3
"""Render source-paper crops for the RKBS representer question and caveat."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"

CROPS = [
    (
        "natural_question_crop.png",
        1,
        fitz.Rect(60, 70, 535, 245),
    ),
    (
        "training_site_caveat_crop.png",
        14,
        fitz.Rect(60, 65, 535, 245),
    ),
]


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    doc = fitz.open(PDF)
    matrix = fitz.Matrix(2.5, 2.5)
    for name, page_index, rect in CROPS:
        pix = doc[page_index].get_pixmap(matrix=matrix, clip=rect, alpha=False)
        pix.save(FIGURES / name)
        print(f"wrote {FIGURES / name}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render source-paper crops for the two relevant remarks."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"

CROPS = [
    (
        "open_problem_crop.png",
        11,
        fitz.Rect(110, 150, 485, 255),
    ),
    (
        "complement_angle_crop.png",
        20,
        fitz.Rect(105, 430, 490, 565),
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

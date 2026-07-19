#!/usr/bin/env python3
"""Render source-paper crops for the attained-cotype theorem and epsilon caveat."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"

CROPS = [
    (
        "main_theorem_crop.png",
        0,
        fitz.Rect(105, 185, 530, 315),
    ),
    (
        "nonattained_cotype_crop.png",
        10,
        fitz.Rect(75, 395, 560, 535),
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

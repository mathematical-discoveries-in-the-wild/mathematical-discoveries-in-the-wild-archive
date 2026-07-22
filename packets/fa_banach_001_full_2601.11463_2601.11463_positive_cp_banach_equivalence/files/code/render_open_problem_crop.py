#!/usr/bin/env python3
"""Render the page-27 crop containing Question 4.3 of arXiv:2601.11463."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[26]  # one-based page 27
    bounds = page.rect
    # Full readable page width.  The vertical interval contains the complete
    # lead-in and Question 4.3, without clipping its final line.
    crop = fitz.Rect(bounds.x0, 500, bounds.x1, 630)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), clip=crop, alpha=False)
    pixmap.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render the page-5 passage containing the open question."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[4]  # one-based page 5
    bounds = page.rect
    # Full page width; tightly includes the setup, equation (7), and complete
    # open-question sentence so the source text stays legible in the packet.
    crop = fitz.Rect(bounds.x0, 325, bounds.x1, 550)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
    pixmap.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render the page-11 open-question crop from the source paper."""

from pathlib import Path

import fitz


PACKET_DIR = Path(__file__).resolve().parents[1]
SOURCE_PDF = PACKET_DIR / "source_paper.pdf"
OUTPUT_PNG = PACKET_DIR / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE_PDF)
    page = document[10]  # Printed page 11.
    clip = fitz.Rect(70, 160, 542, 304)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pixmap.save(OUTPUT_PNG)


if __name__ == "__main__":
    main()


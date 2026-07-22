#!/usr/bin/env python3
"""Render Question 12.1 from page 54 of source_paper.pdf."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[53]  # PDF page 54, zero-indexed here.
    clip = fitz.Rect(90, 115, 522, 315)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()

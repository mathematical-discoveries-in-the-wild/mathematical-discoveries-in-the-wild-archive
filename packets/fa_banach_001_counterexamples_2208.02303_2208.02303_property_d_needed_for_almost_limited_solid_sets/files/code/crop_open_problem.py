#!/usr/bin/env python3
"""Render the source-paper crop containing Proposition 3.2.1."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PDF = ROOT / "source_paper.pdf"
OUT_DIR = ROOT / "figures"
OUT_PATH = OUT_DIR / "open_problem_crop.png"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(SOURCE_PDF)
    # Rendered source page 16, where Proposition 3.2.1 and the open
    # question appear. Coordinates were read from PyMuPDF text blocks.
    page = doc[15]
    crop = fitz.Rect(88, 255, 523, 448)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
    pix.save(OUT_PATH)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

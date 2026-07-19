#!/usr/bin/env python3
"""Render the source-paper crop containing Remark 6.11."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[15]  # printed page 16 in the PDF, containing Remark 6.11
    rect = fitz.Rect(45, 335, 550, 555)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

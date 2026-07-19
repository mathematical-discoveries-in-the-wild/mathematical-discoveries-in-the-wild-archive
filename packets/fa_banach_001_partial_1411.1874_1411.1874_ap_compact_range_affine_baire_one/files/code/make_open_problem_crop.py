#!/usr/bin/env python3
"""Recreate the Question 10.1 crop from the source PDF."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[37]  # PDF page 38, zero-based in PyMuPDF.
    clip = fitz.Rect(105, 435, 510, 516)
    pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()

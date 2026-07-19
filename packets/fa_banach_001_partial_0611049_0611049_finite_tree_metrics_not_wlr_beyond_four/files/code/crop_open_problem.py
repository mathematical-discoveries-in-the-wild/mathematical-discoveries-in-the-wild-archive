#!/usr/bin/env python3
"""Regenerate the crop of Question 5 from the source PDF."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[19]  # PDF page 20, zero-indexed
    rect = fitz.Rect(90, 120, 520, 505)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

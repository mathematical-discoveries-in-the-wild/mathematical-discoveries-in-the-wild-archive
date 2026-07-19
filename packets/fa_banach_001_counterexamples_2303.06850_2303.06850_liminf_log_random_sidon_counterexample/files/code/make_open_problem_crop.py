"""Render the source-paper crop containing Problem 8."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[29]  # source PDF page 30, "Questions on S and T"
    clip = fitz.Rect(0, 55, page.rect.width, 560)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

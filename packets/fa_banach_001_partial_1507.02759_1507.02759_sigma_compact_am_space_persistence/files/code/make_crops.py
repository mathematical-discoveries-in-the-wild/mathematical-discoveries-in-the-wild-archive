"""Create source-question crop for the 1507.02759 partial packet."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[1]
    # Page 2, paragraph containing the AM-space order-isomorphism question.
    rect = fitz.Rect(48, 355, 565, 455)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

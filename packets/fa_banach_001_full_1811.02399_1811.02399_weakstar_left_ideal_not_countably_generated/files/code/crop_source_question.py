"""Create a crop of the source question/provenance passage from arXiv:1811.02399."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[0]
    # Page 1: title, abstract, and the first paragraph posing the natural question.
    rect = fitz.Rect(45, 55, 565, 390)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

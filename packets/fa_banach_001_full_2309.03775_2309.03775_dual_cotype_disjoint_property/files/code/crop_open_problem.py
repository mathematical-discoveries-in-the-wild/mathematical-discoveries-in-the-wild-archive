"""Render the source-paper crop containing Remark 2.8.

The crop is intentionally full text width with generous vertical padding, so
that a reviewer can verify the exact open question from the arXiv PDF.
"""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[4]  # printed page 5, arXiv PDF page containing Remark 2.8
    rect = fitz.Rect(48, 610, 564, 724)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

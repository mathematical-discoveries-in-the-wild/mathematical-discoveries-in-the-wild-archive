"""Create the required full-width crop showing the source open problem."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[8]  # page 9 in the PDF viewer
    # Full page width, enough vertical context to include the end of
    # Proposition 6 and the complete open-problem line.
    rect = fitz.Rect(0, 280, page.rect.width, 385)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

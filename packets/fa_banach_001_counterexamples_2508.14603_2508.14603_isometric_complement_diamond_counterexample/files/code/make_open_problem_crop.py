from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[11]  # PDF page 12, Section 3.3.
    rect = fitz.Rect(50, 125, 550, 455)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect, alpha=False)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

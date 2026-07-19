from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[15]  # PDF page 16, Section 3.5.
    rect = fitz.Rect(82, 285, 530, 395)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

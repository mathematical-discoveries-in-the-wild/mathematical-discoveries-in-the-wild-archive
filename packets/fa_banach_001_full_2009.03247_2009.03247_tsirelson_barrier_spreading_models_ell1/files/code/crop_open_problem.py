from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[25]  # Page 26 in the PDF.
    rect = fitz.Rect(45, 40, 570, 235)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

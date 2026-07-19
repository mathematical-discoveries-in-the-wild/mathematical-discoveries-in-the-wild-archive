from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[9]  # PDF page 10, where Theorem 2.12 and the question appear.
    rect = fitz.Rect(45, 45, 570, 610)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=rect, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

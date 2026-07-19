from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[22]  # PDF page 23, zero-based index.
    rect = fitz.Rect(0, 220, page.rect.width, 340)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

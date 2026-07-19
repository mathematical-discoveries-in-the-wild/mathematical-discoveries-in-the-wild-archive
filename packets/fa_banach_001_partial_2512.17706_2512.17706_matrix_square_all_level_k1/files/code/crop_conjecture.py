from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "conjecture_5_2_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[30]  # PDF page 31, Conjecture 5.2.
    rect = fitz.Rect(35, 420, 610, 720)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

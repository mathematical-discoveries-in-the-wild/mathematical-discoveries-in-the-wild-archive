from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[6]
PDF = ROOT / "data/raw/arxiv/2305.01499/2305.01499.pdf"
OUT = Path(__file__).resolve().parents[1] / "figures/open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[12]  # PDF page 13.
    rect = fitz.Rect(70, 52, 545, 195)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()

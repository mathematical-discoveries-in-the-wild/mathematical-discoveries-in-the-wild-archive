from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[13]  # PDF page 14: optimality paragraph, Definition 4.2, Lemma 4.4.
    rect = fitz.Rect(72, 102, 540, 500)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

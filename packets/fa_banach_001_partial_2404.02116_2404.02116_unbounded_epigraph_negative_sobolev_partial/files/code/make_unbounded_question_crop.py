from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "unbounded_question_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[11]
    # Crop the paragraph immediately before the proof of Theorem 3.2.
    rect = fitz.Rect(55, 245, 545, 355)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

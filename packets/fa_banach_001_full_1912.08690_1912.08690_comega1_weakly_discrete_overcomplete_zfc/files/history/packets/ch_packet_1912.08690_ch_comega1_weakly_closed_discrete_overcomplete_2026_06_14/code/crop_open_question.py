from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_page10_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[9]
    # Page 10, paragraph beginning "One might wonder if the above result..."
    rect = fitz.Rect(54, 108, 558, 260)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    OUT.parent.mkdir(exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

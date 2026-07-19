from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_page20_question326.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[19]  # PDF page 20, zero indexed.
    rect = page.rect
    clip = fitz.Rect(36, 175, rect.width - 36, 520)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

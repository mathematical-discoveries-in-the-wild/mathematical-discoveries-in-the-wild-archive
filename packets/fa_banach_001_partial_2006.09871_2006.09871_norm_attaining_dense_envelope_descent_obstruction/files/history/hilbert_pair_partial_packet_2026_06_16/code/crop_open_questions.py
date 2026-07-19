from pathlib import Path

import fitz


BASE = Path(__file__).resolve().parents[1]
PDF = BASE / "source_paper.pdf"
OUT = BASE / "figures" / "open_questions_page.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[22]  # page 23, containing Question 6.1
    pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

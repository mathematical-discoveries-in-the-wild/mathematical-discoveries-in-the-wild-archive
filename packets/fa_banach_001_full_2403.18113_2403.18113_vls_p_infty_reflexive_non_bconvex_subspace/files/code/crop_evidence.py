from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "vls_question_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[11]  # Printed page 12.
    clip = fitz.Rect(45, 55, 550, 245)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    pix.save(OUT)


if __name__ == "__main__":
    main()

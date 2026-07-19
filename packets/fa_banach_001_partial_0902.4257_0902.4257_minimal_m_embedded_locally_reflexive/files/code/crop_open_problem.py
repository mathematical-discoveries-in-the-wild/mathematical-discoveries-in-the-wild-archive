from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[11]  # PDF page 12, local-reflexivity question remark.
    clip = fitz.Rect(90, 476, 522, 574)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()

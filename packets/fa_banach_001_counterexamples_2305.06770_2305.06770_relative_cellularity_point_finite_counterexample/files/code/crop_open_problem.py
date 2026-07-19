"""Crop the source paragraph containing the relative point-finite question."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[7]  # PDF page 8
    clip = fitz.Rect(55, 440, 560, 625)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

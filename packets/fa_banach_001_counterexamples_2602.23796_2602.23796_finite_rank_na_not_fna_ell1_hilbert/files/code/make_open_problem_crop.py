from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[10]  # Printed page 11 of the arXiv PDF.
    clip = fitz.Rect(35, 95, page.rect.width - 35, 372)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.6, 2.6), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

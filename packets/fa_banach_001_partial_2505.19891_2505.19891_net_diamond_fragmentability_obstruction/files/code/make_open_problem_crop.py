"""Render the source-paper crop used in the packet.

The crop shows Remark 3.7 on page 10 of arXiv:2505.19891, where the
weak-fragmentability-index problem for nets and grids is stated.
"""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[9]  # PDF page 10.
    # Full text-column crop around Remark 3.7, including margins.
    clip = fitz.Rect(70, 205, 542, 382)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

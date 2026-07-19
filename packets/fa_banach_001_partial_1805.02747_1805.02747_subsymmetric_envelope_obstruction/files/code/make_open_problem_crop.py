"""Render the open-question crop for the packet.

The crop uses page 35 of the arXiv PDF, where Question 6.1 appears.
It keeps the full readable text width and enough vertical context to show the
complete question.
"""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[34]  # one-based page 35
    clip = fitz.Rect(45, 550, 567, 648)
    pix = page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

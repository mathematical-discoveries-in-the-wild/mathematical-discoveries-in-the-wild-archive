"""Render the source-paper crop used by the packet.

Usage:
  conda run --no-capture-output -n sandbox python code/render_open_problem_crop.py
"""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[17]  # printed page 18; zero-indexed in PyMuPDF
    clip = fitz.Rect(52, 420, 560, 510)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

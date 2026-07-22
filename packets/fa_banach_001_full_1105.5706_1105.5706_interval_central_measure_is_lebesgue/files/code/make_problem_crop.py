"""Crop the open question from PDF page 7 of arXiv:1105.5706."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
doc = fitz.open(ROOT / "source_paper.pdf")
page = doc[6]
clip = fitz.Rect(72, 415, 525, 570)
pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
pix.save(ROOT / "figures" / "open_problem_crop.png")


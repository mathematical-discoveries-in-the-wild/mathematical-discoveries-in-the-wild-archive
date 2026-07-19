"""Render the open singularity question from page 25 of the source PDF."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"


document = fitz.open(SOURCE)
page = document[24]
clip = fitz.Rect(76, 254, 536, 319)
pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
pixmap.save(FIGURES / "open_problem_crop.png")

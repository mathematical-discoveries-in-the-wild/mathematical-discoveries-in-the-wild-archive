"""Render Question 6.6 and Lemma 6.8 from the copied arXiv source PDF."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"


def render_crop(page_number: int, rect: fitz.Rect, output_name: str) -> None:
    document = fitz.open(SOURCE)
    page = document[page_number - 1]
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    pixmap.save(FIGURES / output_name)


render_crop(48, fitz.Rect(116, 263, 496, 334), "open_problem_crop.png")
render_crop(48, fitz.Rect(116, 532, 496, 652), "source_lemma_6_8.png")

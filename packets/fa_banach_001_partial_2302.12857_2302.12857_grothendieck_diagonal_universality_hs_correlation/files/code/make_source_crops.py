"""Render the exact source theorem and open-problem blocks from arXiv:2302.12857."""

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


render_crop(3, fitz.Rect(116, 145, 496, 325), "source_equation_2.png")
render_crop(4, fitz.Rect(116, 106, 496, 172), "open_problem_crop.png")

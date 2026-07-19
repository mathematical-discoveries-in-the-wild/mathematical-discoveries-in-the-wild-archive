from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def render_page(page_number: int, filename: str) -> None:
    doc = fitz.open(PDF)
    page = doc[page_number - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    pix.save(FIGURES / filename)


if __name__ == "__main__":
    FIGURES.mkdir(exist_ok=True)
    render_page(3, "definition_context_page3.png")
    render_page(9, "open_problem_context_page9.png")

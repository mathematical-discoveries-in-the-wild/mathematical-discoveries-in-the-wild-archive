from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def render_page(page_index: int, name: str) -> None:
    doc = fitz.open(PDF)
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
    pix.save(FIGURES / name)


if __name__ == "__main__":
    FIGURES.mkdir(exist_ok=True)
    render_page(10, "maharam_decomposition_page11.png")
    render_page(12, "l1_amalgamation_lemma_page13.png")
    render_page(13, "sigma_finite_question_page14.png")

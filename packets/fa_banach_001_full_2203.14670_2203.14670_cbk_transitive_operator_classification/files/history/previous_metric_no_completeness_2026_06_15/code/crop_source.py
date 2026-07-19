from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def save_crop(page_index: int, rect, name: str, zoom: float = 2.2) -> None:
    doc = fitz.open(PDF)
    page = doc[page_index]
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, clip=fitz.Rect(*rect), alpha=False)
    pix.save(FIGURES / name)


if __name__ == "__main__":
    FIGURES.mkdir(exist_ok=True)
    # Page 27: section heading and full Theorem 16.1 statement.
    save_crop(26, (55, 425, 575, 635), "open_problem_crop.png")
    # Page 28: proof tail where the completeness hypothesis is used.
    save_crop(27, (55, 120, 575, 315), "source_proof_tail_crop.png")

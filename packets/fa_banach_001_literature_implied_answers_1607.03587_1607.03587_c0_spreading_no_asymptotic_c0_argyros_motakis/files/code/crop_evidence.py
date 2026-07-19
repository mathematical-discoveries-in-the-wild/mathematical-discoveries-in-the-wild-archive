from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)


def save_crop(pdf_name: str, page_index: int, y0: float, y1: float, out_name: str) -> None:
    doc = fitz.open(ROOT / pdf_name)
    page = doc[page_index]
    rect = fitz.Rect(36, y0, page.rect.width - 36, y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.8, 2.8), clip=rect, alpha=False)
    pix.save(FIGURES / out_name)


save_crop("source_paper.pdf", 13, 300, 520, "open_problem_crop.png")
save_crop("supporting_paper_1902.10092.pdf", 3, 120, 365, "supporting_theorem_a_crop.png")
save_crop("supporting_paper_1902.10092.pdf", 4, 155, 325, "supporting_theorem_c_crop.png")
save_crop("supporting_paper_1902.10092.pdf", 35, 118, 255, "supporting_no_asymptotic_c0_crop.png")

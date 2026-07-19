from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


def crop(pdf_name: str, page_index: int, rect, output_name: str, zoom: float = 2.0) -> None:
    doc = fitz.open(ROOT / pdf_name)
    page = doc[page_index]
    clip = fitz.Rect(*rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False)
    pix.save(FIGURES / output_name)


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    crop("source_paper.pdf", 19, (58, 315, 552, 455), "open_question_crop.png")
    crop("supporting_paper_2406.10986.pdf", 3, (58, 385, 540, 542), "supporting_intro_crop.png")
    crop("supporting_paper_2406.10986.pdf", 44, (58, 330, 540, 465), "supporting_corollary_crop.png")


if __name__ == "__main__":
    main()


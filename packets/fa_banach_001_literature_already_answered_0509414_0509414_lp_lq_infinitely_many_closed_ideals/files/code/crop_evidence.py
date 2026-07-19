from pathlib import Path

import fitz


BASE = Path(__file__).resolve().parents[1]
FIGURES = BASE / "figures"
FIGURES.mkdir(exist_ok=True)


def crop(pdf_name: str, page_index: int, rect, output_name: str, zoom: float = 3.0) -> None:
    doc = fitz.open(BASE / pdf_name)
    page = doc[page_index]
    clip = fitz.Rect(*rect)
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
    pix.save(FIGURES / output_name)


def main() -> None:
    crop(
        "source_paper.pdf",
        0,
        (60, 145, 555, 272),
        "open_problem_crop.png",
    )
    crop(
        "supporting_paper_1409.3480.pdf",
        0,
        (62, 205, 535, 465),
        "supporting_pietsch_problem_crop.png",
    )
    crop(
        "supporting_paper_1409.3480.pdf",
        1,
        (62, 165, 535, 235),
        "supporting_main_theorem_crop.png",
    )
    crop(
        "supporting_paper_2006.15415.pdf",
        13,
        (62, 455, 535, 555),
        "supporting_exact_cardinality_crop.png",
    )


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    doc = fitz.open(SOURCE)
    crops = [
        (
            "open_problem_page37_bottom.png",
            36,
            fitz.Rect(45, 520, 570, 780),
        ),
        (
            "open_problem_page38_top.png",
            37,
            fitz.Rect(45, 40, 570, 155),
        ),
    ]
    matrix = fitz.Matrix(2.5, 2.5)
    for name, page_index, rect in crops:
        pix = doc[page_index].get_pixmap(matrix=matrix, clip=rect, alpha=False)
        pix.save(FIGURES / name)


if __name__ == "__main__":
    main()

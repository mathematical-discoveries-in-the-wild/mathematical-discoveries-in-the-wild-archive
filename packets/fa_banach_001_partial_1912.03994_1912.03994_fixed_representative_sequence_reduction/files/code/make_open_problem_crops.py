from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    doc = fitz.open(PDF)
    specs = [
        (19, 60, 670, 535, 790, "open_problem_crop_page20.png"),
        (20, 60, 80, 535, 210, "open_problem_crop_page21.png"),
    ]
    for page_index, x0, y0, x1, y1, name in specs:
        page = doc[page_index]
        pix = page.get_pixmap(
            matrix=fitz.Matrix(2.5, 2.5),
            clip=fitz.Rect(x0, y0, x1, y1),
            alpha=False,
        )
        pix.save(FIGURES / name)


if __name__ == "__main__":
    main()


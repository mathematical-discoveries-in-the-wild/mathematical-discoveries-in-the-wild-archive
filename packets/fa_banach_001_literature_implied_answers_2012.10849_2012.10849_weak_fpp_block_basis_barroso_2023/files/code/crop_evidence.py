from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]


def crop(pdf_name, page_index, rect, out_name, zoom=2.5):
    doc = fitz.open(ROOT / pdf_name)
    page = doc[page_index]
    pix = page.get_pixmap(
        matrix=fitz.Matrix(zoom, zoom),
        clip=fitz.Rect(*rect),
        alpha=False,
    )
    pix.save(ROOT / "figures" / out_name)


def main():
    crop(
        "source_paper.pdf",
        4,
        (55, 235, 540, 535),
        "open_problem_crop.png",
    )
    crop(
        "supporting_paper_2302.11287.pdf",
        1,
        (55, 350, 555, 505),
        "supporting_context_crop.png",
    )
    crop(
        "supporting_paper_2302.11287.pdf",
        7,
        (55, 340, 555, 435),
        "supporting_theorem_crop.png",
    )


if __name__ == "__main__":
    main()

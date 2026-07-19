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
        (90, 280, 510, 430),
        "source_open_problems_crop.png",
    )
    crop(
        "supporting_paper_1411.4240.pdf",
        3,
        (90, 445, 510, 525),
        "supporting_theorem_3_3_crop.png",
    )
    crop(
        "supporting_paper_1411.4240.pdf",
        4,
        (90, 605, 510, 830),
        "supporting_example_3_4_crop.png",
    )
    crop(
        "supporting_paper_1411.4240.pdf",
        5,
        (90, 112, 510, 148),
        "supporting_example_3_4_continuation_crop.png",
    )


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)


def render_crop(pdf_path: Path, page_index: int, rect, zoom: float = 3.0) -> Image.Image:
    doc = fitz.open(pdf_path)
    page = doc[page_index]
    clip = fitz.Rect(*rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


def save_stitched_open_question() -> None:
    source_pdf = ROOT / "source_paper.pdf"
    doc = fitz.open(source_pdf)
    page_width = doc[24].rect.width

    # The open question begins near the bottom of p. 25 and continues onto p. 26.
    first = render_crop(source_pdf, 24, (0, 548, page_width, 820))
    second = render_crop(source_pdf, 25, (0, 82, page_width, 242))

    gap = 24
    out = Image.new(
        "RGB",
        (max(first.width, second.width), first.height + gap + second.height),
        "white",
    )
    out.paste(first, (0, 0))
    out.paste(second, (0, first.height + gap))
    out.save(FIGURES / "open_problem_crop.png")


def save_support_crops() -> None:
    support_pdf = ROOT / "supporting_paper_2604.01875.pdf"
    doc = fitz.open(support_pdf)
    page_width = doc[1].rect.width
    theorem = render_crop(support_pdf, 1, (0, 430, page_width, 540))
    theorem.save(FIGURES / "supporting_theorem_1_1_crop.png")

    page_width = doc[4].rect.width
    relation = render_crop(support_pdf, 4, (0, 182, page_width, 322))
    relation.save(FIGURES / "supporting_prop_2_2_crop.png")


if __name__ == "__main__":
    save_stitched_open_question()
    save_support_crops()
    print("Wrote evidence crops to", FIGURES)

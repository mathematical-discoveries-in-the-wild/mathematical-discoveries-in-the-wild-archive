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


def save_source_crop() -> None:
    source_pdf = ROOT / "source_paper.pdf"
    doc = fitz.open(source_pdf)
    page_width = doc[2].rect.width
    crop = render_crop(source_pdf, 2, (34, 330, page_width - 34, 432))
    crop.save(FIGURES / "source_conjecture_crop.png")


def save_support_crop() -> None:
    support_pdf = ROOT / "supporting_paper_2207.03614.pdf"
    doc = fitz.open(support_pdf)
    page_width = doc[4].rect.width
    crop = render_crop(support_pdf, 4, (70, 430, page_width - 55, 535))
    crop.save(FIGURES / "supporting_corollary_crop.png")


if __name__ == "__main__":
    save_source_crop()
    save_support_crop()
    print("Wrote evidence crops to", FIGURES)

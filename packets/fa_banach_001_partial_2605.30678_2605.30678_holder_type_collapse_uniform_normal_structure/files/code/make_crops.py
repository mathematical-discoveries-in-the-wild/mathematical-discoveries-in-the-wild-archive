from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
FIGURES = PACKET / "figures"


def crop_phrase(pdf_name: str, page_no: int, phrase: str, out_name: str, above: float, below: float) -> None:
    """Crop a paragraph around the first occurrence of phrase on a 1-based page."""
    pdf_path = PACKET / pdf_name
    doc = fitz.open(pdf_path)
    page = doc[page_no - 1]
    hits = page.search_for(phrase)
    if not hits:
        raise RuntimeError(f"phrase not found on page {page_no}: {phrase!r}")

    hit = hits[0]
    clip = fitz.Rect(
        36,
        max(0, hit.y0 - above),
        page.rect.width - 36,
        min(page.rect.height, hit.y1 + below),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
    pix.save(FIGURES / out_name)


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    crop_phrase(
        "source_paper.pdf",
        3,
        "While these results significantly",
        "source_future_investigation_crop.png",
        above=80,
        below=175,
    )
    crop_phrase(
        "source_paper.pdf",
        4,
        "While this problem remains open",
        "source_dlt_remains_open_crop.png",
        above=105,
        below=95,
    )
    crop_phrase(
        "supporting_paper_2201.02802.pdf",
        11,
        "Theorem 5.3.",
        "supporting_uniform_normal_structure_crop.png",
        above=70,
        below=135,
    )


if __name__ == "__main__":
    main()

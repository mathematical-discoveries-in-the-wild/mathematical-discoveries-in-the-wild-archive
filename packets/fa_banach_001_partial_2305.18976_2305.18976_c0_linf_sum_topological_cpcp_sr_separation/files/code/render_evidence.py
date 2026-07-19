from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def render_clip(page_index: int, clip, out_name: str, zoom: float = 2.1) -> None:
    doc = fitz.open(PDF)
    pix = doc[page_index].get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(*clip), alpha=False)
    pix.save(FIGURES / out_name)


def dump_context(needle: str) -> None:
    doc = fitz.open(PDF)
    for page_index, page in enumerate(doc):
        text = page.get_text()
        pos = text.find(needle)
        if pos >= 0:
            print(f"{needle!r}: page {page_index + 1}")
            print(text[max(0, pos - 400) : pos + 800].replace("\n", " | "))
            return
    raise RuntimeError(f"Could not find {needle!r}")


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    dump_context("starting from a Banach space")
    dump_context("There exists a locally convex topology")
    render_clip(13, (55, 95, 560, 265), "broad_question_crop.png")
    render_clip(14, (65, 585, 540, 705), "c0_theorem_crop.png")


if __name__ == "__main__":
    main()

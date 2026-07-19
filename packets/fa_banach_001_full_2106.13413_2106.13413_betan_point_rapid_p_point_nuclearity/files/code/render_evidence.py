from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
SUPPORT = ROOT / "supporting_paper_1208.3690.pdf"
FIGURES = ROOT / "figures"


def find_page(pdf_path: Path, needle: str) -> int:
    doc = fitz.open(pdf_path)
    for index, page in enumerate(doc):
        if needle in page.get_text():
            return index
    raise RuntimeError(f"Could not find {needle!r} in {pdf_path}")


def render_clip(pdf_path: Path, page_index: int, clip, out_name: str, zoom: float = 2.3) -> None:
    doc = fitz.open(pdf_path)
    page = doc[page_index]
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, clip=fitz.Rect(*clip), alpha=False)
    pix.save(FIGURES / out_name)


def dump_context(pdf_path: Path, needle: str) -> None:
    doc = fitz.open(pdf_path)
    page_index = find_page(pdf_path, needle)
    text = doc[page_index].get_text()
    pos = text.find(needle)
    context = text[max(0, pos - 500) : pos + 900]
    print(f"{pdf_path.name}: page {page_index + 1}")
    print(context.replace("\n", " | "))


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    source_page = find_page(SOURCE, "Problem 5.5")
    support_page = find_page(SUPPORT, "Theorem 1.1")
    dump_context(SOURCE, "Problem 5.5")
    dump_context(SUPPORT, "Theorem 1.1")

    # Letter page coordinates in points. These crops isolate the source problem
    # and the rapid/summable-ideal characterization used in the proof.
    render_clip(SOURCE, source_page, (55, 395, 610, 610), "open_problem_5_5_crop.png")
    render_clip(SUPPORT, support_page, (105, 520, 505, 640), "rapid_summable_theorem_page1_crop.png")
    render_clip(SUPPORT, support_page + 1, (105, 105, 505, 170), "rapid_summable_theorem_page2_crop.png")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    target = None
    for page_index, page in enumerate(doc):
        rects = page.search_for("Problem 1")
        if rects:
            target = (page_index, rects[0])
            break
    if target is None:
        raise RuntimeError("Could not find Problem 1 in source_paper.pdf")

    page_index, rect = target
    page = doc[page_index]
    clip = fitz.Rect(
        50,
        max(0, rect.y0 - 130),
        page.rect.width - 50,
        min(page.rect.height, rect.y1 + 130),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} from PDF page {page_index + 1}")


if __name__ == "__main__":
    main()

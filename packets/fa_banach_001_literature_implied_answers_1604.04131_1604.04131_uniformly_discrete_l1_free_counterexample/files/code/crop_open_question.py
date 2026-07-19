"""Recreate the open-question screenshot from the source PDF."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "Let M be a uniformly discrete metric space"
    for page_index, page in enumerate(doc):
        rects = page.search_for(needle)
        if not rects:
            continue
        rect = rects[0]
        clip = fitz.Rect(
            0,
            max(0, rect.y0 - 105),
            page.rect.width,
            min(page.rect.height, rect.y1 + 95),
        )
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
        OUT.parent.mkdir(exist_ok=True)
        pix.save(OUT)
        print(f"wrote {OUT} from PDF page {page_index + 1}")
        return
    raise RuntimeError(f"Could not find {needle!r}")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "Suppose p"
    for page_index, page in enumerate(doc):
        hits = page.search_for(needle)
        if not hits:
            hits = page.search_for("Does X have the SHAI property")
        if not hits:
            continue
        rect = hits[0]
        # The problem spans several lines.  Crop a generous band around it.
        clip = fitz.Rect(
            0,
            max(0, rect.y0 - 75),
            page.rect.x1,
            min(page.rect.y1, rect.y1 + 145),
        )
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
        pix.save(OUT)
        print(f"wrote {OUT} from page {page_index + 1}")
        return
    raise SystemExit("open problem text not found")


if __name__ == "__main__":
    main()

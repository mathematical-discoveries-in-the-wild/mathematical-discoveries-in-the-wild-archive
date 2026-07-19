from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "So, we cannot find"
    for page_index, page in enumerate(doc):
        text = page.get_text()
        if needle in text or "slowly going to zero" in text:
            rects = page.search_for("Open question")
            if rects:
                y0 = max(0, rects[0].y0 - 70)
            else:
                y0 = page.rect.height * 0.56
            crop = fitz.Rect(45, y0, page.rect.width - 45, min(page.rect.height - 45, y0 + 230))
            pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
            OUT.parent.mkdir(parents=True, exist_ok=True)
            pix.save(OUT)
            print(f"wrote {OUT} from page {page_index + 1}")
            return
    raise RuntimeError("Could not find Section 7 open question text")


if __name__ == "__main__":
    main()

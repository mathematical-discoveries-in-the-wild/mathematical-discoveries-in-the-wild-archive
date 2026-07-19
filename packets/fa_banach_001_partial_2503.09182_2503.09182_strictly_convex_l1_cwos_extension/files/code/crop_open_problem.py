from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    for page in doc:
        text = " ".join(page.get_text().split())
        if "A natural question" in text and "injective tensor product" in text:
            rects = page.search_for("A natural question")
            if not rects:
                raise RuntimeError("Found question page but not crop anchor")
            anchor = rects[0]
            clip = fitz.Rect(45, max(35, anchor.y0 - 45), page.rect.width - 45, min(page.rect.height - 35, anchor.y1 + 115))
            pix = page.get_pixmap(matrix=fitz.Matrix(2.6, 2.6), clip=clip, alpha=False)
            pix.save(OUT)
            print(f"wrote {OUT} from PDF page {page.number + 1}")
            return
    raise RuntimeError("Could not find natural question prompt in source PDF")


if __name__ == "__main__":
    main()

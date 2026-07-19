from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "finally, we note that throughout section 3"
    for page in doc:
        text = " ".join(page.get_text().split()).lower()
        if needle in text:
            rects = page.search_for("Finally, we note")
            if not rects:
                raise RuntimeError("Located page text but could not locate crop anchor")
            anchor = rects[0]
            clip = fitz.Rect(45, max(35, anchor.y0 - 100), page.rect.width - 45, min(page.rect.height - 35, anchor.y1 + 85))
            pix = page.get_pixmap(matrix=fitz.Matrix(2.6, 2.6), clip=clip, alpha=False)
            pix.save(OUT)
            print(f"wrote {OUT} from PDF page {page.number + 1}")
            return
    raise RuntimeError("Did not find final complete-separable-metric-spaces problem prompt")


if __name__ == "__main__":
    main()

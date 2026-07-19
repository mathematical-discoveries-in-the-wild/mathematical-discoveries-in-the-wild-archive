from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    for page_index, page in enumerate(doc):
        text = page.get_text()
        if "operator" in text and "Reiter" in text and "Problem 47" in text:
            hits = page.search_for("The particular case")
            if hits:
                y0 = max(0, hits[0].y0 - 25)
            else:
                y0 = page.rect.height * 0.50
            crop = fitz.Rect(45, y0, page.rect.width - 45, min(page.rect.height - 45, y0 + 270))
            pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
            OUT.parent.mkdir(parents=True, exist_ok=True)
            pix.save(OUT)
            print(f"wrote {OUT} from page {page_index + 1}")
            return
    raise RuntimeError("Could not locate operator alpha problem")


if __name__ == "__main__":
    main()

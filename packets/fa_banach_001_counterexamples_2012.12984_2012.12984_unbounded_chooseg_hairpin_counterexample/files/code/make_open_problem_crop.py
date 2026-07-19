from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    for page_index, page in enumerate(doc):
        hits = page.search_for("Question. Does Lemma 4.2 hold")
        if not hits:
            continue
        hit = hits[0]
        rect = fitz.Rect(55, max(0, hit.y0 - 125), page.rect.width - 55, min(page.rect.height, hit.y1 + 65))
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        pix.save(OUT)
        print(f"wrote {OUT} from PDF page {page_index + 1}")
        return
    raise SystemExit("question text not found")


if __name__ == "__main__":
    main()

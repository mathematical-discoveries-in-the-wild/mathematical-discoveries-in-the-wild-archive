from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    for index, page in enumerate(doc):
        text = page.get_text()
        if "We do not know" in text:
            print(f"found passage on PDF page {index + 1}")
            print(text[:1200].replace("\n", " | "))
            # Full-width crop around Lemma 3.4, the remark after it, and
            # Remark 3.5. Coordinates are in PDF points.
            rect = fitz.Rect(45, 470, 570, 765)
            pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=rect, alpha=False)
            pix.save(OUT)
            print(f"wrote {OUT}")
            return
    raise SystemExit("open-problem passage not found")


if __name__ == "__main__":
    main()

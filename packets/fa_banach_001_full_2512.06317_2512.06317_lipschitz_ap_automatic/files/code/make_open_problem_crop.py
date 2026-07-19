from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"
TMP_FULL = ROOT / "tmp" / "source_page18_full.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[17]  # Page 18 in the PDF, zero-indexed here.
    matrix = fitz.Matrix(3, 3)
    TMP_FULL.parent.mkdir(parents=True, exist_ok=True)
    page.get_pixmap(matrix=matrix, alpha=False).save(TMP_FULL)

    # Full text-width crop around the final open-question bullet list.
    clip = fitz.Rect(55, 405, 557, 560)
    pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()

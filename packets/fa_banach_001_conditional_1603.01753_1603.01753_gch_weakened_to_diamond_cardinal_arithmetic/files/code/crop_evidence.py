from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    doc = fitz.open(SOURCE)
    page = doc[4]  # PDF page 5, Introduction near the Theorem 3 repeat.
    # Full readable page width, with vertical room for the theorem ending,
    # the open-question paragraph, and the black-box context.
    clip = fitz.Rect(55, 335, 557, 505)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    pix.save(FIGURES / "open_problem_page5_gch_removal.png")


if __name__ == "__main__":
    main()

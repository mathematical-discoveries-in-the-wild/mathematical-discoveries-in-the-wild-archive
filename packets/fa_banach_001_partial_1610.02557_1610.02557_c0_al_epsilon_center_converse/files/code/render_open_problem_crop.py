from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[16]  # printed page 17
    # Paragraph from Definition 4.2 through the displayed rho_epsilon formula.
    clip = fitz.Rect(110, 470, 505, 705)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

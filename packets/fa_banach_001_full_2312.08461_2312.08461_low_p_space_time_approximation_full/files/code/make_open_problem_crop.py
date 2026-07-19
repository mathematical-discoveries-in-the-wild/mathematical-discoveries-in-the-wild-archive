from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    # Page 4 contains the current p >= 2 theorem statement and the p < 2
    # future-work passage.  The crop records the latter.
    page = doc[3]
    clip = fitz.Rect(72, 595, 540, 642)
    pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

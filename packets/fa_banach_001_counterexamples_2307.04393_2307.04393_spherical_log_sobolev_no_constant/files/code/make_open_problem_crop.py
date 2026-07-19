from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[7]  # Source page 8: introduction, spherical log-Sobolev question.
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    src = ROOT / "tmp" / "source_page_8_for_crop.png"
    src.parent.mkdir(exist_ok=True)
    pix.save(src)

    import PIL.Image

    img = PIL.Image.open(src)
    # Coordinates are at 2x render scale and isolate the question plus formula.
    crop = img.crop((145, 1125, 1115, 1505))
    OUT.parent.mkdir(exist_ok=True)
    crop.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

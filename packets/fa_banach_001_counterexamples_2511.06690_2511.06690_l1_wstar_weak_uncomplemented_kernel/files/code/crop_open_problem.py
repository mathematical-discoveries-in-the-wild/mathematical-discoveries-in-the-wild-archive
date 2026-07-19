from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    matrix = fitz.Matrix(2.5, 2.5)
    pieces = []
    specs = [
        ("open_problem_crop_page11.png", 10, (35, 335, 577, 760)),
        ("open_problem_crop_page12.png", 11, (35, 45, 577, 205)),
    ]
    for name, page_index, box in specs:
        page = doc[page_index]
        crop = fitz.Rect(*box)
        path = ROOT / "figures" / name
        pix = page.get_pixmap(matrix=matrix, clip=crop, alpha=False)
        pix.save(path)
        pieces.append(Image.open(path))
        print(f"wrote {path} from page {page_index + 1}, crop={box}")

    width = max(piece.width for piece in pieces)
    height = sum(piece.height for piece in pieces)
    stitched = Image.new("RGB", (width, height), "white")
    y = 0
    for piece in pieces:
        stitched.paste(piece, (0, y))
        y += piece.height
    stitched.save(OUT)
    print(f"wrote stitched crop {OUT}")


if __name__ == "__main__":
    main()

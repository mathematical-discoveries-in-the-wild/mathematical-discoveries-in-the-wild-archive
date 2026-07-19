from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[6]
PDF = ROOT / "data/raw/arxiv/1806.00980/1806.00980.pdf"
OUT = Path(__file__).resolve().parents[1] / "figures/open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    matrix = fitz.Matrix(3, 3)

    heading_pix = doc[34].get_pixmap(
        matrix=matrix, clip=fitz.Rect(112, 652, 500, 704), alpha=False
    )
    body_pix = doc[35].get_pixmap(
        matrix=matrix, clip=fitz.Rect(112, 108, 500, 378), alpha=False
    )

    heading = Image.frombytes("RGB", (heading_pix.width, heading_pix.height), heading_pix.samples)
    body = Image.frombytes("RGB", (body_pix.width, body_pix.height), body_pix.samples)
    gap = Image.new("RGB", (body.width, 18), "white")
    stitched = Image.new("RGB", (body.width, heading.height + gap.height + body.height), "white")
    stitched.paste(heading, (0, 0))
    stitched.paste(gap, (0, heading.height))
    stitched.paste(body, (0, heading.height + gap.height))
    stitched.save(OUT)
    print(f"wrote {OUT} ({stitched.width}x{stitched.height})")


if __name__ == "__main__":
    main()

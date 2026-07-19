from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "main remaining challenge"
    for page_index, page in enumerate(doc):
        rects = page.search_for(needle)
        if not rects:
            continue
        hit = rects[0]
        page_rect = page.rect
        crop1 = fitz.Rect(
            page_rect.x0 + 35,
            max(page_rect.y0, hit.y0 - 55),
            page_rect.x1 - 35,
            page_rect.y1 - 25,
        )
        next_page = doc[page_index + 1]
        next_rect = next_page.rect
        crop2 = fitz.Rect(
            next_rect.x0 + 35,
            next_rect.y0 + 55,
            next_rect.x1 - 35,
            next_rect.y0 + 190,
        )
        matrix = fitz.Matrix(2.5, 2.5)
        pix1 = page.get_pixmap(matrix=matrix, clip=crop1, alpha=False)
        pix2 = next_page.get_pixmap(matrix=matrix, clip=crop2, alpha=False)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        img1 = Image.frombytes("RGB", (pix1.width, pix1.height), pix1.samples)
        img2 = Image.frombytes("RGB", (pix2.width, pix2.height), pix2.samples)
        width = max(img1.width, img2.width)
        stitched = Image.new("RGB", (width, img1.height + img2.height), "white")
        stitched.paste(img1, (0, 0))
        stitched.paste(img2, (0, img1.height))
        stitched.save(OUT)
        print(f"wrote {OUT} from PDF pages {page_index + 1}-{page_index + 2}")
        return
    raise SystemExit(f"Could not find {needle!r} in {PDF}")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def render_clip(doc, page_index, rect, zoom=3):
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(rect), alpha=False)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


def main():
    doc = fitz.open(PDF)
    clips = [
        render_clip(doc, 18, (100, 648, 520, 724)),
        render_clip(doc, 19, (100, 96, 520, 164)),
    ]
    width = max(img.width for img in clips)
    height = sum(img.height for img in clips) + 18
    canvas = Image.new("RGB", (width, height), "white")
    y = 0
    for img in clips:
        canvas.paste(img, (0, y))
        y += img.height + 18
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT)


if __name__ == "__main__":
    main()

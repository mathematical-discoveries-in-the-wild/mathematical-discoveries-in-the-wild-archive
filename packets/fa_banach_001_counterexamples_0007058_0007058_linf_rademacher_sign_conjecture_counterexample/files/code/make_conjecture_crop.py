from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "source_conjectures_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[1]
    rects = page.search_for("CONJECTURE 2")
    if not rects:
        raise RuntimeError("Could not find CONJECTURE 2 on source PDF page 2")
    y0 = max(0, rects[0].y0 - 80)
    clip = fitz.Rect(55, y0, page.rect.width - 45, min(page.rect.height, y0 + 360))
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    target_page = None
    rects = []
    for page in doc:
        page_rects = page.search_for("What is a natural condition")
        page_rects += page.search_for("boundedly complete basis")
        if page_rects:
            target_page = page
            rects = page_rects
            break
    if target_page is None:
        raise RuntimeError("Could not find the open-problem text in source_paper.pdf")

    clip = rects[0]
    for rect in rects[1:]:
        clip |= rect
    page_box = target_page.rect
    clip.x0 = max(page_box.x0, clip.x0 - 45)
    clip.x1 = min(page_box.x1, clip.x1 + 45)
    clip.y0 = max(page_box.y0, clip.y0 - 145)
    clip.y1 = min(page_box.y1, clip.y1 + 85)

    pix = target_page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    target_page = None
    rects = []
    needles = [
        "Which C0-semigroups",
        "Which C",
        "admit an (approximate) invertible dilation",
    ]
    for page in doc:
        found = []
        for needle in needles:
            found.extend(page.search_for(needle))
        if found:
            target_page = page
            rects = found
            break
    if target_page is None:
        raise RuntimeError("Could not locate the dilation question in source_paper.pdf")

    clip = rects[0]
    for rect in rects[1:]:
        clip |= rect
    box = target_page.rect
    clip.x0 = max(box.x0, clip.x0 - 55)
    clip.x1 = min(box.x1, clip.x1 + 55)
    clip.y0 = max(box.y0, clip.y0 - 95)
    clip.y1 = min(box.y1, clip.y1 + 70)

    pix = target_page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
pdf_path = ROOT / "source_paper.pdf"
out_path = ROOT / "figures" / "open_problem_crop.png"
out_path.parent.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
needles = [
    "It is interesting to obtain the LLN",
    "Under the assumptions of Theorem",
]

for page in doc:
    rects = []
    for needle in needles:
        rects.extend(page.search_for(needle))
    if rects:
        rect = rects[0]
        for other in rects[1:]:
            rect |= other
        rect.x0 = max(0, rect.x0 - 30)
        rect.x1 = min(page.rect.x1, rect.x1 + 260)
        rect.y0 = max(0, rect.y0 - 40)
        rect.y1 = min(page.rect.y1, rect.y1 + 140)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
        pix.save(out_path)
        print(out_path)
        break
else:
    raise SystemExit("Could not find conjecture text in source PDF")

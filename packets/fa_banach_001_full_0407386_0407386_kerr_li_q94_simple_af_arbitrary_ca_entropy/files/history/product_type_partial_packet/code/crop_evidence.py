from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


doc = fitz.open(PDF)
target_page = None
for i, page in enumerate(doc):
    text = page.get_text()
    if "Question 9.4" in text:
        target_page = i
        break

if target_page is None:
    raise SystemExit("Could not find the source question page")

page = doc[target_page]
rects = page.search_for("Question 9.4")
if not rects:
    raise SystemExit("Could not locate crop anchor")

anchor = rects[0]
clip = fitz.Rect(40, max(0, anchor.y0 - 190), page.rect.width - 40, min(page.rect.height, anchor.y1 + 95))
pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip, alpha=False)
pix.save(OUT)
print(f"page={target_page + 1} crop={OUT}")

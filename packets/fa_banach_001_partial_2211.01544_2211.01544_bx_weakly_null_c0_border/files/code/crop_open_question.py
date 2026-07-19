from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(PDF)
needle = "Which Banach spaces"
for page in doc:
    hits = page.search_for(needle)
    if not hits:
        continue
    rect = hits[0]
    crop = fitz.Rect(45, max(0, rect.y0 - 125), page.rect.width - 45, min(page.rect.height, rect.y1 + 105))
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} from page {page.number + 1}")
    break
else:
    raise SystemExit(f"could not find {needle!r}")

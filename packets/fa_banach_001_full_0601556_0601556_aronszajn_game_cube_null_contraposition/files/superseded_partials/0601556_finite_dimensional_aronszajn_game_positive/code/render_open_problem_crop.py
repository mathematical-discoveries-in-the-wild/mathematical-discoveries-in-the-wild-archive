import fitz

pdf = "../source_paper.pdf"
out = "../figures/open_problem_crop.png"

doc = fitz.open(pdf)
for index, page in enumerate(doc):
    hits = page.search_for("The converse is open")
    if hits:
        rect = hits[0]
        clip = fitz.Rect(
            40,
            max(0, rect.y0 - 80),
            page.rect.width - 40,
            min(page.rect.height, rect.y1 + 80),
        )
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip)
        pix.save(out)
        print(f"wrote {out} from page {index + 1}")
        break
else:
    raise RuntimeError("open-question text not found")

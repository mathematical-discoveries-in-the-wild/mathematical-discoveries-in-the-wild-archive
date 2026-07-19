from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"
META = ROOT / "figures" / "crop_metadata.txt"


def main() -> None:
    doc = fitz.open(PDF)
    target = None
    for page_index, page in enumerate(doc):
        text = page.get_text("text")
        if "Does the pair" in text and "(c0, c0)" in text:
            rects = page.search_for("Does the pair")
            if not rects:
                continue
            target = (page_index, page, rects[0])
            break

    if target is None:
        raise RuntimeError("Could not locate the open question in the source PDF.")

    page_index, page, hit = target
    page_rect = page.rect

    # Full-width crop with enough vertical context to show the lead-in,
    # the question label, and the whole question text.
    crop = fitz.Rect(
        page_rect.x0,
        max(page_rect.y0, hit.y0 - 78),
        page_rect.x1,
        min(page_rect.y1, hit.y1 + 42),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)

    META.write_text(
        "\n".join(
            [
                f"source={PDF}",
                f"page_index={page_index}",
                f"page_number={page_index + 1}",
                f"crop_points={tuple(round(v, 2) for v in crop)}",
                f"rendered_pixels={pix.width}x{pix.height}",
                "target_text=Question 3.6. Does the pair (c0, c0) have the CPPm?",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

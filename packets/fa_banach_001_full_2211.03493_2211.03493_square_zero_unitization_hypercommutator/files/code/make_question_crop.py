#!/usr/bin/env python3
"""Best-effort crop of the source question from the arXiv PDF."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    packet = Path(__file__).resolve().parents[1]
    pdf_path = packet / "source_paper.pdf"
    out_path = packet / "figures" / "open_problem_crop.png"
    fallback_path = packet / "figures" / "open_problem_excerpt.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        import fitz  # type: ignore
    except Exception as exc:  # pragma: no cover - environment-dependent fallback
        fallback_path.write_text(
            "PyMuPDF was unavailable, so no PDF crop was rendered.\n"
            f"Import error: {exc!r}\n",
            encoding="utf-8",
        )
        return

    doc = fitz.open(pdf_path)
    for page_number, page in enumerate(doc):
        blocks = page.get_text("blocks")
        question_blocks = []
        for block in blocks:
            x0, y0, x1, y1, text = block[:5]
            normalized = " ".join(text.lower().split())
            if (
                "question 3.6" in normalized
                or "does there exist an" in normalized
                or "with a nonzero hyper-commutator" in normalized
            ):
                question_blocks.append(fitz.Rect(x0, y0, x1, y1))

        if not question_blocks:
            continue

        crop = question_blocks[0]
        for rect in question_blocks[1:]:
            crop |= rect
        crop.x0 = max(0, crop.x0 - 72)
        crop.y0 = max(0, crop.y0 - 72)
        crop.x1 = min(page.rect.x1, crop.x1 + 72)
        crop.y1 = min(page.rect.y1, crop.y1 + 96)

        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
        pix.save(out_path)
        fallback_path.write_text(
            f"Rendered crop from PDF page {page_number + 1}.\n",
            encoding="utf-8",
        )
        return

    fallback_path.write_text(
        "Could not locate the question text by PDF text search.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

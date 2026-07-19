from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE_PDF = ROOT / "source_paper.pdf"
SUPPORTING_PDF = ROOT / "supporting_paper_2501.16855.pdf"
META = FIGURES / "crop_metadata.txt"


def crop_search(pdf_path: Path, needle: str, out_name: str, before: float, after: float) -> str:
    doc = fitz.open(pdf_path)
    for page_index, page in enumerate(doc):
        text = page.get_text("text")
        if needle not in text:
            continue
        rects = page.search_for(needle)
        if not rects:
            continue
        hit = rects[0]
        page_rect = page.rect
        crop = fitz.Rect(
            page_rect.x0,
            max(page_rect.y0, hit.y0 - before),
            page_rect.x1,
            min(page_rect.y1, hit.y1 + after),
        )
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
        out_path = FIGURES / out_name
        pix.save(out_path)
        return "\n".join(
            [
                f"{out_name}:",
                f"  source={pdf_path.name}",
                f"  page_number={page_index + 1}",
                f"  needle={needle}",
                f"  crop_points={tuple(round(v, 2) for v in crop)}",
                f"  rendered_pixels={pix.width}x{pix.height}",
            ]
        )
    raise RuntimeError(f"Could not locate {needle!r} in {pdf_path}")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    records = [
        crop_search(
            SOURCE_PDF,
            "Question 1. Is there a Banach space",
            "open_problem_crop.png",
            before=72,
            after=82,
        ),
        crop_search(
            SUPPORTING_PDF,
            "Question 1. Is there a Banach space",
            "supporting_answer_crop.png",
            before=160,
            after=95,
        ),
        crop_search(
            SUPPORTING_PDF,
            "Theorem 2.8. Let X be a Banach space",
            "supporting_theorem_crop.png",
            before=35,
            after=60,
        ),
    ]
    META.write_text("\n\n".join(records) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

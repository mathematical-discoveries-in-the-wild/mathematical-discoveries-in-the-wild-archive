from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def render_crop(page_number: int, rect, out_name: str, zoom: float = 2.4) -> None:
    doc = fitz.open(PDF)
    page = doc[page_number - 1]
    clip = fitz.Rect(*rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False)
    FIGURES.mkdir(exist_ok=True)
    pix.save(FIGURES / out_name)


def main() -> None:
    # Page 11: Remark 5.3 identifies Schatten classes and says that
    # corresponding upper bounds are not pursued in the source paper.
    render_crop(
        11,
        (64, 490, 532, 770),
        "noncommutative_schatten_gap_crop.png",
    )

    # Page 12: the appendix states that the sharp covering-index decay
    # remains open even for the classical Schatten classes.
    render_crop(
        12,
        (64, 270, 532, 405),
        "open_problem_crop.png",
    )


if __name__ == "__main__":
    main()

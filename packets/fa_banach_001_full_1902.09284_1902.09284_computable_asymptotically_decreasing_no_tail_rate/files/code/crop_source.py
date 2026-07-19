"""Crop the two pieces of Powell's pages 4--5 containing the conjecture."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RENDERED = ROOT / "tmp" / "pdfs"
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], target: str) -> None:
    with Image.open(RENDERED / source) as image:
        image.crop(box).save(FIGURES / target, optimize=True)


crop(
    "source-page-04.png",
    (180, 1450, 1360, 1905),
    "open_problem_context.png",
)
crop(
    "source-page-05.png",
    (180, 285, 1360, 430),
    "open_problem_continuation.png",
)
crop(
    "source-page-05.png",
    (180, 1610, 1360, 1705),
    "open_problem_footnote.png",
)

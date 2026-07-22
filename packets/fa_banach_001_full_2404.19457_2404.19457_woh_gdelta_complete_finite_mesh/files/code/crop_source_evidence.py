"""Render and stitch the open-question passage from source PDF pages 24–25."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp" / "source_pages"
FIGURES = PACKET / "figures"


def main() -> None:
    page24 = Image.open(TMP / "page-24.png").convert("RGB")
    page25 = Image.open(TMP / "page-25.png").convert("RGB")

    w24, h24 = page24.size
    w25, h25 = page25.size
    if w24 != w25:
        raise ValueError("Rendered source pages have different widths")

    # Keep full page width. The first crop includes the transition from the
    # preceding open question; the second includes all of equation (7.7) and
    # the exact-complexity question.
    top = page24.crop((0, int(0.69 * h24), w24, int(0.90 * h24)))
    bottom = page25.crop((0, int(0.035 * h25), w25, int(0.35 * h25)))

    gap = 24
    stitched = Image.new("RGB", (w24, top.height + gap + bottom.height), "white")
    stitched.paste(top, (0, 0))
    stitched.paste(bottom, (0, top.height + gap))

    FIGURES.mkdir(parents=True, exist_ok=True)
    stitched.save(FIGURES / "open_problem_crop.png", optimize=True)


if __name__ == "__main__":
    main()

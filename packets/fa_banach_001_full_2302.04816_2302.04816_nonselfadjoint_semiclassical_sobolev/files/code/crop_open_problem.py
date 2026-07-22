"""Crop Figure 2 and its conjectural caption from source page 7."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE_PAGE = PACKET / "tmp" / "source_page-07.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    # Full text width, from the top of Figure 2 through its complete caption.
    crop = image.crop((145, 930, 1390, 1570))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

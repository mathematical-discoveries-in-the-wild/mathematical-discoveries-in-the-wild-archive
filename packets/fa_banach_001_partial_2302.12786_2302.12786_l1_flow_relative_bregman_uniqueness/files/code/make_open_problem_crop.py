"""Crop the title and abstract containing the source open statement."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE_PAGE = PACKET / "tmp" / "pdfs" / "source_page1.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    # Full text width with generous side margins; title, authors, and complete abstract.
    crop = image.crop((120, 250, 1435, 900))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()

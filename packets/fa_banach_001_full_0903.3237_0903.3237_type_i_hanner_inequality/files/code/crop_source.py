"""Crop the source excerpt containing Conjecture 3.15."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGE = ROOT / "tmp" / "source_page_25.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    # Full width, top section containing the complete conjecture and its context.
    crop = image.crop((110, 235, image.width - 100, 335))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} with size {crop.size}")


if __name__ == "__main__":
    main()

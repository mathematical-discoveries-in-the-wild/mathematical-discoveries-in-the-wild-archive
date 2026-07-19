"""Crop Remark 13 from the rendered sixth page of arXiv:2401.01033v3."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source-page-06.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Keep the full readable text width and the entire future-research remark.
    crop = image.crop((115, 1610, 1348, 1838))
    crop.save(OUTPUT)
    print(f"saved {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

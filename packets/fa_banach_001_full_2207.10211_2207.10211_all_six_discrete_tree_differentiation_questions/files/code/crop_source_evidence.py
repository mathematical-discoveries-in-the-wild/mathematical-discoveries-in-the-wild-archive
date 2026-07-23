"""Crop the open-question block from rendered page 17 of arXiv:2207.10211."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page-17.png"
TARGET = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Keep the full page width and both side margins; retain the running head,
    # section heading, introduction, and all six questions.
    crop = image.crop((0, 65, image.width, 570))
    crop.save(TARGET)
    print(f"wrote {TARGET} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()

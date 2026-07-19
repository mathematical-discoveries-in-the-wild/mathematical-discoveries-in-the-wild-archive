"""Reproduce the open-problem crop from the rendered source page."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "open_problem_page-15.png"
TARGET = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Coordinates for page 15 rendered at 180 dpi by pdftoppm.
    crop = image.crop((300, 495, 1240, 750))
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    crop.save(TARGET)
    print(f"wrote {TARGET}")


if __name__ == "__main__":
    main()

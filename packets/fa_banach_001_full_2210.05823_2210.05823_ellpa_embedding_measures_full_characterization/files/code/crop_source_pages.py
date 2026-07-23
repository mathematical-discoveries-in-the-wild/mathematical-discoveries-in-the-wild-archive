#!/usr/bin/env python3
"""Crop the equation and open-question evidence from rendered source pages."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(name: str, output: str, top_fraction: float) -> None:
    image = Image.open(TMP / name)
    width, height = image.size
    # Retain the full readable page width and the complete top statement area.
    result = image.crop((0, 0, width, int(height * top_fraction)))
    result.save(FIGURES / output)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    crop("source_page27-27.png", "equation_7_2_crop.png", 0.46)
    crop("source_page35-35.png", "open_question_crop.png", 0.18)


if __name__ == "__main__":
    main()


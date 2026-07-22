#!/usr/bin/env python3
"""Crop the theorem context and conjecture from rendered source pages 10--11."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], target: str) -> None:
    image = Image.open(TMP / source)
    image.crop(box).save(FIGURES / target, optimize=True)


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    # Keep the full rendered width so neither text nor margins are clipped.
    crop(
        "source_page-10.png",
        (0, 365, 1275, 1605),
        "open_problem_context_page10.png",
    )
    crop(
        "source_page-11.png",
        (0, 0, 1275, 690),
        "open_problem_conjecture_page11.png",
    )


if __name__ == "__main__":
    main()

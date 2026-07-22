#!/usr/bin/env python3
"""Create readable full-width crops from rendered source-paper pages."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def crop(src: str, dst: str, top: int, bottom: int) -> None:
    image = Image.open(src)
    out = image.crop((0, top, image.width, bottom))
    out.save(ROOT / "figures" / dst)


crop("/tmp/2311_moment-05.png", "open_problem_crop.png", 170, 690)
crop(
    "/tmp/2311_threshold_start-09.png",
    "threshold_conjecture_crop_page9.png",
    1540,
    2040,
)
crop(
    "/tmp/2311_threshold-10.png",
    "threshold_conjecture_crop_page10.png",
    0,
    620,
)

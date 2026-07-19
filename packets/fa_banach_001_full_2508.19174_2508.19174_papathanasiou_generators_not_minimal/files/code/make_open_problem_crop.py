#!/usr/bin/env python3
"""Render and crop the source-paper passage containing the target question."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "open_problem_crop.png"
TMP = PACKET / "tmp" / "crop_render"
BUNDLED_PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"
)


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None and BUNDLED_PDFTOPPM.exists():
        pdftoppm = str(BUNDLED_PDFTOPPM)
    if pdftoppm is None:
        raise SystemExit("pdftoppm not found")

    prefix = TMP / "source_page"
    subprocess.run(
        [
            pdftoppm,
            "-f",
            "17",
            "-l",
            "17",
            "-png",
            "-r",
            "220",
            str(PDF),
            str(prefix),
        ],
        check=True,
    )

    page = Image.open(TMP / "source_page-17.png")
    scale = 220 / 180
    # Page 17, top paragraph through the table caption. Coordinates were chosen
    # on a 180 dpi render and scaled here.
    box_180dpi = (230, 235, 1315, 835)
    box = tuple(round(v * scale) for v in box_180dpi)
    crop = page.crop(box)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()

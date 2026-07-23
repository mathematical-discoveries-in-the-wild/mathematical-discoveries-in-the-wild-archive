#!/usr/bin/env python3
"""Render source pages 4-5 and crop the two-page open-problem passage."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp" / "source_render"
FIGURES = ROOT / "figures"


def main() -> None:
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    TMP.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    prefix = TMP / "source"
    subprocess.run(
        [
            renderer,
            "-f",
            "4",
            "-l",
            "5",
            "-r",
            "160",
            "-png",
            str(ROOT / "source_paper.pdf"),
            str(prefix),
        ],
        check=True,
    )

    page4 = Image.open(TMP / "source-04.png")
    page5 = Image.open(TMP / "source-05.png")
    # Full readable text width, with enough margin to avoid clipping.
    page4.crop((115, 1292, 1215, 1730)).save(
        FIGURES / "open_problem_crop_page4.png"
    )
    page5.crop((115, 70, 1215, 220)).save(
        FIGURES / "open_problem_crop_page5.png"
    )


if __name__ == "__main__":
    main()

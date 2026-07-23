#!/usr/bin/env python3
"""Render and crop Open Problem 3.4 from arXiv:2108.05174."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp" / "pdfs"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise SystemExit("pdftoppm was not found on PATH")

    TMP.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    prefix = TMP / "source_page6"
    subprocess.run(
        [
            pdftoppm,
            "-f",
            "6",
            "-singlefile",
            "-r",
            "180",
            "-png",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )

    with Image.open(prefix.with_suffix(".png")) as page:
        # Keep the full page width and enough vertical context to include the
        # end of Corollary 3.3, the lead-in, and all of Open Problem 3.4.
        crop = page.crop((0, 705, page.width, 1115))
        crop.save(OUTPUT)

    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()

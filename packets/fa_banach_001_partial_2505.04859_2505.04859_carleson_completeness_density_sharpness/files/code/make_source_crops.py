#!/usr/bin/env python3
"""Render the source PDF and crop the future-work and theorem passages."""

from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"
TMP = PACKET / "tmp" / "source_crops"
KNOWN_PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/native/poppler/poppler/bin/pdftoppm"
)


def pdftoppm() -> str:
    found = shutil.which("pdftoppm")
    if found:
        return found
    if KNOWN_PDFTOPPM.exists():
        return str(KNOWN_PDFTOPPM)
    raise RuntimeError("pdftoppm was not found")


def render(page: int, stem: str) -> Path:
    out = TMP / stem
    subprocess.run(
        [
            pdftoppm(),
            "-f",
            str(page),
            "-l",
            str(page),
            "-r",
            "180",
            "-png",
            "-singlefile",
            str(SOURCE),
            str(out),
        ],
        check=True,
    )
    return out.with_suffix(".png")


def crop(source: Path, box: tuple[int, int, int, int], target: Path) -> None:
    with Image.open(source) as image:
        result = image.crop(box)
        result.save(target, optimize=True)


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(SOURCE)
    FIGURES.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    page3 = render(3, "page3")
    page11 = render(11, "page11")

    # Keep the full page width and generous margins.  Only vertical whitespace
    # and unrelated text are removed.
    crop(page3, (0, 680, 1530, 1150), FIGURES / "open_problem_crop.png")
    crop(page11, (0, 450, 1530, 730), FIGURES / "source_theorem_crop.png")

    print(FIGURES / "open_problem_crop.png")
    print(FIGURES / "source_theorem_crop.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"crop generation failed: {exc}", file=sys.stderr)
        raise

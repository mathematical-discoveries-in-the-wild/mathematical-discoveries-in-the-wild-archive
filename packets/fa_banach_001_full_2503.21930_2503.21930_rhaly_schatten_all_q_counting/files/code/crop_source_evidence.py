"""Render source page 36 and crop the complete endpoint open question."""

from pathlib import Path
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
RENDER_DIR = PACKET / "tmp" / "pdfs" / "source"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    prefix = RENDER_DIR / "page"
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            "36",
            "-l",
            "36",
            "-png",
            "-r",
            "180",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )
    page = Image.open(RENDER_DIR / "page-36.png")
    width, height = page.size
    crop = page.crop(
        (
            int(0.16 * width),
            int(0.43 * height),
            int(0.85 * width),
            int(0.65 * height),
        )
    )
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

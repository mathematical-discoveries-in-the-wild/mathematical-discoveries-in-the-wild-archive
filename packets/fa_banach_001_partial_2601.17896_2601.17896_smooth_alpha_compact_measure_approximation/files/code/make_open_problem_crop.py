"""Crop Remark 1.3 from the rendered fourth page of arXiv:2601.17896v3."""

from pathlib import Path
import sys

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: make_open_problem_crop.py INPUT_PNG OUTPUT_PNG")
    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    with Image.open(source) as image:
        # The source page is rendered at 200 dpi (1654 x 2339 pixels).
        # Keep the full text width and the complete Remark 1.3 context.
        crop = image.crop((220, 675, 1435, 1125))
        output.parent.mkdir(parents=True, exist_ok=True)
        crop.save(output)


if __name__ == "__main__":
    main()

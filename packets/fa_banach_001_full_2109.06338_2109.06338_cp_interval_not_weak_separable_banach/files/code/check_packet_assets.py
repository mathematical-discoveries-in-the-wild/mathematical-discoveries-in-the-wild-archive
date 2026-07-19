#!/usr/bin/env python3
"""Lightweight reproducibility check for the 2109.06338 solution packet."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[4]


def main() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "main.tex",
        ROOT / "source_paper.pdf",
        ROOT / "solution_packet.pdf",
        ROOT / "figures" / "open_problem_crop.png",
    ]
    missing = [str(path.relative_to(REPO)) for path in required if not path.exists()]
    if missing:
        raise SystemExit("missing packet assets:\n" + "\n".join(missing))

    source = REPO / "data" / "parsed" / "arxiv_sources" / "2109.06338" / "source.tex"
    text = source.read_text(encoding="utf-8")
    required_strings = [
        r"\begin{problem}\label{prob5}",
        "Does there exist a separable Banach space",
        r"E_w",
        r"C_p[0,1]",
    ]
    absent = [needle for needle in required_strings if needle not in text]
    if absent:
        raise SystemExit("source problem strings not found: " + ", ".join(absent))

    pdf_size = (ROOT / "source_paper.pdf").stat().st_size
    crop_size = (ROOT / "figures" / "open_problem_crop.png").stat().st_size
    packet_size = (ROOT / "solution_packet.pdf").stat().st_size
    if min(pdf_size, crop_size, packet_size) <= 0:
        raise SystemExit("one or more packet assets are empty")

    print("packet asset check passed")
    print(f"source_paper.pdf bytes: {pdf_size}")
    print(f"open_problem_crop.png bytes: {crop_size}")
    print(f"solution_packet.pdf bytes: {packet_size}")


if __name__ == "__main__":
    main()

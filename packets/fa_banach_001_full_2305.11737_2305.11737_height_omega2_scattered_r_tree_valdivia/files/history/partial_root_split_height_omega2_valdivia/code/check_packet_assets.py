#!/usr/bin/env python3
"""Lightweight checks for the 2305.11737 root-split packet assets."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "main.tex",
        ROOT / "source_paper.pdf",
        ROOT / "figures" / "open_problem_crop.png",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        raise SystemExit("missing required packet files: " + ", ".join(map(str, missing)))

    crop = ROOT / "figures" / "open_problem_crop.png"
    if crop.stat().st_size < 10_000:
        raise SystemExit("open problem crop is unexpectedly small")

    tex = (ROOT / "main.tex").read_text(encoding="utf-8")
    required_phrases = [
        "rooted scattered compact",
        "htte(V_s)<\\omega_2",
        "one-point compactification",
        "Russo--Somaglia",
    ]
    missing_phrases = [phrase for phrase in required_phrases if phrase not in tex]
    if missing_phrases:
        raise SystemExit("main.tex missing phrases: " + ", ".join(missing_phrases))

    print("packet asset checks passed")


if __name__ == "__main__":
    main()

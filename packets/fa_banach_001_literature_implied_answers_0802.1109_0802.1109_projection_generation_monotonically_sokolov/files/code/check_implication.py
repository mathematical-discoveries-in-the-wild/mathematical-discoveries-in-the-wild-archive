#!/usr/bin/env python3
"""Verify the decisive PDF snippets for the literature-implied packet."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]


CHECKS = {
    "source_paper.pdf": [
        "Find a topological property",
        "generates projections in X",
    ],
    "supporting_paper_1805.11901.pdf": [
        "The following assertions are equivalent",
        "D is induced by a projectional skeleton",
        "monotonically Sokolov",
    ],
}


def extract_text(path: Path) -> str:
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def main() -> None:
    missing: list[str] = []
    for rel_path, snippets in CHECKS.items():
        path = ROOT / rel_path
        text = extract_text(path)
        for snippet in snippets:
            if snippet not in text:
                missing.append(f"{rel_path}: {snippet}")
    if missing:
        raise SystemExit("Missing snippets:\n" + "\n".join(missing))
    print("Verified source problem and supporting theorem snippets.")


if __name__ == "__main__":
    main()

"""Exploratory smoke check for finite-translate rectangle examples.

This script is not part of the proof. It only documents the bounded search that
failed to find a counterexample to the full supermodularity question for
axis-aligned rectangles A and finite point sets B,C.
"""

from __future__ import annotations

import random


def union_area(points: list[tuple[float, float]], width: float, height: float) -> float:
    rects = [(x, x + width, y, y + height) for x, y in points]
    xs = sorted({edge for x0, x1, _, _ in rects for edge in (x0, x1)})
    total = 0.0
    for left, right in zip(xs, xs[1:]):
        mid_x = 0.5 * (left + right)
        active = [(y0, y1) for x0, x1, y0, y1 in rects if x0 <= mid_x <= x1]
        if not active:
            continue
        active.sort()
        start, end = active[0]
        length = 0.0
        for y0, y1 in active[1:]:
            if y0 <= end:
                end = max(end, y1)
            else:
                length += end - start
                start, end = y0, y1
        length += end - start
        total += (right - left) * length
    return total


def sumset(
    first: list[tuple[float, float]],
    second: list[tuple[float, float]],
) -> list[tuple[float, float]]:
    return [(x + u, y + v) for x, y in first for u, v in second]


def main() -> None:
    random.seed(170405486)
    best = float("inf")
    best_case = None
    for width, height in [(1.0, 1.0), (2.0, 0.2), (5.0, 0.2), (3.0, 1.0)]:
        for m, n, trials in [(2, 2, 5000), (2, 3, 5000), (3, 3, 5000)]:
            for _ in range(trials):
                b_points = [
                    (random.random() * 2 * width - width, random.random() * 2 * height - height)
                    for _ in range(m)
                ]
                c_points = [
                    (random.random() * 2 * width - width, random.random() * 2 * height - height)
                    for _ in range(n)
                ]
                margin = (
                    union_area(sumset(b_points, c_points), width, height)
                    + width * height
                    - union_area(b_points, width, height)
                    - union_area(c_points, width, height)
                )
                if margin < best:
                    best = margin
                    best_case = (width, height, m, n)
    print(f"best_margin={best:.12g}")
    print(f"best_case={best_case}")
    print("No counterexample found in this bounded randomized smoke check.")


if __name__ == "__main__":
    main()

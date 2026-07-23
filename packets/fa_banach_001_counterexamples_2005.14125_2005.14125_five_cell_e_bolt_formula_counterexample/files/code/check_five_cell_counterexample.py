#!/usr/bin/env python3
"""Exact checks for the five-cell e-bolt formula counterexample."""

from fractions import Fraction
from itertools import combinations


F = Fraction


def positive_part(t: Fraction) -> Fraction:
    return max(t, F(0))


def f(x: Fraction, y: Fraction) -> Fraction:
    return min(x, F(1)) * min(y, F(1)) - min(
        positive_part(x - 1), F(1)
    ) * positive_part(y - 1)


def mixed_increment(
    x0: Fraction, x1: Fraction, y0: Fraction, y1: Fraction
) -> Fraction:
    return f(x0, y0) + f(x1, y1) - f(x0, y1) - f(x1, y0)


def rectangle_is_contained(
    x0: Fraction, x1: Fraction, y0: Fraction, y1: Fraction
) -> bool:
    """Characterize rectangles contained in the five-cell U-shaped Q."""
    assert 0 <= x0 < x1 <= 3
    assert 0 <= y0 < y1 <= 2
    return y1 <= 1 or x1 <= 1 or x0 >= 2


def bolt_value(points: tuple[tuple[int, int], ...]) -> Fraction:
    total = sum(
        (1 if k % 2 == 0 else -1) * f(F(x), F(y))
        for k, (x, y) in enumerate(points)
    )
    return total / len(points)


def main() -> None:
    outer = ((0, 0), (3, 0), (3, 2), (0, 2))
    left_l = ((0, 0), (3, 0), (3, 1), (1, 1), (1, 2), (0, 2))
    right_l = ((0, 0), (3, 0), (3, 2), (2, 2), (2, 1), (0, 1))
    short = ((0, 0), (1, 0), (1, 1), (0, 1))

    values = {
        "r": bolt_value(outer),
        "r12": bolt_value(left_l),
        "r13": bolt_value(right_l),
        "q": bolt_value(short),
    }
    expected = {"r": F(0), "r12": F(1, 6), "r13": F(1, 6), "q": F(1, 4)}
    assert values == expected

    mesh = 8
    xs = [F(k, mesh) for k in range(3 * mesh + 1)]
    ys = [F(k, mesh) for k in range(2 * mesh + 1)]
    tested = 0
    minimum = None
    for x0, x1 in combinations(xs, 2):
        for y0, y1 in combinations(ys, 2):
            if rectangle_is_contained(x0, x1, y0, y1):
                delta = mixed_increment(x0, x1, y0, y1)
                assert delta >= 0
                tested += 1
                minimum = delta if minimum is None else min(minimum, delta)

    print("exact bolt values:", values)
    print("source maximum:", max(abs(values[k]) for k in ("r", "r12", "r13")))
    print("short-bolt lower bound:", abs(values["q"]))
    print("contained mesh-1/8 rectangles tested:", tested)
    print("minimum tested mixed increment:", minimum)


if __name__ == "__main__":
    main()


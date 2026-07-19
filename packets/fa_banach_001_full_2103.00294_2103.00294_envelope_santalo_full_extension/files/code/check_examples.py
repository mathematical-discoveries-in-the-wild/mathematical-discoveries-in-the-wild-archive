#!/usr/bin/env python3
"""Reproducible arithmetic checks; none is used as a substitute for proof."""

from fractions import Fraction
from math import atan, log, pi


def log_critical_point() -> float:
    def q(t: float) -> float:
        return 2.0 * t / (1.0 + t) - log(1.0 + t)

    lo, hi = 1.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if q(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    root = (lo + hi) / 2.0
    print(f"t_star={root:.12f}")
    print(f"critical_residual={q(root):.3e}")
    print(f"q_before={q(0.9 * root):.6e}")
    print(f"q_after={q(1.1 * root):.6e}")
    return root


def arctangent_strictness() -> None:
    for m in (2, 3, 7):
        for s in (0.25, 0.5, 2.0, 4.0):
            product = atan(s ** (1.0 / m)) * atan(s ** (-1.0 / m))
            assert product < pi * pi / 16.0
    print("arctangent_scaled_ball_strictness=verified")


def polygon_centroid(vertices):
    twice_area = Fraction(0)
    x_numerator = Fraction(0)
    y_numerator = Fraction(0)
    for (x, y), (u, v) in zip(vertices, vertices[1:] + vertices[:1]):
        cross = x * v - u * y
        twice_area += cross
        x_numerator += (x + u) * cross
        y_numerator += (y + v) * cross
    return (
        x_numerator / (3 * twice_area),
        y_numerator / (3 * twice_area),
    )


def polar_centroid_counterexample() -> None:
    f = Fraction
    body = [
        (-f(7, 9), -f(4, 9)),
        (f(11, 9), -f(4, 9)),
        (f(2, 9), f(5, 9)),
        (-f(7, 9), f(5, 9)),
    ]
    polar = [
        (f(0), -f(9, 4)),
        (f(9, 7), f(9, 7)),
        (f(0), f(9, 5)),
        (-f(9, 7), f(0)),
    ]
    assert polygon_centroid(body) == (f(0), f(0))
    assert polygon_centroid(polar) == (f(0), f(9, 140))
    print(f"body_centroid={polygon_centroid(body)}")
    print(f"polar_centroid={polygon_centroid(polar)}")


if __name__ == "__main__":
    log_critical_point()
    arctangent_strictness()
    polar_centroid_counterexample()

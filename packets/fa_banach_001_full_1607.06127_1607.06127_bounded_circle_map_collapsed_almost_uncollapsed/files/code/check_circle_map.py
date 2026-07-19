#!/usr/bin/env python3
"""Numerical smoke check for the circle-map construction."""

import math


def f(x: float) -> tuple[float, float]:
    return (math.cos(x), math.sin(x))


def dist(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def main() -> None:
    samples = [j / 8 for j in range(-64, 65)]
    exact_pi_distances = [dist(f(x), f(x + math.pi)) for x in samples]
    period_distances = [dist(f(x), f(x + 2 * math.pi * k)) for x in samples for k in range(1, 8)]
    sup_norms = [dist(f(x), (0.0, 0.0)) for x in samples]

    assert min(exact_pi_distances) > 1.999999
    assert max(period_distances) < 1e-12
    assert max(sup_norms) <= 1.000001
    print("circle-map smoke check passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Sanity checks for the radial-twist counterexample.

The proof in main.tex is exact. This script only samples the map in
finite-dimensional Hilbert space and checks the advertised inequalities.
"""

from __future__ import annotations

import math
import random


L = math.pi / 4.0
LOWER = 1.0 / math.sqrt(2.0)
UPPER = 1.0 + L


def norm(x: list[float]) -> float:
    return math.sqrt(sum(t * t for t in x))


def sub(x: list[float], y: list[float]) -> list[float]:
    return [a - b for a, b in zip(x, y)]


def dist_to_4z(t: float) -> float:
    k = round(t / 4.0)
    best = abs(t - 4.0 * k)
    return min(best, abs(t - 4.0 * (k - 1)), abs(t - 4.0 * (k + 1)))


def phi(t: float) -> float:
    return L * min(dist_to_4z(t), 2.0)


def theta(r: float) -> float:
    return phi(math.log1p(r))


def F(x: list[float]) -> list[float]:
    r = norm(x)
    t = theta(r)
    return [math.cos(t) * a for a in x] + [math.sin(t) * a for a in x]


def F1(x: list[float]) -> list[float]:
    t = theta(norm(x))
    return [math.cos(t) * a for a in x]


def F2(x: list[float]) -> list[float]:
    t = theta(norm(x))
    return [math.sin(t) * a for a in x]


def rand_vec(dim: int) -> list[float]:
    return [random.gauss(0.0, 1.0) * random.uniform(0.0, 30.0) for _ in range(dim)]


def sample_lipschitz(dim: int = 5, trials: int = 20_000) -> tuple[float, float]:
    min_ratio = float("inf")
    max_ratio = 0.0
    for _ in range(trials):
        x = rand_vec(dim)
        y = rand_vec(dim)
        d = norm(sub(x, y))
        if d == 0:
            continue
        ratio = norm(sub(F(x), F(y))) / d
        min_ratio = min(min_ratio, ratio)
        max_ratio = max(max_ratio, ratio)
        if ratio + 1e-10 < LOWER or ratio - 1e-10 > UPPER:
            raise AssertionError((ratio, LOWER, UPPER, x, y))
    return min_ratio, max_ratio


def check_coordinate_collapses(dim: int = 5, count: int = 6) -> None:
    unit = [1.0] + [0.0] * (dim - 1)
    for k in range(count):
        r1 = math.exp(4 * k + 2) - 1.0
        x1 = [r1 * a for a in unit]
        if norm(F1(x1)) > 1e-6:
            raise AssertionError(("F1 did not collapse", k, norm(F1(x1))))

        r2 = math.exp(4 * k) - 1.0
        x2 = [r2 * a for a in unit]
        if norm(F2(x2)) > 1e-6:
            raise AssertionError(("F2 did not collapse", k, norm(F2(x2))))


def main() -> None:
    random.seed(160408661)
    min_ratio, max_ratio = sample_lipschitz()
    check_coordinate_collapses()
    print(f"proved lower constant: {LOWER:.12f}")
    print(f"proved upper constant: {UPPER:.12f}")
    print(f"sampled ratio range:  {min_ratio:.12f} to {max_ratio:.12f}")
    print("coordinate collapse checks: passed")


if __name__ == "__main__":
    main()

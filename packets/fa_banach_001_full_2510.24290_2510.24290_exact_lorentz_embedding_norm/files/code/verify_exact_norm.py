#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the exact Lorentz embedding norm.

This is not part of the proof.  It samples decreasing sequences generated from
random nonnegative jumps and compares every observed ratio with the exact
initial-block maximum on the same finite coordinate set.
"""

from __future__ import annotations

import math
import random


def weights(p: float, q: float, size: int) -> list[float]:
    exponent = -1.0 if math.isinf(p) else q / p - 1.0
    return [n**exponent for n in range(1, size + 1)]


def lorentz_norm(x: list[float], p: float, q: float) -> float:
    if math.isinf(q):
        if math.isinf(p):
            return max(x, default=0.0)
        return max((n ** (1.0 / p)) * value for n, value in enumerate(x, 1))
    w = weights(p, q, len(x))
    return sum(weight * value**q for weight, value in zip(w, x)) ** (1.0 / q)


def block_ratios(
    p1: float, q1: float, p2: float, q2: float, size: int
) -> list[float]:
    w1 = weights(p1, q1, size)
    sum1 = 0.0
    ratios: list[float] = []
    if math.isinf(q2):
        for n, a in enumerate(w1, 1):
            sum1 += a
            numerator = 1.0 if math.isinf(p2) else n ** (1.0 / p2)
            ratios.append(numerator / sum1 ** (1.0 / q1))
        return ratios

    w2 = weights(p2, q2, size)
    sum2 = 0.0
    for a, b in zip(w1, w2):
        sum1 += a
        sum2 += b
        ratios.append(sum2 ** (1.0 / q2) / sum1 ** (1.0 / q1))
    return ratios


def random_decreasing_sequence(size: int, rng: random.Random) -> list[float]:
    jumps = [rng.expovariate(1.0) if rng.random() < 0.35 else 0.0 for _ in range(size)]
    x = [0.0] * size
    running = 0.0
    for index in range(size - 1, -1, -1):
        running += jumps[index]
        x[index] = running
    return x


def check_case(p1: float, q1: float, p2: float, q2: float) -> None:
    sample_size = 64
    ratios = block_ratios(p1, q1, p2, q2, sample_size)
    exact_finite = max(ratios)
    maximizing_n = 1 + max(range(sample_size), key=ratios.__getitem__)

    block = [1.0 if n <= maximizing_n else 0.0 for n in range(1, sample_size + 1)]
    block_ratio = lorentz_norm(block, p2, q2) / lorentz_norm(block, p1, q1)
    assert abs(block_ratio - exact_finite) <= 2e-12 * max(1.0, exact_finite)

    rng = random.Random(20260719)
    largest_sample = 0.0
    for _ in range(4000):
        x = random_decreasing_sequence(sample_size, rng)
        if not any(x):
            continue
        ratio = lorentz_norm(x, p2, q2) / lorentz_norm(x, p1, q1)
        largest_sample = max(largest_sample, ratio)
        assert ratio <= exact_finite * (1.0 + 2e-12)

    source_constant = (q1 / p1) ** (1.0 / q1 - (0.0 if math.isinf(q2) else 1.0 / q2))
    assert exact_finite < source_constant
    print(
        f"(p1,q1,p2,q2)=({p1},{q1},{p2},{q2}): "
        f"finite exact={exact_finite:.12g} at N={maximizing_n}, "
        f"largest random={largest_sample:.12g}, source bound={source_constant:.12g}"
    )


def main() -> None:
    cases = [
        (1.0, 2.0, 2.0, 4.0),
        (1.0, 2.0, 1.1, 8.0),
        (0.5, 0.75, 1.0, 2.0),
        (1.0, 2.0, 1.2, math.inf),
        (1.0, 2.0, math.inf, 4.0),
    ]
    for case in cases:
        check_case(*case)
    print("all finite-dimensional sanity checks passed")


if __name__ == "__main__":
    main()

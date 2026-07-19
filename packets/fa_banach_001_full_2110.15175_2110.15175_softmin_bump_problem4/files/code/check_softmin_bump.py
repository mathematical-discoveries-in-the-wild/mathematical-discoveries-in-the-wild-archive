#!/usr/bin/env python3
"""Numerical sanity checks for the soft-min bump packet.

The proof in the packet is analytic. This script only samples the constructed
functions to catch sign mistakes, support mistakes, or a badly scaled constant.
"""

from __future__ import annotations

import math
import random
from typing import Iterable, List


def logsumexp(values: Iterable[float]) -> float:
    vals = list(values)
    m = max(vals)
    return m + math.log(sum(math.exp(v - m) for v in vals))


def soft_m(x: List[float], beta: float) -> float:
    return -logsumexp(beta * (xi * xi - 1.0) for xi in x) / beta


def bump_g(x: List[float], beta: float) -> float:
    m = soft_m(x, beta)
    return 0.5 * m * m if m > 0.0 else 0.0


def bump_f(x: List[float]) -> float:
    n = len(x)
    if n == 1:
        return 0.0
    beta = 2.0 * math.log(n)
    return bump_g(x, beta) / (6.0 + 4.0 * beta)


def sup_norm(x: List[float]) -> float:
    return max(abs(v) for v in x)


def rand_vec(n: int, radius: float) -> List[float]:
    return [random.uniform(-radius, radius) for _ in range(n)]


def main() -> None:
    random.seed(211015175)
    print("soft-min bump sanity check")
    print("The theoretical proof supplies the global bounds; samples should be below 1.")

    for n in [2, 3, 5, 10, 25]:
        beta = 2.0 * math.log(n)
        height = bump_f([0.0] * n)
        lower = 1.0 / (8.0 * (6.0 + 8.0 * math.log(n)))
        max_lip_ratio = 0.0
        max_second_ratio = 0.0
        support_violations = 0

        for _ in range(4000):
            x = rand_vec(n, 2.0)
            y = rand_vec(n, 2.0)
            fx = bump_f(x)
            fy = bump_f(y)
            if fx > 1e-12 and sup_norm(x) >= 1.0:
                support_violations += 1

            d = sup_norm([xi - yi for xi, yi in zip(x, y)])
            if d > 0.0:
                max_lip_ratio = max(max_lip_ratio, abs(fx - fy) / d)

            center = rand_vec(n, 1.5)
            direction = rand_vec(n, 1.0)
            r = sup_norm(direction)
            if r > 0.0:
                plus = [a + b for a, b in zip(center, direction)]
                minus = [a - b for a, b in zip(center, direction)]
                second = abs(bump_f(plus) - 2.0 * bump_f(center) + bump_f(minus))
                max_second_ratio = max(max_second_ratio, second / (r * r))

        print(
            f"n={n:2d} beta={beta:.6f} f(0)={height:.8f} "
            f"lower={lower:.8f} lip_sample={max_lip_ratio:.6f} "
            f"second_sample={max_second_ratio:.6f} support_violations={support_violations}"
        )


if __name__ == "__main__":
    main()

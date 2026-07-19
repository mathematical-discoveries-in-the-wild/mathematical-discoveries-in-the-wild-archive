"""Numerical probes for the high-p endpoint refinement.

The candidate exact formula for p >= 2 is

    dim_{ell_p}(gamma) = max{n : (E |S_n/n|^p)^{1/p} >= gamma},

where S_n is a sum of n independent Rademacher signs.  This script checks the
two scalar pieces that would make that formula natural:

1. For the Rademacher-system lower bound, the minimum of
   E |sum a_i eps_i|^p over the l1 simplex appears at a_i=1/n.
2. For the upper bound, the sharp inequality
   E |sum a_i eps_i|^p <= (E |S_n|^p / n) sum |a_i|^p
   appears to have equality at equal coefficients.

This is exploratory evidence only, not a proof.
"""

from __future__ import annotations

import itertools
import math
import random
from typing import Iterable


def signs(n: int) -> Iterable[tuple[int, ...]]:
    return itertools.product((-1, 1), repeat=n)


def moment(a: list[float], p: float) -> float:
    total = 0.0
    for eps in signs(len(a)):
        total += abs(sum(x * e for x, e in zip(a, eps))) ** p
    return total / (2 ** len(a))


def equal_moment(n: int, p: float) -> float:
    return moment([1.0] * n, p)


def equal_moment_binomial(n: int, p: float) -> float:
    total = 0.0
    for k in range(n + 1):
        s = 2 * k - n
        total += math.comb(n, k) * abs(s) ** p
    return total / (2**n)


def random_simplex(n: int) -> list[float]:
    xs = [random.expovariate(1.0) for _ in range(n)]
    s = sum(xs)
    return [x / s for x in xs]


def random_lp_sphere(n: int, p: float) -> list[float]:
    xs = [random.expovariate(1.0) for _ in range(n)]
    s = sum(xs)
    weights = [x / s for x in xs]
    return [w ** (1 / p) for w in weights]


def probe(n: int, p: float, trials: int = 20_000) -> None:
    uniform_l1 = [1 / n] * n
    min_l1 = moment(uniform_l1, p)
    best_l1 = min_l1
    best_l1_a = uniform_l1
    for _ in range(trials):
        a = random_simplex(n)
        val = moment(a, p)
        if val < best_l1:
            best_l1 = val
            best_l1_a = a

    scalar_const = equal_moment(n, p) / n
    uniform_lp = [n ** (-1 / p)] * n
    max_lp_ratio = moment(uniform_lp, p) / scalar_const
    best_lp_a = uniform_lp
    for _ in range(trials):
        a = random_lp_sphere(n, p)
        ratio = moment(a, p) / scalar_const
        if ratio > max_lp_ratio:
            max_lp_ratio = ratio
            best_lp_a = a

    print(f"n={n:2d} p={p:5.2f}")
    print(f"  l1 uniform moment={min_l1:.10g}; best random/min ratio={best_l1/min_l1:.10g}")
    print(f"  l1 best a={['%.3f' % x for x in best_l1_a]}")
    print(f"  lp scalar const={scalar_const:.10g}; best random ratio={max_lp_ratio:.10g}")
    print(f"  lp best a={['%.3f' % x for x in best_lp_a]}")


def thresholds(p: float, max_n: int = 80) -> None:
    vals = []
    for n in range(1, max_n + 1):
        vals.append((equal_moment_binomial(n, p) / (n**p)) ** (1 / p))
    print(f"threshold values for p={p}")
    for n, val in enumerate(vals, start=1):
        if n <= 10 or n % 5 == 0:
            print(f"  n={n:3d}: {val:.8f}")


if __name__ == "__main__":
    random.seed(260307221)
    for p in (2.5, 3.0, 4.0, 6.0, 10.0):
        for n in (2, 3, 4, 5, 6, 8):
            probe(n, p, trials=2500)
        thresholds(p, max_n=30)

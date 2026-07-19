#!/usr/bin/env python3
"""Verifier for the p=4 and p=6 B_q^n moment packet.

The script checks the moment formulas for the iid model with density
proportional to exp(-|x|^q), the Schur-concavity bracket for p=6, and random
simplex samples against the claimed equal-coordinate maximiser.
"""

from __future__ import annotations

import math
import random


def moment(q: float, r: int) -> float:
    """Return E Y^r for density proportional to exp(-|x|^q)."""
    return math.gamma((r + 1.0) / q) / math.gamma(1.0 / q)


def f4(q: float, x: list[float]) -> float:
    m2 = moment(q, 2)
    m4 = moment(q, 4)
    return 3 * m2 * m2 + (m4 - 3 * m2 * m2) * sum(t * t for t in x)


def f6(q: float, x: list[float]) -> float:
    m2 = moment(q, 2)
    m4 = moment(q, 4)
    m6 = moment(q, 6)
    c2 = 15 * m2 * (m4 - 3 * m2 * m2)
    c3 = m6 - 15 * m4 * m2 + 30 * m2**3
    return 15 * m2**3 + c2 * sum(t * t for t in x) + c3 * sum(t**3 for t in x)


def random_simplex(n: int) -> list[float]:
    vals = [random.expovariate(1.0) for _ in range(n)]
    total = sum(vals)
    return [v / total for v in vals]


def check_q(q: float) -> None:
    m2 = moment(q, 2)
    m4 = moment(q, 4)
    m6 = moment(q, 6)
    rho4 = m4 / m2**2
    rho6 = m6 / m2**3

    assert rho4 < 3.0, (q, rho4)
    assert rho6 < 5.0 * rho4, (q, rho6, rho4)

    c2 = 15 * m2 * (m4 - 3 * m2 * m2)
    c3 = m6 - 15 * m4 * m2 + 30 * m2**3
    # Schur bracket for p=6 is 2*c2 + 3*c3*s, with 0<=s<=1.
    max_bracket = max(2 * c2, 2 * c2 + 3 * c3)
    assert max_bracket < 0.0, (q, c2, c3, max_bracket)

    for n in [2, 3, 5, 10]:
        uniform = [1.0 / n] * n
        f4_uniform = f4(q, uniform)
        f6_uniform = f6(q, uniform)
        for _ in range(3000):
            x = random_simplex(n)
            assert f4(q, x) <= f4_uniform + 1e-10
            assert f6(q, x) <= f6_uniform + 1e-10

        rho4_n = 3 + (rho4 - 3) / n
        rho6_n = (rho6 + 15 * (n - 1) * rho4 + 15 * (n - 1) * (n - 2)) / n**2
        assert abs(f4_uniform / m2**2 - rho4_n) < 1e-10
        assert abs(f6_uniform / m2**3 - rho6_n) < 1e-10


def main() -> None:
    random.seed(180107597)
    for q in [2.01, 2.1, 3.0, 4.0, 10.0, 100.0]:
        check_q(q)
        print(f"q={q}: checks passed")
    print("All p=4/p=6 checks passed.")


if __name__ == "__main__":
    main()

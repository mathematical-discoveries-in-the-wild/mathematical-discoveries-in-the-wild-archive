#!/usr/bin/env python3
"""Exact audits for the weighted-product metric parallel-sum theorem.

The symbolic and rational checks below support, but do not replace, the proof.
"""

from fractions import Fraction
import random

import sympy as sp


def symbolic_checks() -> None:
    a, b, A, B, D = sp.symbols("a b A B D", positive=True)
    effective_sq = a**2 * b**2 / (a**2 + b**2)
    defect = sp.factor(a**2 * A**2 + b**2 * B**2 - effective_sq * (A + B) ** 2)
    assert defect == (a**2 * A - b**2 * B) ** 2 / (a**2 + b**2)

    t = b**2 / (a**2 + b**2)
    attained = sp.simplify(a**2 * (t * D) ** 2 + b**2 * ((1 - t) * D) ** 2)
    assert sp.simplify(attained - effective_sq * D**2) == 0

    tripod_effective = sp.simplify((1 + sp.Rational(1, 4)) ** sp.Rational(-1, 2))
    assert tripod_effective == 2 / sp.sqrt(5)


def rational_path_checks(cases: int = 300) -> None:
    """Check the lower bound on product paths in rational line factors."""
    rng = random.Random(250312939)
    for _ in range(cases):
        m = rng.randint(1, 4)
        n = rng.randint(1, 6)
        w1 = [Fraction(rng.randint(1, 6), rng.randint(1, 5)) for _ in range(m)]
        w2 = [Fraction(rng.randint(1, 6), rng.randint(1, 5)) for _ in range(m)]
        x = [[Fraction(rng.randint(-8, 8), 3) for _ in range(m)] for _ in range(n + 1)]
        y = [[Fraction(rng.randint(-8, 8), 3) for _ in range(m)] for _ in range(n)]

        energy = Fraction(0)
        for i in range(1, n + 1):
            for k in range(m):
                a_step = abs(x[i - 1][k] - y[i - 1][k])
                b_step = abs(y[i - 1][k] - x[i][k])
                energy += n * (w1[k] ** 2 * a_step**2 + w2[k] ** 2 * b_step**2)

        endpoint_sq = Fraction(0)
        for k in range(m):
            effective_sq = w1[k] ** 2 * w2[k] ** 2 / (w1[k] ** 2 + w2[k] ** 2)
            endpoint_sq += effective_sq * abs(x[0][k] - x[-1][k]) ** 2
        assert energy >= endpoint_sq


def exact_attainment_checks(cases: int = 200) -> None:
    """Check the constructed N-path energy using exact rational arithmetic."""
    rng = random.Random(50312939)
    for _ in range(cases):
        m = rng.randint(1, 5)
        n = rng.randint(1, 8)
        d = [Fraction(rng.randint(0, 9), rng.randint(1, 5)) for _ in range(m)]
        w1 = [Fraction(rng.randint(1, 7), rng.randint(1, 5)) for _ in range(m)]
        w2 = [Fraction(rng.randint(1, 7), rng.randint(1, 5)) for _ in range(m)]

        one_step = Fraction(0)
        target = Fraction(0)
        for k in range(m):
            t = w2[k] ** 2 / (w1[k] ** 2 + w2[k] ** 2)
            a_step = t * d[k] / n
            b_step = (1 - t) * d[k] / n
            one_step += w1[k] ** 2 * a_step**2 + w2[k] ** 2 * b_step**2
            effective_sq = w1[k] ** 2 * w2[k] ** 2 / (w1[k] ** 2 + w2[k] ** 2)
            target += effective_sq * d[k] ** 2
        total_energy = n * n * one_step
        assert total_energy == target


def main() -> None:
    symbolic_checks()
    rational_path_checks()
    exact_attainment_checks()
    print("symbolic parallel-sum identity: passed")
    print("300 rational lower-bound path checks: passed")
    print("200 exact attaining-path checks: passed")
    print("tripod effective coefficient 2/sqrt(5): passed")
    print("all checks passed")


if __name__ == "__main__":
    main()

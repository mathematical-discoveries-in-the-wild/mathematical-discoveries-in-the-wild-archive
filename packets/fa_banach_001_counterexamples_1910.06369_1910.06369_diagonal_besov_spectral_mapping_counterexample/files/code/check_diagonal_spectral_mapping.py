#!/usr/bin/env python3
"""Deterministic scalar audit for the diagonal Besov counterexample."""

from __future__ import annotations

import cmath


def b(n: int, t: float) -> complex:
    return 1j * t * n / (1 + 1j * t * n)


def main() -> None:
    times = (0.125, 0.5, 1.0, 3.7)
    pairs = ((0.2, 0.21), (0.5, 0.9), (2.0, 1.25), (7.0, 7.001))
    indices = (1, 2, 7, 31, 1000, 100_000)

    for t in times:
        for n in indices:
            resolvent_formula = 1 - 1 / (1 + 1j * t * n)
            assert abs(b(n, t) - resolvent_formula) < 1e-14
            assert abs((1 - b(n, t)) - 1 / (1 + 1j * t * n)) < 1e-14
            assert b(n, t) != 1

    worst_ratio = 0.0
    for s, t in pairs:
        bound = abs(t - s) / min(s, t)
        for n in indices:
            diff = abs(b(n, t) - b(n, s))
            assert diff <= bound + 1e-14
            if bound:
                worst_ratio = max(worst_ratio, diff / bound)

    for t in times:
        for n in (10, 100, 1000, 10_000):
            exact_distance = 1 / cmath.sqrt(1 + (t * n) ** 2).real
            assert abs(abs(1 - b(n, t)) - exact_distance) < 1e-14
        assert abs(1 - b(10_000, t)) < 1 / (t * 10_000) + 1e-14

    print("PASS: resolvent and diagonal formulas agree")
    print("PASS: no finite diagonal entry equals the missing point 1")
    print("PASS: all tested norm differences obey |t-s|/min(s,t)")
    print(f"largest tested difference/bound ratio: {worst_ratio:.12f}")
    print("PASS: diagonal entries converge to the extra spectral point 1")


if __name__ == "__main__":
    main()

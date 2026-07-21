#!/usr/bin/env python3
"""Finite smoke tests for the analytic submultiplicativity proof.

This script is not part of the proof.  It evaluates the exact one-dimensional
Gamma integral, checks the Beta splitting inequality on a finite grid, and
tests A_{n+m} <= A_n A_m for small dimensions.
"""

from __future__ import annotations

import math

from scipy.integrate import quad


def h(q: float) -> float:
    w = math.sqrt(1.0 + 4.0 * q * q)
    return w - 1.0 - math.log((w + 1.0) / 2.0)


def h_prime(q: float) -> float:
    w = math.sqrt(1.0 + 4.0 * q * q)
    return 4.0 * q / (w + 1.0)


def h_triple_prime(q: float) -> float:
    w = math.sqrt(1.0 + 4.0 * q * q)
    return -16.0 * q * (2.0 * w + 1.0) / (w**3 * (w + 1.0) ** 2)


def F(n: int, s: float) -> float:
    return 0.5 * (n + 1) * h(s / (n + 1))


def A(n: int) -> float:
    log_gamma = math.lgamma(n)

    def integrand(s: float) -> float:
        if s == 0.0:
            return math.exp(-log_gamma) if n == 1 else 0.0
        return math.exp(
            (n - 1) * math.log(s) - s - log_gamma - F(n, s)
        )

    return quad(
        integrand,
        0.0,
        math.inf,
        epsabs=2e-13,
        epsrel=2e-13,
        limit=500,
    )[0]


def mean_split_energy(n: int, m: int, s: float) -> float:
    log_beta = math.lgamma(n) + math.lgamma(m) - math.lgamma(n + m)

    def integrand(d: float) -> float:
        if d <= 0.0 or d >= 1.0:
            return 0.0
        log_density = (
            (n - 1) * math.log(d)
            + (m - 1) * math.log1p(-d)
            - log_beta
        )
        return math.exp(log_density) * (F(n, s * d) + F(m, s * (1.0 - d)))

    return quad(
        integrand,
        0.0,
        1.0,
        epsabs=2e-12,
        epsrel=2e-12,
        limit=500,
    )[0]


def main() -> None:
    concavity_points = [10.0 ** (k / 4.0) for k in range(-16, 17)]
    worst_h3 = max(h_triple_prime(q) for q in concavity_points)
    assert worst_h3 < 0.0

    values = {n: A(n) for n in range(1, 13)}
    for n, value in values.items():
        print(f"A_{n:2d}={value:.15g}  root={value ** (1.0 / n):.15g}")

    max_submult_residual = -math.inf
    for n in range(1, 7):
        for m in range(1, 7):
            residual = values[n + m] - values[n] * values[m]
            max_submult_residual = max(max_submult_residual, residual)
            assert residual < 2e-11, (n, m, residual)

    max_energy_residual = -math.inf
    for n in range(1, 6):
        for m in range(1, 6):
            for s in (0.05, 0.2, 1.0, 3.0, 10.0, 30.0):
                residual = mean_split_energy(n, m, s) - F(n + m, s)
                max_energy_residual = max(max_energy_residual, residual)
                assert residual < 2e-10, (n, m, s, residual)

    print(f"largest h''' on test grid: {worst_h3:.6e}")
    print(f"largest A_(n+m)-A_n A_m: {max_submult_residual:.6e}")
    print(f"largest split-energy residual: {max_energy_residual:.6e}")
    print(f"A_1 = {values[1]:.12f}")
    print("all finite smoke tests passed")


if __name__ == "__main__":
    main()

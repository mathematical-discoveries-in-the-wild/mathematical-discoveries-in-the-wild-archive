#!/usr/bin/env python3
"""Numerical checks for the exact Aubin--Talenti threshold formula.

This script is supporting evidence, not the proof.  The packet derives the
Gamma formula and the N -> N+2 recurrence analytically.
"""

from __future__ import annotations

import argparse

import mpmath as mp


def log_q(n: int, s: mp.mpf) -> mp.mpf:
    """Log of Q_{N,s}=[U]_s^2/||grad U||_2^2."""
    b = mp.mpf(n) / 2
    a = b + s - 1
    return (
        mp.log(2)
        + b * mp.log(mp.pi)
        + mp.log(abs(mp.gamma(-s)))
        + 2 * mp.loggamma(a)
        + mp.loggamma(a - 1)
        + mp.loggamma(n)
        - mp.log(n)
        - mp.log(n - 2)
        - 2 * mp.loggamma(b - 1)
        - 2 * mp.loggamma(b)
        - mp.loggamma(n + 2 * s - 2)
    )


def q(n: int, s: mp.mpf) -> mp.mpf:
    return mp.exp(log_q(n, s))


def barrier(n: int) -> mp.mpf:
    return mp.power(2, mp.mpf(2) / n) - 1


def recurrence(n: int, s: mp.mpf) -> mp.mpf:
    """Exact quotient Q_{N+2,s}/Q_{N,s}."""
    return (
        2
        * mp.pi
        * (n + 1)
        * (n + 2 * s - 2)
        * (n + 2 * s - 4)
        / ((n + 2 * s - 1) * n * (n - 2) * (n + 2))
    )


def q_from_bessel_quadrature(n: int, s: mp.mpf) -> mp.mpf:
    """Independent radial quadrature before the K_1 Mellin evaluation."""
    b = mp.mpf(n) / 2
    omega = 2 * mp.pi**b / mp.gamma(b)
    fourier_constant = mp.power(2, 2 - b) / mp.gamma(b - 1)
    fractional_constant = (
        mp.power(4, s) * mp.gamma(b + s) / (mp.pi**b * abs(mp.gamma(-s)))
    )
    integrand = lambda r: r ** (n + 2 * s - 3) * mp.besselk(1, r) ** 2
    multiplier_energy = (
        omega
        * fourier_constant**2
        * (mp.quad(integrand, [0, 1]) + mp.quad(integrand, [1, mp.inf]))
    )
    raw_seminorm = 2 * multiplier_energy / fractional_constant
    gradient_energy = (
        omega
        * n
        * (n - 2)
        / 2
        * mp.gamma(b) ** 2
        / mp.gamma(n)
    )
    return raw_seminorm / gradient_energy


def threshold(s: mp.mpf, max_n: int) -> int:
    """First N>=7 with two consecutive strict successes."""
    for n in range(7, max_n):
        if q(n, s) < barrier(n) and q(n + 1, s) < barrier(n + 1):
            return n
    raise RuntimeError(f"no threshold pair through dimension {max_n}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, default=80)
    parser.add_argument("--max-n", type=int, default=500)
    args = parser.parse_args()
    mp.mp.dps = args.digits

    samples = [
        mp.mpf("0.05"),
        mp.mpf("0.1"),
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("0.75"),
        mp.mpf("0.9"),
        mp.mpf("0.99"),
    ]
    for s in samples:
        n0 = threshold(s, args.max_n)
        print(
            f"s={mp.nstr(s, 8):>8}  N0={n0:3d}  "
            f"F(N0)={mp.nstr(q(n0, s) / barrier(n0), 14)}  "
            f"F(N0+1)={mp.nstr(q(n0 + 1, s) / barrier(n0 + 1), 14)}"
        )

    # Audit the closed recurrence against independent Gamma evaluations.
    max_relative_error = mp.mpf("0")
    for s in samples:
        for n in range(7, 80):
            direct = q(n + 2, s) / q(n, s)
            closed = recurrence(n, s)
            max_relative_error = max(max_relative_error, abs(direct / closed - 1))
    print(f"max recurrence relative error: {mp.nstr(max_relative_error, 8)}")

    quadrature_error = mp.mpf("0")
    for n, s in [(5, mp.mpf("0.5")), (8, mp.mpf("0.25")), (19, mp.mpf("0.75"))]:
        direct = q_from_bessel_quadrature(n, s)
        closed = q(n, s)
        quadrature_error = max(quadrature_error, abs(direct / closed - 1))
    print(f"max Bessel-quadrature relative error: {mp.nstr(quadrature_error, 8)}")

    # The proof bounds the normalized recurrence by its s -> 1 endpoint.
    worst_margin = mp.inf
    for s in samples:
        for n in range(7, 80):
            normalized_ratio = recurrence(n, s) * barrier(n) / barrier(n + 2)
            worst_margin = min(worst_margin, 1 - normalized_ratio)
    print(f"minimum sampled monotonicity margin: {mp.nstr(worst_margin, 12)}")


if __name__ == "__main__":
    main()

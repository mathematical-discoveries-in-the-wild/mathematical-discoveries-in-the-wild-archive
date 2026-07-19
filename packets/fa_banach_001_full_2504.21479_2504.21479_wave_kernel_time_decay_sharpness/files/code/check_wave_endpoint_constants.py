#!/usr/bin/env python3
"""Deterministic algebra audit for the wave-kernel endpoint constants."""

from __future__ import annotations

import math

import mpmath as mp
import sympy as sp


def check_gapless_exact_models() -> None:
    # Integral_0^infty exp(i t r) r^(nu-1) exp(-r) dr
    # equals Gamma(nu) (1-i t)^(-nu).
    for nu in (3, 4, 5, 8):
        target = mp.gamma(nu) * mp.e ** (0.5j * mp.pi * nu)
        for t in (1000.0, 10000.0, 100000.0):
            scaled = (t**nu) * mp.gamma(nu) / (1.0 - 1.0j * t) ** nu
            relative_error = abs(scaled / target - 1.0)
            assert relative_error < 0.01, (nu, t, relative_error)


def check_positive_gap_jacobian() -> None:
    s, a = sp.symbols("s a", positive=True)
    for nu in (3, 4, 5, 8):
        mu = sp.Rational(nu, 2)
        transformed = (s + a) * (s * (s + 2 * a)) ** (mu - 1)
        coefficient = sp.simplify(sp.limit(transformed / s ** (mu - 1), s, 0, dir="+"))
        expected = sp.simplify(2 ** (mu - 1) * a**mu)
        assert sp.simplify(coefficient - expected) == 0, (nu, coefficient, expected)


def check_a2_angular_positivity() -> None:
    # Three positive reduced A_2 root directions, represented at angles
    # 0, pi/3 and 2*pi/3.  The product of squared root forms is nonnegative
    # and has a strictly positive circular integral.
    f = lambda theta: math.prod(
        math.cos(theta - angle) ** 2 for angle in (0.0, math.pi / 3.0, 2.0 * math.pi / 3.0)
    )
    samples = 200_000
    integral = (2.0 * math.pi / samples) * sum(f(2.0 * math.pi * j / samples) for j in range(samples))
    assert integral > 0.1, integral


def main() -> None:
    mp.mp.dps = 50
    check_gapless_exact_models()
    check_positive_gap_jacobian()
    check_a2_angular_positivity()
    print("all wave endpoint constant checks passed")


if __name__ == "__main__":
    main()

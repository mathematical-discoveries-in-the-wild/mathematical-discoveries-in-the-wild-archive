#!/usr/bin/env python3
"""Numerical sanity checks for the q,l-ball classification packet.

This checks exact identities used in the proof at high precision.  It is not
a proof of positive definiteness or of the theorem.
"""

from __future__ import annotations

import itertools

import mpmath as mp


mp.mp.dps = 60


def density(c: mp.mpf, q: mp.mpf, lam: mp.mpf) -> mp.mpf:
    return (q + lam) * c ** (q - 1) * (1 + c**q) ** (-lam / q - 2)


def mixture_value(q: mp.mpf, lam: mp.mpf, r: mp.mpf, s: mp.mpf) -> mp.mpf:
    split = r / s
    integrand = lambda c: max(r / c, s) ** (-lam) * density(c, q, lam)
    return mp.quad(integrand, [0, split, mp.inf])


def check_mixture() -> int:
    cases = 0
    for q, lam, r, s in itertools.product(
        [mp.mpf("2.5"), mp.mpf("4"), mp.mpf("7")],
        [mp.mpf("0.35"), mp.mpf("1.7"), mp.mpf("4.2")],
        [mp.mpf("0.4"), mp.mpf("1.3")],
        [mp.mpf("0.7"), mp.mpf("2.1")],
    ):
        mass = mp.quad(lambda c: density(c, q, lam), [0, 1, mp.inf])
        got = mixture_value(q, lam, r, s)
        want = (r**q + s**q) ** (-lam / q)
        assert mp.almosteq(mass, 1, rel_eps=mp.mpf("1e-40"), abs_eps=mp.mpf("1e-40"))
        assert mp.almosteq(got, want, rel_eps=mp.mpf("1e-35"), abs_eps=mp.mpf("1e-35"))
        cases += 1
    return cases


def check_hypergeometric() -> int:
    cases = 0
    dimensions = [
        (2, 2, mp.mpf("0.3")),
        (3, 2, mp.mpf("1.2")),
        (4, 4, mp.mpf("2.3")),
        (6, 2, mp.mpf("4.5")),
        (7, 3, mp.mpf("5.2")),
    ]
    z_grid = [
        mp.mpf("0"),
        mp.mpf("0.1"),
        mp.mpf("0.5"),
        mp.mpf("0.9"),
        mp.mpf("0.99"),
        mp.mpf("0.9999"),
    ]
    for a, b, lam in dimensions:
        assert lam > max(a, b) - 2
        assert lam < a + b
        old_a = (a + b - lam) / 2
        old_b = (b - lam) / 2
        c = mp.mpf(b) / 2 + 1
        new_a = (lam + 2 - a) / 2
        new_b = (lam + 2) / 2
        exponent = lam + 1 - mp.mpf(a + b) / 2
        gamma_denominator = mp.gamma((lam + 2 - b) / 2)
        assert gamma_denominator > 0
        assert new_a > 0 and new_b > 0
        for z in z_grid:
            original = mp.hyper([old_a, old_b], [c], z)
            transformed = (1 - z) ** exponent * mp.hyper([new_a, new_b], [c], z)
            assert mp.almosteq(
                original,
                transformed,
                rel_eps=mp.mpf("1e-40"),
                abs_eps=mp.mpf("1e-40"),
            )
            assert transformed / gamma_denominator > 0
            cases += 1
    return cases


def main() -> None:
    mixture_cases = check_mixture()
    hypergeometric_cases = check_hypergeometric()
    print(f"mixture cases: {mixture_cases}")
    print(f"hypergeometric cases: {hypergeometric_cases}")
    print("PASS: all sanity checks succeeded")


if __name__ == "__main__":
    main()


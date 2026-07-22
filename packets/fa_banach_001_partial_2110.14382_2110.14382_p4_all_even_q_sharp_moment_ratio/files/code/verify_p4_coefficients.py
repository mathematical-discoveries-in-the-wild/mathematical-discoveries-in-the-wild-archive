#!/usr/bin/env python3
"""Exact regression checks for the p=4 all-even-q proof packet.

This script is not part of the proof.  It verifies the moment-generating
recurrence, the coefficient-extraction certificate, and positivity for a
user-selected finite range.
"""

from __future__ import annotations

import argparse

import sympy as sp


def moments(max_m: int):
    """Return e_m(y)=E[X_z^(2m)]/(2m)! from the exact MGF recurrence."""
    y, z = sp.symbols("y z")
    coeff = [sp.Integer(0)] * (2 * max_m + 1)
    coeff[0] = sp.Integer(1)
    curvature = (1 - z**2) / 4
    for n in range(1, 2 * max_m + 1):
        coeff[n] = sp.expand(
            z**n / sp.factorial(n)
            - z * coeff[n - 1]
            + (curvature * coeff[n - 2] if n >= 2 else 0)
        )
    answer = {}
    for m in range(1, max_m + 1):
        pz = sp.Poly(coeff[2 * m], z)
        answer[m] = sp.Poly(
            sum(a * y ** (power[0] // 2) for power, a in pz.terms()), y
        ).as_expr()
    return y, answer


def extracted_coefficient(m: int, k: int) -> sp.Rational:
    """The closed coefficient [y^k](4^m e_m)."""
    return sp.simplify(
        sum(
            (-1) ** ell
            * 2**ell
            / sp.factorial(ell)
            * sp.binomial(2 * m - ell + 1, 2 * k - ell)
            for ell in range(2 * k + 1)
        )
    )


def check(max_m: int) -> None:
    y, em = moments(max_m)
    g = 1 + 4 * y + y**2

    for m in range(1, max_m + 1):
        scaled = sp.Poly(sp.expand(4**m * em[m]), y)
        for k in range(m + 1):
            assert scaled.coeff_monomial(y**k) == extracted_coefficient(m, k)

    for m in range(3, max_m + 1):
        numerator = sp.cancel(
            (2 * g * sp.diff(em[m], y) - m * sp.diff(g, y) * em[m])
            / (1 - y)
        )
        poly = sp.Poly(numerator, y)
        assert poly.degree() == m - 1
        assert all(c > 0 for c in poly.all_coeffs())

        # Closed forms for the first two coefficients of 4^m R_m.
        rho0 = sp.expand(4**m * poly.coeff_monomial(1))
        rho1 = sp.expand(4**m * poly.coeff_monomial(y))
        assert rho0 == 2 * (m - 2) * (2 * m - 1)
        cubic = 4 * m**3 - 24 * m**2 + 47 * m - 31
        assert rho1 == sp.Rational(2, 3) * (m - 2) * cubic

    # Check the transformed low-coefficient certificate symbolically.
    j, n = sp.symbols("j n", integer=True, positive=True)
    big_p = (
        8 * j**3
        + 12 * j**2 * n
        - 12 * j**2
        + 12 * j * n**2
        - 12 * j * n
        - 2 * j
        + 12 * n**3
        - 12 * n**2
        - 3 * n
        + 3
    )
    h = sp.symbols("h", integer=True, nonnegative=True)
    manifest = (
        8 * j**3
        - 2 * j
        + 12 * j**2 * h
        + 12 * j * (h**2 + h)
        + 12 * h**3
        + 24 * h**2
        + 9 * h
    )
    assert sp.expand(big_p.subs(n, h + 1) - manifest) == 0

    print(f"PASS: exact identities and coefficient positivity for 3<=m<={max_m}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=35)
    args = parser.parse_args()
    check(args.max_m)


if __name__ == "__main__":
    main()

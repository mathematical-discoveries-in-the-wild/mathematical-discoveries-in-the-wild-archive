#!/usr/bin/env python3
"""Exact finite-order audit of the all-j upper-critical formula.

The mathematical proof uses coefficient extraction and Lagrange residues for
arbitrary j.  This script independently reconstructs the complete invariant
Weyl recurrence (including all angular moments) and checks the resulting
closed formula through a requested order.
"""

from __future__ import annotations

import argparse

import sympy as sp

from explore_all_j import exact_c


def recovered_residues(j: int):
    d = 4*j-1
    mu = 6*j-1
    _, groups, terms, _ = exact_c(d, j, mu)
    assert set(groups) == {(j-1, 0), (j, 1)}
    residues = {}
    for (xp, ell), group in groups.items():
        x_integral = (
            sp.pi**(sp.Rational(d, 2))
            * sp.gamma(xp+sp.Rational(d, 2))
            * sp.gamma(mu+ell-xp-sp.Rational(d, 2))
            / (sp.gamma(sp.Rational(d, 2))*sp.gamma(mu+ell))
        )
        # The contour sign and the sign of f^(ell) cancel after the source's
        # outer factor -2, leaving this positive normalization.
        prefactor = 2*(2*sp.pi)**(-d)*sp.rf(mu, ell)/sp.factorial(ell)*x_integral
        residues[ell] = sp.factor(group/prefactor)
    return residues, terms


def expected_h0(j: int):
    bernoulli_coefficient = (
        2*(1-2**(2*j-1))*sp.bernoulli(2*j)/sp.factorial(2*j)
    )
    return sp.factor(
        sp.pi**(2*j)*(-1)**j*6*4**(j-1)*j*(2*j-1)*bernoulli_coefficient
    )


def expected_trace_constant(j: int):
    s_j = 2*(1-2**(2*j-1))*sp.bernoulli(2*j)/sp.factorial(2*j)
    return sp.factor(
        (-1)**j*6*(2*j-1)*sp.sqrt(sp.pi)
        / (2**(2*j+1)*sp.gamma(2*j-sp.Rational(1, 2)))
        * s_j
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--through", type=int, default=7)
    args = parser.parse_args()
    for j in range(1, args.through+1):
        residues, terms = recovered_residues(j)
        h0, h1 = residues[0], residues[1]
        assert h0 == expected_h0(j)
        assert h1 == -h0/(3*j)
        assert expected_trace_constant(j) > 0
        print(
            f"j={j}, d={4*j-1}, numerator monomials={terms}: "
            f"H0={h0}, H1/H0={sp.factor(h1/h0)}"
        )
    print("All exact full-recurrence assertions passed.")


if __name__ == "__main__":
    main()

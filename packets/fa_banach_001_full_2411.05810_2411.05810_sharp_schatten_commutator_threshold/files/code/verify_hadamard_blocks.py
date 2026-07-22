#!/usr/bin/env python3
"""Exact finite checks for the Hadamard blocks in the counterexample.

This is a smoke test, not a proof.  It verifies H H^T = N I exactly and the
closed-form eigenvalues of A^T A for several powers of two.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

import sympy as sp


def sylvester(order: int) -> sp.Matrix:
    h = sp.Matrix([[1]])
    while h.rows < order:
        h = h.row_join(h).col_join(h.row_join(-h))
    return h


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-power", type=int, default=6)
    args = parser.parse_args()

    for q in range(1, args.max_power + 1):
        n = 2**q
        h = sylvester(n)
        assert h * h.T == n * sp.eye(n)

        # Use a rational weight w=1/2 only to keep the check exact.
        w = Fraction(1, 2)
        a = sp.Rational(w.numerator, w.denominator) * h / n
        gram = a.T * a
        expected = sp.Rational(w.numerator**2, w.denominator**2 * n)
        assert gram == expected * sp.eye(n)
        assert gram.eigenvals() == {expected: n}
        print(f"N={n}: H H^T=N I; block singular value={w}/sqrt({n}) x {n}")

    print("PASS")


if __name__ == "__main__":
    main()

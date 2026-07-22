#!/usr/bin/env python3
"""Exact symbolic checks for the standard-Gaussian Kim--Milman packet.

This script verifies only the finite-dimensional algebra and elementary
double integral.  The smoothing and perturbative ODE arguments are proved in
the packet and are not replaced by this computation.
"""

import sympy as sp


def main() -> None:
    t, s = sp.symbols("t s", nonnegative=True)
    a = sp.Matrix([1, 0])
    b = sp.Matrix([1, 1])
    p = b * b.T
    q = a * a.T + 2 * b * b.T
    commutator = p * q - q * p

    r_t = sp.exp(-2 * t)
    r_s = sp.exp(-2 * s)
    scalar_integrand = r_t * r_s * (r_t - r_s)
    scalar_integral = sp.integrate(
        sp.integrate(scalar_integrand, (s, 0, t)), (t, 0, sp.oo)
    )
    skew_coefficient = sp.simplify(144 * scalar_integral) * commutator

    expected_commutator = sp.Matrix([[0, -1], [1, 0]])
    expected_coefficient = sp.Matrix([[0, 6], [-6, 0]])

    assert commutator == expected_commutator
    assert scalar_integral == -sp.Rational(1, 24)
    assert skew_coefficient == expected_coefficient

    print("P =")
    sp.pprint(p)
    print("Q =")
    sp.pprint(q)
    print("[P,Q] =")
    sp.pprint(commutator)
    print("double scalar integral =", scalar_integral)
    print("second-order skew coefficient =")
    sp.pprint(skew_coefficient)
    print("PASS: all exact checks agree with the proof.")


if __name__ == "__main__":
    main()

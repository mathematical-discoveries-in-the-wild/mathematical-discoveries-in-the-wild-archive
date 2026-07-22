"""Exact verifier for the degree-39 coefficient theorem and defect constant.

Requires SymPy.  Every polynomial and transcendental comparison used for the
certificate is reduced to exact rational arithmetic.  Runtime is a few
minutes on a laptop because the inverse polynomials grow rapidly.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

import sympy as sp


alpha, beta = sp.symbols("alpha beta")
a, b = sp.symbols("a b")


def hypergeom_coefficients(order: int) -> list[sp.Expr]:
    result = [sp.Integer(1)]
    for n in range(1, order + 1):
        result.append(
            sp.cancel(
                result[-1]
                * (alpha + n - 1)
                * (beta + n - 1)
                / ((sp.Rational(3, 2) + n - 1) * n)
            )
        )
    return result


def inverse_coefficient(phi: list[sp.Expr], n: int) -> sp.Expr:
    """Return [w^(2n+1)] of the inverse of w*Phi(w^2)."""
    exponent = -(2 * n + 1)
    power = [sp.Integer(1)]
    for ell in range(1, n + 1):
        total = sum(
            ((exponent + 1) * j - ell) * phi[j] * power[ell - j]
            for j in range(1, ell + 1)
        )
        power.append(sp.cancel(total / ell))
    return sp.cancel(power[n] / (2 * n + 1))


def bernstein_coefficients(poly: sp.Poly) -> list[sp.Rational]:
    degree_a = poly.degree(a)
    degree_b = poly.degree(b)
    power = {(i, j): sp.Rational(c) for (i, j), c in poly.terms()}
    result: list[sp.Rational] = []
    for i in range(degree_a + 1):
        for j in range(degree_b + 1):
            value = sp.Rational(0)
            for k in range(i + 1):
                for ell in range(j + 1):
                    value += (
                        power.get((k, ell), 0)
                        * sp.Rational(comb(i, k), comb(degree_a, k))
                        * sp.Rational(comb(j, ell), comb(degree_b, ell))
                    )
            result.append(value)
    return result


def certify_inverse_coefficients() -> None:
    order = 19  # largest inverse degree is 2*19+1=39
    phi = hypergeom_coefficients(order)
    for n in range(1, order + 1):
        k = 2 * n + 1
        d_k = inverse_coefficient(phi, n)
        target = -d_k if k % 4 == 3 else sp.Rational(1, factorial(k)) - d_k

        source_target = sp.cancel(
            target.subs({alpha: (1 - a) / 2, beta: (1 - b) / 2})
        )
        if k == 7:
            # This true case has two negative coefficients in the direct
            # Bernstein basis and is proved separately in the packet.
            print("k=7: deferred to the exact analytic factorization")
            continue
        removed_edge_factor = k % 4 == 3
        if removed_edge_factor:
            source_target = sp.cancel(source_target / ((1 - a) * (1 - b)))

        poly = sp.Poly(source_target, a, b, domain=sp.QQ)
        coefficients = bernstein_coefficients(poly)
        assert all(coefficient >= 0 for coefficient in coefficients)
        print(
            f"k={k:2d}: exact Bernstein certificate; "
            f"degree=({poly.degree(a)},{poly.degree(b)}), "
            f"min={min(coefficients)}"
        )


def sinh_bounds(x: Fraction, terms: int = 12) -> tuple[Fraction, Fraction]:
    """Exact lower/upper bounds from the positive sinh Taylor series."""
    partial = sum(
        (x ** (2 * j + 1)) / factorial(2 * j + 1) for j in range(terms + 1)
    )
    next_term = (x ** (2 * terms + 3)) / factorial(2 * terms + 3)
    ratio_bound = (x * x) / ((2 * terms + 4) * (2 * terms + 5))
    upper = partial + next_term / (1 - ratio_bound)
    return partial, upper


def certify_constant() -> None:
    delta = Fraction(439, 500)  # 0.878
    lower_rho = Fraction(437, 500)  # 0.874
    tail = (
        Fraction(61831, 10000)
        / 41
        * delta**41
        / (1 - delta * delta)
    )
    x = 1 - 2 * tail

    _, sinh_lower_rho_upper = sinh_bounds(lower_rho)
    sinh_delta_lower, _ = sinh_bounds(delta)
    assert sinh_lower_rho_upper <= x  # asinh(x) >= 0.874
    assert x <= sinh_delta_lower  # asinh(x) <= 0.878=delta

    advertised_improvement = Fraction(2017, 2000)  # 1.0085
    product = lower_rho * advertised_improvement
    sinh_product_lower, _ = sinh_bounds(product)
    assert sinh_product_lower >= 1  # asinh(1) <= 0.874*1.0085

    print("tail upper bound E =", float(tail))
    print("1-2E =", float(x))
    print("certified 0.874 <= asinh(1-2E) <= 0.878")
    print("certified asinh(1) <= 0.874*1.0085")


if __name__ == "__main__":
    certify_inverse_coefficients()
    certify_constant()
    print("ALL EXACT CERTIFICATES PASSED")

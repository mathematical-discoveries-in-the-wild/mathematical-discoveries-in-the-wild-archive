#!/usr/bin/env python3
"""Exact verifier for C_6 in dimensions 9 and 11 for P(x)=|x|^2.

The computation uses only rational arithmetic and SymPy's exact gamma
identities.  It implements the invariant Weyl-parametrix recurrence from
Aboud--Robert, integrates each monomial first in xi and then in x, and takes
the normalized contour residue.  No floating-point value is used in an
assertion.
"""

from __future__ import annotations

import sympy as sp


def invariant_symbols(dimension: int):
    """Return K_0,K_2,K_4,K_6 in (a,b,c,w) invariants.

    a=|x|^2, b=|xi|^2, c=x.xi, w=a-z, and L=b+w^2.  Differentiation
    in x at fixed z sends partial_a to D_a=partial_a+partial_w.
    """

    a, b, c, w = sp.symbols("a b c w")
    d = sp.Integer(dimension)
    L = b + w**2
    K0 = 1 / L

    def da_fixed_z(F):
        return sp.diff(F, a) + sp.diff(F, w)

    def laplace_x(F):
        return (
            2 * d * da_fixed_z(F)
            + 4 * a * da_fixed_z(da_fixed_z(F))
            + 4 * c * da_fixed_z(sp.diff(F, c))
            + b * sp.diff(F, c, 2)
        )

    def laplace_xi(F):
        return (
            2 * d * sp.diff(F, b)
            + 4 * b * sp.diff(F, b, 2)
            + 4 * c * sp.diff(F, b, c)
            + a * sp.diff(F, c, 2)
        )

    def S2(F):
        # Sum of the |alpha|+|beta|=2 terms in formula (3.10).
        xx_hessian_xi = (
            2 * a * sp.diff(F, b)
            + 4 * c**2 * sp.diff(F, b, 2)
            + 4 * a * c * sp.diff(F, b, c)
            + a**2 * sp.diff(F, c, 2)
        )
        return (
            sp.Rational(1, 4) * laplace_x(F)
            + sp.Rational(1, 2) * w * laplace_xi(F)
            + xx_hessian_xi
        )

    def S4(F):
        # D_x^4 L = 8(delta_ij delta_kl + delta_ik delta_jl
        #                    + delta_il delta_jk), hence the order-four
        # contraction is (1/16) Delta_xi^2 F.
        return sp.Rational(1, 16) * laplace_xi(laplace_xi(F))

    K2 = sp.factor(-K0 * S2(K0))
    K4 = sp.factor(-K0 * (S2(K2) + S4(K0)))
    K6 = sp.factor(-K0 * (S2(K4) + S4(K2)))

    # Low-order audit against equation (3.11) of the source for P=|x|^2.
    source_K2 = (2 * d * w + 4 * a) / L**3 + (
        -4 * w * b - 8 * c**2 - 8 * a * w**2
    ) / L**4
    assert sp.cancel(K2 - source_K2) == 0
    return (a, b, c, w, L), (K0, K2, K4, K6)


def exact_c6(dimension: int, mu: int):
    """Compute C_6^d(f) for f(z)=(z+1)^(-mu), P=|x|^2."""

    (a, b, c, w, L), (_, _, _, K6) = invariant_symbols(dimension)
    d = sp.Integer(dimension)
    mu = sp.Integer(mu)

    numerator, denominator = sp.together(K6).as_numer_denom()
    q = 10
    denominator_constant = sp.simplify(denominator / L**q)
    assert not denominator_constant.has(a, b, c, w)

    total = 0
    groups: dict[tuple[int, int], sp.Expr] = {}
    polynomial = sp.Poly(sp.expand(numerator), a, b, c, w)

    for (power_a, power_b, power_c, power_w), raw_coefficient in polynomial.terms():
        assert power_c % 2 == 0
        k = power_c // 2
        radial_power = power_b + k
        coefficient = sp.Rational(raw_coefficient) / denominator_constant

        # Spherical average of (x.xi)^(2k):
        # E[cos(theta)^(2k)] = (1/2)_k/(d/2)_k.
        angular_factor = sp.rf(sp.Rational(1, 2), k) / sp.rf(d / 2, k)
        convergence_gap = q - radial_power - d / 2
        assert convergence_gap > 0  # each monomial is honestly integrable

        xi_integral = (
            sp.pi ** (d / 2)
            * sp.gamma(radial_power + d / 2)
            * sp.gamma(convergence_gap)
            / (sp.gamma(d / 2) * sp.gamma(q))
            * angular_factor
        )

        x_power = power_a + k
        # The exponent after xi integration and multiplication by the outer
        # w=P-z in the trace formula.
        contour_power = power_w + 2 * radial_power + d - 2 * q + 1
        if contour_power >= 0:
            continue

        residue_order = -contour_power
        derivative_order = residue_order - 1
        contour_factor = (-1) ** residue_order / sp.factorial(derivative_order)

        # f^(ell)(a)=(-1)^ell (mu)_ell (a+1)^(-mu-ell).
        f_derivative_factor = (-1) ** derivative_order * sp.rf(mu, derivative_order)
        x_integral = (
            sp.pi ** (d / 2)
            * sp.gamma(x_power + d / 2)
            * sp.gamma(mu + derivative_order - x_power - d / 2)
            / (sp.gamma(d / 2) * sp.gamma(mu + derivative_order))
        )

        term = sp.simplify(
            -2
            * (2 * sp.pi) ** (-d)
            * coefficient
            * xi_integral
            * contour_factor
            * f_derivative_factor
            * x_integral
        )
        total += term
        key = (x_power, derivative_order)
        groups[key] = sp.simplify(groups.get(key, 0) + term)

    return sp.factor(sp.simplify(total)), {
        key: sp.factor(value) for key, value in sorted(groups.items()) if value != 0
    }


def main() -> None:
    c9, groups9 = exact_c6(9, 15)
    c11, groups11 = exact_c6(11, 18)

    expected9 = sp.Rational(212857, 901943132160) * sp.pi
    expected11 = sp.Rational(84227, 2727476031651840) * sp.pi
    assert c9 == expected9
    assert c11 == expected11
    assert c9 > 0 and c11 > 0

    print("d=9 grouped contributions:")
    for key, value in groups9.items():
        print(f"  (x power, f derivative order)={key}: {value}")
    print(f"C_6^(9)((z+1)^-15) = {c9}")
    print()
    print("d=11 grouped contributions:")
    for key, value in groups11.items():
        print(f"  (x power, f derivative order)={key}: {value}")
    print(f"C_6^(11)((z+1)^-18) = {c11}")
    print("All exact assertions passed.")


if __name__ == "__main__":
    main()

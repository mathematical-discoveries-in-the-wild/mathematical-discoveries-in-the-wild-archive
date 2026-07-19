"""Symmetry atlas for the 8/7 certificate.

This helper is not needed to verify the theorem.  It explains why the exact
verifier is small: the 130 polynomial checks collapse, under the natural
symmetries m <-> 1-m, r <-> 1-r, and m <-> r, into 10 classes.

For each class it reports a representative polynomial and the minimum exact
Bernstein coefficient on the four quadrants of [0,1]^2.  Nonnegative quadrant
coefficients give a compact hand-auditable version of the certificate.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

import sympy as sp

from verify_8over7_certificate import build_certificate_polynomials


def bernstein_coefficients(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]):
    expanded = sp.Poly(sp.expand(poly), *variables)
    if expanded.is_zero:
        return [[Fraction(0)]]
    nx = expanded.degree(variables[0])
    ny = expanded.degree(variables[1])
    power_coefficients = {}
    for monomial, coeff in expanded.terms():
        power_coefficients[monomial] = Fraction(int(coeff.p), int(coeff.q))

    output: list[list[Fraction]] = []
    for i in range(nx + 1):
        row = []
        for j in range(ny + 1):
            total = Fraction(0)
            for k in range(i + 1):
                for ell in range(j + 1):
                    coeff = power_coefficients.get((k, ell), Fraction(0))
                    if coeff:
                        total += (
                            coeff
                            * Fraction(comb(i, k), comb(nx, k))
                            * Fraction(comb(j, ell), comb(ny, ell))
                        )
            row.append(total)
        output.append(row)
    return output


def min_bernstein_on_box(
    poly: sp.Expr,
    variables: tuple[sp.Symbol, sp.Symbol],
    box: tuple[Fraction, Fraction, Fraction, Fraction],
) -> Fraction:
    m, r = variables
    m0, m1, r0, r1 = box
    local = sp.expand(
        poly.subs(
            {
                m: sp.Rational(m0.numerator, m0.denominator)
                + sp.Rational((m1 - m0).numerator, (m1 - m0).denominator) * m,
                r: sp.Rational(r0.numerator, r0.denominator)
                + sp.Rational((r1 - r0).numerator, (r1 - r0).denominator) * r,
            }
        )
    )
    flat = [entry for row in bernstein_coefficients(local, variables) for entry in row]
    return min(flat)


def canonical_key(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]) -> str:
    m, r = variables
    transforms = [
        {m: m, r: r},
        {m: 1 - m, r: r},
        {m: m, r: 1 - r},
        {m: 1 - m, r: 1 - r},
        {m: r, r: m},
        {m: 1 - r, r: m},
        {m: r, r: 1 - m},
        {m: 1 - r, r: 1 - m},
    ]
    candidates = []
    for transform in transforms:
        candidate = sp.Poly(sp.expand(poly.subs(transform)), m, r).as_expr()
        candidates.append(str(candidate))
    return min(candidates)


def centered_form(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]) -> sp.Expr:
    m, r = variables
    x, y = sp.symbols("x y")
    return sp.factor(sp.expand(poly.subs({m: (1 + x) / 2, r: (1 + y) / 2})))


def main() -> None:
    variables, checks = build_certificate_polynomials()
    groups: dict[str, list[tuple[str, sp.Expr]]] = {}
    for name, expression in checks:
        polynomial = sp.factor(sp.together(expression).as_numer_denom()[0])
        groups.setdefault(canonical_key(polynomial, variables), []).append((name, polynomial))

    quadrants = [
        (Fraction(0), Fraction(1, 2), Fraction(0), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1), Fraction(0), Fraction(1, 2)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(1)),
        (Fraction(1, 2), Fraction(1), Fraction(1, 2), Fraction(1)),
    ]

    print(f"checks={len(checks)}")
    print(f"symmetry_classes={len(groups)}")
    for index, (_, items) in enumerate(
        sorted(groups.items(), key=lambda item: (-len(item[1]), item[0]))
    ):
        name, representative = items[0]
        quadrant_minima = [
            min_bernstein_on_box(representative, variables, quadrant)
            for quadrant in quadrants
        ]
        print()
        print(f"class={index}")
        print(f"count={len(items)}")
        print(f"representative={name}")
        print(f"quadrant_minima={quadrant_minima}")
        print(f"centered={centered_form(representative, variables)}")


if __name__ == "__main__":
    main()

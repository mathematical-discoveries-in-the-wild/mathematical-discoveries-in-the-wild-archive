"""Exact verifier for the arXiv:1809.10616 universal 8/7 gap packet.

The verifier checks the two-parameter boundary certificate used in the packet.
All arithmetic in the Bernstein subdivision stage is rational.  The script
proves, over (m,r) in [0,1]^2, that:

1. the common denominator of the tensor A(m,r) is positive;
2. every vertex product satisfies |x^T A(m,r) y| <= 1;
3. the CHSH pairing <W,A(m,r)> is at least 16/7.

Together these imply the tensor-norm ratio lower bound 8/7 after the analytic
reductions in the packet.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

import sympy as sp


def _poly_coeffs(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]):
    p = sp.Poly(sp.expand(poly), *variables)
    if p.is_zero:
        return {}, 0, 0
    coeffs = {}
    for monomial, coeff in p.terms():
        coeffs[monomial] = Fraction(int(coeff.p), int(coeff.q))
    return coeffs, p.degree(variables[0]), p.degree(variables[1])


def _bernstein_coeffs(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]):
    coeffs, nx, ny = _poly_coeffs(poly, variables)
    out: list[list[Fraction]] = []
    for i in range(nx + 1):
        row = []
        for j in range(ny + 1):
            total = Fraction(0)
            for k in range(i + 1):
                for ell in range(j + 1):
                    coeff = coeffs.get((k, ell), Fraction(0))
                    if coeff:
                        total += (
                            coeff
                            * Fraction(comb(i, k), comb(nx, k))
                            * Fraction(comb(j, ell), comb(ny, ell))
                        )
            row.append(total)
        out.append(row)
    return out


def _bernstein_bounds(poly: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol]):
    coeffs = _bernstein_coeffs(poly, variables)
    flat = [entry for row in coeffs for entry in row]
    return min(flat), max(flat)


def _substitute_box(
    poly: sp.Expr,
    variables: tuple[sp.Symbol, sp.Symbol],
    box: tuple[Fraction, Fraction, Fraction, Fraction],
) -> sp.Expr:
    m, r = variables
    m0, m1, r0, r1 = box
    return sp.expand(
        poly.subs(
            {
                m: sp.Rational(m0.numerator, m0.denominator)
                + sp.Rational((m1 - m0).numerator, (m1 - m0).denominator) * m,
                r: sp.Rational(r0.numerator, r0.denominator)
                + sp.Rational((r1 - r0).numerator, (r1 - r0).denominator) * r,
            }
        )
    )


def prove_nonnegative(
    poly: sp.Expr,
    variables: tuple[sp.Symbol, sp.Symbol],
    box: tuple[Fraction, Fraction, Fraction, Fraction] = (
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(1),
    ),
    depth: int = 0,
    max_depth: int = 12,
) -> tuple[bool, int]:
    """Prove nonnegativity on a box by exact Bernstein subdivision."""

    local_poly = _substitute_box(poly, variables, box)
    lo, hi = _bernstein_bounds(local_poly, variables)
    if lo >= 0:
        return True, depth
    if hi < 0 or depth >= max_depth:
        return False, depth

    m0, m1, r0, r1 = box
    if (m1 - m0) >= (r1 - r0):
        mid = (m0 + m1) / 2
        first = (m0, mid, r0, r1)
        second = (mid, m1, r0, r1)
    else:
        mid = (r0 + r1) / 2
        first = (m0, m1, r0, mid)
        second = (m0, m1, mid, r1)

    ok_first, depth_first = prove_nonnegative(poly, variables, first, depth + 1, max_depth)
    if not ok_first:
        return False, depth_first
    ok_second, depth_second = prove_nonnegative(poly, variables, second, depth + 1, max_depth)
    return ok_second, max(depth_first, depth_second)


def boundary_vertices(parameter: sp.Symbol):
    """Vertices of H_{1+m,2-m}; parameter is m or r."""

    t = parameter
    return [
        sp.Matrix([1, t]),
        sp.Matrix([1, t - 1]),
        sp.Matrix([-1, -t]),
        sp.Matrix([-1, 1 - t]),
        sp.Matrix([t, 1]),
        sp.Matrix([t - 1, 1]),
        sp.Matrix([-t, -1]),
        sp.Matrix([1 - t, -1]),
    ]


def build_certificate_polynomials():
    m, r = sp.symbols("m r")
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    amat = sp.Matrix([[a11, a12], [a21, a22]])
    xverts = boundary_vertices(m)
    yverts = boundary_vertices(r)

    equations = [
        (xverts[0].T * amat * yverts[0])[0] - 1,
        (xverts[1].T * amat * yverts[4])[0] - 1,
        (xverts[4].T * amat * yverts[1])[0] - 1,
        (xverts[5].T * amat * yverts[5])[0] + 1,
    ]
    solution = sp.solve(equations, [a11, a12, a21, a22], simplify=True, dict=True)[0]
    common_denominator = sp.denom(solution[a11])
    certified_matrix = sp.Matrix(
        [
            [solution[a11], solution[a12]],
            [solution[a21], solution[a22]],
        ]
    )

    checks: list[tuple[str, sp.Expr]] = [("positive denominator", common_denominator)]

    objective = sp.simplify(solution[a11] + solution[a12] + solution[a21] - solution[a22])
    checks.append(
        (
            "CHSH objective at least 16/7",
            sp.simplify((objective - sp.Rational(16, 7)) * common_denominator),
        )
    )

    for i, x in enumerate(xverts):
        for j, y in enumerate(yverts):
            value = sp.simplify((x.T * certified_matrix * y)[0])
            checks.append(
                (
                    f"upper vertex inequality ({i},{j})",
                    sp.simplify((1 - value) * common_denominator),
                )
            )
            checks.append(
                (
                    f"lower vertex inequality ({i},{j})",
                    sp.simplify((1 + value) * common_denominator),
                )
            )
    return (m, r), checks


def main() -> None:
    variables, checks = build_certificate_polynomials()
    failures = []
    max_depth_used = 0
    for name, polynomial in checks:
        numerator = sp.together(polynomial).as_numer_denom()[0]
        ok, depth = prove_nonnegative(numerator, variables)
        max_depth_used = max(max_depth_used, depth)
        if not ok:
            failures.append(name)

    print(f"checks={len(checks)}")
    print(f"failures={len(failures)}")
    print(f"max_depth_used={max_depth_used}")
    if failures:
        for name in failures:
            print(f"FAILED: {name}")
        raise SystemExit(1)
    print("certificate verified")


if __name__ == "__main__":
    main()

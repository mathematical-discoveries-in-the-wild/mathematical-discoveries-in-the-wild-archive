#!/usr/bin/env python3
"""Exact symbolic checks for the Weak C6 obstruction in arXiv:2412.09987.

This script audits algebra used in the proof packet.  It is not a substitute
for the mixed-distributional-derivative proof.
"""

import sympy as sp


def main() -> None:
    y1, y2, y3 = sp.symbols("y1 y2 y3")
    h11, h12, h13, h21, h22, h23, h31, h32, h33 = sp.symbols(
        "h11 h12 h13 h21 h22 h23 h31 h32 h33"
    )

    y = (y1, y2, y3)
    K = sp.Matrix([y2 * y3, y1 * y3, -sp.Rational(1, 2) * y1 * y2])
    g1 = sp.Matrix([[h11, h12, h13]])
    g2 = sp.Matrix([[h21, h22, h23]])
    g3 = sp.Matrix([[h31, h32, h33]])

    def scalar(row: sp.Matrix, col: sp.Matrix) -> sp.Expr:
        return sp.expand((row * col)[0])

    R23 = sp.expand(scalar(g2, K.diff(y3)) + scalar(g3, K.diff(y2)))
    R13 = sp.expand(scalar(g1, K.diff(y3)) + scalar(g3, K.diff(y1)))
    R12 = sp.expand(scalar(g1, K.diff(y2)) + scalar(g2, K.diff(y1)))

    expected_R23 = (h22 - h33 / 2) * y1 + h21 * y2 + h31 * y3
    expected_R13 = h12 * y1 + (h11 - h33 / 2) * y2 + h32 * y3
    expected_R12 = -h13 * y1 / 2 - h23 * y2 / 2 + (h11 + h22) * y3
    assert sp.expand(R23 - expected_R23) == 0
    assert sp.expand(R13 - expected_R13) == 0
    assert sp.expand(R12 - expected_R12) == 0

    compatibility_defect = sp.expand(sp.diff(R23, y1) - sp.diff(R13, y2))
    assert compatibility_defect == h22 - h11

    # At x=(1,0,0), multiply the Hessian by 4*pi to avoid transcendental
    # constants.  The scaled Hessian is diag(2,-1,-1).
    axis_values = {
        h11: 2,
        h22: -1,
        h33: -1,
        h12: 0,
        h13: 0,
        h21: 0,
        h23: 0,
        h31: 0,
        h32: 0,
    }
    axis_R23 = sp.expand(R23.subs(axis_values))
    axis_R13 = sp.expand(R13.subs(axis_values))
    axis_R12 = sp.expand(R12.subs(axis_values))
    assert axis_R23 == -y1 / 2
    assert axis_R13 == sp.Rational(5, 2) * y2
    assert axis_R12 == y3

    # A general homogeneous cubic has only one coefficient for y1*y2*y3.
    # The first equation demands it be -1/2, while the second demands 5/2.
    coeffs = {}
    Q = 0
    for a in range(4):
        for b in range(4 - a):
            c = 3 - a - b
            symbol = sp.symbols(f"c{a}{b}{c}")
            coeffs[(a, b, c)] = symbol
            Q += symbol * y1**a * y2**b * y3**c
    c111 = coeffs[(1, 1, 1)]
    assert sp.Poly(sp.diff(Q, y2, y3), *y).coeff_monomial(y1) == c111
    assert sp.Poly(sp.diff(Q, y1, y3), *y).coeff_monomial(y2) == c111
    assert sp.solve(
        [c111 + sp.Rational(1, 2), c111 - sp.Rational(5, 2)], [c111]
    ) == []

    # Audit the tentative cubic from Question 6.4.
    K1 = sp.Matrix(
        [y1 * y2 * y3, y1**2 * y3 / 2, -y1**2 * y2 / 4]
    )
    K2 = sp.Matrix(
        [y2**2 * y3 / 2, y1 * y2 * y3, -y1 * y2**2 / 4]
    )
    K3 = sp.Matrix(
        [y2 * y3**2 / 2, y1 * y3**2 / 2, -y1 * y2 * y3 / 2]
    )
    proposed_Q = sp.expand(scalar(g1, K1) + scalar(g2, K2) + scalar(g3, K3))
    residuals = (
        sp.expand(sp.diff(proposed_Q, y2, y3) - R23),
        sp.expand(sp.diff(proposed_Q, y1, y3) - R13),
        sp.expand(sp.diff(proposed_Q, y1, y2) - R12),
    )
    assert residuals == (h11 * y1, h22 * y2, -h33 * y3 / 2)

    print("R23 =", R23)
    print("R13 =", R13)
    print("R12 =", R12)
    print("compatibility defect d1(R23)-d2(R13) =", compatibility_defect)
    print("scaled axis right-hand sides =", axis_R23, ";", axis_R13, ";", axis_R12)
    print("proposed-cubic residuals =", residuals)
    print("all exact checks passed")


if __name__ == "__main__":
    main()

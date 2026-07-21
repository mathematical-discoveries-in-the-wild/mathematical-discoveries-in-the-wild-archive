#!/usr/bin/env python3
"""Symbolically verify the finite-dimensional identities in the packet.

This is a regression check for signs and normalization constants.  The
Gaussian-kernel argument in main.tex is the proof.
"""

import sympy as sp


def main() -> None:
    sqrt2 = sp.sqrt(2)
    u1 = sp.Matrix([1, 0])
    u2 = sp.Matrix([0, 1])
    u3 = sp.Matrix([1 / sqrt2, 1 / sqrt2])
    u4 = sp.Matrix([1 / sqrt2, -1 / sqrt2])
    directions = [u1, u2, u3, u4]
    alpha = [-1, -1, 1, 1]
    heights = [sp.Integer(1), sp.Integer(1), sqrt2, sqrt2]

    tensor_relation = sp.zeros(2)
    for coefficient, direction in zip(alpha, directions):
        tensor_relation += coefficient * direction * direction.T
    assert tensor_relation == sp.zeros(2)

    x1, x2 = sp.symbols("x1 x2", real=True)
    x = sp.Matrix([x1, x2])
    quadratic_relation = sp.simplify(
        sum(
            coefficient * (direction.dot(x)) ** 2
            for coefficient, direction in zip(alpha, directions)
        )
    )
    assert quadratic_relation == 0

    c_dot_g = sp.simplify(sum(a * h**2 for a, h in zip(alpha, heights)))
    g_norm_sq = sp.simplify(sp.Rational(8, 3) * sum(h**3 for h in heights))
    base_radius_sq = sp.simplify(sp.Rational(1, 2) * sum(heights))
    radius_drop = sp.simplify(c_dot_g**2 / g_norm_sq)
    improved_radius_sq = sp.simplify(base_radius_sq - radius_drop)

    mu1 = sp.simplify(4 * sum(heights))
    conjectured_coefficient = sp.simplify(mu1 / 4)
    improved_coefficient = sp.simplify(2 * improved_radius_sq)
    strict_gap = sp.simplify(conjectured_coefficient - improved_coefficient)

    assert c_dot_g == 2
    assert sp.simplify(
        g_norm_sq - sp.Rational(16, 3) * (1 + 2 * sqrt2)
    ) == 0
    assert base_radius_sq == 1 + sqrt2
    assert sp.simplify(
        radius_drop - sp.Rational(3, 4) / (1 + 2 * sqrt2)
    ) == 0
    assert mu1 == 8 + 8 * sqrt2
    assert sp.simplify(
        strict_gap - sp.Rational(3, 2) / (1 + 2 * sqrt2)
    ) == 0
    assert strict_gap > 0

    print("tensor relation =")
    sp.pprint(tensor_relation)
    print(f"<c,g> = {c_dot_g}")
    print(f"||g||^2 = {g_norm_sq}")
    print(f"R_0^2 = {base_radius_sq}")
    print(f"radius drop = {radius_drop}")
    print(f"mu_1^E(K) = {mu1}")
    print(f"conjectured coefficient = {conjectured_coefficient}")
    print(f"strict upper coefficient = {improved_coefficient}")
    print(f"strict gap = {strict_gap} = {sp.N(strict_gap, 12)}")


if __name__ == "__main__":
    main()

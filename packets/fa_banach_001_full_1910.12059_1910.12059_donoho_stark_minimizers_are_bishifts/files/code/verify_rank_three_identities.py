#!/usr/bin/env python3
"""Exact symbolic checks for the strict-support expressions in the proof."""

import sympy as sp


u, v, a, b, r = sp.symbols("u v a b r", positive=True)
t = sp.symbols("t")
s = a * v - b * u + 1
root_polynomial = t**2 - s * t - b * u

assert sp.simplify(
    root_polynomial.subs(t, sp.Rational(1, 2))
    + (1 + 2 * a * v + 2 * b * u) / 4
) == 0

nu_minus_one = 1 + 1 / u + 4 / v
gap_minus_one = sp.factor((1 + u) * (1 - 1 / nu_minus_one) - 1)
assert sp.simplify(
    gap_minus_one - 4 * u / (v * nu_minus_one)
) == 0

nu_two = 1 + 4 / u + 1 / v
gap_two = sp.factor((1 + v) * (1 - 1 / nu_two) - 1)
assert sp.simplify(gap_two - 4 * v / (u * nu_two)) == 0

type_ii_fp_gap = sp.factor(4 * r**2 / (1 + 2 * r) - 1)
type_ii_complex_gap = sp.factor(2 * r * (1 + r) / (1 + 2 * r) - 1)
assert sp.simplify(type_ii_fp_gap - (4 * r**2 - 2 * r - 1) / (2 * r + 1)) == 0
assert sp.simplify(type_ii_complex_gap - (2 * r**2 - 1) / (2 * r + 1)) == 0

print("type-I P(1/2) =", sp.factor(root_polynomial.subs(t, sp.Rational(1, 2))))
print("type-I lambda=-1 support gap =", gap_minus_one)
print("type-I lambda=2 support gap =", gap_two)
print("type-II FP-omission gap =", type_ii_fp_gap)
print("type-II complex-omission gap =", type_ii_complex_gap)
print("all symbolic identities verified")

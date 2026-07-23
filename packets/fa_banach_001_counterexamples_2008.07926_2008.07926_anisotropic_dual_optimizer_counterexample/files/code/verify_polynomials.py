#!/usr/bin/env python3
"""Exact symbolic checks for the anisotropic dual-optimizer packet."""

import sympy as sp


x, y, z, A, B = sp.symbols("x y z A B")
s = x + y + z


def f(parameter, u, v):
    parameter = sp.sympify(parameter)
    return (
        -sp.Rational(1, 12) * (u**3 + v**3)
        - sp.Rational(1, 2) * u * v * (u + v)
        - (parameter - 2)
        * (
            sp.Rational(1, 12) * u**2
            + sp.Rational(1, 3) * u * v
            + sp.Rational(1, 12) * v**2
        )
        - sp.Rational(1, 12) * (1 - 2 * parameter) * (u + v)
        - sp.Rational(1, 18) * parameter
    )


h12 = (x - y) * (x + y - 1) ** 2
h13 = x * z * (2 * x + z - 2)
h23 = -y * z * (2 * y + z - 2)
h_total = h12 + h13 + h23

source_gap = x * y * z - f(A, x, y) - f(A, x, z) - f(A, y, z)
assert sp.expand(source_gap - (s - 1) ** 2 * (s + A) / 6) == 0
assert sp.expand(h_total - (s - 1) ** 2 * (x - y)) == 0
assert sp.diff(h_total, x, y, z) == 0

g12 = f(1, x, y) + h12 / 12
g13 = f(1, x, z) + h13 / 12
g23 = f(1, y, z) + h23 / 12
new_gap = sp.factor(x * y * z - g12 - g13 - g23)
expected_gap = (s - 1) ** 2 * (2 + x + 3 * y + 2 * z) / 12
assert sp.expand(new_gap - expected_gap) == 0

f_b_total = f(B, x, y) + f(B, x, z) + f(B, y, z)
new_total = g12 + g13 + g23
difference = sp.Poly(sp.expand(new_total - f_b_total), x, y, z)
assert difference.as_expr() != 0
assert sp.diff(difference.as_expr(), x).subs({x: 0, y: 0, z: 0}) != 0

print("source gap:", sp.factor(source_gap))
print("pair perturbation sum:", sp.factor(h_total))
print("new gap:", new_gap)
print("all exact polynomial checks passed")

#!/usr/bin/env python3
"""Exact algebra check for the packet's twice-integrated identity.

This verifies the calculus identity on a polynomial kernel profile and a
generic polynomial F.  The proof packet separately justifies the improper
endpoint limits for the singular kernels in the source paper.
"""

import sympy as sp


t, x, d = sp.symbols("t x d", positive=True, finite=True)
z = sp.symbols("z", real=True)

F = z**6 - 2 * z**4 + 3 * z**2 + z
Fpp = sp.diff(F, z, 2)

# h=(1-t)^3, Q=int_t^1 h=(1-t)^4/4, and k=-h'=3(1-t)^2.
Q = (1 - t) ** 4 / 4
k = 3 * (1 - t) ** 2

lhs = sp.integrate(
    Q * (Fpp.subs(z, x + d * t) + Fpp.subs(z, x - d * t)),
    (t, 0, 1),
)
second_difference = (
    F.subs(z, x + d * t) + F.subs(z, x - d * t) - 2 * F.subs(z, x)
)
rhs = sp.integrate(k * second_difference, (t, 0, 1)) / d**2

difference = sp.factor(sp.expand(lhs - rhs))
print(f"symbolic_difference={difference}")
if difference != 0:
    raise SystemExit("FAIL: the two sides are not identical")
print("PASS")

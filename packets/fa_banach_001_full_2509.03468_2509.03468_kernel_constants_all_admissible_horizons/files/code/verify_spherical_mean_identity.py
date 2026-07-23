#!/usr/bin/env python3
"""Exact check of the multidimensional spherical-mean identity.

The check uses n=3, F(y)=|y|^4, an arbitrary squared center radius a=|x|^2,
and g(r)=(1-r)^4.  With Q'(r)=-g(r)/r^(n-1), it verifies

  int_B Q(|z|) Delta F(x+d z) dz
    = |S^(n-1)|/d^2 int_0^1 -g'(r) (M_x(r)-M_x(0)) dr.

The common sphere-area factor is omitted.
"""

import sympy as sp


r, s, a, d = sp.symbols("r s a d", positive=True, finite=True)
n = sp.Integer(3)
g = (1 - r) ** 4
Q = sp.integrate((1 - s) ** 4 / s ** (n - 1), (s, r, 1))

# For F(y)=|y|^4:
# Delta F(y)=4(n+2)|y|^2 and
# average_S |x+d r theta|^4
# = a^2 + (2+4/n) a d^2 r^2 + d^4 r^4.
average_laplacian = 4 * (n + 2) * (a + d**2 * r**2)
mean_increment = (2 + sp.Rational(4, n)) * a * d**2 * r**2 + d**4 * r**4

lhs = sp.integrate(Q * r ** (n - 1) * average_laplacian, (r, 0, 1))
rhs = sp.integrate(-sp.diff(g, r) * mean_increment, (r, 0, 1)) / d**2
difference = sp.factor(sp.expand(lhs - rhs))

print(f"Q(r)={sp.simplify(Q)}")
print(f"symbolic_difference={difference}")
if difference != 0:
    raise SystemExit("FAIL: spherical-mean identity mismatch")
print("PASS")

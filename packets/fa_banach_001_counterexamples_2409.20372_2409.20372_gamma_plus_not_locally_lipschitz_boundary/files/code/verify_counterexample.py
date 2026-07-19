#!/usr/bin/env python3
"""Exact checks for the gamma-plus boundary counterexample."""

import sympy as sp


V = sp.Matrix([
    [4, 1],
    [-1, -1],
    [-4, 1],
    [0, 4],
])
A = V * V.T
H = sp.Matrix([[81, 7], [7, 44]])

expected_A = sp.Matrix([
    [17, -5, -15, 4],
    [-5, 2, 3, -4],
    [-15, 3, 17, 4],
    [4, -4, 4, 16],
])

assert A == expected_A
assert A.rank() == 2
assert H.trace() == 125

t = sp.symbols("t", real=True)
Q = 81 + 14 * t + 44 * t**2
pieces = [
    (-1 - 7 * t, 5 * (t**2 - 16)),
    (7 - 5 * t, -19 * (t + 4) * (t + sp.Rational(8, 19))),
    (9 - 3 * t, -t * (68 + 35 * t)),
    (9 + 5 * t, 19 * t * (4 - t)),
    (1 + 7 * t, 5 * (t**2 - 16)),
]
for norm_piece, factored_gap in pieces:
    assert sp.expand(norm_piece**2 - Q - factored_gap) == 0

q0 = sp.Matrix([1, 0])
qp = sp.Matrix([1, 4])
qm = sp.Matrix([-1, 4])
weights = [sp.Rational(15, 16), sp.Rational(1, 32), sp.Rational(1, 32)]
directions = [q0, qp, qm]

frame = sp.zeros(2)
for weight, q in zip(weights, directions):
    frame += weight * q * q.T
assert frame == sp.eye(2)


def l1(vector: sp.Matrix) -> sp.Expr:
    return sum(abs(int(entry)) for entry in vector)


x0, xp, xm = [V * q for q in directions]
assert x0 == sp.Matrix([4, -1, -4, 0])
assert xp == sp.Matrix([8, -5, 0, 16])
assert xm == sp.Matrix([0, -3, 8, 16])
assert [l1(x0), l1(xp), l1(xm)] == [9, 29, 27]

cost = sum(weight * l1(x) ** 2 for weight, x in zip(weights, [x0, xp, xm]))
assert cost == 125
assert xp - xm == 2 * x0

# Equality at the three contact vectors would impose these second coordinates.
tx0_second = -9
txp_second = -29
txm_second = -27
assert txp_second - txm_second == -2
assert 2 * tx0_second == -18
assert txp_second - txm_second != 2 * tx0_second

print("A =")
sp.pprint(A)
print("rank(A) =", A.rank())
print("H =")
sp.pprint(H)
print("tight frame =")
sp.pprint(frame)
print("optimal factorization cost =", cost)
print("contact relation: x_plus - x_minus = 2*x_zero")
print("forced second coordinates: -29 - (-27) = -2, but 2*(-9) = -18")
print("all exact checks passed")


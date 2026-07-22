#!/usr/bin/env python3
"""Exact and numerical checks for the stretched-tetrahedron counterexample."""

from itertools import combinations

import sympy as sp


def length(x):
    return sp.sqrt(sp.simplify(x.dot(x)))


def triangle_area(a, b, c):
    return sp.simplify(length((b - a).cross(c - a)) / 2)


def triangle_inradius(a, b, c):
    area = triangle_area(a, b, c)
    perimeter = length(b - a) + length(c - a) + length(c - b)
    return sp.simplify(2 * area / perimeter)


sqrt = sp.sqrt
v = [
    sp.Matrix([0, 0, 0]),
    sp.Matrix([1, 0, 0]),
    sp.Matrix([sp.Rational(1, 2), sqrt(3) / 2, 0]),
    sp.Matrix([sp.Rational(1, 2), 1 / (2 * sqrt(3)), sqrt(sp.Rational(2, 3))]),
]

# The input tetrahedron is regular with unit edge length.
assert all(sp.simplify(length(v[j] - v[i]) - 1) == 0 for i, j in combinations(range(4), 2))

T = sp.diag(3, 1, 1)
w = [T * x for x in v]

volume = sp.simplify(abs(sp.det(sp.Matrix.hstack(w[1] - w[0], w[2] - w[0], w[3] - w[0]))) / 6)
facets = list(combinations(range(4), 3))
areas = [triangle_area(*(w[i] for i in f)) for f in facets]
facet_radii = [triangle_inradius(*(w[i] for i in f)) for f in facets]
surface_area = sp.simplify(sum(areas))
radius = sp.simplify(3 * volume / surface_area)

assert sp.simplify(volume - sqrt(2) / 4) == 0
assert sorted(map(str, areas)) == sorted(map(str, [3 * sqrt(3) / 4] * 2 + [sqrt(11) / 4] * 2))

r_A = 3 * sqrt(3) / (2 * (3 + 2 * sqrt(3)))
r_B = sqrt(11) / (2 * (1 + 2 * sqrt(3)))
assert all(any(sp.simplify(x - y) == 0 for y in (r_A, r_B)) for x in facet_radii)
assert sp.simplify(radius - 3 * sqrt(2) / (2 * (3 * sqrt(3) + sqrt(11)))) == 0

q_A = sp.simplify(radius / r_A)
q_B = sp.simplify(radius / r_B)
q_regular = 1 / sqrt(2)

# Exact positivity certificates used in the written proof.
certificate_A = sp.simplify(3 * sqrt(3) + sqrt(11) - 2 * (3 + 2 * sqrt(3)) / sqrt(3))
certificate_B_squared = sp.simplify((3 * sqrt(33)) ** 2 - (12 * sqrt(3) - 5) ** 2)
assert sp.simplify(certificate_A - (sqrt(3) + sqrt(11) - 4)) == 0
assert float(certificate_A) > 0
assert sp.simplify(certificate_B_squared - (120 * sqrt(3) - 160)) == 0
assert float(certificate_B_squared) > 0
assert float(q_A) < float(q_regular)
assert float(q_B) < float(q_regular)

print(f"volume = {volume}")
print(f"facet areas = {areas}")
print(f"inradius = {radius}")
print(f"facet inradii = {facet_radii}")
print(f"type-A ratio = {q_A} = {sp.N(q_A, 12)}")
print(f"type-B ratio = {q_B} = {sp.N(q_B, 12)}")
print(f"regular ratio = {q_regular} = {sp.N(q_regular, 12)}")
print(f"certificate A = {certificate_A} > 0")
print(f"certificate B after squaring = {certificate_B_squared} > 0")
print("PASS: every facet/body ratio is strictly below the regular-tetrahedron value.")

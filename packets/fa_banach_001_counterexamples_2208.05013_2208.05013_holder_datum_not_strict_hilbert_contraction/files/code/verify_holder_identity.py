"""Verify the 2x2 Holder-datum Hilbert-distance equality.

For the datum A_1=A_2=I_2 and w_1=w_2=1/2, the source Picard map is G(X)=X.
Normalizing by a positive matrix norm does not change Hilbert projective
distance.
"""

from __future__ import annotations

import math


def hilbert_diag(x: tuple[float, float], y: tuple[float, float]) -> float:
    ratios = [x_i / y_i for x_i, y_i in zip(x, y)]
    return math.log(max(ratios) / min(ratios))


def normalize_operator_diag(x: tuple[float, float]) -> tuple[float, float]:
    scale = max(x)
    return tuple(x_i / scale for x_i in x)


X = (2.0, 1.0)
Y = (1.0, 1.0)

before = hilbert_diag(X, Y)
after = hilbert_diag(normalize_operator_diag(X), normalize_operator_diag(Y))

print(f"delta_H(X,Y) = {before:.12f}")
print(f"delta_H(tildeG(X),tildeG(Y)) = {after:.12f}")
print(f"log(2) = {math.log(2):.12f}")
print(f"strictly_decreased = {after < before}")

assert abs(before - math.log(2)) < 1e-12
assert abs(after - before) < 1e-12
assert not (after < before)

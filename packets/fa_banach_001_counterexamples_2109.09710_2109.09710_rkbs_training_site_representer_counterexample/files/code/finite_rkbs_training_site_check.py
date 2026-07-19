#!/usr/bin/env python3
"""Exact checks for the finite RKBS training-site counterexample."""

from fractions import Fraction
from math import sqrt

import numpy as np


s = Fraction(3, 5)
K = np.array([[1.0, float(s), 0.0], [float(s), 1.0, float(s)], [0.0, float(s), 1.0]])

eigs = np.linalg.eigvalsh(K)
print("kernel eigenvalues:", eigs)
assert np.all(eigs > 0)

print("exact determinant:", Fraction(7, 25))
print("exact eigenvalues:", "1,", f"1 - 3*sqrt(2)/5 = {1 - 3 * sqrt(2) / 5:.12f},", f"1 + 3*sqrt(2)/5 = {1 + 3 * sqrt(2) / 5:.12f}")


def h(m: Fraction) -> Fraction:
    return 2 * abs(Fraction(1) - s * m) + abs(m)


candidates = [Fraction(-2), Fraction(0), Fraction(5, 3), Fraction(2), Fraction(10, 3)]
for candidate in candidates:
    print(f"h({candidate}) = {h(candidate)}")

assert h(Fraction(5, 3)) == Fraction(5, 3)
assert h(Fraction(0)) == Fraction(2)

# Check the three linear regions around the kink points.
assert h(Fraction(-1)) > h(Fraction(0)) > h(Fraction(5, 3))
assert h(Fraction(2)) > h(Fraction(5, 3))

mu_star = np.array([0.0, 5.0 / 3.0, 0.0])
observed = np.array([[1.0, float(s), 0.0], [0.0, float(s), 1.0]]) @ mu_star
print("mu_star:", mu_star)
print("observed training values:", observed)
print("TV(mu_star):", np.abs(mu_star).sum())

assert np.allclose(observed, [1.0, 1.0])
assert abs(np.abs(mu_star).sum() - 5.0 / 3.0) < 1e-12

print("Training-supported interpolant has TV = 2, strictly larger than 5/3.")

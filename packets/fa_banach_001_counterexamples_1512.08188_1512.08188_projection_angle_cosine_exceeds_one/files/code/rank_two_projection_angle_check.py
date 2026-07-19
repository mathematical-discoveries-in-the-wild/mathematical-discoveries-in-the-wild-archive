#!/usr/bin/env python3
"""Sanity checks for the two-dimensional projection-angle counterexample."""

import math

import numpy as np


def op_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


P1 = np.array([[1.0, 0.0], [0.0, 0.0]])
P2 = np.array([[1.0, 0.0], [1.0, 0.0]])
P12 = np.zeros((2, 2))

Q1 = np.eye(2) - P1
Q2 = np.eye(2) - P2

assert np.allclose(P1 @ P1, P1)
assert np.allclose(P2 @ P2, P2)
assert np.allclose(P12 @ P1, P12)
assert np.allclose(P12 @ P2, P12)

cosine = max(op_norm(P1 @ (P2 - P12)), op_norm(P2 @ (P1 - P12)))

print(f"||P1(P2-P12)|| = {op_norm(P1 @ (P2 - P12)):.12f}")
print(f"||P2(P1-P12)|| = {op_norm(P2 @ (P1 - P12)):.12f}")
print(f"defined cosine    = {cosine:.12f}")
print(f"sqrt(2)           = {math.sqrt(2):.12f}")

assert abs(cosine - math.sqrt(2)) < 1e-12
assert cosine > 1.0

# Any projection R onto span(e2) has form [[0, 0], [c, 1]].
# R Q1 = R forces c = 0; then R Q2 = Q2 != Q1 = R.
R = Q1.copy()
assert np.allclose(R @ Q1, R)
assert not np.allclose(R @ Q2, R)

print("Complement angle obstruction verified: no compatible R can exist.")

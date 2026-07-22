#!/usr/bin/env python3
"""Check the closed antipodal formula against the augmented interpolation system.

This is finite-dimensional numerical evidence only. The proof in main.tex is
the exact ODE argument.
"""

from __future__ import annotations

import math

import numpy as np


def closed_value(n: int) -> float:
    if n < 5 or n % 2 == 0:
        raise ValueError("n must be odd and at least 5")
    return ((2.0 * math.cos(math.pi / n) - 1.0) / math.cos(math.pi / (2.0 * n)) - 1.0) / n


def augmented_value(n: int) -> float:
    theta = 2.0 * math.pi * np.arange(n) / n
    differences = theta[:, None] - theta[None, :]
    kernel_matrix = np.sqrt(np.maximum(0.0, 1.0 - np.cos(differences)))
    polynomial_matrix = np.column_stack((np.ones(n), np.cos(theta), np.sin(theta)))
    augmented = np.block(
        [
            [kernel_matrix, polynomial_matrix],
            [polynomial_matrix.T, np.zeros((3, 3))],
        ]
    )
    right_hand_side = np.concatenate((np.eye(n)[0], np.zeros(3)))
    solution = np.linalg.solve(augmented, right_hand_side)
    kernel_at_pi = np.sqrt(np.maximum(0.0, 1.0 - np.cos(math.pi - theta)))
    polynomial_at_pi = np.array((1.0, -1.0, 0.0))
    return float(kernel_at_pi @ solution[:n] + polynomial_at_pi @ solution[n:])


def main() -> None:
    limit = 7.0 * math.pi**2 / 8.0
    print(f"predicted limit 7*pi^2/8 = {limit:.12f}")
    print(" N        augmented          closed          abs_error       -N^3*closed")
    for n in (9, 13, 17, 25, 33, 49, 65, 97, 129):
        numeric = augmented_value(n)
        exact = closed_value(n)
        print(
            f"{n:3d}  {numeric: .12e}  {exact: .12e}  "
            f"{abs(numeric - exact):.3e}  {-n**3 * exact:.10f}"
        )


if __name__ == "__main__":
    main()

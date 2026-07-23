#!/usr/bin/env python3
"""Finite numerical checks for the rank-two coordinate-gap lemma.

This script is not part of the proof. It samples complex two-dimensional
subspaces, enumerates all coordinate subsets, and checks that the largest
eigenvalue gap is at least 1/4 up to floating-point tolerance.
"""

from itertools import combinations

import numpy as np


def best_gap(isometry: np.ndarray) -> float:
    rows = [np.outer(row.conj(), row) for row in isometry]
    dimension = len(rows)
    best = 0.0
    for size in range(dimension + 1):
        for subset in combinations(range(dimension), size):
            compression = sum(
                (rows[index] for index in subset), np.zeros((2, 2), complex)
            )
            eigenvalues = np.linalg.eigvalsh(compression)
            best = max(best, float(eigenvalues[1] - eigenvalues[0]))
    return best


def main() -> None:
    rng = np.random.default_rng(221102775)
    checked = 0
    minimum = float("inf")
    for ambient_dimension in range(2, 11):
        for _ in range(40):
            matrix = (
                rng.standard_normal((ambient_dimension, 2))
                + 1j * rng.standard_normal((ambient_dimension, 2))
            )
            isometry, _ = np.linalg.qr(matrix)
            gap = best_gap(isometry)
            assert gap >= 0.25 - 1e-10, (ambient_dimension, gap)
            minimum = min(minimum, gap)
            checked += 1
    print(f"checked={checked} minimum_best_gap={minimum:.12f}")


if __name__ == "__main__":
    main()

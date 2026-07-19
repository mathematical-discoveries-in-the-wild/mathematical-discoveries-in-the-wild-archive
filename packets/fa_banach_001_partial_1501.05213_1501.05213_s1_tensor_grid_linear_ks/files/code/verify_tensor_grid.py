#!/usr/bin/env python3
"""Regression checks for the weighted tensor-grid linear-KS theorem.

The mathematical proof is in the packet. This script enumerates selectors and
checks the explicit singular-value formulas on random small instances.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def lhs_formula(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, axis=1).mean())


def modified_rhs_formula(a: np.ndarray) -> float:
    n = a.shape[0]
    total = 0.0
    count = 0
    for choice in itertools.product(range(n), repeat=n):
        block_norms = []
        for k in range(n):
            values = [abs(a[j, k]) for j in range(n) if choice[j] == k]
            block_norms.append(float(np.linalg.norm(values)))
        total += sum(block_norms)
        count += 1
    return total / count


def permutation_rhs_formula(a: np.ndarray) -> float:
    n = a.shape[0]
    values = [
        sum(abs(a[j, permutation[j]]) for j in range(n))
        for permutation in itertools.permutations(range(n))
    ]
    return float(np.mean(values))


def selected_matrix(a: np.ndarray, choice: tuple[int, ...], signs: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    matrix = np.zeros((n, n), dtype=float)
    for j, k in enumerate(choice):
        matrix[j, k] += signs[j] * a[j, k]
    return matrix


def nuclear_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def main() -> None:
    rng = np.random.default_rng(150105213)
    worst_modified_ratio = 0.0
    worst_permutation_ratio = 0.0
    cases = 0

    for n in range(1, 6):
        for _ in range(40):
            # Mix ordinary and highly inhomogeneous weights.
            a = rng.normal(size=(n, n)) * np.exp(rng.normal(scale=1.2, size=(n, n)))
            lhs = lhs_formula(a)
            modified_rhs = modified_rhs_formula(a)
            permutation_rhs = permutation_rhs_formula(a)
            assert lhs <= math.e * modified_rhs + 1e-10
            assert lhs <= permutation_rhs + 1e-10
            worst_modified_ratio = max(worst_modified_ratio, lhs / modified_rhs)
            worst_permutation_ratio = max(worst_permutation_ratio, lhs / permutation_rhs)
            cases += 1

            if n <= 4:
                for _ in range(10):
                    choice = tuple(int(x) for x in rng.integers(0, n, size=n))
                    signs = rng.choice((-1.0, 1.0), size=n)
                    matrix = selected_matrix(a, choice, signs)
                    expected = sum(
                        np.linalg.norm([a[j, k] for j in range(n) if choice[j] == k])
                        for k in range(n)
                    )
                    assert abs(nuclear_norm(matrix) - expected) <= 1e-9 * (1.0 + expected)

    print(f"verified randomized arrays: {cases}")
    print(f"largest observed modified ratio: {worst_modified_ratio:.9f} < e")
    print(f"largest observed permutation ratio: {worst_permutation_ratio:.9f} <= 1")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Non-proof checks for the sharp Gaussian EOT asymptotic constant."""

from __future__ import annotations

import numpy as np


def sym_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2)
    if values.min() <= 0:
        raise ValueError("matrix is not positive definite")
    return (vectors * np.sqrt(values)) @ vectors.T


def matrix_shrinkage(z: np.ndarray, epsilon: float) -> np.ndarray:
    values, vectors = np.linalg.eigh((z + z.T) / 2)
    shrunk = 2 * values / (np.sqrt(4 * values**2 + epsilon**2) + epsilon)
    return (vectors * shrunk) @ vectors.T


def spd(rng: np.random.Generator, dimension: int) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension))
    return raw @ raw.T + 0.3 * np.eye(dimension)


def coefficient_and_ratio(
    a: np.ndarray, b: np.ndarray, epsilon: float
) -> tuple[float, float, float]:
    ah = sym_sqrt(a)
    z = sym_sqrt(ah @ b @ ah)
    y = z @ np.linalg.solve(a, z)
    s = a + y
    coefficient = float(np.trace(np.linalg.solve(s, z)))

    r = matrix_shrinkage(z, epsilon)
    q = a @ a + y @ y + a @ r @ y + y @ r @ a
    w2_squared = 2 * (np.trace(s) - np.trace(sym_sqrt(q)))
    ratio = float(w2_squared / epsilon)

    amgm = (a - z) @ np.linalg.solve(a, a - z)
    min_amgm_eigenvalue = float(np.linalg.eigvalsh((amgm + amgm.T) / 2).min())
    return coefficient, ratio, min_amgm_eigenvalue


def main() -> None:
    rng = np.random.default_rng(14)
    epsilons = (1e-3, 3e-4, 1e-4)
    max_final_error = 0.0
    tested = 0

    for dimension in (1, 2, 5, 10):
        for trial in range(5):
            a, b = spd(rng, dimension), spd(rng, dimension)
            ratios = []
            for epsilon in epsilons:
                coefficient, ratio, min_amgm = coefficient_and_ratio(a, b, epsilon)
                ratios.append(ratio)
                assert coefficient <= dimension / 2 + 2e-10
                assert min_amgm >= -2e-9
            final_error = abs(ratios[-1] - coefficient)
            max_final_error = max(max_final_error, final_error)
            assert final_error < 1e-3
            print(
                f"d={dimension:2d} trial={trial} coefficient={coefficient:.9f} "
                f"ratios={[round(value, 9) for value in ratios]}"
            )
            tested += 1

        a = spd(rng, dimension)
        coefficient, _, _ = coefficient_and_ratio(a, a, epsilons[-1])
        assert abs(coefficient - dimension / 2) < 2e-10

    print(f"PASS: {tested} random pairs; max final ratio error={max_final_error:.3e}")


if __name__ == "__main__":
    main()

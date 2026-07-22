#!/usr/bin/env python3
"""Finite-matrix sanity checks for the trace-tail proof.

This checks spectral truncation, the Markov trace bound, the L2 bound, and
right-multiplication contractivity. It is not a proof of the theorem.
"""

from __future__ import annotations

import numpy as np


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def l2_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, "fro"))


def polar_and_abs(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    u, singular, vh = np.linalg.svd(matrix, full_matrices=False)
    polar = u @ vh
    absolute = vh.conj().T @ np.diag(singular) @ vh
    return polar, absolute


def main() -> None:
    rng = np.random.default_rng(190108056)
    cases = 0
    max_error = 0.0

    for dimension in (2, 3, 5, 8):
        for _ in range(20):
            h = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
                size=(dimension, dimension)
            )
            perturbation = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
                size=(dimension, dimension)
            )
            polar, absolute = polar_and_abs(h)
            eigenvalues, eigenvectors = np.linalg.eigh(absolute)

            positive = eigenvalues[eigenvalues > 1e-12]
            levels = [0.2, 0.5, 0.8]
            if positive.size:
                levels = [float(np.quantile(positive, q)) for q in levels]

            for level in levels:
                high = eigenvalues > level
                projection = eigenvectors @ np.diag(high.astype(float)) @ eigenvectors.conj().T
                low_abs = eigenvectors @ np.diag(eigenvalues * (~high)) @ eigenvectors.conj().T
                truncation = polar @ low_abs
                tail = h @ projection

                err_identity = abs(trace_norm(h - truncation) - trace_norm(tail))
                err_markov = max(0.0, float(high.sum()) - trace_norm(h) / level)
                err_l2 = max(0.0, l2_norm(truncation) ** 2 - level * trace_norm(h))
                err_contract = max(
                    0.0,
                    trace_norm((h - perturbation) @ projection)
                    - trace_norm(h - perturbation),
                )

                max_error = max(
                    max_error, err_identity, err_markov, err_l2, err_contract
                )
                cases += 1

    tolerance = 2e-8
    if max_error > tolerance:
        raise AssertionError(f"maximum error {max_error:.3e} exceeds {tolerance:.1e}")
    print(f"PASS: {cases} matrix/truncation cases; max error {max_error:.3e}")


if __name__ == "__main__":
    main()

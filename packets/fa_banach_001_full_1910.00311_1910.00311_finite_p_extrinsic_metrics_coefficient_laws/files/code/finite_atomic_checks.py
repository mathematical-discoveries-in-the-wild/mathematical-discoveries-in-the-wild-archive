#!/usr/bin/env python3
"""Finite-atomic regression checks for the coefficient-law formulas.

This is evidence against transcription errors, not a proof.  For random
atomic laws at p=2 it compares moment norms with weighted embedding matrices
and compares the factorized rank-k operator with the weighted kernel matrix.
"""

from __future__ import annotations

import argparse

import numpy as np


def run_trial(rng: np.random.Generator, atoms: int, dim: int) -> float:
    weights = rng.random(atoms)
    weights /= weights.sum()
    root_w = np.sqrt(weights)

    a0 = rng.normal(size=(atoms, dim))
    a1 = rng.normal(size=(atoms, dim))
    b0 = rng.normal(size=(atoms, dim))
    b1 = rng.normal(size=(atoms, dim))

    # Weighted L2 coordinate matrices of the four evaluation maps.
    A0 = root_w[:, None] * a0
    A1 = root_w[:, None] * a1
    B0 = root_w[:, None] * b0
    B1 = root_w[:, None] * b1

    residuals: list[float] = []
    for _ in range(8):
        x = rng.normal(size=dim)
        direct = np.sum(weights * (a0 @ x) ** 2)
        embedded = np.linalg.norm(A0 @ x) ** 2
        residuals.append(abs(direct - embedded))

        y = rng.normal(size=dim)
        pair_direct = np.sum(weights * ((a0 @ x) - (b0 @ y)) ** 2)
        pair_embedded = np.linalg.norm((A0 @ x) - (B0 @ y)) ** 2
        residuals.append(abs(pair_direct - pair_embedded))

    # In standard Euclidean coordinates for weighted L2(mu), the kernel
    # operator is diag(sqrt(w)) K diag(sqrt(w)).
    raw_kernel = a0 @ a1.T - b0 @ b1.T
    weighted_kernel = root_w[:, None] * raw_kernel * root_w[None, :]
    factorized = A0 @ A1.T - B0 @ B1.T
    residuals.append(np.linalg.norm(weighted_kernel - factorized, ord=2))
    residuals.append(
        abs(
            np.linalg.norm(weighted_kernel, ord=2)
            - np.linalg.norm(factorized, ord=2)
        )
    )
    return max(residuals)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=191000311)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    worst = 0.0
    for _ in range(args.trials):
        atoms = int(rng.integers(4, 13))
        dim = int(rng.integers(1, min(5, atoms) + 1))
        worst = max(worst, run_trial(rng, atoms, dim))

    tolerance = 1e-10
    if worst > tolerance:
        raise SystemExit(f"FAILED: maximum residual {worst:.3e}")
    print(f"PASS: {args.trials} trials; maximum residual {worst:.3e}")


if __name__ == "__main__":
    main()

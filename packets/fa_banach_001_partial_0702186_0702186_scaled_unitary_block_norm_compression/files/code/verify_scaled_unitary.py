#!/usr/bin/env python3
"""Numerically verify the scaled-unitary norm-compression reduction.

This is a regression check, not a proof.  It compares direct Schatten norms
against the two-by-two spectral formula and checks the conjectured inequality
direction on seeded random complex instances.
"""

from __future__ import annotations

import argparse

import numpy as np


P_VALUES = np.array([1.0, 1.2, 1.5, 1.9, 2.0, 2.2, 2.8, 3.5, 5.0, 8.0])


def haar_unitary(rng: np.random.Generator, d: int) -> np.ndarray:
    raw = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(raw)
    diagonal = np.diag(r)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return q * phases.conj()


def schatten_power(matrix: np.ndarray, p: float) -> float:
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False) ** p))


def f_value(alpha: float, beta: float, s: np.ndarray, q: float) -> np.ndarray:
    delta = np.sqrt((alpha - beta) ** 2 + 4.0 * s**2)
    plus = np.maximum(0.0, (alpha + beta + delta) / 2.0)
    minus = np.maximum(0.0, (alpha + beta - delta) / 2.0)
    return plus**q + minus**q


def run(trials: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    max_full_formula_error = 0.0
    max_compression_formula_error = 0.0
    max_direction_violation = 0.0
    min_slack = np.inf

    for _ in range(trials):
        d = int(rng.integers(1, 7))
        n = int(rng.integers(2, 8))
        p = float(rng.choice(P_VALUES))
        q = p / 2.0

        # The lognormal scale exercises both near-zero and unbalanced blocks.
        a = rng.lognormal(mean=0.0, sigma=0.9, size=n)
        b = rng.lognormal(mean=0.0, sigma=0.9, size=n)
        u = [haar_unitary(rng, d) for _ in range(n)]
        v = [haar_unitary(rng, d) for _ in range(n)]

        top = np.hstack([a[i] * u[i] for i in range(n)])
        bottom = np.hstack([b[i] * v[i] for i in range(n)])
        t_matrix = np.vstack([top, bottom])

        scale = d ** (1.0 / p)
        compression = scale * np.vstack([a, b])
        direct_full = schatten_power(t_matrix, p)
        direct_compression = schatten_power(compression, p)

        alpha = float(a @ a)
        beta = float(b @ b)
        c = float(a @ b)
        z = sum(a[i] * b[i] * (u[i] @ v[i].conj().T) for i in range(n))
        s = np.linalg.svd(z, compute_uv=False)
        formula_full = float(np.sum(f_value(alpha, beta, s, q)))
        formula_compression = float(d * f_value(alpha, beta, np.array(c), q))

        full_scale = max(1.0, direct_full, formula_full)
        comp_scale = max(1.0, direct_compression, formula_compression)
        max_full_formula_error = max(
            max_full_formula_error, abs(direct_full - formula_full) / full_scale
        )
        max_compression_formula_error = max(
            max_compression_formula_error,
            abs(direct_compression - formula_compression) / comp_scale,
        )

        relation_scale = max(1.0, direct_full, direct_compression)
        if p < 2.0:
            slack = (direct_full - direct_compression) / relation_scale
        elif p > 2.0:
            slack = (direct_compression - direct_full) / relation_scale
        else:
            slack = -abs(direct_full - direct_compression) / relation_scale
        min_slack = min(min_slack, slack)
        max_direction_violation = max(max_direction_violation, max(0.0, -slack))

    tolerance = 2.0e-10
    print(f"seed={seed}")
    print(f"trials={trials}")
    print(f"max_relative_full_formula_error={max_full_formula_error:.3e}")
    print(
        "max_relative_compression_formula_error="
        f"{max_compression_formula_error:.3e}"
    )
    print(f"max_relative_direction_violation={max_direction_violation:.3e}")
    print(f"minimum_normalized_slack={min_slack:.3e}")

    if max_full_formula_error > tolerance:
        raise SystemExit("full spectral formula exceeded tolerance")
    if max_compression_formula_error > tolerance:
        raise SystemExit("compression formula exceeded tolerance")
    if max_direction_violation > tolerance:
        raise SystemExit("norm-compression direction exceeded tolerance")
    print("PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260719)
    args = parser.parse_args()
    run(args.trials, args.seed)


if __name__ == "__main__":
    main()

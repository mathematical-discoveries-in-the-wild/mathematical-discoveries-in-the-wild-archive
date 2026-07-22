#!/usr/bin/env python3
"""Numerical checks for the one-factor Wishart minor mixture.

The proof is analytic. These checks compare direct real-degree Wishart
samples with the scalar-mixture determinant representation and test the two
claimed inequalities.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.linalg import block_diag
from scipy.stats import ncx2, wishart


SEED = 231100202
CASES = 12
SAMPLES = 60_000


def sem(x: np.ndarray) -> float:
    return float(np.std(x, ddof=1) / math.sqrt(x.size))


def block_determinants(samples: np.ndarray, sizes: list[int]) -> np.ndarray:
    out = np.empty((samples.shape[0], len(sizes)))
    start = 0
    for j, size in enumerate(sizes):
        stop = start + size
        out[:, j] = np.linalg.det(samples[:, start:stop, start:stop])
        start = stop
    return out


def mixture_determinants(
    rng: np.random.Generator,
    alpha: float,
    blocks: list[np.ndarray],
    loadings: list[np.ndarray],
    samples: int,
) -> np.ndarray:
    common = rng.chisquare(alpha, size=samples)
    out = np.empty((samples, len(blocks)))
    for i, (residual, loading) in enumerate(zip(blocks, loadings)):
        strength = float(loading @ np.linalg.solve(residual, loading))
        value = np.linalg.det(residual) * ncx2.rvs(
            alpha,
            common * strength,
            size=samples,
            random_state=rng,
        )
        for j in range(1, residual.shape[0]):
            value *= rng.chisquare(alpha - j, size=samples)
        out[:, i] = value
    return out


def main() -> None:
    rng = np.random.default_rng(SEED)
    max_moment_z = 0.0
    max_event_z = 0.0
    min_moment_gap_z = float("inf")
    min_event_gap_z = float("inf")

    for case in range(CASES):
        d = int(rng.integers(3, 5))
        sizes = [int(x) for x in rng.integers(1, 3, size=d)]
        p = sum(sizes)
        alpha = p - 1 + rng.uniform(1.1, 4.8)

        blocks: list[np.ndarray] = []
        loadings: list[np.ndarray] = []
        for size in sizes:
            raw = rng.normal(size=(size, size))
            residual = raw @ raw.T / size + np.eye(size) * 0.7
            blocks.append(residual)
            loadings.append(rng.normal(scale=0.75, size=size))

        residual_full = block_diag(*blocks)
        loading_full = np.concatenate(loadings)
        sigma = residual_full + np.outer(loading_full, loading_full)

        direct_matrix = wishart.rvs(
            df=alpha,
            scale=sigma,
            size=SAMPLES,
            random_state=rng,
        )
        direct = block_determinants(direct_matrix, sizes)
        mixture = mixture_determinants(
            rng, alpha, blocks, loadings, SAMPLES
        )

        powers = rng.uniform(0.15, 0.8, size=d)
        normalizer = np.median(direct, axis=0)
        direct_stat = np.prod((direct / normalizer) ** powers, axis=1)
        mixture_stat = np.prod((mixture / normalizer) ** powers, axis=1)
        moment_z = abs(float(np.mean(direct_stat) - np.mean(mixture_stat))) / math.sqrt(
            sem(direct_stat) ** 2 + sem(mixture_stat) ** 2
        )
        max_moment_z = max(max_moment_z, moment_z)

        thresholds = np.quantile(direct, 0.55, axis=0)
        direct_event = np.all(direct <= thresholds, axis=1).astype(float)
        mixture_event = np.all(mixture <= thresholds, axis=1).astype(float)
        event_z = abs(float(np.mean(direct_event) - np.mean(mixture_event))) / math.sqrt(
            sem(direct_event) ** 2 + sem(mixture_event) ** 2
        )
        max_event_z = max(max_event_z, event_z)

        powered = (direct / normalizer) ** powers
        joint = np.prod(powered, axis=1)
        product_of_means = float(np.prod(np.mean(powered, axis=0)))
        gap = joint - product_of_means
        min_moment_gap_z = min(min_moment_gap_z, float(np.mean(gap)) / sem(gap))

        split = d // 2
        left = np.all(direct[:, :split] <= thresholds[:split], axis=1).astype(float)
        right = np.all(direct[:, split:] <= thresholds[split:], axis=1).astype(float)
        event_gap = left * right - float(np.mean(left) * np.mean(right))
        min_event_gap_z = min(min_event_gap_z, float(np.mean(event_gap)) / sem(event_gap))

        print(
            f"case={case + 1:02d} p={p} d={d} alpha={alpha:.3f} "
            f"mixture_moment_z={moment_z:.2f} mixture_event_z={event_z:.2f}"
        )

    print(f"max mixture moment discrepancy z: {max_moment_z:.3f}")
    print(f"max mixture event discrepancy z:  {max_event_z:.3f}")
    print(f"min moment-inequality gap z:       {min_moment_gap_z:.3f}")
    print(f"min threshold-inequality gap z:    {min_event_gap_z:.3f}")
    if max_moment_z > 4.5 or max_event_z > 4.5:
        raise SystemExit("mixture comparison exceeded the 4.5-sigma audit bound")
    if min_moment_gap_z < -4.5 or min_event_gap_z < -4.5:
        raise SystemExit("an inequality failed beyond the 4.5-sigma audit bound")


if __name__ == "__main__":
    main()


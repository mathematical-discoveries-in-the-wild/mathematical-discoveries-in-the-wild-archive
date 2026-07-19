#!/usr/bin/env python3
"""Numerical sanity checks for the wedge-energy partial results.

This is not used as proof.  It verifies the closed formulas on orthonormal
systems, regular simplices, and the cyclic (N,m)=(5,3) family, and it checks
random configurations against the proved ETF lower bound.
"""

from __future__ import annotations

import math

import numpy as np


def wedge_energy(z: np.ndarray) -> float:
    gram = np.clip(z @ z.T, -1.0, 1.0)
    # Every input row is a unit vector; impose the exact diagonal to avoid the
    # square-root sensitivity of arcsin near 1 in floating-point arithmetic.
    np.fill_diagonal(gram, 1.0)
    return float(np.square(np.arcsin(gram)).sum() / math.pi**2)


def lower_bound(ambient_dim: int, n_vectors: int) -> float:
    if n_vectors <= ambient_dim:
        return n_vectors / 4.0
    coherence_sq = (n_vectors - ambient_dim) / (
        ambient_dim * (n_vectors - 1)
    )
    return n_vectors / 4.0 + (
        n_vectors
        * (n_vectors - 1)
        / math.pi**2
        * math.asin(math.sqrt(coherence_sq)) ** 2
    )


def regular_simplex(ambient_dim: int) -> np.ndarray:
    n_vectors = ambient_dim + 1
    gram = (
        (n_vectors / ambient_dim) * np.eye(n_vectors)
        - np.ones((n_vectors, n_vectors)) / ambient_dim
    )
    values, vectors = np.linalg.eigh(gram)
    positive = values > 1e-10
    return (np.sqrt(values[positive])[:, None] * vectors[:, positive].T).T


def random_unit_vectors(
    rng: np.random.Generator, n_vectors: int, ambient_dim: int
) -> np.ndarray:
    z = rng.standard_normal((n_vectors, ambient_dim))
    return z / np.linalg.norm(z, axis=1, keepdims=True)


def cyclic_five_frame(q: float) -> np.ndarray:
    k = np.arange(5)
    theta = 2 * math.pi * k / 5
    return np.column_stack(
        [
            math.sqrt(1 - q) * np.cos(theta),
            math.sqrt(1 - q) * np.sin(theta),
            np.full(5, math.sqrt(q)),
        ]
    )


def cyclic_derivative(q: float) -> float:
    root_five = math.sqrt(5)
    c = (root_five - 1) / 4
    capital_c = -(root_five + 1) / 4
    a = q + (1 - q) * c
    b = -q - (1 - q) * capital_c

    def ratio(x: float) -> float:
        return math.asin(x) / math.sqrt(1 - x * x)

    return 20 / math.pi**2 * (
        (1 - c) * ratio(a) - (1 - capital_c) * ratio(b)
    )


def cyclic_optimum() -> float:
    left, right = 0.0, 1 / 3
    assert cyclic_derivative(left) < 0 < cyclic_derivative(right)
    for _ in range(100):
        middle = (left + right) / 2
        if cyclic_derivative(middle) < 0:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def main() -> None:
    rng = np.random.default_rng(20260719)

    orthonormal = np.eye(4)[:3]
    orth_value = wedge_energy(orthonormal)
    assert abs(orth_value - lower_bound(4, 3)) < 1e-12
    print(f"orthonormal m=4 N=3: energy={orth_value:.12f}")

    for ambient_dim in (2, 3, 4):
        simplex = regular_simplex(ambient_dim)
        n_vectors = ambient_dim + 1
        value = wedge_energy(simplex)
        bound = lower_bound(ambient_dim, n_vectors)
        assert np.max(np.abs(np.linalg.norm(simplex, axis=1) - 1.0)) < 1e-12
        assert abs(value - bound) < 1e-11

        random_min = math.inf
        for _ in range(20_000):
            sample = random_unit_vectors(rng, n_vectors, ambient_dim)
            sample_value = wedge_energy(sample)
            assert sample_value >= bound - 1e-11
            random_min = min(random_min, sample_value)

        print(
            f"simplex m={ambient_dim} N={n_vectors}: "
            f"energy=bound={value:.12f}; random_min={random_min:.12f}"
        )

    tight_q = 1 / 3
    tight_frame = cyclic_five_frame(tight_q)
    tight_energy = wedge_energy(tight_frame)
    expected_tight = 5 / 4 + 10 / math.pi**2 * (
        math.asin((1 + math.sqrt(5)) / 6) ** 2
        + math.asin((math.sqrt(5) - 1) / 6) ** 2
    )
    frame_operator = tight_frame.T @ tight_frame
    assert np.max(np.abs(frame_operator - (5 / 3) * np.eye(3))) < 1e-12
    assert abs(tight_energy - expected_tight) < 1e-12
    assert cyclic_derivative(tight_q) > 0.16

    optimum_q = cyclic_optimum()
    optimum_energy = wedge_energy(cyclic_five_frame(optimum_q))
    assert abs(optimum_q - 0.31480032734257923) < 1e-12
    assert abs(optimum_energy - 1.6208431595684651) < 1e-12
    assert optimum_energy < tight_energy
    print(
        "cyclic N=5 m=3: "
        f"tight_energy={tight_energy:.12f}; "
        f"derivative_at_tight={cyclic_derivative(tight_q):.12f}; "
        f"q_star={optimum_q:.12f}; energy={optimum_energy:.12f}"
    )


if __name__ == "__main__":
    main()

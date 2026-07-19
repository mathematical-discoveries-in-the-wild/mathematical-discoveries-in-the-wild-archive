#!/usr/bin/env python3
"""Finite sanity checks for the all-p Schatten-distortion packet.

This checks exact scalar inequalities and small matrix-valued instances of
the endpoint and high-p mechanisms. It is not a proof of the theorem.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2e-9


def schatten_norm(a: np.ndarray, p: float) -> float:
    return float(np.sum(np.linalg.svd(a, compute_uv=False) ** p) ** (1.0 / p))


def mazur_p_to_2(a: np.ndarray, p: float) -> np.ndarray:
    """Return u|a|^(p/2), evaluated from an SVD a=U diag(s) V*."""
    u, singular, vh = np.linalg.svd(a, full_matrices=False)
    return (u * singular ** (p / 2.0)) @ vh


def cycle_transition(n: int) -> np.ndarray:
    pmat = np.zeros((n, n))
    for i in range(n):
        pmat[i, (i - 1) % n] += 0.5
        pmat[i, (i + 1) % n] += 0.5
    return pmat


def complete_transition(n: int) -> np.ndarray:
    return (np.ones((n, n)) - np.eye(n)) / (n - 1)


def spectral_gap(pmat: np.ndarray) -> float:
    vals = np.linalg.eigvalsh(pmat)
    return float(1.0 - vals[-2])


def transition_energy(pmat: np.ndarray, values: np.ndarray, p: float) -> float:
    n = len(values)
    return sum(
        pmat[i, j] * schatten_norm(values[i] - values[j], p) ** p
        for i in range(n)
        for j in range(n)
    ) / n


def pair_energy(values: np.ndarray, p: float) -> float:
    n = len(values)
    return sum(
        schatten_norm(values[i] - values[j], p) ** p
        for i in range(n)
        for j in range(n)
    ) / (n * n)


def selected_k(p: float, delta: float) -> int:
    alpha = 1.0 - delta / 2.0
    if alpha <= 0:
        return 1
    return max(1, math.ceil((p - 1.0) * math.log(2.0) / (-math.log(alpha))))


def interpolation_bound(p: float, delta: float, k: int) -> float:
    alpha = max(0.0, 1.0 - delta / 2.0)
    return 2.0 ** (1.0 - 2.0 / p) * alpha ** (2.0 * k / p)


def check_weighted_lemma(values: np.ndarray, p: float) -> None:
    n = len(values)
    distances = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            distances[i, j] = schatten_norm(values[i] - values[j], p)
    b = float(np.mean(distances**p))
    origins = np.mean(distances**p, axis=0)
    origin = int(np.argmin(origins))
    assert origins[origin] <= b * (1.0 + TOL)

    q = 2.0 - p
    radii = distances[:, origin]
    weighted = 0.0
    for i in range(n):
        for j in range(n):
            denominator = radii[i] ** q + radii[j] ** q
            if denominator > 0:
                weighted += distances[i, j] ** 2 / denominator
            else:
                assert distances[i, j] <= TOL
    weighted /= n * n
    assert weighted + TOL >= b / 2.0, (p, weighted, b / 2.0)


def check_mazur_and_hilbert(
    pmat: np.ndarray, values: np.ndarray, p: float
) -> tuple[float, float]:
    n = len(values)
    distances = np.array(
        [
            [schatten_norm(values[i] - values[j], p) for j in range(n)]
            for i in range(n)
        ]
    )
    origin = int(np.argmin(np.mean(distances**p, axis=0)))
    translated = values - values[origin]
    transformed = np.array([mazur_p_to_2(a, p) for a in translated])

    pair_h = pair_energy(transformed, 2.0)
    edge_h = transition_energy(pmat, transformed, 2.0)
    delta = spectral_gap(pmat)
    assert pair_h <= edge_h / delta * (1.0 + TOL)

    forward_ratios = []
    inverse_ratios = []
    for i in range(n):
        for j in range(n):
            d = distances[i, j]
            h = schatten_norm(transformed[i] - transformed[j], 2.0)
            if d > TOL:
                forward_ratios.append(h / d ** (p / 2.0))
            radius = max(
                schatten_norm(translated[i], p), schatten_norm(translated[j], p)
            )
            denominator = radius ** (1.0 - p / 2.0) * h
            if d > TOL:
                assert denominator > 0
                inverse_ratios.append(d / denominator)
    assert np.isfinite(forward_ratios).all()
    assert np.isfinite(inverse_ratios).all()
    return max(forward_ratios, default=0.0), max(inverse_ratios, default=0.0)


def run() -> None:
    for p in [2.0, 2.5, 4.0, 8.0, 32.0]:
        for delta in [0.01, 0.05, 0.2, 0.7, 1.0, 1.8, 2.0]:
            k = selected_k(p, delta)
            bound = interpolation_bound(p, delta, k)
            assert bound <= 0.5 * (1.0 + 1e-12), (p, delta, k, bound)
            assert k <= (2.0 + 2.0 * math.log(2.0)) * p / delta + 1e-12

    rng = np.random.default_rng(240503517)
    max_forward = 0.0
    max_inverse = 0.0
    for pmat in [cycle_transition(7), complete_transition(7)]:
        delta = spectral_gap(pmat)
        values = rng.normal(size=(len(pmat), 3, 3)) + 1j * rng.normal(
            size=(len(pmat), 3, 3)
        )

        for p in [1.0, 1.1, 1.35, 1.7, 1.95]:
            check_weighted_lemma(values, p)
            forward, inverse = check_mazur_and_hilbert(pmat, values, p)
            max_forward = max(max_forward, forward)
            max_inverse = max(max_inverse, inverse)

        qmat = (np.eye(len(pmat)) + pmat) / 2.0
        for p in [2.0, 3.0, 6.0]:
            k = selected_k(p, delta)
            ek = transition_energy(np.linalg.matrix_power(qmat, k), values, p)
            e1 = transition_energy(pmat, values, p)
            epair = pair_energy(values, p)
            assert ek <= (k**p) * 0.5 * e1 * (1.0 + TOL)
            assert epair ** (1.0 / p) <= 4.0 * ek ** (1.0 / p) * (1.0 + TOL)
            assert epair ** (1.0 / p) <= 4.0 * k * e1 ** (1.0 / p) * (
                1.0 + TOL
            )

    print("PASS: weighted endpoint, Mazur, Hilbert, and high-p sanity checks")
    print(f"observed Mazur ratios: forward={max_forward:.6f}, inverse={max_inverse:.6f}")


if __name__ == "__main__":
    run()

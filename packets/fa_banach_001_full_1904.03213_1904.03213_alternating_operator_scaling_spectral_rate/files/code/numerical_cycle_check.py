#!/usr/bin/env python3
"""Sanity check for the alternating-normalization contraction mechanism.

This is not used in the proof.  It builds a random exactly balanced quantum
expander, applies small two-sided positive perturbations, and records the
marginal error and spectral gap during exact left/right normalization cycles.
"""

from __future__ import annotations

import numpy as np


def invsqrt(a: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((a + a.T) / 2)
    return (vectors * values ** -0.5) @ vectors.T


def exp_symmetric(a: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((a + a.T) / 2)
    return (vectors * np.exp(values)) @ vectors.T


def random_orthogonal(rng: np.random.Generator, n: int) -> np.ndarray:
    q, r = np.linalg.qr(rng.normal(size=(n, n)))
    signs = np.sign(np.diag(r))
    signs[signs == 0] = 1
    return q * signs


def marginals(ops: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, float]:
    left = sum(a @ a.T for a in ops)
    right = sum(a.T @ a for a in ops)
    size = float(np.trace(left))
    return left, right, size


def normalized_error(ops: list[np.ndarray]) -> float:
    left, right, size = marginals(ops)
    n = left.shape[0]
    eye = np.eye(n)
    return max(
        np.linalg.norm(n * left / size - eye, 2),
        np.linalg.norm(n * right / size - eye, 2),
    )


def spectral_gap(ops: list[np.ndarray]) -> float:
    _, _, size = marginals(ops)
    n = ops[0].shape[0]
    matrix = sum(np.kron(a, a) for a in ops)
    singular = np.linalg.svd(matrix, compute_uv=False)
    return float(1 - singular[1] / (size / n))


def right_balance(ops: list[np.ndarray]) -> list[np.ndarray]:
    _, right, _ = marginals(ops)
    r = invsqrt(right)
    return [a @ r for a in ops]


def full_cycle(ops: list[np.ndarray]) -> list[np.ndarray]:
    left, _, _ = marginals(ops)
    ell = invsqrt(left)
    half = [ell @ a for a in ops]
    return right_balance(half)


def main() -> None:
    rng = np.random.default_rng(190403213)
    n, k = 5, 14
    base = [random_orthogonal(rng, n) / np.sqrt(k) for _ in range(k)]

    h = rng.normal(size=(n, n))
    h = (h + h.T) / 2
    h -= np.trace(h) * np.eye(n) / n
    h /= np.linalg.norm(h, 2)
    g = rng.normal(size=(n, n))
    g = (g + g.T) / 2
    g -= np.trace(g) * np.eye(n) / n
    g /= np.linalg.norm(g, 2)
    perturbation = 0.035
    left_scale = exp_symmetric(perturbation * h)
    right_scale = exp_symmetric(perturbation * g)
    ops = right_balance([left_scale @ a @ right_scale for a in base])

    errors: list[float] = []
    gaps: list[float] = []
    for _ in range(24):
        errors.append(normalized_error(ops))
        gaps.append(spectral_gap(ops))
        ops = full_cycle(ops)

    usable = [errors[i + 1] / errors[i] for i in range(len(errors) - 1) if errors[i] > 1e-12]
    print(f"initial marginal error: {errors[0]:.6e}")
    print(f"final marginal error:   {errors[-1]:.6e}")
    print(f"initial spectral gap:   {gaps[0]:.6f}")
    print(f"minimum spectral gap:   {min(gaps):.6f}")
    print(f"maximum cycle ratio:    {max(usable):.6f}")
    print(f"median cycle ratio:     {np.median(usable):.6f}")


if __name__ == "__main__":
    main()

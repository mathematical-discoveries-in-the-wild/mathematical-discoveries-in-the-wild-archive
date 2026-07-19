"""Numerical sanity checks for the two finite-dimensional linear-algebra steps.

This is evidence against transcription mistakes, not part of the proof.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import expm


def random_symplectic(n: int, rng: np.random.Generator) -> np.ndarray:
    identity = np.eye(n)
    symplectic_form = np.block(
        [[np.zeros((n, n)), identity], [-identity, np.zeros((n, n))]]
    )
    raw = rng.standard_normal((2 * n, 2 * n))
    hessian = (raw + raw.T) / 2
    return expm(symplectic_form @ hessian)


def check_gaussian_orbit_matrix(trials: int = 250) -> float:
    rng = np.random.default_rng(20260719)
    smallest = np.inf
    for _ in range(trials):
        n = int(rng.integers(1, 7))
        symplectic = random_symplectic(n, rng)
        p = symplectic[:n, :n]
        r = symplectic[n:, :n]

        raw_x = rng.standard_normal((n, n))
        x = raw_x.T @ raw_x + 0.25 * np.eye(n)
        raw_y = rng.standard_normal((n, n))
        y = (raw_y + raw_y.T) / 2
        z = x + 1j * y

        singular_values = np.linalg.svd(z @ p + 1j * r, compute_uv=False)
        smallest = min(smallest, float(singular_values[-1]))
        if singular_values[-1] < 1e-10:
            raise AssertionError("unexpected nearly singular ZP+iR")
    return smallest


def check_log_recovery(order: int = 60) -> float:
    rng = np.random.default_rng(314159)
    n = 4
    while True:
        c = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        if abs(np.linalg.det(c)) > 0.2:
            break

    samples = rng.uniform(-1, 1, size=(4000, n))
    linear_forms = samples @ c
    epsilon = 0.15 / max(1.0, float(np.max(np.abs(linear_forms))))
    w = np.exp(epsilon * linear_forms)
    u = w - 1

    log_series = np.zeros_like(w)
    power = np.ones_like(w)
    for degree in range(1, order + 1):
        power *= u
        log_series += ((-1) ** (degree + 1)) * power / degree

    recovered_linear_forms = log_series / epsilon
    recovered_samples = recovered_linear_forms @ np.linalg.inv(c)
    return float(np.max(np.abs(recovered_samples - samples)))


if __name__ == "__main__":
    min_singular_value = check_gaussian_orbit_matrix()
    max_coordinate_error = check_log_recovery()
    print(f"minimum sampled singular value: {min_singular_value:.6e}")
    print(f"maximum logarithm-recovery error: {max_coordinate_error:.6e}")

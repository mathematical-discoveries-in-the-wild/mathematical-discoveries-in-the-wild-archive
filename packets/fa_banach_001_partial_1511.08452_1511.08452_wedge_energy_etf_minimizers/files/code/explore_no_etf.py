#!/usr/bin/env python3
"""Seeded numerical exploration of the first non-ETF case (N,m)=(5,3).

This is not proof.  It runs 250 unconstrained local optimizations and reports
the correlation distribution and frame-operator spectrum of the best points.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def normalized_rows(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rows = x.reshape(5, 3)
    norms = np.linalg.norm(rows, axis=1)
    return rows / norms[:, None], norms


def energy_and_gradient(x: np.ndarray) -> tuple[float, np.ndarray]:
    z, norms = normalized_rows(x)
    gram = z @ z.T
    energy = 5 / 4
    grad_z = np.zeros_like(z)
    for i in range(5):
        for j in range(i + 1, 5):
            t = float(np.clip(gram[i, j], -1 + 1e-13, 1 - 1e-13))
            angle = np.arcsin(t)
            energy += 2 * angle * angle / np.pi**2
            derivative = 4 * angle / (np.pi**2 * np.sqrt(1 - t * t))
            grad_z[i] += derivative * z[j]
            grad_z[j] += derivative * z[i]

    grad_x = np.empty_like(z)
    for i in range(5):
        tangent = grad_z[i] - np.dot(grad_z[i], z[i]) * z[i]
        grad_x[i] = tangent / norms[i]
    return energy, grad_x.ravel()


def report(label: str, z: np.ndarray) -> None:
    z = z / np.linalg.norm(z, axis=1)[:, None]
    gram = z @ z.T
    correlations = np.sort(np.abs(gram[np.triu_indices(5, 1)]))
    frame_eigenvalues = np.linalg.eigvalsh(z.T @ z)
    value, gradient = energy_and_gradient(z.ravel())
    print(f"{label}: energy={value:.15f}, tangent_grad={np.linalg.norm(gradient):.3e}")
    print("  correlations", np.array2string(correlations, precision=12))
    print("  frame eigenvalues", np.array2string(frame_eigenvalues, precision=12))


def main() -> None:
    rng = np.random.default_rng(151108452)
    optima: list[tuple[float, np.ndarray]] = []
    for _ in range(250):
        x0 = rng.normal(size=(5, 3))
        result = minimize(
            energy_and_gradient,
            x0.ravel(),
            jac=True,
            method="L-BFGS-B",
            options={"maxiter": 5000, "ftol": 1e-14, "gtol": 1e-10, "maxls": 50},
        )
        z, _ = normalized_rows(result.x)
        optima.append((result.fun, z))

    optima.sort(key=lambda item: item[0])
    values = np.array([item[0] for item in optima])
    print("energy quantiles", np.quantile(values, [0, 0.1, 0.5, 0.9, 1]))
    for rank, (_, z) in enumerate(optima[:5], start=1):
        report(f"optimum {rank}", z)


if __name__ == "__main__":
    main()

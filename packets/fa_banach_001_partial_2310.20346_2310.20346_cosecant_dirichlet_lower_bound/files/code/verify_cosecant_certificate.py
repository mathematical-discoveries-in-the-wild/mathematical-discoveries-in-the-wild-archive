#!/usr/bin/env python3
"""Numerically audit the finite cosecant/Hankel certificate."""

from __future__ import annotations

import numpy as np


def cosecant_matrix(n: int) -> np.ndarray:
    r = np.arange(n)[:, None]
    s = np.arange(n)[None, :]
    return 1.0 / (n * np.sin(np.pi * (r + s + 0.5) / n))


def certificate_coefficients(n: int) -> np.ndarray:
    k = np.arange(n)
    return 1.0 / (n * np.sin(np.pi * (k + 0.5) / n))


def max_hankel_block_norm(a: np.ndarray) -> float:
    m = len(a) - 1
    values = []
    for degree in range(m + 1):
        block = np.fromfunction(
            lambda i, j: a[(i + j).astype(int)],
            (m - degree + 1, degree + 1),
            dtype=int,
        )
        values.append(np.linalg.svd(block, compute_uv=False)[0])
    return float(max(values))


def dirichlet_h1(n: int, samples: int = 1 << 21) -> float:
    # Midpoint sampling avoids evaluating the removable singularity directly.
    theta = 2 * np.pi * (np.arange(samples) + 0.5) / samples
    values = np.sin(n * theta / 2) / np.sin(theta / 2)
    return float(np.mean(np.abs(values)))


def main() -> None:
    print("N orthogonality_defect max_block_norm certificate H1 ratio")
    for n in (3, 4, 10, 25, 50, 100):
        cmat = cosecant_matrix(n)
        defect = np.linalg.norm(cmat @ cmat.T - np.eye(n), ord=2)
        a = certificate_coefficients(n)
        block_norm = max_hankel_block_norm(a)
        certificate = float(np.sum(a))
        h1 = dirichlet_h1(n)
        print(
            n,
            f"{defect:.3e}",
            f"{block_norm:.12f}",
            f"{certificate:.12f}",
            f"{h1:.12f}",
            f"{certificate / h1:.12f}",
        )
    print("target_pi_over_2", f"{np.pi / 2:.12f}")


if __name__ == "__main__":
    main()


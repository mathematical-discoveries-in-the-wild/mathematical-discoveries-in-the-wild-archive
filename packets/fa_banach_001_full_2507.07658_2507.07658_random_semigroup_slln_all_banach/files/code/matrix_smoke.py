"""Finite-dimensional smoke check for the random-semigroup SLLN packet.

This is not a proof.  It samples bounded i.i.d. 2x2 generators and checks that
the product exp(A_1 t/n)...exp(A_n t/n) approaches exp(E[A] t) on a small
time grid.
"""

from __future__ import annotations

import math
import random

import numpy as np


def expm_2x2(a: np.ndarray) -> np.ndarray:
    """Small self-contained matrix exponential via eigendecomposition."""
    vals, vecs = np.linalg.eig(a)
    return (vecs @ np.diag(np.exp(vals)) @ np.linalg.inv(vecs)).real


def main() -> None:
    random.seed(1729)
    np.random.seed(1729)

    choices = [
        np.array([[0.0, 0.8], [-0.2, 0.1]]),
        np.array([[0.1, -0.4], [0.3, -0.2]]),
        np.array([[-0.3, 0.2], [0.5, 0.0]]),
    ]
    mean = sum(choices) / len(choices)
    x = np.array([1.0, -0.5])
    grid = np.linspace(0.0, 2.0, 41)

    for n in [50, 100, 200, 400, 800]:
        sample = [choices[random.randrange(len(choices))] for _ in range(n)]
        worst = 0.0
        for t in grid:
            h = t / n
            prod = np.eye(2)
            for a in reversed(sample):
                # reversed application gives exp(A_1 h)...exp(A_n h) x
                prod = expm_2x2(a * h) @ prod
            target = expm_2x2(mean * t)
            worst = max(worst, float(np.linalg.norm((prod - target) @ x)))
        print(f"n={n:4d} grid_sup_error={worst:.6f}")


if __name__ == "__main__":
    main()

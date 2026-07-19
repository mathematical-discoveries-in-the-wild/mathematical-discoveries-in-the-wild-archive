"""Numerical sanity checks for the 2410.15118 Schatten conjecture packet.

This script is not part of the proof. It samples real two-row matrices B and
compares the Schatten r norm with an angular-grid estimate of the exact
rank-two reduction of ||B: ell_2 -> ell_p||.

Run from the repository root with:
    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/full/2410.15118_schatten_interpolation_conjecture/code/finite_probe.py
"""

from __future__ import annotations

import numpy as np


def op_norm_two_rows(B: np.ndarray, p: float, grid: int = 200_000) -> float:
    """Estimate ||B: ell_2 -> ell_p|| for a two-row matrix.

    A two-row matrix has rank at most two. After singular value decomposition,
    the domain unit sphere can be reduced to the unit circle in the two
    singular directions.
    """
    U, s, _ = np.linalg.svd(B, full_matrices=False)
    C = U[:, : len(s)] @ np.diag(s)
    theta = np.linspace(0.0, 2.0 * np.pi, grid, endpoint=False)
    X = np.stack([np.cos(theta), np.sin(theta)], axis=0)
    Y = C @ X
    return float(np.max(np.sum(np.abs(Y) ** p, axis=0) ** (1.0 / p)))


def main() -> None:
    rng = np.random.default_rng(20260629)
    for p in (1.1, 1.25, 1.5, 1.75, 1.9):
        r = 2 * p / (2 - p)
        worst = 0.0
        for m in (2, 3, 5, 8, 13):
            for _ in range(100):
                B = rng.normal(size=(2, m))
                singular_values = np.linalg.svd(B, compute_uv=False)
                schatten = float(np.sum(singular_values**r) ** (1.0 / r))
                op_norm = op_norm_two_rows(B, p)
                worst = max(worst, schatten / op_norm)
        print(f"p={p:.2f}, r={r:.6g}, max two-row ratio={worst:.6f}")


if __name__ == "__main__":
    main()

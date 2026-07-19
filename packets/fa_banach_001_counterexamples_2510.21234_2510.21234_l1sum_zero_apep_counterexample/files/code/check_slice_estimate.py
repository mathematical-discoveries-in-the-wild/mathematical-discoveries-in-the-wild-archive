"""Numerical sanity checks for the l1-sum zero-APEP counterexample.

This script does not prove the theorem. It checks the finite-dimensional
linear algebra used in the proof: given m test vectors in R^n with n>m,
we can choose a unit vector u orthogonal to all tests, and vectors h with
<h,u> close to 1 satisfy the bound ||h-u|| <= sqrt(2 delta).
"""

from __future__ import annotations

import numpy as np


def orthogonal_unit(rows: np.ndarray) -> np.ndarray:
    """Return a unit vector orthogonal to the rows of a full row-rank matrix."""
    _, _, vh = np.linalg.svd(rows, full_matrices=True)
    u = vh[-1]
    return u / np.linalg.norm(u)


def main() -> None:
    rng = np.random.default_rng(20260608)
    trials = 200
    worst_orthogonality = 0.0
    worst_bound_gap = -np.inf

    for m in range(1, 8):
        n = m + 3
        for _ in range(trials):
            rows = rng.normal(size=(m, n))
            u = orthogonal_unit(rows)
            worst_orthogonality = max(worst_orthogonality, np.max(np.abs(rows @ u)))

            # Build h with <h,u> = 1-delta and ||h|| <= 1.
            v = rng.normal(size=n)
            v = v - np.dot(v, u) * u
            v = v / np.linalg.norm(v)
            for delta in (1e-1, 1e-2, 1e-3, 1e-4):
                h = (1 - delta) * u + np.sqrt(2 * delta - delta * delta) * v
                assert np.linalg.norm(h) <= 1 + 1e-12
                assert np.dot(h, u) > 1 - delta - 1e-12
                bound_gap = np.linalg.norm(h - u) - np.sqrt(2 * delta)
                worst_bound_gap = max(worst_bound_gap, bound_gap)

    print(f"trials per m: {trials}")
    print(f"worst |<a_j,u>|: {worst_orthogonality:.3e}")
    print(f"worst (||h-u|| - sqrt(2 delta)): {worst_bound_gap:.3e}")
    print("status: ok")


if __name__ == "__main__":
    main()


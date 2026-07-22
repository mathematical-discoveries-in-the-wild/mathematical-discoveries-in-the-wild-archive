"""Numerical checks for the inverse-distribution L1 isometry.

This is evidence only.  Random monotone step functions are sampled on a fine
uniform grid, transformed by Dq(t)=measure{u:q(u)<=t}, and the L1 distance and
mean-complement identities are checked to grid accuracy.
"""

from __future__ import annotations

import numpy as np


def transform(q: np.ndarray, levels: np.ndarray) -> np.ndarray:
    return np.searchsorted(q, levels, side="right") / q.size


def main() -> None:
    rng = np.random.default_rng(11055706)
    grid_size = 12000
    levels = (np.arange(grid_size) + 0.5) / grid_size
    max_distance_error = 0.0
    max_mean_error = 0.0

    for _ in range(80):
        q = np.sort(rng.random(grid_size))
        r = np.sort(rng.random(grid_size))
        dq = transform(q, levels)
        dr = transform(r, levels)

        distance_error = abs(np.mean(np.abs(q - r)) - np.mean(np.abs(dq - dr)))
        mean_error = abs(np.mean(dq) - (1.0 - np.mean(q)))
        max_distance_error = max(max_distance_error, distance_error)
        max_mean_error = max(max_mean_error, mean_error)

    tolerance = 3.0 / grid_size
    print(f"max L1-isometry error: {max_distance_error:.3e}")
    print(f"max mean-complement error: {max_mean_error:.3e}")
    print(f"grid tolerance: {tolerance:.3e}")
    if max(max_distance_error, max_mean_error) > tolerance:
        raise SystemExit("finite-grid check failed")


if __name__ == "__main__":
    main()

"""Finite sanity check for the cyclic Green-matrix transfer lemma.

This script is not a proof.  It builds finite cyclic models of

    (D_N x)_i(j) = x_{i+1}(j) - w_{j+1} x_i(j+1),

computes the Green matrix D_N^{-1}, and checks that random mixed
sup_time ell_p amplifications stay below the Schur bound used in the
packet proof.
"""

from __future__ import annotations

import numpy as np


def node(t: int, j: int, n_time: int, n_space: int) -> int:
    return (t % n_time) * n_space + (j % n_space)


def defect_matrix(weights: np.ndarray, n_time: int) -> np.ndarray:
    n_space = len(weights)
    dim = n_time * n_space
    d = np.zeros((dim, dim), dtype=float)
    for t in range(n_time):
        for j in range(n_space):
            row = node(t, j, n_time, n_space)
            d[row, node(t + 1, j, n_time, n_space)] += 1.0
            d[row, node(t, j + 1, n_time, n_space)] -= weights[(j + 1) % n_space]
    return d


def mixed_norm(v: np.ndarray, n_time: int, n_space: int, p: float) -> float:
    arr = v.reshape(n_time, n_space)
    return max(np.linalg.norm(arr[t], ord=p) for t in range(n_time))


def schur_mixed_bound(green_abs: np.ndarray, n_time: int, n_space: int, p: float) -> float:
    row_sum = green_abs.sum(axis=1).max()
    q_factor = row_sum ** (1.0 - 1.0 / p)
    best = 0.0
    for out_t in range(n_time):
        time_sum = 0.0
        out_rows = [node(out_t, j, n_time, n_space) for j in range(n_space)]
        for in_t in range(n_time):
            col_max = 0.0
            for in_j in range(n_space):
                col = node(in_t, in_j, n_time, n_space)
                col_max = max(col_max, green_abs[out_rows, col].sum())
            time_sum += col_max
        best = max(best, q_factor * (time_sum ** (1.0 / p)))
    return best


def run_trial(rng: np.random.Generator, n_time: int, n_space: int, p: float) -> tuple[float, float]:
    weights = np.exp(rng.normal(0.0, 0.7, size=n_space))
    d = defect_matrix(weights, n_time)
    green = np.linalg.inv(d)
    bound = schur_mixed_bound(np.abs(green), n_time, n_space, p)
    worst = 0.0
    for _ in range(200):
        e = rng.normal(size=n_time * n_space)
        e /= mixed_norm(e, n_time, n_space, p)
        x = green @ e
        worst = max(worst, mixed_norm(x, n_time, n_space, p))
    return worst, bound


def main() -> None:
    rng = np.random.default_rng(17)
    cases = [(3, 5, 1.0), (4, 7, 1.5), (5, 8, 2.0), (6, 9, 3.0)]
    for n_time, n_space, p in cases:
        worst_seen = 0.0
        smallest_margin = float("inf")
        for _ in range(20):
            worst, bound = run_trial(rng, n_time, n_space, p)
            worst_seen = max(worst_seen, worst)
            smallest_margin = min(smallest_margin, bound - worst)
            if worst > bound * (1 + 1e-10):
                raise AssertionError((n_time, n_space, p, worst, bound))
        print(
            f"N={n_time:2d} M={n_space:2d} p={p:3.1f}: "
            f"sampled amplification <= {worst_seen:.4g}, "
            f"Schur margin >= {smallest_margin:.4g}"
        )
    print("finite Green-matrix transfer sanity checks passed")


if __name__ == "__main__":
    main()

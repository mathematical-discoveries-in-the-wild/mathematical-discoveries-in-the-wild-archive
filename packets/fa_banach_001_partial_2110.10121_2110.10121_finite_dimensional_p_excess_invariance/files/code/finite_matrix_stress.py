"""Finite matrix sanity checks for the p-excess packet.

This is not part of the proof.  It samples finite-dimensional exact-dual
matrix models and checks that the finite p-excess agrees in the sampled
examples.
"""

from itertools import combinations

import numpy as np


def rank(matrix, tol=1e-9):
    return np.linalg.matrix_rank(np.asarray(matrix, dtype=float), tol)


def nullspace(matrix, tol=1e-10):
    _, singular_values, vh = np.linalg.svd(np.asarray(matrix, dtype=float), full_matrices=True)
    r = (singular_values > tol).sum()
    return vh[r:].T


def p_excess(functional_rows, vector_cols):
    """Return finite p-excess for F:Nxd and T:dxN."""
    f = np.asarray(functional_rows, dtype=float)
    t = np.asarray(vector_cols, dtype=float)
    n, d = f.shape
    best = -1
    for size in range(n + 1):
        for deleted in combinations(range(n), size):
            keep = [i for i in range(n) if i not in deleted]
            if rank(t[:, keep]) == d and rank(f[keep, :]) == d:
                best = max(best, size)
    return best


def main():
    rng = np.random.default_rng(20260618)
    for d in [1, 2, 3]:
        for n in range(d, d + 5):
            for _ in range(200):
                f = rng.normal(size=(n, d))
                t = rng.normal(size=(d, n))
                if rank(f) < d or rank(t) < d or rank(t @ f) < d:
                    continue
                assert p_excess(f, t) == n - d

                # Sample exact duals: T H = I and R F = I.
                h0 = t.T @ np.linalg.inv(t @ t.T)
                k = nullspace(t)
                r0 = np.linalg.inv(f.T @ f) @ f.T
                z = nullspace(f.T)
                for _ in range(20):
                    a = rng.normal(size=(k.shape[1], d)) if k.shape[1] else np.zeros((0, d))
                    c = rng.normal(size=(d, z.shape[1])) if z.shape[1] else np.zeros((d, 0))
                    h = h0 + k @ a
                    r = r0 + c @ z.T
                    if rank(r @ h) == d:
                        assert p_excess(h, r) == n - d
    print("finite matrix stress checks passed")


if __name__ == "__main__":
    main()

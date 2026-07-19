#!/usr/bin/env python3
"""Numerical sanity checks for the odd-dimensional Hilbert-space packet.

The proof is exact linear algebra. This script only checks random instances of
the Sylvester range step:

    X |-> A X + X B

where A and B are skew-symmetric matrices with one-dimensional kernels and
disjoint nonzero rotation frequencies. For a prescribed C, the proof chooses
unit vectors a,b with <C b,a>=0, makes ker(A)=Ra and ker(B)=Rb, and then C
should lie in the range of the Sylvester map.
"""

from __future__ import annotations

import argparse
import numpy as np


def orthonormal_basis_with_first(first: np.ndarray) -> np.ndarray:
    """Return an orthogonal matrix whose first column is first/||first||."""
    first = np.asarray(first, dtype=float)
    first = first / np.linalg.norm(first)
    n = first.size
    cols = [first]
    for j in range(n):
        v = np.zeros(n)
        v[j] = 1.0
        for c in cols:
            v -= np.dot(v, c) * c
        if np.linalg.norm(v) > 1e-10:
            cols.append(v / np.linalg.norm(v))
        if len(cols) == n:
            break
    return np.column_stack(cols)


def skew_with_kernel(kernel: np.ndarray, freqs: list[float]) -> np.ndarray:
    """Skew-symmetric matrix with the requested one-dimensional kernel."""
    n = len(kernel)
    q = orthonormal_basis_with_first(kernel)
    s = np.zeros((n, n))
    for i, freq in enumerate(freqs):
        j = 1 + 2 * i
        s[j, j + 1] = -freq
        s[j + 1, j] = freq
    return q @ s @ q.T


def choose_a_perp_to_cb(c: np.ndarray, b: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    cb = c @ b
    n = b.size
    if np.linalg.norm(cb) < 1e-12:
        a = rng.normal(size=n)
    else:
        a = rng.normal(size=n)
        a -= np.dot(a, cb) / np.dot(cb, cb) * cb
    while np.linalg.norm(a) < 1e-12:
        a = rng.normal(size=n)
        if np.linalg.norm(cb) >= 1e-12:
            a -= np.dot(a, cb) / np.dot(cb, cb) * cb
    return a / np.linalg.norm(a)


def sylvester_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    # vec(A X + X B) = (I kron A + B^T kron I) vec(X), column-major.
    return np.kron(np.eye(n), a) + np.kron(b.T, np.eye(n))


def run_trial(n: int, rng: np.random.Generator) -> tuple[int, float, float]:
    c = rng.normal(size=(n, n))
    b = rng.normal(size=n)
    b /= np.linalg.norm(b)
    a_vec = choose_a_perp_to_cb(c, b, rng)
    m = (n - 1) // 2
    a_freqs = [float(i + 1) for i in range(m)]
    b_freqs = [float(m + 2 + i) for i in range(m)]
    a = skew_with_kernel(a_vec, a_freqs)
    bmat = skew_with_kernel(b, b_freqs)
    lmat = sylvester_matrix(a, bmat)
    rhs = c.reshape(-1, order="F")
    sol, *_ = np.linalg.lstsq(lmat, rhs, rcond=None)
    residual = float(np.linalg.norm(lmat @ sol - rhs))
    rank = int(np.linalg.matrix_rank(lmat, tol=1e-9))
    obstruction = float(abs(a_vec @ c @ b))
    return rank, residual, obstruction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", nargs="*", type=int, default=[3, 5, 7])
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--seed", type=int, default=190512257)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    for n in args.dims:
        if n < 3 or n % 2 == 0:
            raise SystemExit(f"dimension must be odd and at least 3, got {n}")
        expected_rank = n * n - 1
        max_residual = 0.0
        max_obstruction = 0.0
        ranks = set()
        for _ in range(args.trials):
            rank, residual, obstruction = run_trial(n, rng)
            ranks.add(rank)
            max_residual = max(max_residual, residual)
            max_obstruction = max(max_obstruction, obstruction)
        print(
            f"n={n}: ranks={sorted(ranks)}, expected_rank={expected_rank}, "
            f"max_residual={max_residual:.3e}, "
            f"max_obstruction={max_obstruction:.3e}"
        )
        if ranks != {expected_rank} or max_residual > 1e-8 or max_obstruction > 1e-8:
            raise SystemExit("sanity check failed")


if __name__ == "__main__":
    main()

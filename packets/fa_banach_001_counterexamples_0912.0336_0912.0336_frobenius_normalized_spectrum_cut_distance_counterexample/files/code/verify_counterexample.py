#!/usr/bin/env python3
"""Verify the star-row versus identity counterexample for small n."""

from itertools import combinations
import numpy as np


def cut_norm_bruteforce(M):
    n, m = M.shape
    best = 0.0
    rows = range(n)
    cols = range(m)
    for r in range(n + 1):
        for X in combinations(rows, r):
            X = list(X)
            for c in range(m + 1):
                for Y in combinations(cols, c):
                    Y = list(Y)
                    val = abs(M[np.ix_(X, Y)].sum()) / (n * m)
                    best = max(best, val)
    return best


def matrices(n):
    A = np.zeros((n, n))
    A[0, :] = 1.0
    B = np.eye(n)
    return A, B


def main():
    for n in range(2, 9):
        A, B = matrices(n)
        fro_a = np.linalg.norm(A, "fro")
        fro_b = np.linalg.norm(B, "fro")
        s_a = np.linalg.svd(A, compute_uv=False)
        s_b = np.linalg.svd(B, compute_uv=False)
        cut_a = cut_norm_bruteforce(A)
        cut_b = cut_norm_bruteforce(B)
        cut_diff = cut_norm_bruteforce(A - B)
        print(
            f"n={n}: ||A||F={fro_a:.6g}, ||B||F={fro_b:.6g}, "
            f"top gap={s_a[0]/fro_a - s_b[0]/fro_b:.6g}, "
            f"cut(A)={cut_a:.6g}, cut(B)={cut_b:.6g}, "
            f"cut(A-B)={cut_diff:.6g}, 2/n={2/n:.6g}"
        )


if __name__ == "__main__":
    main()

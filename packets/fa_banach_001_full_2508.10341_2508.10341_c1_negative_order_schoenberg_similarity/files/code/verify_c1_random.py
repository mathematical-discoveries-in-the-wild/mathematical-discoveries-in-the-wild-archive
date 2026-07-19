#!/usr/bin/env python3
"""Random sanity checks for the Conjecture 6.3 matrix inequality.

The reciprocal critical points are the eigenvalues of
    B = diag(u) + u 1^T.
The claimed inequality is
    sum |eig(B)|^2 <= 3 sum |u_j|^2 + |sum u_j|^2.
"""

from __future__ import annotations

import argparse

import numpy as np


def trial(rng: np.random.Generator, n: int) -> float:
    u = rng.normal(size=n) + 1j * rng.normal(size=n)
    b = np.diag(u) + np.outer(u, np.ones(n))
    lhs = float(np.sum(np.abs(np.linalg.eigvals(b)) ** 2))
    rhs = float(3 * np.sum(np.abs(u) ** 2) + abs(np.sum(u)) ** 2)
    return lhs - rhs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--tol", type=float, default=1e-8)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    worst = -float("inf")
    worst_n = None
    for n in range(1, args.max_n + 1):
        for _ in range(args.trials):
            gap = trial(rng, n)
            if gap > worst:
                worst = gap
                worst_n = n
            if gap > args.tol:
                raise SystemExit(f"violation: n={n} gap={gap}")
    print(f"ok max_n={args.max_n} trials={args.trials} worst_gap={worst:.3e} at n={worst_n}")


if __name__ == "__main__":
    main()

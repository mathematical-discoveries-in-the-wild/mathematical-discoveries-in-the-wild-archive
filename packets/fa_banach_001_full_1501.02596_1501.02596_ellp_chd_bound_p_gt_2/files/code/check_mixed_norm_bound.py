#!/usr/bin/env python3
"""Randomized stress test for the weighted centering inequality.

This is evidence only.  The solution packet contains a proof by interpolation.
"""

from __future__ import annotations

import argparse

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=150_102_596)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    worst_ratio = 0.0
    worst_case: tuple[int, int, float, float, float] | None = None

    for n in (2, 3, 4, 6):
        for k in range(2, n + 1):
            for p in (2.05, 2.2, 3.0, 4.0, 8.0, 20.0):
                conjugate = p / (p - 1.0)
                theta = 1.0 - 2.0 / p
                for _ in range(args.samples):
                    alpha = rng.dirichlet(np.full(k, 0.35))
                    points = rng.normal(size=(k, n))
                    norms = np.linalg.norm(points, ord=p, axis=1)
                    points /= np.maximum(1.0, norms)[:, None]

                    center = alpha @ points
                    distances = np.linalg.norm(points - center, ord=p, axis=1)
                    lhs = float((alpha @ (distances**conjugate)) ** (1.0 / conjugate))
                    c_alpha = max(0.0, float(2.0 * (1.0 - alpha @ alpha)))
                    rhs = c_alpha**theta
                    # A floating-point Dirichlet draw can underflow to a
                    # one-point weight.  Then T_alpha is zero and both sides
                    # are zero; there is no ratio to test.
                    if rhs == 0.0:
                        continue
                    ratio = lhs / rhs

                    if ratio > worst_ratio:
                        worst_ratio = ratio
                        worst_case = (n, k, p, lhs, rhs)

    print(f"worst_ratio={worst_ratio:.12f}")
    print(f"worst_case={worst_case}")
    if worst_ratio > 1.0 + 1e-10:
        raise SystemExit("sampled violation")


if __name__ == "__main__":
    main()

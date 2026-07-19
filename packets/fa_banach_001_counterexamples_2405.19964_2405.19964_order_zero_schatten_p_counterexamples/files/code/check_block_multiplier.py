#!/usr/bin/env python3
"""Finite-dimensional sanity check for the sign-block multiplier mechanism.

This numerically samples random sign polynomials, chooses the best sampled
input, and compares its L^q norm with the Dirichlet-kernel output norm.  It is
illustrative only; the packet proof uses Khintchine's inequality.
"""

from __future__ import annotations

import argparse

import numpy as np


def lp_norm(values: np.ndarray, q: float) -> float:
    return float(np.mean(np.abs(values) ** q) ** (1.0 / q))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=float, default=4.0)
    parser.add_argument("--trials", type=int, default=256)
    parser.add_argument("--grid", type=int, default=32768)
    parser.add_argument("--seed", type=int, default=240519964)
    args = parser.parse_args()

    if args.q <= 2:
        raise SystemExit("q must exceed 2")

    rng = np.random.default_rng(args.seed)
    theta = 2 * np.pi * np.arange(args.grid) / args.grid

    print("q N best_random_Lq dirichlet_Lq ratio")
    for n in (16, 32, 64, 128, 256):
        phases = np.exp(1j * np.outer(np.arange(1, n + 1), theta))
        dirichlet = phases.sum(axis=0)
        output_norm = lp_norm(dirichlet, args.q)

        best = float("inf")
        for _ in range(args.trials):
            signs = rng.choice(np.array([-1.0, 1.0]), size=n)
            best = min(best, lp_norm(signs @ phases, args.q))

        print(f"{args.q:g} {n:3d} {best:12.6f} {output_norm:12.6f} {output_norm / best:9.4f}")


if __name__ == "__main__":
    main()

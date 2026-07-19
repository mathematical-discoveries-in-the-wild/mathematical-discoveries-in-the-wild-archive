#!/usr/bin/env python3
"""Finite-grid sanity check for the SPAP obstruction.

This is not a proof of the theorem. It models the proof on a dyadic grid:
a coarse conditional expectation kills all sufficiently fine Rademacher
signs, so the error on those signs stays equal to the norm of the unit.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def rademacher(level: int, grid_bits: int) -> np.ndarray:
    n = 2**grid_bits
    block = 2 ** (grid_bits - level)
    indices = np.arange(n)
    return np.where((indices // block) % 2 == 0, 1.0, -1.0)


def conditional_expectation(values: np.ndarray, sigma_bits: int) -> np.ndarray:
    if sigma_bits == 0:
        return np.full_like(values, values.mean())
    n = len(values)
    block = n // (2**sigma_bits)
    out = np.empty_like(values)
    for start in range(0, n, block):
        out[start : start + block] = values[start : start + block].mean()
    return out


def lp_norm(values: np.ndarray, p: float) -> float:
    return float(np.mean(np.abs(values) ** p) ** (1.0 / p))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid-bits", type=int, default=12)
    parser.add_argument("--coarse-bits", type=int, default=4)
    parser.add_argument("--p", type=float, default=3.0)
    args = parser.parse_args()

    if not (1 <= args.coarse_bits < args.grid_bits):
        raise SystemExit("--coarse-bits must be between 1 and grid-bits-1")

    unit_norm = lp_norm(np.ones(2**args.grid_bits), args.p)
    print(f"unit L_{args.p:g} norm on probability grid: {unit_norm:.6f}")
    print("level  ||E_coarse r_level||_p  ||r_level-E_coarse r_level||_p")
    for level in range(1, args.grid_bits + 1):
        r = rademacher(level, args.grid_bits)
        er = conditional_expectation(r, args.coarse_bits)
        print(
            f"{level:5d}  {lp_norm(er, args.p):22.6f}"
            f"  {lp_norm(r - er, args.p):31.6f}"
        )

    tail_level = args.coarse_bits + 1
    expected = lp_norm(
        rademacher(tail_level, args.grid_bits)
        - conditional_expectation(rademacher(tail_level, args.grid_bits), args.coarse_bits),
        args.p,
    )
    if not math.isclose(expected, unit_norm, rel_tol=1e-12, abs_tol=1e-12):
        raise SystemExit("unexpected tail obstruction value")


if __name__ == "__main__":
    main()

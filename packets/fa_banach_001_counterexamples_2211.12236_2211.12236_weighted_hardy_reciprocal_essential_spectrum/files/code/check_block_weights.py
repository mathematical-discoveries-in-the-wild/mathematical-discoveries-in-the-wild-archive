#!/usr/bin/env python3
"""Sanity checks for the block-weight counterexample.

The proof is analytic.  This script checks the recursive block parameters,
the reciprocal-series peak terms, and the explicit singular-vector residuals.
"""

from __future__ import annotations

import math


A = 1.5


def blocks(count: int):
    n = 0
    for m in range(1, count + 1):
        length = (n + 1) ** 2
        yield m, n, length
        n += 2 * length


def singular_residual(q: int) -> float:
    right = A / 2
    left = 1 / (2 * A)
    norm_sq = sum(right ** (2 * j) for j in range(q + 1))
    norm_sq += sum(left ** (2 * j) for j in range(1, q + 1))
    error_sq = (0.5 * left**q) ** 2 + (A * right**q) ** 2
    return math.sqrt(error_sq / norm_sq)


print("m  valley N_m  half-length L_m  log reciprocal peak term")
records = list(blocks(7))
for m, n, length in records:
    peak_log = 2 * (
        length * math.log(2) - (n + length + 1) * math.log(A)
    )
    print(f"{m:1d}  {n:12d}  {length:16d}  {peak_log: .6e}")

print("\nq  normalized singular residual")
for q in (2, 4, 8, 16, 32, 64):
    print(f"{q:2d}  {singular_residual(q):.12e}")

assert all(length > 0 for _, _, length in records)
assert all(records[j + 1][1] == records[j][1] + 2 * records[j][2]
           for j in range(len(records) - 1))
assert singular_residual(64) < 1e-7
assert records[-1][2] / (records[-1][1] + 1) > 100


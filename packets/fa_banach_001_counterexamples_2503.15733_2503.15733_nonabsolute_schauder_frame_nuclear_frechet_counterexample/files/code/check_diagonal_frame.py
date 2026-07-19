#!/usr/bin/env python3
"""Finite sanity check for the diagonal non-absolute Schauder-frame example."""

from __future__ import annotations

import math


def diagonal_pairs(limit: int):
    count = 0
    diag = 2
    while count < limit:
        for j in range(1, diag):
            k = diag - j
            yield j, k
            count += 1
            if count >= limit:
                return
        diag += 1


def r(k: int) -> float:
    return ((-1) ** (k + 1)) / (k * math.log(2.0))


def main() -> None:
    coeffs = {j: 1.0 / (j**6) for j in range(1, 41)}
    row_sums = {j: 0.0 for j in coeffs}
    abs_row_1 = 0.0

    checkpoints = [100, 500, 1000, 3000, 6000]
    checkpoint_set = set(checkpoints)

    for n, (j, k) in enumerate(diagonal_pairs(max(checkpoints)), start=1):
        if j in row_sums:
            row_sums[j] += r(k)
        if j == 1:
            abs_row_1 += abs(r(k))
        if n in checkpoint_set:
            err_p0 = max(abs(coeffs[j] * (row_sums[j] - 1.0)) for j in coeffs)
            print(f"N={n:5d}  sampled_p0_error={err_p0:.6e}  row1_abs_sum={abs_row_1:.6f}")

    print("The sampled error decreases while the absolute row-1 sum keeps growing.")
    print("This script illustrates the proof mechanism; it is not a proof.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite sanity check for the disjoint Lorentz upper p-estimate."""

from __future__ import annotations

import itertools
import random


def lorentz_norm_p(values: list[float], weights: list[float], p: float) -> float:
    ordered = sorted((abs(v) for v in values), reverse=True)
    return sum(weights[i] * (ordered[i] ** p) for i in range(len(ordered)))


def main() -> None:
    random.seed(11086026)
    p = 1.7
    weights = [1 / ((i + 1) ** 0.35) for i in range(80)]
    blocks: list[list[float]] = []
    for block_len in [3, 5, 4, 6, 2]:
        blocks.append([random.random() for _ in range(block_len)])
    coeffs = [random.uniform(-2, 2) for _ in blocks]

    union: list[float] = []
    for coeff, block in zip(coeffs, blocks):
        union.extend([coeff * value for value in block])

    lhs = lorentz_norm_p(union, weights, p)
    rhs = sum(abs(c) ** p * lorentz_norm_p(block, weights, p) for c, block in zip(coeffs, blocks))
    assert lhs <= rhs + 1e-9, (lhs, rhs)
    print("disjoint Lorentz upper p-estimate sanity check passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the finite-dimensional algebra in the orthant upper bound.

The lower bound is analytic and is proved in the packet.  This script checks
Sylvester-Hadamard identities, the determinant/simplex-volume formula, and the
binary entropy estimate used to cover every dimension.
"""

from __future__ import annotations

import math

import numpy as np


def sylvester_hadamard(dimension: int) -> np.ndarray:
    if dimension < 1 or dimension & (dimension - 1):
        raise ValueError("dimension must be a power of two")
    matrix = np.ones((1, 1), dtype=np.int64)
    while matrix.shape[0] < dimension:
        matrix = np.block([[matrix, matrix], [matrix, -matrix]])
    return matrix


def block_probability(dimension: int) -> float:
    return dimension ** (dimension / 2) / (
        2**dimension * math.factorial(dimension)
    )


def check_hadamard_blocks() -> None:
    print("SYLVESTER-HADAMARD BLOCKS")
    for dimension in [1, 2, 4, 8, 16, 32, 64, 128]:
        matrix = sylvester_hadamard(dimension)
        assert np.array_equal(matrix[0], np.ones(dimension, dtype=np.int64))
        assert np.array_equal(
            matrix.T @ matrix, dimension * np.eye(dimension, dtype=np.int64)
        )
        sign, logdet = np.linalg.slogdet(matrix.astype(float))
        expected_logdet = (dimension / 2) * math.log(dimension)
        assert abs(sign) == 1
        assert abs(logdet - expected_logdet) < 1e-8 * max(1, dimension)
        probability = block_probability(dimension)
        upper = (math.e / (2 * math.sqrt(dimension))) ** dimension
        assert probability <= upper * (1 + 1e-12)
        print(
            f"d={dimension:3d}: H^T H=dI, "
            f"log|det H|={logdet:.6f}, orthant probability={probability:.6e}"
        )
    print("HADAMARD CHECKS: PASS")


def binary_blocks(n: int) -> list[int]:
    return [1 << k for k in range(n.bit_length()) if n & (1 << k)]


def check_binary_entropy(limit: int = 100_000) -> None:
    worst_ratio = 0.0
    worst_n = 1
    for n in range(1, limit + 1):
        blocks = binary_blocks(n)
        assert sum(blocks) == n
        entropy_sum = sum(d * math.log(n / d) for d in blocks)
        assert entropy_sum <= 4 * n * math.log(2) + 1e-11
        ratio = entropy_sum / n
        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_n = n

        log_probability_upper = sum(
            d * math.log(math.e / (2 * math.sqrt(d))) for d in blocks
        )
        claimed_log_upper = n * math.log(2 * math.e / math.sqrt(n))
        assert log_probability_upper <= claimed_log_upper + 1e-10

    print("BINARY BLOCK CHECKS: PASS")
    print(f"tested every 1 <= n <= {limit}")
    print(
        "largest observed binary entropy per coordinate = "
        f"{worst_ratio:.12f} at n={worst_n}; proof bound = {4*math.log(2):.12f}"
    )


def print_lower_constant() -> None:
    moment_constant = 4 + 8 / math.log(2) ** 2
    endpoint_constant = 1 / math.sqrt(1 + math.e * moment_constant)
    alpha_constant = 2 * endpoint_constant / math.sqrt(2 * math.pi * math.e)
    print("EXPLICIT LOWER-BOUND CONSTANTS")
    print(f"C0 = 4 + 8/log(2)^2 = {moment_constant:.12f}")
    print(f"centered inball factor = {endpoint_constant:.12f}")
    print(f"alpha_n >= {alpha_constant:.12f}/sqrt(n)")
    print(f"upper proof gives alpha_n <= {4*math.e:.12f}/sqrt(n)")


if __name__ == "__main__":
    check_hadamard_blocks()
    check_binary_entropy()
    print_lower_constant()
    print("ALL VERIFICATION CHECKS: PASS")

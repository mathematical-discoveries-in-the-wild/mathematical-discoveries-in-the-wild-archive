#!/usr/bin/env python3
"""Finite-dimensional checks for the CAR multiplication witness.

For z_d = sum_j e_{1j} tensor e_{j1}, this script checks that z_d is a
partial isometry of norm one and that matrix multiplication maps it to
d e_11.  The general CAR argument in the packet is analytic; these checks
only guard against an index, adjoint, or tensor-order mistake.
"""

from __future__ import annotations

import argparse

import numpy as np


def matrix_unit(d: int, i: int, j: int) -> np.ndarray:
    out = np.zeros((d, d), dtype=np.float64)
    out[i, j] = 1.0
    return out


def verify(d: int, tolerance: float = 1e-12) -> dict[str, float | int]:
    z = np.zeros((d * d, d * d), dtype=np.float64)
    product = np.zeros((d, d), dtype=np.float64)
    for j in range(d):
        left = matrix_unit(d, 0, j)
        right = matrix_unit(d, j, 0)
        z += np.kron(left, right)
        product += left @ right

    norm_z = float(np.linalg.norm(z, ord=2))
    target = d * matrix_unit(d, 0, 0)
    product_error = float(np.linalg.norm(product - target, ord=2))
    partial_isometry_error = float(np.linalg.norm(z @ z.T @ z - z, ord=2))

    if abs(norm_z - 1.0) > tolerance:
        raise AssertionError(f"d={d}: ||z_d||={norm_z}, expected 1")
    if product_error > tolerance:
        raise AssertionError(f"d={d}: multiplication error={product_error}")
    if partial_isometry_error > tolerance:
        raise AssertionError(
            f"d={d}: partial-isometry error={partial_isometry_error}"
        )

    return {
        "d": d,
        "tensor_operator_norm": norm_z,
        "multiplication_norm": float(np.linalg.norm(product, ord=2)),
        "product_error": product_error,
        "partial_isometry_error": partial_isometry_error,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimensions", nargs="+", type=int, default=[2, 4, 8, 16])
    args = parser.parse_args()
    for dimension in args.dimensions:
        if dimension < 1:
            raise ValueError("dimensions must be positive")
        print(verify(dimension))


if __name__ == "__main__":
    main()

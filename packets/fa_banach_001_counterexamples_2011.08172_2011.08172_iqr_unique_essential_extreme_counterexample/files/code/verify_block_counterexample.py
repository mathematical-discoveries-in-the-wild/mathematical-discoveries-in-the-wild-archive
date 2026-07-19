#!/usr/bin/env python3
"""Finite-block sanity checks for the IQR essential-spectrum counterexample."""

from __future__ import annotations

import math

import numpy as np


def block(k: int) -> np.ndarray:
    a = 1.0 - 1.0 / (2 * k)
    b = 1.0 - 1.0 / (2 * k + 1)
    u = np.array([[1.0, 1.0], [1.0, -1.0]]) / math.sqrt(2.0)
    return u.T @ np.diag([a, b]) @ u


def direct_sum(num_blocks: int) -> np.ndarray:
    mat = np.zeros((2 * num_blocks, 2 * num_blocks))
    for k in range(1, num_blocks + 1):
        mat[2 * k - 2 : 2 * k, 2 * k - 2 : 2 * k] = block(k)
    return mat


def main() -> None:
    for k in range(1, 8):
        b = block(k)
        evals = np.linalg.eigvalsh(b)
        expected = np.array([1.0 - 1.0 / (2 * k), 1.0 - 1.0 / (2 * k + 1)])
        assert abs(b[0, 1]) > 0.0
        assert np.allclose(evals, expected)

    # A finite QR simulation of initial reducing blocks.  The proof does not
    # depend on this: it only illustrates that the top sections never pass the
    # spectral ceiling of the finite reducing block that contains them.
    for m in range(1, 13):
        k = math.ceil(m / 2)
        mat = direct_sum(k)
        current = mat.copy()
        for _ in range(20):
            q, r = np.linalg.qr(current)
            current = r @ q
        section = current[:m, :m]
        max_ritz = np.linalg.eigvalsh(section).max()
        ceiling = 1.0 - 1.0 / (2 * k + 1)
        gap = 1.0 - ceiling
        assert max_ritz <= ceiling + 1e-10
        print(f"m={m:2d} K={k:2d} max_section={max_ritz:.12f} ceiling={ceiling:.12f} gap={gap:.12f}")

    tail_norms = [1.0 / (2 * k) for k in (5, 10, 50, 100)]
    print("tail norms for T-I after block K:", tail_norms)


if __name__ == "__main__":
    main()

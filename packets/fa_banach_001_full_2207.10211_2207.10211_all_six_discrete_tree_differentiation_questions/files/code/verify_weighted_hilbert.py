"""Finite-truncation check for the weighted-Hilbert norm counterexample.

The proof in the packet is exact.  This script builds the binary-tree model
through a finite depth and checks the claimed C_b norm and the explicit
alternating test-vector formula for D.
"""

from __future__ import annotations

import math

import numpy as np


def matrices(depth: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    size = 2 ** (depth + 1) - 1
    u = np.zeros((size, size))
    for parent in range(2**depth - 1):
        u[2 * parent + 1, parent] = 1 / math.sqrt(2)
        u[2 * parent + 2, parent] = 1 / math.sqrt(2)
    p = np.zeros((size, size))
    p[0, 0] = 1
    cb = p + u
    d = np.eye(size) - cb
    return u, cb, d


def main() -> None:
    depth = 10
    u, cb, d = matrices(depth)
    cb_norm = np.linalg.svd(cb, compute_uv=False)[0]
    d_norm = np.linalg.svd(d, compute_uv=False)[0]
    assert abs(cb_norm - math.sqrt(2)) < 1e-12
    assert d_norm <= 2 + 1e-12

    e0 = np.zeros(cb.shape[0])
    e0[0] = 1
    orbit = e0.copy()
    y = np.zeros_like(e0)
    n = depth
    for k in range(n):
        y += (-1) ** k * orbit
        orbit = u @ orbit
    y /= math.sqrt(n)
    observed = float(np.dot(d @ y, d @ y))
    expected = 4 - 3 / n
    assert abs(observed - expected) < 1e-12

    print(f"depth={depth}")
    print(f"||C_b||={cb_norm:.12f} (expected sqrt(2))")
    print(f"||D|| on truncation={d_norm:.12f} (bounded above by 2)")
    print(f"||D y_N||^2={observed:.12f} (expected {expected:.12f})")


if __name__ == "__main__":
    main()

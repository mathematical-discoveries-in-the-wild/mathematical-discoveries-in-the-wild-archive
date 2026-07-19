#!/usr/bin/env python3
"""Finite-dimensional checks for the 0408004 SBD dual counterexample.

The proof in the packet is analytic.  This script verifies the local
three-vector computations numerically for several epsilon values:

  v1 = e1, v2 = e1 + eps e2 + e3, v3 = e3.

The primal middle-skip projection from span(v1,v3) onto span(v1)
has norm 1.  The dual middle-skip projection from span(y1,y3)
onto span(y1), where y1,y2,y3 are biorthogonal to v1,v2,v3,
has norm at least ||y1|| / ||y1-y3||.
"""

from __future__ import annotations

import numpy as np


def projection_norm_along(u: np.ndarray, z: np.ndarray) -> float:
    """Norm of projection span(u)+span(z) -> span(u) with kernel span(z)."""
    gram = np.array([[np.dot(u, u), np.dot(u, z)], [np.dot(z, u), np.dot(z, z)]])
    # In coordinates (a,b), domain norm is sqrt([a,b] G [a,b]^T);
    # output norm is |a| ||u||.  The squared operator norm is the
    # largest generalized eigenvalue of diag(||u||^2,0) against G.
    a_mat = np.array([[np.dot(u, u), 0.0], [0.0, 0.0]])
    vals = np.linalg.eigvals(np.linalg.solve(gram, a_mat))
    return float(np.sqrt(max(vals.real)))


def constants(eps: float) -> tuple[float, float, float]:
    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    v1 = e1
    v2 = e1 + eps * e2 + e3
    v3 = e3

    primal_middle = projection_norm_along(v1, v3)

    v = np.column_stack([v1, v2, v3])
    y = np.linalg.inv(v).T
    y1 = y[:, 0]
    y3 = y[:, 2]
    dual_middle = projection_norm_along(y1, y3)
    elementary_lower_bound = np.linalg.norm(y1) / np.linalg.norm(y1 - y3)
    return primal_middle, dual_middle, elementary_lower_bound


def main() -> None:
    print("eps        primal_middle   dual_middle     lower_bound")
    for k in range(1, 9):
        eps = 2.0 ** (-k)
        primal, dual, lower = constants(eps)
        print(f"{eps:8.5f}   {primal:14.8f}   {dual:12.8f}   {lower:12.8f}")


if __name__ == "__main__":
    main()

"""Finite-dimensional sanity check for the operator-ideal construction.

This does not prove the infinite-dimensional theorem. It checks the algebraic
orientation used in the packet in a toy model E = R^3 and F = span(e1,e2):

* matrices with range in F form a right ideal of B(E);
* the quotient B(E)/J contains E/F as a complemented copy through rank-one
  operators and evaluation at a fixed vector.
"""

from __future__ import annotations

import numpy as np


def in_j(matrix: np.ndarray, tol: float = 1e-10) -> bool:
    """Range contained in F = span(e1,e2), i.e. last row is zero."""

    return np.linalg.norm(matrix[2, :]) < tol


def rank_one(x: np.ndarray, f: np.ndarray) -> np.ndarray:
    return np.outer(x, f)


def quotient_coordinate(x: np.ndarray) -> float:
    """Coordinate of E/F when F = span(e1,e2)."""

    return float(x[2])


def main() -> None:
    rng = np.random.default_rng(20260618)
    for _ in range(20):
        t = rng.normal(size=(3, 3))
        t[2, :] = 0.0
        s = rng.normal(size=(3, 3))
        assert in_j(t @ s), "J should be a right ideal"

    x0 = np.array([1.0, 0.0, 0.0])
    f = np.array([1.0, 0.0, 0.0])
    y_lift = np.array([0.0, 0.0, 7.0])
    op = rank_one(y_lift, f)
    projected = quotient_coordinate(op @ x0)
    assert projected == quotient_coordinate(y_lift)
    print("finite-dimensional structure check passed")


if __name__ == "__main__":
    main()

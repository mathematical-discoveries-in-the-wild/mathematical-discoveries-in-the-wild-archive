#!/usr/bin/env python3
"""Numerically verify the p=q=3/2 mixed-norm counterexample."""

from __future__ import annotations

import math

import numpy as np


def lp_norm(matrix: np.ndarray, p: float) -> float:
    return float(np.sum(np.abs(matrix) ** p) ** (1.0 / p))


def main() -> None:
    p = 1.5
    t = 0.25
    r = 7.0 / 8.0
    alpha = r ** (1.0 / p)

    a = np.array([[0.0, 1.0], [alpha, t]])
    b = np.array([[t, alpha], [1.0, 0.0]])

    lhs = lp_norm(a.T @ b, p) ** 2
    rhs = lp_norm(a.T @ a, p) * lp_norm(b.T @ b, p)
    ratio = lhs / rhs

    s = (7.0 + math.sqrt(2.0)) / 4.0
    x = (63.0 + 17.0 * math.sqrt(17.0)) / 64.0

    print(f"p=q={p}")
    print(f"alpha=(7/8)^(2/3)={alpha:.15f}")
    print(f"lhs={lhs:.15f}")
    print(f"rhs={rhs:.15f}")
    print(f"ratio={ratio:.15f}")
    print(f"S={s:.15f}")
    print(f"X={x:.15f}")
    assert ratio > 1.0
    assert s > x


if __name__ == "__main__":
    main()

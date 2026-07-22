#!/usr/bin/env python3
"""Algebra checks for the supersonic moving-interface obstruction."""

from __future__ import annotations

import math

import numpy as np


def main() -> None:
    sigma = np.block(
        [
            [np.zeros((2, 2)), np.eye(2)],
            [np.eye(2), np.zeros((2, 2))],
        ]
    )
    # Acting on [f_1,f_2,e_1,e_2]^T, these rows impose f_1=e_2=0,
    # equivalently x_2(2)=x_2(-2)=0.
    w_b = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
    gram = w_b @ sigma @ w_b.T

    assert np.linalg.matrix_rank(w_b) == 2
    assert np.allclose(gram, np.zeros((2, 2)))

    c = 2.0
    print("rank(W_B) =", np.linalg.matrix_rank(w_b))
    print("W_B Sigma W_B^T =")
    print(gram)
    print()
    print("t       u-foot   v-foot   u-trace  v-trace  x2-trace")
    for t in (0.01, 0.025, 0.05, 0.1):
        u_foot = (c - 1.0) * t
        v_foot = (c + 1.0) * t
        # eta is identically one on [-1/2,1/2].
        assert v_foot < 0.5
        u_trace = u_foot
        v_trace = 0.0
        x2_trace = (u_trace - v_trace) / 2.0

        # At intermediate time s, the backward characteristics remain right
        # of l(s)=cs by gaps (c-1)(t-s) and (c+1)(t-s).
        for j in range(101):
            s = t * j / 100.0
            u_path = c * t - (t - s)
            v_path = c * t + (t - s)
            assert u_path >= c * s - 1e-14
            assert v_path >= c * s - 1e-14

        assert math.isclose(x2_trace, t / 2.0)
        print(
            f"{t:0.3f}   {u_foot:0.3f}    {v_foot:0.3f}    "
            f"{u_trace:0.3f}    {v_trace:0.3f}    {x2_trace:0.3f}"
        )

    print("\nAll checks passed; the required interface trace x_2=0 is violated.")


if __name__ == "__main__":
    main()

"""Illustrate the finite-subset supremum in the counterexample.

This simulation is not part of the proof.  It samples standard Gaussian
variables and tracks the coordinates indexed by
F_N = {i <= N : xi_i > 1}.  The plotted/printed quantity is a lower bound for
the ell_infty norm of the formal sample.
"""

from __future__ import annotations

import random


def run(max_n: int = 200_000, seed: int = 20260619) -> None:
    random.seed(seed)
    lower = 0.0
    checkpoints = {
        10,
        100,
        1_000,
        10_000,
        50_000,
        100_000,
        max_n,
    }
    for i in range(1, max_n + 1):
        x = random.gauss(0.0, 1.0)
        if x > 1.0:
            lower += x / i
        if i in checkpoints:
            print(f"N={i:6d} lower_bound={lower:.6f}")


if __name__ == "__main__":
    run()

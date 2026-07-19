#!/usr/bin/env python3
"""Sanity checks for the interpolation constants in the proof packet.

This is not a proof assistant. It records the elementary parameter
relations used in the LaTeX proof:

    t = 1/k,  1 < k < 2  =>  1/2 < t < 1,
    unconditional constant <= 1/t = k,
    branch coefficient loss <= epsilon / (1 - t).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    k: float
    t: float
    unconditional_bound: float
    branch_loss_multiplier: float


def check_k(k: float) -> Check:
    if not 1.0 < k < 2.0:
        raise ValueError("k must lie in (1, 2)")
    t = 1.0 / k
    assert 0.5 < t < 1.0
    unconditional_bound = 1.0 / t
    assert abs(unconditional_bound - k) < 1e-12
    branch_loss_multiplier = 1.0 / (1.0 - t)
    assert branch_loss_multiplier > 0.0
    return Check(k, t, unconditional_bound, branch_loss_multiplier)


def main() -> None:
    for k in (1.05, 1.25, 1.5, 1.9):
        result = check_k(k)
        print(
            f"k={result.k:.2f}: t={result.t:.8f}, "
            f"unconditional_bound={result.unconditional_bound:.8f}, "
            f"branch_loss_multiplier={result.branch_loss_multiplier:.8f}"
        )


if __name__ == "__main__":
    main()


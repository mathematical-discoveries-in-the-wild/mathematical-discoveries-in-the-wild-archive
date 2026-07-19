#!/usr/bin/env python3
"""Finite numerical checks for the Fourier-positive even-p theorem.

These checks are regression tests, not part of the proof.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.linalg import hadamard


def lp_norm(values: np.ndarray, p: int) -> float:
    return float(np.mean(np.abs(values) ** p) ** (1.0 / p))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=6)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--seed", type=int, default=241019949)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    checked = 0
    smallest_slack = np.inf
    worst_case = None

    for n in range(2, args.max_n + 1):
        size = 1 << n
        walsh = hadamard(size, dtype=float)
        degrees = np.fromiter((j.bit_count() for j in range(size)), dtype=float)
        for d in range(1, n + 1):
            tail = degrees >= d
            for p in (4, 6, 8):
                for _ in range(args.trials):
                    coefficients = np.zeros(size)
                    coefficients[tail] = rng.exponential(size=int(np.sum(tail)))
                    coefficients /= np.linalg.norm(coefficients)
                    f = walsh @ coefficients
                    delta_f = walsh @ (2.0 * degrees * coefficients)
                    ratio = lp_norm(delta_f, p) / lp_norm(f, p)
                    slack = ratio - 2.0 * d
                    checked += 1
                    if slack < smallest_slack:
                        smallest_slack = slack
                        worst_case = {"n": n, "d": d, "p": p, "ratio": ratio}
                    if slack < -1e-9:
                        raise AssertionError((n, d, p, ratio, slack))

    print(
        json.dumps(
            {
                "checked": checked,
                "max_n": args.max_n,
                "trials_per_parameter_triple": args.trials,
                "smallest_slack": smallest_slack,
                "worst_case": worst_case,
            }
        )
    )


if __name__ == "__main__":
    main()

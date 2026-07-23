#!/usr/bin/env python3
"""Finite sanity check for the negative Hilbert-weight moment theorem.

Model: d=1, x=0, X_i uniform on [-1,1], beta=-1/2.
Prediction:
    E[w_0**(-1/2)] ~ (2/3) * sqrt(n * log(n)).

The checked moment has infinite variance, so Monte Carlo convergence is slow.
This script is evidence against elementary normalization mistakes, not a proof.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def estimate(n: int, repetitions: int, batch_size: int, rng: np.random.Generator) -> tuple[float, float]:
    total = 0.0
    total_sq = 0.0
    completed = 0
    while completed < repetitions:
        current = min(batch_size, repetitions - completed)
        radii = rng.uniform(np.finfo(float).tiny, 1.0, size=(current, n + 1))
        inverse_radii = 1.0 / radii
        weights_zero = inverse_radii[:, 0] / inverse_radii.sum(axis=1)
        values = weights_zero ** (-0.5)
        total += float(values.sum())
        total_sq += float(np.square(values).sum())
        completed += current

    mean = total / repetitions
    empirical_variance = max(total_sq / repetitions - mean * mean, 0.0)
    standard_error = math.sqrt(empirical_variance / repetitions)
    return mean, standard_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repetitions", type=int, default=100_000)
    parser.add_argument("--batch-size", type=int, default=1_000)
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=[64, 256, 1024, 4096],
    )
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    print("n,repetitions,estimate,naive_se,prediction,ratio")
    for n in args.sizes:
        mean, standard_error = estimate(
            n=n,
            repetitions=args.repetitions,
            batch_size=args.batch_size,
            rng=rng,
        )
        prediction = (2.0 / 3.0) * math.sqrt(n * math.log(n))
        print(
            f"{n},{args.repetitions},{mean:.8f},{standard_error:.8f},"
            f"{prediction:.8f},{mean / prediction:.8f}"
        )


if __name__ == "__main__":
    main()

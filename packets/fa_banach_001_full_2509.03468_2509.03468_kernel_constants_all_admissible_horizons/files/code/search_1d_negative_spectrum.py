#!/usr/bin/env python3
"""Search for nonpositive spectrum under irregular admissible flat horizons.

Exploratory only.  The random horizons are smooth and flat at the endpoints:
a positive trigonometric modulation is multiplied by exp(1/(x^2-1)), then
scaled so that delta(x) <= safety * dist(x, boundary) at all cell centers.
"""

from __future__ import annotations

import argparse

import numpy as np

from scan_1d_spectrum import kernel_cdf


def random_horizon(
    centers: np.ndarray,
    rng: np.random.Generator,
    modes: int,
    roughness: float,
    safety: float,
) -> np.ndarray:
    flat = np.exp(1.0 / (centers * centers - 1.0))
    phase = np.zeros_like(centers)
    for k in range(1, modes + 1):
        decay = roughness / np.sqrt(k)
        phase += decay * (
            rng.normal() * np.sin(np.pi * k * (centers + 1.0) / 2.0)
            + rng.normal() * np.cos(np.pi * k * (centers + 1.0) / 2.0)
        )
    raw = flat * np.exp(np.clip(phase, -12.0, 12.0))
    distance = 1.0 - np.abs(centers)
    scale = safety * np.min(distance / raw)
    return scale * raw


def averaging_matrix(
    centers: np.ndarray, edges: np.ndarray, horizons: np.ndarray, s: float
) -> np.ndarray:
    left = (edges[:-1][None, :] - centers[:, None]) / horizons[:, None]
    right = (edges[1:][None, :] - centers[:, None]) / horizons[:, None]
    return kernel_cdf(right, s) - kernel_cdf(left, s)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=90)
    parser.add_argument("--draws", type=int, default=1000)
    parser.add_argument("--modes", type=int, default=12)
    parser.add_argument("--roughness", type=float, default=1.4)
    parser.add_argument("--safety", type=float, default=0.98)
    parser.add_argument("--seed", type=int, default=250903468)
    parser.add_argument("--s-values", type=float, nargs="+", default=[0.1, 0.5, 0.9])
    args = parser.parse_args()

    edges = np.linspace(-1.0, 1.0, args.n + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    rng = np.random.default_rng(args.seed)

    global_best = np.inf
    best_record: tuple[int, float, float, float, float] | None = None
    for draw in range(args.draws):
        horizons = random_horizon(
            centers, rng, args.modes, args.roughness, args.safety
        )
        for s in args.s_values:
            matrix = averaging_matrix(centers, edges, horizons, s)
            eigenvalues = np.linalg.eigvals(matrix)
            min_real = float(eigenvalues.real.min())
            min_abs = float(np.min(np.abs(eigenvalues)))
            max_imag = float(np.max(np.abs(eigenvalues.imag)))
            if min_real < global_best:
                global_best = min_real
                best_record = (
                    draw,
                    s,
                    min_real,
                    min_abs,
                    max_imag,
                )
                print(
                    "best",
                    f"draw={draw}",
                    f"s={s}",
                    f"min_real={min_real:.9g}",
                    f"min_abs={min_abs:.9g}",
                    f"max_imag={max_imag:.9g}",
                    f"delta_min={horizons.min():.9g}",
                    f"delta_max={horizons.max():.9g}",
                )
            if min_real <= 0.0 or min_abs < 1e-7:
                np.savez(
                    "candidate_nonpositive_spectrum.npz",
                    centers=centers,
                    edges=edges,
                    horizons=horizons,
                    matrix=matrix,
                    eigenvalues=eigenvalues,
                    s=s,
                    draw=draw,
                )
                print("candidate saved")
                return

    print("no nonpositive candidate", best_record)


if __name__ == "__main__":
    main()

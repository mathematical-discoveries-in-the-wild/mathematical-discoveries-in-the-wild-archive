#!/usr/bin/env python3
"""Exploratory Nyström scan for a variable-bandwidth averaging operator.

This is not a proof.  It uses the normalized one-dimensional kernel

    Q_s(t) = (1-s)/(2s) * (|t|^{-s} - 1),  0 < |t| < 1,

whose Fourier transform is positive for the homogeneous averaging problem.
Cell integrals are evaluated analytically, including the integrable
singularity at t=0.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def flat_horizon(x: np.ndarray, amplitude: float) -> np.ndarray:
    """A exp(1/(x^2-1)), extended flatly by zero at +/-1."""
    return amplitude * np.exp(1.0 / (x * x - 1.0))


def kernel_cdf(t: np.ndarray, s: float) -> np.ndarray:
    """Integral of Q_s from 0 to t, clipped to the support [-1,1]."""
    clipped = np.clip(t, -1.0, 1.0)
    magnitude = np.abs(clipped)
    coefficient = (1.0 - s) / (2.0 * s)
    primitive = coefficient * (
        magnitude ** (1.0 - s) / (1.0 - s) - magnitude
    )
    return np.sign(clipped) * primitive


def averaging_matrix(n: int, amplitude: float, s: float) -> tuple[np.ndarray, np.ndarray]:
    edges = np.linspace(-1.0, 1.0, n + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    horizons = flat_horizon(centers, amplitude)

    left = (edges[:-1][None, :] - centers[:, None]) / horizons[:, None]
    right = (edges[1:][None, :] - centers[:, None]) / horizons[:, None]
    matrix = kernel_cdf(right, s) - kernel_cdf(left, s)
    return matrix, horizons


def scan(n: int, s: float, amplitudes: np.ndarray) -> None:
    print(
        "amplitude delta_max row_error min_singular "
        "min_real_eig max_imag_eig negative_real_eigs"
    )
    for amplitude in amplitudes:
        matrix, horizons = averaging_matrix(n, float(amplitude), s)
        singular_values = np.linalg.svd(matrix, compute_uv=False)
        eigenvalues = np.linalg.eigvals(matrix)
        print(
            f"{amplitude:.9g} "
            f"{horizons.max():.9g} "
            f"{np.max(np.abs(matrix.sum(axis=1) - 1.0)):.3e} "
            f"{singular_values[-1]:.9g} "
            f"{eigenvalues.real.min():.9g} "
            f"{np.max(np.abs(eigenvalues.imag)):.3e} "
            f"{np.count_nonzero(eigenvalues.real < -1e-10)}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=240)
    parser.add_argument("--s", type=float, default=0.5)
    parser.add_argument("--count", type=int, default=32)
    parser.add_argument("--min-amplitude", type=float, default=0.05)
    parser.add_argument("--max-amplitude", type=float, default=math.e)
    args = parser.parse_args()
    amplitudes = np.geomspace(
        args.min_amplitude, args.max_amplitude, args.count
    )
    scan(args.n, args.s, amplitudes)


if __name__ == "__main__":
    main()

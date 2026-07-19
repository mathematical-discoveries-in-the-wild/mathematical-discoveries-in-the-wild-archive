"""Numerical probe for polynomially weighted Poisson shifts on ell^p."""

from __future__ import annotations

import numpy as np
from scipy.signal import correlate, convolve
from scipy.stats import poisson


def apply_k(x: np.ndarray, kernel: np.ndarray, weight: np.ndarray) -> np.ndarray:
    corr = correlate(weight * x, kernel, mode="full", method="fft")
    start = len(kernel) - 1
    return corr[start : start + len(x)] / weight


def apply_kt(x: np.ndarray, kernel: np.ndarray, weight: np.ndarray) -> np.ndarray:
    return weight * convolve(x / weight, kernel, mode="full", method="fft")[: len(x)]


def induced_p_norm(radius: int, p: float, beta: float) -> float:
    length = 8 * radius + 512
    cutoff = int(radius + 10 * np.sqrt(radius) + 30)
    indices = np.arange(length, dtype=float)
    kernel = poisson.pmf(np.arange(cutoff + 1), radius)
    weight = (indices + 1.0) ** beta

    rng = np.random.default_rng(230214135)
    x = rng.random(length)
    x /= np.linalg.norm(x, ord=p)
    q = p / (p - 1.0)
    value = 0.0
    for _ in range(120):
        y = np.maximum(apply_k(x, kernel, weight), 0.0)
        value = np.linalg.norm(y, ord=p)
        dual = (y / value) ** (p - 1.0)
        gradient = np.maximum(apply_kt(dual, kernel, weight), 0.0)
        gradient_norm = np.linalg.norm(gradient, ord=q)
        x_next = (gradient / gradient_norm) ** (q - 1.0)
        if np.linalg.norm(x_next - x, ord=p) < 1e-10:
            x = x_next
            break
        x = x_next
    return value


def main() -> None:
    for p in (1.5, 2.0, 4.0):
        for beta in (0.05, 0.1, 0.2):
            values = []
            for radius in (20, 80, 320, 1280):
                values.append(induced_p_norm(radius, p, beta))
            rendered = " ".join(f"{value:.5f}" for value in values)
            print(f"p={p:.1f} beta={beta:.2f}: {rendered}")


if __name__ == "__main__":
    main()

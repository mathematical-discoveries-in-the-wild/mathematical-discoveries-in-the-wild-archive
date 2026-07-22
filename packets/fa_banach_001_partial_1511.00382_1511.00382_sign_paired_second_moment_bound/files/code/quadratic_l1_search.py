#!/usr/bin/env python3
"""Monte Carlo search for large L1 norms of centered Gaussian quadratic forms."""

from __future__ import annotations

import numpy as np


def search(n: int, samples: int, restarts: int, iterations: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    y = rng.standard_normal((samples, n)) ** 2 - 1.0
    candidates: list[tuple[float, np.ndarray]] = []

    starts = [
        np.ones(n) / np.sqrt(n),
        np.eye(1, n, 0).ravel(),
    ]
    starts.extend(rng.standard_normal(n) for _ in range(restarts))

    for start in starts:
        u = start / np.linalg.norm(start)
        for _ in range(iterations):
            values = y @ u
            gradient = np.mean(y * np.sign(values)[:, None], axis=0)
            if np.linalg.norm(gradient) == 0:
                break
            u = gradient / np.linalg.norm(gradient)
        objective = float(np.mean(np.abs(y @ u)))
        candidates.append((objective, u.copy()))

    candidates.sort(key=lambda item: item[0], reverse=True)
    value, vector = candidates[0]
    print(
        f"n={n:2d} best={value:.8f} target={2 / np.sqrt(np.pi):.8f} "
        f"weights={np.round(vector, 4)}"
    )


def main() -> None:
    for n in (1, 2, 3, 4, 5, 8, 12, 20):
        search(n=n, samples=250_000, restarts=12, iterations=30, seed=1729 + n)


if __name__ == "__main__":
    main()

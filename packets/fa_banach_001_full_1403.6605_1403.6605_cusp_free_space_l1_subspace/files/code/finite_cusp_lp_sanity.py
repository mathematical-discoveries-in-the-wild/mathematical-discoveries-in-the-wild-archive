"""Finite-metric sanity checks for the cusp packet.

This script is not used in the proof. It checks that the obvious normalized
vertical molecules in finite cusp samples behave like an ell_1 basis, so the
proof does not rely on a hidden finite-dimensional obstruction.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import linprog


def free_norm(points: list[tuple[float, float]], coeffs: np.ndarray) -> float:
    pairs: list[tuple[int, int]] = []
    costs: list[float] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])
            pairs.append((i, j))
            costs.extend([d, d])

    incidence = np.zeros((len(points), 2 * len(pairs)))
    for k, (i, j) in enumerate(pairs):
        incidence[i, 2 * k] += 1
        incidence[j, 2 * k] -= 1
        incidence[i, 2 * k + 1] -= 1
        incidence[j, 2 * k + 1] += 1

    result = linprog(costs, A_eq=incidence, b_eq=coeffs, bounds=(0, None), method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.fun)


def main() -> None:
    for n in [3, 4, 5, 6]:
        ts = [2.0 ** (-i) for i in range(2, n + 2)]
        points = [(0.0, 0.0)]
        lower: list[int] = []
        upper: list[int] = []
        for t in ts:
            lower.append(len(points))
            points.append((t, 0.0))
            upper.append(len(points))
            points.append((t, t * t))

        values: list[float] = []
        for signs in itertools.product([-1, 1], repeat=n):
            coeffs = np.zeros(len(points))
            for sign, i, j, t in zip(signs, lower, upper, ts):
                coeffs[j] += sign / (t * t)
                coeffs[i] -= sign / (t * t)
            values.append(free_norm(points, coeffs))

        print(f"n={n} min={min(values):.6g} max={max(values):.6g} expected={n}")


if __name__ == "__main__":
    main()

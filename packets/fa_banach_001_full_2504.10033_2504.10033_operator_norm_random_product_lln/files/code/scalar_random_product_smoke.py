"""Finite-dimensional sanity check for the random product LLN.

This is not a proof.  It uses two noncommuting nilpotent 2x2 matrices A and B
with equal probability.  Since A^2 = B^2 = 0, exp(hA)=I+hA and exp(hB)=I+hB.
The theorem predicts convergence to exp(t(A+B)/2).
"""

from __future__ import annotations

import math
import random

Matrix = tuple[tuple[float, float], tuple[float, float]]

I: Matrix = ((1.0, 0.0), (0.0, 1.0))
A: Matrix = ((0.0, 1.0), (0.0, 0.0))
B: Matrix = ((0.0, 0.0), (1.0, 0.0))


def matmul(x: Matrix, y: Matrix) -> Matrix:
    return (
        (
            x[0][0] * y[0][0] + x[0][1] * y[1][0],
            x[0][0] * y[0][1] + x[0][1] * y[1][1],
        ),
        (
            x[1][0] * y[0][0] + x[1][1] * y[1][0],
            x[1][0] * y[0][1] + x[1][1] * y[1][1],
        ),
    )


def factor(base: Matrix, h: float) -> Matrix:
    return (
        (1.0 + h * base[0][0], h * base[0][1]),
        (h * base[1][0], 1.0 + h * base[1][1]),
    )


def target(t: float) -> Matrix:
    c = math.cosh(t / 2.0)
    s = math.sinh(t / 2.0)
    return ((c, s), (s, c))


def frob_norm(x: Matrix) -> float:
    return math.sqrt(sum(x[r][c] * x[r][c] for r in range(2) for c in range(2)))


def subtract(x: Matrix, y: Matrix) -> Matrix:
    return tuple(
        tuple(x[r][c] - y[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def trial(n: int, t: float = 1.0) -> float:
    product = I
    h = t / n
    for _ in range(n):
        base = A if random.random() < 0.5 else B
        product = matmul(product, factor(base, h))
    return frob_norm(subtract(product, target(t)))


if __name__ == "__main__":
    random.seed(250410033)
    for n in [100, 300, 1000, 3000, 10000]:
        errs = [trial(n) for _ in range(100)]
        print(n, sum(errs) / len(errs), max(errs))

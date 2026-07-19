"""Numerical sanity checks for the C[0,1] BPBp-RSE packet.

These checks are not part of the proof. They verify, on random finite
dimensional samples, the two elementary operator-norm bounds used in the
packet:

1. Real case: if u,v are unit vectors, then
   ||a (u+v)/2 + b (u-v)/2|| <= 1 for |a|,|b| <= 1.
2. Complex case: the norm of (a,b) -> a y0 + b y on l_infty^2 is attained
   on the distinguished boundary |a|=|b|=1.
"""

from __future__ import annotations

import math
import random


def norm2(vec: list[complex]) -> float:
    return math.sqrt(sum(abs(z) ** 2 for z in vec))


def scale(vec: list[complex], scalar: complex) -> list[complex]:
    return [scalar * z for z in vec]


def add(x: list[complex], y: list[complex]) -> list[complex]:
    return [a + b for a, b in zip(x, y)]


def random_real_unit(dim: int) -> list[complex]:
    values = [random.gauss(0, 1) for _ in range(dim)]
    nrm = math.sqrt(sum(t * t for t in values))
    return [t / nrm for t in values]


def random_complex_unit(dim: int) -> list[complex]:
    values = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(dim)]
    nrm = norm2(values)
    return [t / nrm for t in values]


def check_real(samples: int = 1000) -> float:
    worst = 0.0
    for _ in range(samples):
        u = random_real_unit(5)
        v = random_real_unit(5)
        a = random.uniform(-1, 1)
        b = random.uniform(-1, 1)
        image = add(scale(add(u, v), a / 2), scale(add(u, scale(v, -1)), b / 2))
        worst = max(worst, norm2(image))
    return worst


def check_complex(samples: int = 200) -> float:
    worst_gap = 0.0
    for _ in range(samples):
        y0 = random_complex_unit(3)
        y = scale(random_complex_unit(3), random.random())
        inner = sum(a.conjugate() * b for a, b in zip(y0, y))
        exact_boundary_norm = math.sqrt(norm2(y0) ** 2 + norm2(y) ** 2 + 2 * abs(inner))

        interior_best = 0.0
        for _ in range(300):
            s = 2 * math.pi * random.random()
            t = 2 * math.pi * random.random()
            a = random.random() * complex(math.cos(s), math.sin(s))
            b = random.random() * complex(math.cos(t), math.sin(t))
            interior_best = max(interior_best, norm2(add(scale(y0, a), scale(y, b))))
        worst_gap = max(worst_gap, interior_best - exact_boundary_norm)
    return worst_gap


if __name__ == "__main__":
    random.seed(251210442)
    real_worst = check_real()
    complex_gap = check_complex()
    print(f"real sampled operator norm upper bound: {real_worst:.6f} <= 1")
    print(f"complex sampled interior-minus-boundary gap: {complex_gap:.6e} <= 0")

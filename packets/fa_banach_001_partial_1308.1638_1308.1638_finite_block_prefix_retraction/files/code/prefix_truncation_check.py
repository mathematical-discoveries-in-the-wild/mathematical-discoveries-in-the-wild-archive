"""Numerical stress check for the prefix truncation used in the packet.

This is not a proof.  It only samples the scalar finite-dimensional model and
prints the largest observed ratio d(Tx,Ty) / d(x,y)^(1/q).
"""

from __future__ import annotations

import math
import random


def norm(vec: list[float], q: float) -> float:
    return sum(abs(x) ** q for x in vec) ** (1.0 / q)


def prefix_truncate(vec: list[float], q: float) -> list[float]:
    if norm(vec, q) <= 1:
        return vec[:]
    out = [0.0] * len(vec)
    mass = 0.0
    for index, value in enumerate(vec):
        block = abs(value) ** q
        if mass + block < 1:
            out[index] = value
            mass += block
            continue
        remaining = max(0.0, 1.0 - mass)
        out[index] = math.copysign(remaining ** (1.0 / q), value)
        break
    return out


def main() -> None:
    random.seed(13081638)
    for q in [1.0, 1.5, 2.0, 3.0, 10.0]:
        worst = 0.0
        for _ in range(50_000):
            x = [random.gauss(0, 2) for _ in range(6)]
            y = [value + random.gauss(0, 0.05) for value in x]
            distance = norm([a - b for a, b in zip(x, y)], q)
            if distance == 0:
                continue
            tx = prefix_truncate(x, q)
            ty = prefix_truncate(y, q)
            image_distance = norm([a - b for a, b in zip(tx, ty)], q)
            worst = max(worst, image_distance / (distance ** (1.0 / q)))
        print(f"q={q:g} worst sampled ratio={worst:.4f}")


if __name__ == "__main__":
    main()

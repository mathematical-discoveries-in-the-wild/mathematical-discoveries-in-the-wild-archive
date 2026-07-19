"""Finite sanity check for the Laplace partition lemma.

The proof in the packet is analytic.  This script only checks small random
partitions of one aggregate law into independent nonnegative summands.
"""

from __future__ import annotations

import math
import random
from collections import defaultdict


RNG = random.Random(190711588)
ATOMS = [(1.0, 0.35), (3.0, 0.25), (10.0, 0.20), (50.0, 0.15)]
GROUPS = 8
ALPHA = 0.63
LAPLACE_C = 1.0 - math.exp(-1.0)


def random_split(mass: float, groups: int) -> list[float]:
    raw = [RNG.expovariate(1.0) for _ in range(groups)]
    total = sum(raw)
    return [mass * x / total for x in raw]


def random_partition() -> list[dict[float, float]]:
    part = [defaultdict(float) for _ in range(GROUPS)]
    for atom, mass in ATOMS:
        for i, piece in enumerate(random_split(mass, GROUPS)):
            part[i][atom] += piece
    return [dict(group) for group in part]


def laplace_deficit(partition: list[dict[float, float]], t: float) -> tuple[float, float]:
    product = 1.0
    aggregate_u = 0.0
    for group in partition:
        u = sum(prob * (1.0 - math.exp(-t * atom)) for atom, prob in group.items())
        product *= 1.0 - u
        aggregate_u += u
    return 1.0 - product, aggregate_u


def convolve_moment(partition: list[dict[float, float]], alpha: float) -> float:
    law = {0.0: 1.0}
    for group in partition:
        group_law = {0.0: 1.0 - sum(group.values())}
        for atom, prob in group.items():
            group_law[atom] = group_law.get(atom, 0.0) + prob

        new_law: dict[float, float] = defaultdict(float)
        for x, px in law.items():
            for y, py in group_law.items():
                new_law[x + y] += px * py
        law = dict(new_law)
    return sum((x**alpha) * prob for x, prob in law.items())


def main() -> None:
    worst_laplace_violation = 0.0
    worst_ratio = 1.0
    moment_values = []

    for _ in range(200):
        partition = random_partition()
        moment_values.append(convolve_moment(partition, ALPHA))

        for exponent in range(-4, 5):
            t = 10.0**exponent
            deficit, aggregate_u = laplace_deficit(partition, t)
            upper = min(1.0, aggregate_u)
            lower = LAPLACE_C * upper
            if deficit > upper:
                worst_laplace_violation = max(worst_laplace_violation, deficit - upper)
            if deficit < lower:
                worst_laplace_violation = max(worst_laplace_violation, lower - deficit)

    for x in moment_values:
        for y in moment_values:
            worst_ratio = max(worst_ratio, x / y)

    print(f"alpha={ALPHA}")
    print(f"random partitions checked={len(moment_values)}")
    print(f"worst Laplace bound violation={worst_laplace_violation:.3e}")
    print(f"largest observed moment ratio={worst_ratio:.6f}")
    print(f"proof upper ratio={(1.0 / LAPLACE_C):.6f}")


if __name__ == "__main__":
    main()

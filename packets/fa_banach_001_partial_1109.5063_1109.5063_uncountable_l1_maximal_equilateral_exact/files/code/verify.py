#!/usr/bin/env python3
"""Exact algebra and finite-instance checks for the four-point cut argument."""

from fractions import Fraction
from itertools import combinations, permutations
import random

import sympy as sp


def symbolic_cut_check() -> None:
    s1, s2, s3, s4, q12, q13, q14 = sp.symbols(
        "s1 s2 s3 s4 q12 q13 q14", nonnegative=True
    )
    distances = {
        "12": s1 + s2 + q13 + q14,
        "34": s3 + s4 + q13 + q14,
        "13": s1 + s3 + q12 + q14,
        "24": s2 + s4 + q12 + q14,
        "14": s1 + s4 + q12 + q13,
        "23": s2 + s3 + q12 + q13,
    }
    base = distances["12"]
    equations = [sp.expand(value - base) for value in distances.values()]
    solution = sp.linsolve(
        equations, (s1, s2, s3, s4, q12, q13, q14)
    )
    expected = sp.FiniteSet((s4, s4, s4, s4, q14, q14, q14))
    assert solution == expected, (solution, expected)

    s, q = sp.symbols("s q", nonnegative=True)
    side = 2 * s + 2 * q
    radius = s + sp.Rational(3, 2) * q
    deficit = sp.simplify(side - radius)
    assert deficit == s + q / 2
    print("symbolic solution:", solution)
    print("side length:", side)
    print("middle-midpoint radius:", radius)
    print("extension-coordinate size:", deficit)


def l1_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def symmetrized_random_checks(seed: int = 11095063, blocks: int = 12) -> None:
    """Build exact rational examples with all three gaps compressed per coordinate."""
    rng = random.Random(seed)
    points = [[] for _ in range(4)]
    centers = []

    for _ in range(blocks):
        lower_gap = Fraction(rng.randint(1, 17), rng.randint(1, 13))
        middle_gap = Fraction(rng.randint(1, 17), rng.randint(1, 13))
        upper_gap = Fraction(rng.randint(1, 17), rng.randint(1, 13))
        ordered_values = (
            Fraction(0),
            lower_gap,
            lower_gap + middle_gap,
            lower_gap + middle_gap + upper_gap,
        )
        center = (ordered_values[1] + ordered_values[2]) / 2
        for order in permutations(range(4)):
            coordinate = [Fraction(0)] * 4
            for position, label in enumerate(order):
                coordinate[label] = ordered_values[position]
            for label in range(4):
                points[label].append(coordinate[label])
            centers.append(center)

    pair_distances = {
        l1_distance(points[i], points[j]) for i, j in combinations(range(4), 2)
    }
    assert len(pair_distances) == 1
    side = pair_distances.pop()
    radii = {l1_distance(point, centers) for point in points}
    assert len(radii) == 1
    radius = radii.pop()
    assert radius < side

    extension = centers + [side - radius]
    extended_points = [point + [Fraction(0)] for point in points]
    assert {l1_distance(extension, point) for point in extended_points} == {side}
    print(f"random symmetrized coordinates: {len(centers)}")
    print("exact common side:", side)
    print("exact center radius:", radius)
    print("exact added coordinate:", side - radius)


def five_point_check() -> None:
    points = [
        (1, 1, 1, 0),
        (1, -1, -1, 0),
        (-1, 1, -1, 0),
        (-1, -1, 1, 0),
        (0, 0, 0, 1),
    ]
    distances = {
        l1_distance(points[i], points[j]) for i, j in combinations(range(5), 2)
    }
    assert distances == {4}
    print("explicit five-point pairwise distances:", distances)


if __name__ == "__main__":
    symbolic_cut_check()
    symmetrized_random_checks()
    five_point_check()
    print("PASS")

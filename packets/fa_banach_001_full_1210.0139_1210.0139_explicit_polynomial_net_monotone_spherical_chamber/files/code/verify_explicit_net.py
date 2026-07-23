#!/usr/bin/env python3
"""Sanity checks for the explicit weighted-isotonic chamber net."""

from __future__ import annotations

import argparse
import math
import random


def geometric_blocks(m: int, eta: float) -> list[tuple[int, int]]:
    """Return half-open blocks implementing the proof's one-based partition."""
    out: list[tuple[int, int]] = []
    a = 1
    while a <= m:
        length = 1 if a < 2.0 / eta else max(1, math.floor(eta * a))
        b = min(m + 1, a + length)
        out.append((a - 1, b - 1))
        a = b
    return out


def norm(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values))


def normalize(values: list[float]) -> list[float]:
    size = norm(values)
    assert size > 0.0
    return [value / size for value in values]


def distance(x: list[float], y: list[float]) -> float:
    return norm([a - b for a, b in zip(x, y)])


def block_projection(
    x: list[float], partition: list[tuple[int, int]]
) -> list[float]:
    result = [0.0] * len(x)
    for a, b in partition:
        average = sum(x[a:b]) / (b - a)
        result[a:b] = [average] * (b - a)
    return result


def block_coordinates(
    x: list[float], partition: list[tuple[int, int]]
) -> list[float]:
    return [math.sqrt(b - a) * x[a] for a, b in partition]


def expand_coordinates(
    z: list[float], partition: list[tuple[int, int]], m: int
) -> list[float]:
    result = [0.0] * m
    for coordinate, (a, b) in zip(z, partition):
        result[a:b] = [coordinate / math.sqrt(b - a)] * (b - a)
    return result


def weighted_decreasing_nonnegative_projection(
    z: list[float], weights: list[int]
) -> list[float]:
    """Project z onto {z_j/sqrt(w_j) decreasing and nonnegative}."""
    blocks: list[list[float | int]] = []
    for j, (coordinate, weight) in enumerate(zip(z, weights)):
        observation = coordinate / math.sqrt(weight)
        blocks.append([j, j + 1, float(weight), float(weight) * observation])
        while len(blocks) >= 2:
            previous = blocks[-2][3] / blocks[-2][2]
            current = blocks[-1][3] / blocks[-1][2]
            if previous + 1e-15 >= current:
                break
            right = blocks.pop()
            left = blocks.pop()
            blocks.append(
                [
                    left[0],
                    right[1],
                    left[2] + right[2],
                    left[3] + right[3],
                ]
            )

    fitted_heights = [0.0] * len(z)
    for start, end, weight_sum, weighted_sum in blocks:
        fitted = max(0.0, weighted_sum / weight_sum)
        for j in range(int(start), int(end)):
            fitted_heights[j] = fitted
    return [math.sqrt(weight) * height for weight, height in zip(weights, fitted_heights)]


def explicit_center(
    x: list[float], epsilon: float, partition: list[tuple[int, int]]
) -> tuple[list[float], float, float]:
    projected = block_projection(x, partition)
    u = normalize(projected)
    z = block_coordinates(u, partition)
    d = len(z)
    q = math.ceil(8.0 * math.sqrt(d) / epsilon)
    lattice_point = [round(q * coordinate) for coordinate in z]
    weights = [b - a for a, b in partition]
    cone_point = weighted_decreasing_nonnegative_projection(lattice_point, weights)
    center_coordinates = normalize(cone_point)
    center = expand_coordinates(center_coordinates, partition, len(x))
    return center, distance(x, u), distance(u, center)


def random_decreasing_unit(m: int, rng: random.Random) -> list[float]:
    return normalize(sorted((rng.expovariate(1.0) for _ in range(m)), reverse=True))


def run_checks(m: int, epsilon: float, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    eta = epsilon * epsilon / 8.0
    partition = geometric_blocks(m, eta)
    tests = [random_decreasing_unit(m, rng) for _ in range(trials)]
    tests.extend(
        [
            normalize([1.0 / math.sqrt(i + 1.0) for i in range(m)]),
            normalize([1.0 if i < max(1, m // 11) else 0.0 for i in range(m)]),
            normalize([math.exp(-i / max(1.0, m / 13.0)) for i in range(m)]),
        ]
    )

    worst_compression = 0.0
    worst_lattice = 0.0
    worst_total = 0.0
    for x in tests:
        center, compression_error, lattice_error = explicit_center(x, epsilon, partition)
        total_error = distance(x, center)
        assert abs(norm(center) - 1.0) <= 1e-10
        assert min(center) >= -1e-12
        assert all(center[i] + 1e-12 >= center[i + 1] for i in range(m - 1))
        assert compression_error <= epsilon / 2.0 + 1e-10
        assert lattice_error <= epsilon / 8.0 + 1e-10
        assert total_error <= 5.0 * epsilon / 8.0 + 1e-10
        worst_compression = max(worst_compression, compression_error)
        worst_lattice = max(worst_lattice, lattice_error)
        worst_total = max(worst_total, total_error)

    d = len(partition)
    q = math.ceil(8.0 * math.sqrt(d) / epsilon)
    print(
        f"explicit net: M={m}, epsilon={epsilon}, blocks={d}, Q={q}, "
        f"tests={len(tests)}, worst compression={worst_compression:.8g}, "
        f"worst lattice={worst_lattice:.8g}, worst total={worst_total:.8g}, "
        f"theory total={5.0 * epsilon / 8.0:.8g}"
    )
    print("all explicit-net checks passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, default=4096)
    parser.add_argument("--epsilon", type=float, default=0.2)
    parser.add_argument("--trials", type=int, default=300)
    parser.add_argument("--seed", type=int, default=12100139)
    args = parser.parse_args()
    assert args.dimension >= 2
    assert 0.0 < args.epsilon < 1.0
    run_checks(args.dimension, args.epsilon, args.trials, args.seed)


if __name__ == "__main__":
    main()

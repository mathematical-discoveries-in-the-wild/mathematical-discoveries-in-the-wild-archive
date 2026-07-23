#!/usr/bin/env python3
"""Sanity checks for the monotone-chamber entropy proof."""

from __future__ import annotations

import argparse
import itertools
import math
import random


def blocks(m: int, eta: float) -> list[tuple[int, int]]:
    """Return half-open geometric blocks [a,b), with zero-based indices."""
    out: list[tuple[int, int]] = []
    a = 1  # proof indices are one-based
    while a <= m:
        if a < 2.0 / eta:
            length = 1
        else:
            length = max(1, math.floor(eta * a))
        b = min(m + 1, a + length)
        out.append((a - 1, b - 1))
        a = b
    return out


def normalize(values: list[float]) -> list[float]:
    norm = math.sqrt(sum(v * v for v in values))
    return [v / norm for v in values]


def projection(values: list[float], partition: list[tuple[int, int]]) -> list[float]:
    out = [0.0] * len(values)
    for a, b in partition:
        mean = sum(values[a:b]) / (b - a)
        out[a:b] = [mean] * (b - a)
    return out


def right_endpoint_step(values: list[float], partition: list[tuple[int, int]]) -> list[float]:
    out = [0.0] * len(values)
    for a, b in partition:
        out[a:b] = [values[b - 1]] * (b - a)
    return out


def squared_distance(x: list[float], y: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(x, y))


def random_decreasing_unit(m: int, rng: random.Random) -> list[float]:
    raw = sorted((rng.expovariate(1.0) for _ in range(m)), reverse=True)
    return normalize(raw)


def check_compression(m: int, epsilon: float, trials: int, rng: random.Random) -> None:
    eta = epsilon * epsilon / 8.0
    partition = blocks(m, eta)
    dimension_bound = 4.0 / eta * (1.0 + math.log(m))
    assert len(partition) <= dimension_bound + 1e-12

    tests = [random_decreasing_unit(m, rng) for _ in range(trials)]
    tests.extend(
        [
            normalize([1.0 / math.sqrt(i + 1.0) for i in range(m)]),
            normalize([1.0 if i < max(1, m // 7) else 0.0 for i in range(m)]),
            normalize([math.exp(-i / max(1.0, m / 10.0)) for i in range(m)]),
        ]
    )
    worst_step = 0.0
    worst_projection = 0.0
    worst_normalized = 0.0
    for x in tests:
        q = right_endpoint_step(x, partition)
        px = projection(x, partition)
        step_error = squared_distance(x, q)
        projection_error = squared_distance(x, px)
        assert step_error <= eta + 1e-10
        assert projection_error <= step_error + 1e-10
        assert all(px[i] + 1e-14 >= px[i + 1] for i in range(m - 1))
        u = normalize(px)
        normalized_error = squared_distance(x, u)
        assert normalized_error <= 2.0 * eta + 1e-10
        worst_step = max(worst_step, step_error)
        worst_projection = max(worst_projection, projection_error)
        worst_normalized = max(worst_normalized, normalized_error)

    print(
        f"compression: M={m}, epsilon={epsilon}, blocks={len(partition)}, "
        f"bound={dimension_bound:.2f}, worst step={worst_step:.6g}, "
        f"worst projection={worst_projection:.6g}, "
        f"worst normalized={worst_normalized:.6g}"
    )


def balanced_words(d: int) -> list[tuple[int, ...]]:
    words = []
    for plus_positions in itertools.combinations(range(d), d // 2):
        plus = set(plus_positions)
        words.append(tuple(1 if j in plus else -1 for j in range(d)))
    return words


def hamming(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x != y for x, y in zip(a, b))


def greedy_code(d: int) -> list[tuple[int, ...]]:
    remaining = balanced_words(d)
    code = []
    while remaining:
        word = remaining.pop()
        code.append(word)
        remaining = [other for other in remaining if hamming(word, other) >= d / 4.0]
    return code


def packing_vector(word: tuple[int, ...]) -> list[tuple[int, float]]:
    d = len(word)
    vector: list[tuple[int, float]] = []
    for j, sign in enumerate(word):
        size = 16 ** (d - j - 1)
        height = (1.0 + sign / 2.0) / math.sqrt(1.25 * d * size)
        vector.append((size, height))
    return vector


def chordal(x: list[tuple[int, float]], y: list[tuple[int, float]]) -> float:
    assert all(size == other_size for (size, _), (other_size, _) in zip(x, y))
    inner = sum(size * a * b for (size, a), (_, b) in zip(x, y))
    return math.sqrt(max(0.0, 1.0 - inner * inner))


def check_packing(d: int) -> None:
    code = greedy_code(d)
    vectors = [packing_vector(word) for word in code]
    for vector in vectors:
        assert abs(sum(size * height * height for size, height in vector) - 1.0) <= 1e-10
        assert all(vector[i][1] <= vector[i + 1][1] + 1e-14 for i in range(len(vector) - 1))
    minimum = 1.0
    for i, x in enumerate(vectors):
        for y in vectors[i + 1 :]:
            minimum = min(minimum, chordal(x, y))
    assert minimum + 1e-10 >= math.sqrt(19.0) / 10.0
    print(
        f"packing: d={d}, ambient={(16**d - 1)//15}, "
        f"codewords={len(code)}, min chordal={minimum:.12g}, "
        f"theory={math.sqrt(19.0)/10.0:.12g}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, default=4096)
    parser.add_argument("--epsilon", type=float, default=0.2)
    parser.add_argument("--trials", type=int, default=200)
    parser.add_argument("--packing-blocks", type=int, default=8)
    parser.add_argument("--seed", type=int, default=12100139)
    args = parser.parse_args()
    assert 0.0 < args.epsilon < 1.0
    assert args.packing_blocks >= 4 and args.packing_blocks % 2 == 0
    rng = random.Random(args.seed)
    check_compression(args.dimension, args.epsilon, args.trials, rng)
    check_packing(args.packing_blocks)
    print("all checks passed")


if __name__ == "__main__":
    main()

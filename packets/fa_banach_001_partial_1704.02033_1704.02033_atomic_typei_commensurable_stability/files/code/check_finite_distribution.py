#!/usr/bin/env python3
"""Finite sanity checks for the integer-amplification trace identity."""


CASES = [
    ([(3.0, 1.0)], [1]),
    ([(4.0, 2.0), (3.0,)], [2, 1]),
    ([(5.0, 5.0, 0.5), (7.0, 1.0)], [3, 2]),
    ([(1.0,), (), (2.0, 1.5)], [4, 7, 2]),
    ([(0.0, 0.0), (9.0,)], [2, 5]),
    ([(10.0, 3.0, 2.0), (8.0, 8.0), (1.0,)], [1, 3, 4]),
]


def main() -> None:
    thresholds = [-1.0, 0.0, 0.75, 1.0, 1.75, 2.5, 4.5, 8.0, 11.0]
    for blocks, weights in CASES:
        amplified = sorted(
            (value for block, weight in zip(blocks, weights) for value in block for _ in range(weight)),
            reverse=True,
        )
        for threshold in thresholds:
            weighted_count = sum(
                weight * sum(value > threshold for value in block)
                for block, weight in zip(blocks, weights)
            )
            ordinary_count = sum(value > threshold for value in amplified)
            assert weighted_count == ordinary_count
    print(f"PASS: {len(CASES)} cases, {len(thresholds)} thresholds each")


if __name__ == "__main__":
    main()


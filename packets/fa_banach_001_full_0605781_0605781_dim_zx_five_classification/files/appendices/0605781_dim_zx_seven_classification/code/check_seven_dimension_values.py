#!/usr/bin/env python3
"""Sanity check for the seven-dimensional dim Z(X) packet.

This script enumerates the Euclidean-block values
sum_j k_j(k_j-1)/2 over partitions of 7 and lists the missing values up to
Rosenthal's threshold 15. It does not prove the compact Lie algebra exclusions.
"""

from __future__ import annotations


def partitions(n: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    if max_part is None:
        max_part = n
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for k in range(min(n, max_part), 0, -1):
        for tail in partitions(n - k, k):
            out.append((k,) + tail)
    return out


def block_value(partition: tuple[int, ...]) -> int:
    return sum(k * (k - 1) // 2 for k in partition)


def main() -> None:
    n = 7
    values = sorted({block_value(p) for p in partitions(n)})
    threshold = (n - 1) * (n - 2) // 2
    missing = [m for m in range(threshold + 1) if m not in values]
    expected_values = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15, 21]
    expected_missing = [8, 12, 13, 14]
    print(f"n={n}")
    print(f"Euclidean-block values: {values}")
    print(f"Rosenthal threshold: {threshold}")
    print(f"Missing values <= threshold: {missing}")
    assert values == expected_values
    assert missing == expected_missing
    print("OK")


if __name__ == "__main__":
    main()

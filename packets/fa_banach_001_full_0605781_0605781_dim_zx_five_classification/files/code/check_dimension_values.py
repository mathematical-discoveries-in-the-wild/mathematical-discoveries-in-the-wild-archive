"""Sanity checks for the skew-hermitian Lie algebra packet.

This script records the triangular block values P(n) for the low-dimensional
checkpoints used in the packet. It is not a proof of the compact Lie algebra
or representation-theoretic exclusions.
"""

from __future__ import annotations


def so_dim(k: int) -> int:
    return k * (k - 1) // 2


def partitions(total: int, min_part: int = 1):
    if total == 0:
        yield []
        return
    for first in range(min_part, total + 1):
        for rest in partitions(total - first, first):
            yield [first, *rest]


def p_values(n: int) -> list[int]:
    return sorted({sum(so_dim(k) for k in part) for part in partitions(n)})


CONSTRUCTIONS = {
    "ell_infty^5": [],
    "H_2 +_infty ell_infty^3": [2],
    "H_2 +_infty H_2 +_infty R": [2, 2],
    "H_3 +_infty ell_infty^2": [3],
    "H_3 +_infty H_2": [3, 2],
    "H_4 +_infty R": [4],
    "H_5": [5],
}


def main() -> None:
    expected = {
        5: [0, 1, 2, 3, 4, 6, 10],
        6: [0, 1, 2, 3, 4, 6, 7, 10, 15],
        7: [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15, 21],
    }
    for n, values in expected.items():
        actual = p_values(n)
        print(f"P({n}) = {actual}")
        assert actual == values

    values = []
    for name, hilbert_blocks in CONSTRUCTIONS.items():
        value = sum(so_dim(k) for k in hilbert_blocks)
        values.append(value)
        print(f"{value:2d}  {name}")

    assert sorted(values) == [0, 1, 2, 3, 4, 6, 10]

    n = 5
    rosenthal_threshold = (n - 1) * (n - 2) // 2
    hilbert_value = n * (n - 1) // 2
    print(f"Rosenthal threshold: > {rosenthal_threshold} forces {hilbert_value}")
    assert rosenthal_threshold == 6
    assert hilbert_value == 10


if __name__ == "__main__":
    main()

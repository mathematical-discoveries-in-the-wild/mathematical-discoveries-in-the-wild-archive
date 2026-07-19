"""Sanity checks for the weighted lamplighter no-diamonds packet.

This is not a proof assistant. It checks the elementary finite sums and the
scale implication used in the written proof.
"""

from __future__ import annotations

import math


def total_edge_weight(theta: int, n: int) -> int:
    return sum((2**j) * (theta ** (n - j)) for j in range(1, n + 1))


def vertex_count(n: int) -> int:
    return 2 ** (n + 1) - 1


def diameter_bound(theta: int, n: int) -> int:
    return 2 * total_edge_weight(theta, n) + vertex_count(n)


def main() -> None:
    for theta in range(3, 16):
        for n in range(1, 30):
            lhs = diameter_bound(theta, n)
            rhs = 6 * (theta**n)
            assert lhs <= rhs, (theta, n, lhs, rhs)

    for theta in range(3, 16):
        for distortion_power in range(0, 9):
            distortion = 2**distortion_power
            max_k = math.floor(math.log2(6 * distortion * theta))
            for k in range(max_k + 1, max_k + 8):
                assert 2**k > 6 * distortion * theta

    print("checked diameter <= 6 theta^n and k-threshold inequalities")


if __name__ == "__main__":
    main()


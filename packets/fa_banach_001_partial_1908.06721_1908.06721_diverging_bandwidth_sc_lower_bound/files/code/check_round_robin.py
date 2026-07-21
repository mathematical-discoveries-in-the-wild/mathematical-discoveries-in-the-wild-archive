#!/usr/bin/env python3
"""Finite sanity check for the adaptive round-robin enumeration.

This is not a proof.  It constructs phases for the slowly diverging bandwidth
h(n) = floor(log_2(n + 1)) + 1 and checks every finite cut constraint seen in
the generated prefix.
"""

from __future__ import annotations

import math


def h(n: int) -> int:
    return math.floor(math.log2(n + 1)) + 1


def first_tail_at_least(k: int) -> int:
    n = 1
    while h(n) < k:
        n += 1
    return n


def cutpoints(number_of_phases: int) -> list[int]:
    cuts = [0, 1]
    for k in range(1, number_of_phases):
        lower = max(cuts[k] + k, first_tail_at_least(k + 1))
        remainder = (lower - cuts[k]) % k
        if remainder:
            lower += k - remainder
        cuts.append(lower)
    return cuts


def labels(cuts: list[int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for k in range(1, len(cuts) - 1):
        for n in range(cuts[k], cuts[k + 1]):
            result[n] = 1 + (n - cuts[k]) % k
    return result


def main() -> None:
    cuts = cutpoints(15)
    lab = labels(cuts)
    occurrences: dict[int, list[int]] = {}
    for n, j in sorted(lab.items()):
        occurrences.setdefault(j, []).append(n)

    checked_edges = 0
    checked_cuts = 0
    for positions in occurrences.values():
        for p, q in zip(positions, positions[1:]):
            checked_edges += 1
            for n in range(p, q):
                checked_cuts += 1
                assert q <= n + h(n), (p, q, n, h(n))

    print(f"phases={len(cuts) - 2}")
    print(f"positions={len(lab)}")
    print(f"adjacent_ray_edges={checked_edges}")
    print(f"cut_constraints={checked_cuts}")
    print("all finite cut constraints passed")


if __name__ == "__main__":
    main()

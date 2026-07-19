"""Sanity checks for the six-dimensional dim Z(X) packet.

This script does not prove the Lie-algebra exclusions. It only records:

- values realized by ell_infty-sums of Euclidean blocks;
- the values left below Rosenthal's gap threshold for n=6.
"""

from __future__ import annotations


def partitions(n: int, max_part: int | None = None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield []
        return
    for k in range(max_part, 0, -1):
        for rest in partitions(n - k, k):
            yield [k, *rest]


def tri(k: int) -> int:
    return k * (k - 1) // 2


def block_values(n: int) -> dict[int, list[int]]:
    out: dict[int, list[int]] = {}
    for part in partitions(n):
        out.setdefault(sum(tri(k) for k in part), part)
    return dict(sorted(out.items()))


def main() -> None:
    n = 6
    values = block_values(n)
    threshold = (n - 1) * (n - 2) // 2
    hilbert_value = n * (n - 1) // 2
    candidates = set(range(threshold + 1)) | {hilbert_value}
    missing = sorted(candidates - set(values))

    print(f"n={n}")
    print(f"Rosenthal threshold: {threshold}")
    print(f"Hilbert value: {hilbert_value}")
    print("Euclidean-block construction values:")
    for value, part in values.items():
        print(f"  {value:2d}: {part}")
    print(f"Values needing Lie-algebra exclusion: {missing}")

    assert sorted(values) == [0, 1, 2, 3, 4, 6, 7, 10, 15]
    assert missing == [5, 8, 9]


if __name__ == "__main__":
    main()

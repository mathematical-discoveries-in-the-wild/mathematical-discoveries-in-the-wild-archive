"""Exact small-n exploration of the property-Gamma tester question.

Partitions are restricted-growth strings.  All values of phi are stored in
the unnormalized integer scale; the common denominator is n-1.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


def partitions(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(prefix: list[int], next_label: int) -> None:
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for label in range(next_label + 1):
            prefix.append(label)
            rec(prefix, max(next_label, label + 1))
            prefix.pop()

    if n:
        rec([0], 1)
    return out


def canonical(labels: list[int]) -> tuple[int, ...]:
    rename: dict[int, int] = {}
    ans: list[int] = []
    for label in labels:
        if label not in rename:
            rename[label] = len(rename)
        ans.append(rename[label])
    return tuple(ans)


@lru_cache(maxsize=None)
def join(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    n = len(x)
    parent = list(range(n))

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    first_x: dict[int, int] = {}
    first_y: dict[int, int] = {}
    for i in range(n):
        if x[i] in first_x:
            union(i, first_x[x[i]])
        else:
            first_x[x[i]] = i
        if y[i] in first_y:
            union(i, first_y[y[i]])
        else:
            first_y[y[i]] = i
    return canonical([find(i) for i in range(n)])


def blocks(x: tuple[int, ...]) -> int:
    return 1 + max(x)


def nonsingleton_blocks(x: tuple[int, ...]) -> int:
    sizes = [0] * blocks(x)
    for label in x:
        sizes[label] += 1
    return sum(size >= 2 for size in sizes)


def phi_numerator(
    x: tuple[int, ...], y: tuple[int, ...], universe: list[tuple[int, ...]]
) -> int:
    cx, cy, cxy = blocks(x), blocks(y), blocks(join(x, y))
    best = len(x)
    for z in universe:
        first = max(0, cxy + blocks(z) - cx - cy)
        second = cx - blocks(join(x, z))
        third = cy - blocks(join(y, z))
        best = min(best, max(first, second, third))
        if best == 0:
            break
    return best


def describe(x: tuple[int, ...]) -> str:
    grouped: dict[int, list[int]] = {}
    for i, label in enumerate(x, start=1):
        grouped.setdefault(label, []).append(i)
    return "{" + ",".join("".join(map(str, value)) for value in grouped.values()) + "}"


def run(n: int, max_testers: int) -> None:
    universe = partitions(n)
    targets = [y for y in universe if nonsingleton_blocks(y) >= 2]
    print(f"n={n} Bell={len(universe)} nonsingular_targets={len(targets)}")

    table: list[list[int]] = []
    for i, x in enumerate(universe):
        table.append([phi_numerator(x, y, universe) for y in targets])
        if (i + 1) % 50 == 0:
            print(f"computed_rows={i + 1}")

    totals = [0] * len(targets)
    chosen: list[int] = []
    for step in range(1, max_testers + 1):
        best_index = -1
        best_key: tuple[float, int, int] = (-1.0, -1, -1)
        for i, row in enumerate(table):
            if i in chosen:
                continue
            new_totals = [a + b for a, b in zip(totals, row)]
            ratios = [
                value / (nonsingleton_blocks(y) - 1)
                for value, y in zip(new_totals, targets)
            ]
            key = (min(ratios), sum(value > 0 for value in new_totals), sum(new_totals))
            if key > best_key:
                best_key = key
                best_index = i
        chosen.append(best_index)
        totals = [a + b for a, b in zip(totals, table[best_index])]
        worst = min(
            range(len(targets)),
            key=lambda j: totals[j] / (nonsingleton_blocks(targets[j]) - 1),
        )
        ratio = totals[worst] / (nonsingleton_blocks(targets[worst]) - 1)
        uncovered = sum(value == 0 for value in totals)
        print(
            f"K={step} tester={describe(universe[best_index])} "
            f"min_ratio={ratio:.6g} uncovered={uncovered} "
            f"worst={describe(targets[worst])}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--max-testers", type=int, default=8)
    args = parser.parse_args()
    run(args.n, args.max_testers)

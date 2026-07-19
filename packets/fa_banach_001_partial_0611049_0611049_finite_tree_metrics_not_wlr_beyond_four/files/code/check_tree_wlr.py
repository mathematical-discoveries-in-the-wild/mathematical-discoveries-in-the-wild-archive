#!/usr/bin/env python3
"""Combinatorial checks for finite tree-metric WLR obstruction."""

from __future__ import annotations

from itertools import product


def prufer_trees(n: int):
    """Generate labeled trees on range(n) using Prüfer codes."""
    if n == 1:
        yield []
        return
    if n == 2:
        yield [(0, 1)]
        return
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in code:
            degree[v] += 1
        edges = []
        code = list(code)
        for v in code:
            leaf = min(i for i, d in enumerate(degree) if d == 1)
            edges.append((leaf, v))
            degree[leaf] -= 1
            degree[v] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.append((leaves[0], leaves[1]))
        yield edges


def rooted_orientations(n: int, edges: list[tuple[int, int]]) -> set[tuple[int, ...]]:
    """Return sign patterns of ±distance functions in edge order."""
    patterns: set[tuple[int, ...]] = set()
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    for root in range(n):
        parent = [-1] * n
        parent_edge = [-1] * n
        stack = [root]
        order = [root]
        parent[root] = root
        while stack:
            u = stack.pop()
            for v, idx in adj[u]:
                if parent[v] != -1:
                    continue
                parent[v] = u
                parent_edge[v] = idx
                stack.append(v)
                order.append(v)

        signs = [0] * len(edges)
        for v in order:
            if v == root:
                continue
            u = parent[v]
            idx = parent_edge[v]
            a, b = edges[idx]
            # For f = dist(root, .), the oriented edge increment a->b
            # is +length if a is parent of b, and -length otherwise.
            signs[idx] = 1 if (a == u and b == v) else -1
        pat = tuple(signs)
        patterns.add(pat)
        patterns.add(tuple(-s for s in pat))
    return patterns


def is_star_4(edges: list[tuple[int, int]]) -> bool:
    degree = [0] * 4
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    return sorted(degree) == [1, 1, 1, 3]


def main() -> None:
    for n in range(3, 7):
        all_patterns = 2 ** (n - 1)
        for edges in prufer_trees(n):
            distance_patterns = rooted_orientations(n, edges)
            if n >= 5:
                assert len(distance_patterns) <= 2 * n < all_patterns
            if n == 4:
                if is_star_4(edges):
                    assert len(distance_patterns) == all_patterns
                else:
                    assert len(distance_patterns) < all_patterns
    print("Tree WLR combinatorial checks passed.")


if __name__ == "__main__":
    main()

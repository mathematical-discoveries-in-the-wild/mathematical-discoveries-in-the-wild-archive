#!/usr/bin/env python3
"""Numerical sanity checks for the two exact two-ball covering radii.

The packet proof is symbolic.  This script checks its listed covering vertices,
odd cycles, and dense boundary samples.
"""

from __future__ import annotations

import math


def l2(x: tuple[float, float], y: tuple[float, float]) -> float:
    return math.hypot(x[0] - y[0], x[1] - y[1])


def linf(x: tuple[float, float], y: tuple[float, float]) -> float:
    return max(abs(x[0] - y[0]), abs(x[1] - y[1]))


def cyclic_distances(points, metric):
    return [metric(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]


def main() -> None:
    r = math.sqrt(5.0 / 8.0)
    c = (0.25, -0.25)
    half_diamond_vertices = [(1.0, 0.0), (0.0, -1.0), (0.5, 0.5), (-0.5, -0.5)]
    assert all(math.isclose(l2(v, c), r, rel_tol=1e-12) for v in half_diamond_vertices)

    diamond_cycle = [(1.0, 0.0), (-0.5, 0.5), (0.0, -1.0), (0.5, 0.5), (-1.0, 0.0)]
    assert all(d + 1e-12 >= 2.0 * r for d in cyclic_distances(diamond_cycle, l2))

    a = 1.0 / math.sqrt(2.0)
    s = (1.0 + a) / 2.0
    q = ((1.0 - a) / 2.0, (1.0 - a) / 2.0)
    circle_cycle = [(1.0, 0.0), (-a, a), (0.0, -1.0), (a, a), (-1.0, 0.0)]
    assert all(d + 1e-12 >= 2.0 * s for d in cyclic_distances(circle_cycle, linf))

    # Dense boundary checks for the two advertised covers.
    max_diamond = 0.0
    for i in range(20001):
        t = i / 20000.0
        for x in ((t, 1.0 - t), (-t, 1.0 - t), (t, -1.0 + t), (-t, -1.0 + t)):
            max_diamond = max(max_diamond, min(l2(x, c), l2(x, (-c[0], -c[1]))))
    assert max_diamond <= r + 1e-12

    max_circle = 0.0
    for i in range(40000):
        theta = 2.0 * math.pi * i / 40000.0
        x = (math.cos(theta), math.sin(theta))
        max_circle = max(max_circle, min(linf(x, q), linf(x, (-q[0], -q[1]))))
    assert max_circle <= s + 1e-12

    assert s > r
    print(f"epsilon_2(T)  = sqrt(5/8)             = {r:.12f}")
    print(f"epsilon_2(T*) = (1+1/sqrt(2))/2      = {s:.12f}")
    print(f"gap                                      {s-r:.12f}")
    print(f"sampled maxima: diamond={max_diamond:.12f}, disk={max_circle:.12f}")


if __name__ == "__main__":
    main()

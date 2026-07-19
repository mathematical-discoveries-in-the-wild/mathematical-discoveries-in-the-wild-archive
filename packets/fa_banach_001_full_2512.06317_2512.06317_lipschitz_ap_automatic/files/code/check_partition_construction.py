"""Finite-sample sanity check for the Lipschitz partition construction.

This does not prove the theorem. It mirrors the proof on a compact sample in
R^2 and checks that the constructed finite-rank map stays within epsilon on
the sampled compact set.
"""

from __future__ import annotations

import math
from typing import Iterable


Point = tuple[float, float]


def norm(x: Point) -> float:
    return math.hypot(x[0], x[1])


def sub(x: Point, y: Point) -> Point:
    return (x[0] - y[0], x[1] - y[1])


def add(x: Point, y: Point) -> Point:
    return (x[0] + y[0], x[1] + y[1])


def scale(a: float, x: Point) -> Point:
    return (a * x[0], a * x[1])


def greedy_net(points: Iterable[Point], radius: float) -> list[Point]:
    centers: list[Point] = []
    for x in points:
        if not centers or min(norm(sub(x, c)) for c in centers) > radius:
            centers.append(x)
    return centers


def build_map(points: list[Point], epsilon: float):
    delta = epsilon / 16.0
    r = delta
    active = [x for x in points if norm(x) >= delta]
    centers = greedy_net(active, r / 2.0)

    def q(x: Point) -> Point:
        if norm(x) <= delta or not centers:
            return (0.0, 0.0)
        weights = [max(0.0, r - norm(sub(x, c))) for c in centers]
        denom = sum(weights)
        if denom == 0.0:
            return (0.0, 0.0)
        out = (0.0, 0.0)
        for w, c in zip(weights, centers):
            out = add(out, scale(w / denom, c))
        lam = min(1.0, max(0.0, (norm(x) - delta) / delta))
        return scale(lam, out)

    return q, centers


def main() -> None:
    epsilon = 0.20
    points: list[Point] = [(0.0, 0.0)]
    for k in range(240):
        t = 2.0 * math.pi * k / 240.0
        points.append((math.cos(t), 0.55 * math.sin(t)))
    for k in range(1, 80):
        t = k / 80.0
        points.append((0.6 * t, 0.25 * t * t))

    approx, centers = build_map(points, epsilon)
    errors = [norm(sub(approx(x), x)) for x in points]
    print(f"sample_size={len(points)}")
    print(f"finite_centers={len(centers)}")
    print(f"max_error={max(errors):.6f}")
    print(f"target_epsilon={epsilon:.6f}")
    assert max(errors) < epsilon


if __name__ == "__main__":
    main()

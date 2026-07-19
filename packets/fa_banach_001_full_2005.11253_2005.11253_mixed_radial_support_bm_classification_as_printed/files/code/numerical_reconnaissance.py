"""Numerical reconnaissance for arXiv:2005.11253's composition BM problem.

All polygons are planar, convex, and contain the origin in their interior.
The flower operations are approximated on a uniform angular mesh.
"""

from __future__ import annotations

import math
import sys
import numpy as np
from scipy.spatial import ConvexHull


def hull(vertices: np.ndarray) -> np.ndarray:
    vertices = np.asarray(vertices, dtype=float)
    return vertices[ConvexHull(vertices).vertices]


def area(vertices: np.ndarray) -> float:
    return float(ConvexHull(vertices).volume)


def minkowski_sum(k: np.ndarray, l: np.ndarray) -> np.ndarray:
    return hull((k[:, None, :] + l[None, :, :]).reshape(-1, 2))


def radial(vertices: np.ndarray, directions: np.ndarray) -> np.ndarray:
    equations = ConvexHull(vertices).equations
    normals = equations[:, :2]
    offsets = equations[:, 2]
    dots = normals @ directions.T
    bounds = np.full_like(dots, np.inf)
    np.divide((-offsets)[:, None], dots, out=bounds, where=dots > 1e-12)
    return np.min(bounds, axis=0)


def support(vertices: np.ndarray, directions: np.ndarray) -> np.ndarray:
    return np.max(vertices @ directions.T, axis=0)


def compose(t: np.ndarray, k: np.ndarray, directions: np.ndarray, radial_mode: bool) -> np.ndarray:
    multiplier = radial(t, directions) if radial_mode else support(t, directions)
    points = directions * (multiplier * radial(k, directions))[:, None]
    return hull(points)


def random_symmetric_polygon(rng: np.random.Generator, m: int = 6) -> np.ndarray:
    angles = np.sort(rng.uniform(0.0, math.pi, m))
    radii = np.exp(rng.normal(0.0, 0.9, m))
    points = np.column_stack((np.cos(angles), np.sin(angles))) * radii[:, None]
    return hull(np.vstack((points, -points)))


def random_origin_polygon(rng: np.random.Generator, m: int = 7) -> np.ndarray:
    angles = np.linspace(0.0, 2.0 * math.pi, m, endpoint=False)
    angles += rng.uniform(-0.35, 0.35, m) * (2.0 * math.pi / m)
    radii = np.exp(rng.normal(0.0, 1.15, m))
    points = np.column_stack((np.cos(angles), np.sin(angles))) * radii[:, None]
    candidate = hull(points)
    equations = ConvexHull(candidate).equations
    if np.max(equations[:, 2]) >= -1e-8:
        return random_origin_polygon(rng, m)
    return candidate


def random_integer_triangle(rng: np.random.Generator, radius: int = 6) -> np.ndarray:
    while True:
        points = rng.integers(-radius, radius + 1, size=(3, 2)).astype(float)
        if len(np.unique(points, axis=0)) < 3:
            continue
        try:
            candidate = hull(points)
        except Exception:
            continue
        equations = ConvexHull(candidate).equations
        if np.max(equations[:, 2]) < -1e-8:
            return candidate


def rectangle(a: float, b: float, angle: float = 0.0) -> np.ndarray:
    points = np.array([[-a, -b], [a, -b], [a, b], [-a, b]], dtype=float)
    c, s = math.cos(angle), math.sin(angle)
    return points @ np.array([[c, s], [-s, c]])


def ratio(t: np.ndarray, k: np.ndarray, l: np.ndarray, directions: np.ndarray, radial_mode: bool) -> float:
    fk = math.sqrt(area(compose(t, k, directions, radial_mode)))
    fl = math.sqrt(area(compose(t, l, directions, radial_mode)))
    fsum = math.sqrt(area(compose(t, minkowski_sum(k, l), directions, radial_mode)))
    return fsum / (fk + fl)


def inclusion_margin(t: np.ndarray, k: np.ndarray, l: np.ndarray, directions: np.ndarray, radial_mode: bool) -> float:
    fk = compose(t, k, directions, radial_mode)
    fl = compose(t, l, directions, radial_mode)
    fsum = compose(t, minkowski_sum(k, l), directions, radial_mode)
    return float(np.min(support(fsum, directions) - support(fk, directions) - support(fl, directions)))


def main() -> None:
    rng = np.random.default_rng(20260719)
    if sys.argv[1:2] == ["integer"]:
        integer_angles = np.linspace(0.0, 2.0 * math.pi, 768, endpoint=False)
        integer_directions = np.column_stack((np.cos(integer_angles), np.sin(integer_angles)))
        t = rectangle(10.0, 1.0)
        best = (float("inf"), None, None)
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
        for _ in range(count):
            k, l = random_integer_triangle(rng), random_integer_triangle(rng)
            value = ratio(t, k, l, integer_directions, False)
            if value < best[0]:
                best = (value, k, l)
        print(f"thin-rectangle integer-triangle support best_ratio={best[0]:.6f}")
        print("K=", np.array2string(best[1], precision=0, separator=","))
        print("L=", np.array2string(best[2], precision=0, separator=","))
        return
    angles = np.linspace(0.0, 2.0 * math.pi, 4096, endpoint=False)
    directions = np.column_stack((np.cos(angles), np.sin(angles)))

    candidates = [
        ("square", rectangle(1.0, 1.0)),
        ("ellipse-like rectangle", rectangle(4.0, 1.0, 0.2)),
        ("thin rectangle", rectangle(10.0, 1.0, 0.37)),
    ]
    candidates.extend((f"random-{i}", random_symmetric_polygon(rng)) for i in range(8))

    for radial_mode in (False, True):
        print("mode", "radial" if radial_mode else "support")
        for name, t in candidates:
            best = (float("inf"), None, None)
            tests = [
                (rectangle(8.0, 0.3, 0.0), rectangle(8.0, 0.3, math.pi / 2)),
                (rectangle(8.0, 0.3, math.pi / 4), rectangle(8.0, 0.3, -math.pi / 4)),
            ]
            tests.extend((random_symmetric_polygon(rng), random_symmetric_polygon(rng)) for _ in range(80))
            tests.extend((random_origin_polygon(rng), random_origin_polygon(rng)) for _ in range(160))
            for k, l in tests:
                value = ratio(t, k, l, directions, radial_mode)
                if value < best[0]:
                    best = (value, k, l)
            margin = inclusion_margin(t, best[1], best[2], directions, radial_mode)
            print(f"{name:24s} best_ratio={best[0]:.6f} inclusion_margin={margin:.6f}")
            if best[0] < 0.99:
                print("K=", np.array2string(best[1], precision=5, separator=","))
                print("L=", np.array2string(best[2], precision=5, separator=","))

    coarse_angles = np.linspace(0.0, 2.0 * math.pi, 768, endpoint=False)
    coarse_directions = np.column_stack((np.cos(coarse_angles), np.sin(coarse_angles)))
    t = rectangle(1.0, 1.0)
    best = (float("inf"), None, None)
    for _ in range(5000):
        k, l = random_origin_polygon(rng), random_origin_polygon(rng)
        value = ratio(t, k, l, coarse_directions, False)
        if value < best[0]:
            best = (value, k, l)
    print(f"square-deep support best_ratio={best[0]:.6f}")
    print("K=", np.array2string(best[1], precision=5, separator=","))
    print("L=", np.array2string(best[2], precision=5, separator=","))

    integer_angles = np.linspace(0.0, 2.0 * math.pi, 384, endpoint=False)
    integer_directions = np.column_stack((np.cos(integer_angles), np.sin(integer_angles)))
    t = rectangle(10.0, 1.0)
    best = (float("inf"), None, None)
    for _ in range(12000):
        k, l = random_integer_triangle(rng), random_integer_triangle(rng)
        value = ratio(t, k, l, integer_directions, False)
        if value < best[0]:
            best = (value, k, l)
    print(f"thin-rectangle integer-triangle support best_ratio={best[0]:.6f}")
    print("K=", np.array2string(best[1], precision=0, separator=","))
    print("L=", np.array2string(best[2], precision=0, separator=","))


if __name__ == "__main__":
    main()

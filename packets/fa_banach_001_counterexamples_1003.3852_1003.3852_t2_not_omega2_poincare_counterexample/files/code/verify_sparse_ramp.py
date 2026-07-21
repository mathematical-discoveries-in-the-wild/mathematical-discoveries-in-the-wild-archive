#!/usr/bin/env python3
"""Numerical sanity checks for the sparse-ramp counterexample.

The proof in the packet is symbolic.  This script samples the Lipschitz,
one-half-Holder, and transported-cost inequalities, and prints the exact
Muckenhoupt lower bound supplied by the first few ramps.
"""

from __future__ import annotations

import math
import random


def ramp(t: float, a: float) -> float:
    return min(max(t - a, 0.0), 1.0)


def positive_map(t: float) -> float:
    assert t >= 0.0
    value = math.sqrt(t + 1.0) - 1.0
    a = 16.0
    while a < t:
        value += ramp(t, a)
        a *= 16.0
    return value


def transport_map(t: float) -> float:
    return math.copysign(positive_map(abs(t)), t) if t else 0.0


def main() -> None:
    rng = random.Random(10033852)
    points = [0.0, 0.25, 1.0, -1.0]
    for n in range(1, 6):
        a = 16.0**n
        points.extend([a - 1e-6, a, a + 0.25, a + 1.0, a + 1.000001])
        points.extend([-x for x in points[-5:]])
    for _ in range(20_000):
        sign = -1.0 if rng.random() < 0.5 else 1.0
        exponent = rng.uniform(-3.0, 6.2)
        points.append(sign * 16.0**exponent)

    max_lip = 0.0
    max_holder = 0.0
    min_cost_ratio = math.inf
    for _ in range(100_000):
        x, y = rng.sample(points, 2)
        delta = abs(x - y)
        image_delta = abs(transport_map(x) - transport_map(y))
        if delta == 0.0 or image_delta == 0.0:
            continue
        max_lip = max(max_lip, image_delta / delta)
        max_holder = max(max_holder, image_delta / math.sqrt(delta))
        min_cost_ratio = min(
            min_cost_ratio, min(delta * delta, delta) / (image_delta * image_delta)
        )

    assert max_lip <= 1.5 + 1e-10
    assert max_holder <= 2.0 * math.sqrt(2.0) + 1e-10
    assert min_cost_ratio >= 1.0 / 8.0 - 1e-10

    print(f"sampled Lipschitz ratio max       {max_lip:.12f} (bound 1.5)")
    print(
        f"sampled 1/2-Holder ratio max     {max_holder:.12f} "
        f"(bound {2.0 * math.sqrt(2.0):.12f})"
    )
    print(f"sampled cost ratio min           {min_cost_ratio:.12f} (bound 0.125)")
    print("Muckenhoupt lower bounds:")
    previous = 0.0
    for n in range(1, 6):
        a = 16.0**n
        b = math.sqrt(a + 1.0) - 1.0
        lower = 4.0 * (1.0 - math.exp(-1.0)) * b * b
        assert lower > previous
        previous = lower
        print(f"  n={n}: a_n={a:.0f}, lower bound={lower:.12f}")


if __name__ == "__main__":
    main()


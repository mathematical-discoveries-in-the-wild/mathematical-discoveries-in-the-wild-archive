"""Sanity check for the atomic-band calculation in the solution packet.

The proof is exact. This script only samples perturbations in
R^2 \oplus_1 R^k to confirm that the two chosen atom vectors have equal
perturbed norms for ||z||_1 <= 1/8.
"""

from __future__ import annotations

import random


def l1_norm(values: list[float]) -> float:
    return sum(abs(v) for v in values)


def scale_to_ball(values: list[float], radius: float) -> list[float]:
    norm = l1_norm(values)
    if norm == 0:
        return values
    factor = random.random() * radius / norm
    return [factor * v for v in values]


def main() -> None:
    radius = 1.0 / 8.0
    u = [3.0 / 4.0, 1.0 / 4.0]
    v = [1.0 / 4.0, 3.0 / 4.0]
    worst = 0.0
    trials = 20_000

    for _ in range(trials):
        rest_dim = 5
        z = scale_to_ball(
            [random.uniform(-1.0, 1.0) for _ in range(2 + rest_dim)],
            radius,
        )
        uz = [u[0] + z[0], u[1] + z[1], *z[2:]]
        vz = [v[0] + z[0], v[1] + z[1], *z[2:]]
        worst = max(worst, abs(l1_norm(uz) - l1_norm(vz)))

    print(f"trials: {trials}")
    print(f"radius: {radius}")
    print(f"worst norm difference: {worst:.3e}")
    print("status:", "ok" if worst < 1e-12 else "check failed")


if __name__ == "__main__":
    main()

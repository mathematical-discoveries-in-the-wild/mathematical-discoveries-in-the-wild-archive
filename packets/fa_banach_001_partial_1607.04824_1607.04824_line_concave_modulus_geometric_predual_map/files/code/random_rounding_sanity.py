"""Numerical sanity check for the shifted-grid inequality.

This script is not used as proof. It samples standard concave moduli and
checks

    E omega(|Q_h(x+t)-Q_h(x)|) <= omega(t)

for grid rounding with a uniform random shift.
"""

from __future__ import annotations

import math


def expected_cost(omega, h: float, t: float) -> float:
    m = math.floor(t / h)
    s = t - m * h
    return (1.0 - s / h) * omega(m * h) + (s / h) * omega((m + 1) * h)


def main() -> None:
    moduli = {
        "sqrt": lambda t: math.sqrt(t),
        "holder_0.3_capped": lambda t: min(t**0.3, 1.0),
        "log": lambda t: math.log1p(t),
    }
    for name, omega in moduli.items():
        worst = 0.0
        for h in [1.0, 0.5, 0.125, 0.03125]:
            for j in range(1, 5000):
                t = 5.0 * j / 5000
                ratio = expected_cost(omega, h, t) / omega(t)
                worst = max(worst, ratio)
        print(f"{name}: worst sampled ratio {worst:.12f}")


if __name__ == "__main__":
    main()


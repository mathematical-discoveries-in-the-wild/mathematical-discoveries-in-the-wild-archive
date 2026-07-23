#!/usr/bin/env python3
"""Numerical sanity checks for the weak-lp volume-ratio packet.

This script is not part of the proof.  It:
  1. checks the tangent survival inequality on a grid;
  2. checks the closed entropy formula by numerical quadrature; and
  3. evaluates the source paper's exact positive-orthant recurrence.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 100


def density_entropy(p: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    q = 1 / p
    a = (p + 1) ** q
    c = p / (p + 1) ** (1 + q)

    numerical = -(mp.quad(lambda t: c * mp.log(c), [0, a]))
    numerical -= mp.quad(
        lambda t: p * t ** (-p - 1) * mp.log(p * t ** (-p - 1)),
        [a, mp.inf],
    )
    closed = (1 + q) * mp.log(1 + q) - q * mp.log(q) + q
    return numerical, closed


def check_tail(p: mp.mpf) -> mp.mpf:
    q = 1 / p
    a = (p + 1) ** q
    c = p / (p + 1) ** (1 + q)

    def survival(t: mp.mpf) -> mp.mpf:
        return 1 - c * t if t <= a else t ** (-p)

    worst = mp.mpf("-inf")
    for j in range(2001):
        t = 1 + (a - 1) * j / 2000
        worst = max(worst, survival(t) - t ** (-p))
    return worst


def positive_weak_volumes(p: mp.mpf, n_max: int) -> list[mp.mpf]:
    """Theorem 1 recurrence in arXiv:1906.04997."""
    q = 1 / p
    volumes = [mp.mpf(1)]
    for n in range(1, n_max + 1):
        value = mp.mpf(0)
        for j in range(1, n + 1):
            value += (
                (-1) ** (j - 1)
                * mp.binomial(n, j)
                * n ** (-q * j)
                * volumes[n - j]
            )
        volumes.append(value)
    return volumes


def log_ratio_per_dimension(
    p: mp.mpf, n: int, positive_weak_volume: mp.mpf
) -> mp.mpf:
    q = 1 / p
    return (
        mp.log(positive_weak_volume)
        + mp.loggamma(1 + q * n)
        - n * mp.loggamma(1 + q)
    ) / n


def main() -> None:
    for p_raw in (mp.mpf("0.5"), 1, 2, 3, 5, 10, 50):
        p = mp.mpf(p_raw)
        q = 1 / p
        numerical, closed = density_entropy(p)
        tail_error = check_tail(p)
        delta = (1 + q) * mp.log(1 + q) - mp.loggamma(1 + q)
        volumes = positive_weak_volumes(p, 80)
        finite_rate = log_ratio_per_dimension(p, 80, volumes[80])
        print(
            "p=", mp.nstr(p, 6),
            " entropy_error=", mp.nstr(abs(numerical - closed), 5),
            " tail_max_error=", mp.nstr(tail_error, 5),
            " log_Lambda=", mp.nstr(delta, 10),
            " n80_log_rate=", mp.nstr(finite_rate, 10),
        )


if __name__ == "__main__":
    main()


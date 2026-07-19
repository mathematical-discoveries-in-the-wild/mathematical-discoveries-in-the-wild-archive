#!/usr/bin/env python3
"""Numerical checks for the conditional aa_{1/2}^1(2) certificate.

This is not a proof.  It stress-tests the scalar inequality isolated in the
packet and verifies the convex-weight certificate on deterministic samples.
"""

from __future__ import annotations

import math
import random


def scalar_slack_half(u: float, v: float, w: float) -> float:
    """Slack in Scalar Lemma E for p=1/2."""
    a = math.sqrt(u + v)
    b = math.sqrt(u + w)
    c = math.sqrt(v + w)
    uu = math.sqrt(u)
    vv = math.sqrt(v)
    ww = math.sqrt(w)
    return 2 * a * b * (vv + ww - c) - (a + b - c) * (a * ww + b * vv - uu * c)


def weights_half(u: float, v: float, w: float) -> tuple[float, float, float]:
    a = math.sqrt(u + v)
    b = math.sqrt(u + w)
    c = math.sqrt(v + w)
    vv = math.sqrt(v)
    ww = math.sqrt(w)
    l1 = (vv + ww - c) / (a + b - c)
    l2 = (ww - b * l1) / c
    l3 = (vv - a * l1) / c
    return l1, l2, l3


def certificate_slacks(u: float, v: float, w: float) -> tuple[float, float, float, float]:
    """Coefficient-wise slacks for the three linear coefficients.

    The first two should be zero by construction.  The third is equivalent to
    Scalar Lemma E after multiplying by positive factors.
    """
    a = math.sqrt(u + v)
    b = math.sqrt(u + w)
    c = math.sqrt(v + w)
    uu = math.sqrt(u)
    vv = math.sqrt(v)
    ww = math.sqrt(w)
    l1, l2, l3 = weights_half(u, v, w)
    return (
        vv - (l1 * a + l3 * c),
        ww - (l1 * b + l2 * c),
        uu - (l2 * a + l3 * b),
        min(l1, l2, l3),
    )


def normalized_euclidean_slack(r: float, m: float) -> float:
    """Equivalent normalized form with x^2+y^2=1 and m=xy."""
    p = math.sqrt(r**4 + r**2 + m**2)
    s = math.sqrt(1 + 2 * m)
    t = math.sqrt(2 * r**2 + 1 + 2 * p)
    q = math.sqrt(r**2 + 2 * m**2 + 2 * m * p)
    return 2 * p * (s - 1) - (t - 1) * (q - r)


def main() -> None:
    rng = random.Random(231102920)
    min_scalar = float("inf")
    min_third = float("inf")
    min_lambda = float("inf")
    min_norm = float("inf")

    samples: list[tuple[float, float, float]] = []
    for u in [10 ** (k / 4) for k in range(-16, 17)]:
        for v in [10 ** (k / 4) for k in range(-16, 17)]:
            for w in [10 ** (k / 4) for k in range(-16, 17)]:
                samples.append((u, v, w))
    for _ in range(200_000):
        samples.append(
            (
                10 ** rng.uniform(-8, 8),
                10 ** rng.uniform(-8, 8),
                10 ** rng.uniform(-8, 8),
            )
        )

    for u, v, w in samples:
        scalar = scalar_slack_half(u, v, w)
        sx, sy, sz, lam = certificate_slacks(u, v, w)
        min_scalar = min(min_scalar, scalar)
        min_third = min(min_third, sz)
        min_lambda = min(min_lambda, lam)
        if scalar < -1e-9 or sz < -1e-9 or lam < -1e-9:
            raise SystemExit(
                f"certificate failure at u={u}, v={v}, w={w}: "
                f"scalar={scalar}, slacks={(sx, sy, sz)}, min_lambda={lam}"
            )

    for r in [10 ** (k / 5) for k in range(-25, 26)]:
        for j in range(1, 500):
            m = 0.5 * j / 500
            norm = normalized_euclidean_slack(r, m)
            min_norm = min(min_norm, norm)
            if norm < -1e-9:
                raise SystemExit(f"normalized failure at r={r}, m={m}: {norm}")

    print("samples", len(samples))
    print("min_scalar_slack", min_scalar)
    print("min_third_certificate_slack", min_third)
    print("min_lambda", min_lambda)
    print("min_normalized_slack", min_norm)
    print("status numerical_support_only")


if __name__ == "__main__":
    main()

"""Numerical sanity check for the log-periodic counterexample.

This is not part of the proof.  It samples the construction in the packet for
one parameter value and checks the defining identity h(h(x)/tau) = x.
"""

from __future__ import annotations

import math


TAU = 4.0
A = math.log(TAU)
EPSILON = 0.05


def H(u: float) -> float:
    return u + EPSILON * math.sin(2.0 * math.pi * u / A)


def H_inv(y: float) -> float:
    """Invert H by bracketing; H is increasing and H(u)-u is bounded."""
    radius = abs(EPSILON) + 1.0
    lo = y - radius
    hi = y + radius
    while H(lo) > y:
        lo -= radius
    while H(hi) < y:
        hi += radius
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if H(mid) < y:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def R(u: float) -> float:
    return H_inv(H(u) - 0.5 * A)


def h_positive(x: float) -> float:
    return math.exp(R(math.log(x)) + A)


def h(x: float) -> float:
    if x > 0.0:
        return h_positive(x)
    if x < 0.0:
        return -h_positive(-x)
    return 0.0


def main() -> None:
    xs = [
        -20.0,
        -7.5,
        -2.0,
        -0.3,
        -0.01,
        0.01,
        0.3,
        2.0,
        7.5,
        20.0,
    ]
    errors = []
    for x in xs:
        lhs = h(h(x) / TAU)
        err = abs(lhs - x)
        errors.append(err)
        print(f"x={x:8.3g}  h(h(x)/tau)={lhs: .12g}  abs_error={err:.3e}")
    print(f"max_abs_error={max(errors):.3e}")


if __name__ == "__main__":
    main()

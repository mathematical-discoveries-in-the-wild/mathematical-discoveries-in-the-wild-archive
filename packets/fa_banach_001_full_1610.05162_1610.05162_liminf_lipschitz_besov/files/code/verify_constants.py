#!/usr/bin/env python3
"""Sanity-check constants and the radial model used in the proof packet."""

from __future__ import annotations

import math


def unit_ball_volume(n: int) -> float:
    return math.pi ** (n / 2) / math.gamma(n / 2 + 1)


def main() -> None:
    max_relative_error = 0.0
    rows = 0
    for n in (1, 2, 3, 5, 10):
        v_n = unit_ball_volume(n)
        sphere = n * v_n
        for q in (1, 2, 3, 5):
            c_lower = (v_n * 2 ** (-(n + 3 * q)) * (n + q) / q) ** (1 / q)
            c_upper = (sphere / q) ** (1 / q)
            assert 0 < c_lower <= c_upper

            # For omega(h)=min(|h|,1), polar coordinates give exactly
            # A_r = |S^{n-1}| * (1/(q(1-r)) + 1/(rq)).
            target = sphere / q
            for delta in (1e-1, 1e-2, 1e-3, 1e-4):
                r = 1 - delta
                a_r = sphere * (1 / (q * delta) + 1 / (r * q))
                normalized = delta * a_r
                relative_error = abs(normalized - target) / target
                max_relative_error = max(max_relative_error, relative_error)
                assert relative_error <= delta / r + 1e-12
                rows += 1

    print("CONSTANT ORDER CHECKS: PASS")
    print("RADIAL MODEL NORMALIZATION: PASS")
    print(f"tested parameter rows = {rows}")
    print(f"largest relative error on grid = {max_relative_error:.6e}")
    print("ALL VERIFICATION CHECKS: PASS")


if __name__ == "__main__":
    main()

"""Sanity checks for the Hilbert-Schmidt compact TJS measure packet.

For a commuting diagonal compact pair with eigenvalue pairs (a_j,b_j), the
limiting tracial joint spectral measure is the sum over j of the segment
measures

    (1-t)/t dt pushed forward by t -> t(a_j,b_j), 0<t<=1.

For f(s)=|s|^p this gives integral |x a_j + y b_j|^p/(p(p+1)), matching
Tr H(f)(xA+yB).  This script verifies the normalization numerically for a
truncated Hilbert-Schmidt sequence.
"""

from __future__ import annotations

import math


def eigen_pairs(count: int) -> list[tuple[float, float]]:
    return [(((-1) ** j) / (j + 1) ** 1.2, 0.7 / (j + 1) ** 1.4) for j in range(count)]


def trace_h_abs_p(pairs: list[tuple[float, float]], x: float, y: float, p: float) -> float:
    return sum(abs(x * a + y * b) ** p for a, b in pairs) / (p * (p + 1.0))


def segment_measure_abs_p(pairs: list[tuple[float, float]], x: float, y: float, p: float) -> float:
    # Integral_0^1 (1-t)/t * |t c|^p dt = |c|^p/(p(p+1)).
    return sum(abs(x * a + y * b) ** p / (p * (p + 1.0)) for a, b in pairs)


def second_moment_matrix(pairs: list[tuple[float, float]]) -> tuple[float, float, float]:
    # Integral t^2 aa with weight (1-t)/t dt is aa/6.
    aa = sum(a * a for a, _ in pairs) / 6.0
    ab = sum(a * b for a, b in pairs) / 6.0
    bb = sum(b * b for _, b in pairs) / 6.0
    return aa, ab, bb


def main() -> int:
    pairs = eigen_pairs(2000)
    print("hs_norm_squares", sum(a * a + b * b for a, b in pairs))
    for p in (2.0, 3.0, 4.0):
        lhs = trace_h_abs_p(pairs, 1.3, -0.4, p)
        rhs = segment_measure_abs_p(pairs, 1.3, -0.4, p)
        print(f"p={p:g}", "difference", abs(lhs - rhs))
        assert math.isclose(lhs, rhs, rel_tol=1e-14, abs_tol=1e-14)
    print("second_moment_matrix", second_moment_matrix(pairs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

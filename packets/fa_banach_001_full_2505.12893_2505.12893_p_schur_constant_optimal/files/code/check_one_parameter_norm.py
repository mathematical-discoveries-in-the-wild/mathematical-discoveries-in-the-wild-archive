"""Arithmetic checks for the one-parameter sharpness example.

This script does not prove the Banach-space statements.  It checks the scalar
identities used in the proof packet:

  ||(1,e_n)||_c = 2c + 1,
  ||(1 - 2c/m, m^{-1}(e_1 + ... + e_m))||_c = 1,
  max(2A, 2cA) / (2A) = c for c >= 1.
"""

from __future__ import annotations


def norm_c(c: float, t: float, l1_norm: float, linf_norm: float) -> float:
    return max(l1_norm, abs(t) + 2.0 * c * linf_norm)


def main() -> None:
    for c in [1.0, 1.25, 2.0, 3.5, 10.0]:
        y_norm = norm_c(c, 1.0, 1.0, 1.0)
        assert abs(y_norm - (2.0 * c + 1.0)) < 1e-12

        for m in [int(2 * c) + 1, int(2 * c) + 5, int(10 * c) + 10]:
            if m <= 2 * c:
                continue
            avg_norm = norm_c(c, 1.0 - 2.0 * c / m, 1.0, 1.0 / m)
            assert abs(avg_norm - 1.0) < 1e-12

        for A in [0.1, 1.0, 7.0]:
            upper_ca = max(2.0 * A, 2.0 * c * A)
            lower_delta = 2.0 * A
            assert abs(upper_ca / lower_delta - c) < 1e-12

    print("one-parameter norm identities verified")


if __name__ == "__main__":
    main()

"""Sanity checks for the finite-dimensional obstruction in the packet.

The proof is analytic; this script only verifies the normalization formulas
and samples the norm jump for p0 + delta z^k on the ell_1^2 unit ball.
"""

from __future__ import annotations

import cmath
import math


def constants(k: int) -> tuple[float, float, float]:
    c_k = k**k / (k - 1) ** (k - 1)
    t = (k - 1) / k
    max_monomial = t ** (k - 1) * (1 - t)
    a_k = t**k
    return c_k, max_monomial, a_k


def sampled_norm(k: int, delta: complex, samples: int = 2001) -> float:
    c_k, _, _ = constants(k)
    best = 0.0
    # For fixed moduli, phases can align the two terms, so sampling t with
    # aligned phases gives the exact one-variable upper envelope.
    d = abs(delta)
    for j in range(samples):
        t = j / (samples - 1)
        value = c_k * (t ** (k - 1)) * (1 - t) + d * (t**k)
        best = max(best, value)
    return best


def main() -> None:
    roots = [cmath.exp(2j * math.pi * j / 3) for j in range(3)]
    for k in range(2, 9):
        c_k, max_monomial, a_k = constants(k)
        assert abs(c_k * max_monomial - 1.0) < 1e-12
        print(f"k={k}: C_k={c_k:.8g}, a_k={a_k:.8g}")
        for lam in [0, 0.25, 0.5 + 0.2j, -0.3 + 0.4j]:
            distances = [abs(w - lam) for w in roots]
            d = max(distances)
            assert d >= 1 - 1e-12
            lower = 1 + a_k * d
            sample = max(sampled_norm(k, w - lam) for w in roots)
            assert sample + 1e-5 >= lower
            print(f"  lambda={lam!r}: max distance={d:.6g}, sampled norm={sample:.6g}")


if __name__ == "__main__":
    main()

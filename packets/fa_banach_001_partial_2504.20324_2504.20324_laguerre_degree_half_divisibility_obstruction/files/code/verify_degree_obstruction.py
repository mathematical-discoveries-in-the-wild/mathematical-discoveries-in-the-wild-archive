#!/usr/bin/env python3
"""Exact checks for the Laguerre degree and reciprocal-root obstructions.

This is not a proof.  It checks that L_k divides L_n^(m) in the requested
degree-half box only in the predicted case n=k, m=0, and symbolically checks
the coefficient formula used for the stronger reciprocal-root obstruction.
"""

from __future__ import annotations

import argparse

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=12)
    parser.add_argument("--max-m", type=int, default=80)
    args = parser.parse_args()

    x = sp.Symbol("x")
    n_sym, k_sym, m_sym = sp.symbols("n k m", positive=True)

    sigma_r = n_sym / (m_sym + 1) - k_sym
    sigma_b = (m_sym + 2) * sigma_r / m_sym
    sigma_t = sp.factor(sigma_b - k_sym)
    expected_sigma_t = (
        (m_sym + 2) * n_sym - 2 * (m_sym + 1) ** 2 * k_sym
    ) / (m_sym * (m_sym + 1))
    assert sp.simplify(sigma_t - expected_sigma_t) == 0

    cutoff = 2 * (m_sym + 1) ** 2 / (m_sym + 2)
    cutoff_derivative = 2 * (m_sym + 1) * (m_sym + 3) / (m_sym + 2) ** 2
    assert sp.simplify(sp.diff(cutoff, m_sym) - cutoff_derivative) == 0
    tested = 0
    divisible = []

    for k in range(1, args.max_k + 1):
        p = sp.Poly(sp.laguerre(k, x), x, domain=sp.QQ)
        for n in range(1, 2 * k + 1):
            for m in range(args.max_m + 1):
                q = sp.Poly(sp.assoc_laguerre(n, m, x), x, domain=sp.QQ)
                tested += 1
                if q.rem(p).is_zero:
                    divisible.append((n, k, m))
                    if not (n == k and m == 0):
                        raise AssertionError(
                            f"unexpected divisibility: n={n}, k={k}, m={m}"
                        )

    expected = [(k, k, 0) for k in range(1, args.max_k + 1)]
    if divisible != expected:
        raise AssertionError(f"unexpected divisible list: {divisible}")

    print(f"checked {tested} exact triples")
    print(f"divisible cases: {divisible}")
    print(f"symbolic sigma(T): {sigma_t}")
    print("symbolic cutoff derivative is positive for m>0")
    print("PASS")


if __name__ == "__main__":
    main()

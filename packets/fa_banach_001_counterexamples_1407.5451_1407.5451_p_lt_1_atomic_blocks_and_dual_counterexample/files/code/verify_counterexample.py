#!/usr/bin/env python3
"""Numerical sanity checks for the sequential two-jump counterexample formulas."""

from __future__ import annotations

import argparse
import math


def check(p: float, q: float, terms: int) -> None:
    assert 0.0 < p < 1.0
    assert 1.0 < q < math.inf

    lp_sum = 0.0
    atb_upper_p = 0.0
    hp_lower_p = 0.0
    constant = 6.0 * 2.0 ** (-1.0 / p)

    for n in range(1, terms + 1):
        w = 2.0 ** (-n)
        eps = 2.0 ** (-n / (1.0 - p))
        m = w * eps / 2.0
        t = w ** (-1.0 / p)

        # The L_q norm of a subatom equals the source upper bound exactly.
        subatom_lq = (m ** (-1.0 / p) / 3.0) * m ** (1.0 / q)
        source_bound = m ** (1.0 / q - 1.0 / p) / 3.0
        assert math.isclose(subatom_lq, source_bound, rel_tol=1e-12)

        # Exact terminal L_p and square-function H_p values for g_n.
        gn_lp_p = w * eps ** (1.0 - p)
        gn_hp_p = w * (
            (1.0 - eps) * 2.0 ** (p / 2.0)
            + eps * (1.0 + ((1.0 - eps) / eps) ** 2) ** (p / 2.0)
        )
        assert gn_hp_p >= 2.0 ** (p / 2.0 - 1.0) * w

        # After t_n=w_n^{-1/p}, the L_p/atomic sums converge but H_p grows.
        lp_sum += t**p * gn_lp_p
        atb_upper_p += (constant * eps ** (1.0 / p - 1.0)) ** p
        hp_lower_p += t**p * 2.0 ** (p / 2.0 - 1.0) * w

    expected_geometric = sum(2.0 ** (-n) for n in range(1, terms + 1))
    assert math.isclose(lp_sum, expected_geometric, rel_tol=1e-12)
    assert math.isclose(
        atb_upper_p, constant**p * expected_geometric, rel_tol=1e-11
    )
    assert math.isclose(
        hp_lower_p, terms * 2.0 ** (p / 2.0 - 1.0), rel_tol=1e-12
    )

    # Lambda lower bounds for the decaying sum of level signs diverge.
    alpha = 1.0 / p - 1.0
    lambda_bounds = []
    for n in range(2, terms + 2):
        w_n = 2.0 ** (-n)
        w_prev = 2.0 ** (-(n - 1))
        eps_prev = 2.0 ** (-(n - 1) / (1.0 - p))
        beta_n = (w_n / 2.0) ** alpha
        rare_prev = w_prev * eps_prev / 2.0
        lambda_bounds.append(beta_n / rare_prev**alpha)
    assert all(b < a for b, a in zip(lambda_bounds, lambda_bounds[1:]))

    print(f"p={p:g}, q={q:g}, terms={terms}")
    print(f"L_p partial p-sum:          {lp_sum:.12g}")
    print(f"atomic upper partial p-sum:{atb_upper_p:.12g}")
    print(f"H_p lower partial p-sum:   {hp_lower_p:.12g}")
    print(f"last Lambda lower bound:   {lambda_bounds[-1]:.12g}")
    print("all checks passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=float, default=0.5)
    parser.add_argument("--q", type=float, default=2.0)
    parser.add_argument("--terms", type=int, default=20)
    args = parser.parse_args()
    check(args.p, args.q, args.terms)


if __name__ == "__main__":
    main()

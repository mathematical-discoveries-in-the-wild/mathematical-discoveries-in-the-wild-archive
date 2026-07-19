#!/usr/bin/env python3
"""Verify the constants in the 2505.16775 beta/lambda gap packet.

The mathematical proof in main.tex is independent of this script.  This file
enumerates active faces of the positive unit ball for the polyhedral norm

    N(a,b,c) = max(a + 2c/3, b + 2c/3, a + b),  a,b,c >= 0,

and solves the resulting small linear programs.  It also reproduces the
open-problem crop when the rendered source page is available.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parents[1]
W = np.array(
    [
        [1.0, 0.0, 2.0 / 3.0],
        [0.0, 1.0, 2.0 / 3.0],
        [1.0, 1.0, 0.0],
    ]
)


def solve_min_sum(supports: tuple[list[int], list[int]] | None = None):
    """Minimize N(u+v) over positive unit u,v, optionally disjoint supports."""
    m, n = W.shape
    best = (float("inf"), None)
    for active_u, active_v in product(range(m), repeat=2):
        objective = np.zeros(2 * n + 1)
        objective[-1] = 1.0
        a_ub = []
        b_ub = []
        a_eq = []
        b_eq = []

        for row in W:
            r = np.zeros(2 * n + 1)
            r[:n] = row
            a_ub.append(r)
            b_ub.append(1.0)

            r = np.zeros(2 * n + 1)
            r[n : 2 * n] = row
            a_ub.append(r)
            b_ub.append(1.0)

            r = np.zeros(2 * n + 1)
            r[:n] = row
            r[n : 2 * n] = row
            r[-1] = -1.0
            a_ub.append(r)
            b_ub.append(0.0)

        r = np.zeros(2 * n + 1)
        r[:n] = W[active_u]
        a_eq.append(r)
        b_eq.append(1.0)

        r = np.zeros(2 * n + 1)
        r[n : 2 * n] = W[active_v]
        a_eq.append(r)
        b_eq.append(1.0)

        if supports is not None:
            supp_u, supp_v = supports
            for k in range(n):
                if k not in supp_u:
                    r = np.zeros(2 * n + 1)
                    r[k] = 1.0
                    a_eq.append(r)
                    b_eq.append(0.0)
                if k not in supp_v:
                    r = np.zeros(2 * n + 1)
                    r[n + k] = 1.0
                    a_eq.append(r)
                    b_eq.append(0.0)

        result = linprog(
            objective,
            A_ub=np.array(a_ub),
            b_ub=np.array(b_ub),
            A_eq=np.array(a_eq),
            b_eq=np.array(b_eq),
            bounds=[(0, None)] * (2 * n + 1),
            method="highs",
        )
        if result.success and result.fun < best[0] - 1e-9:
            best = (result.fun, result.x)
    return best


def compute_beta():
    best = (float("inf"), None, None)
    for mask_u in range(1, 8):
        for mask_v in range(1, 8):
            if mask_u & mask_v:
                continue
            supp_u = [i for i in range(3) if (mask_u >> i) & 1]
            supp_v = [i for i in range(3) if (mask_v >> i) & 1]
            value, witness = solve_min_sum((supp_u, supp_v))
            if value < best[0] - 1e-9:
                best = (value, supp_u, supp_v, witness)
    return best


def maybe_make_crop():
    try:
        from PIL import Image
    except ImportError:
        return

    src = ROOT / "tmp" / "source_page-06.png"
    dst = ROOT / "figures" / "open_problem_crop.png"
    if not src.exists():
        return
    image = Image.open(src)
    image.crop((120, 1160, image.width - 120, 1292)).save(dst)


def as_fraction(value: float) -> Fraction:
    return Fraction(value).limit_denominator(1000)


def main():
    lambda_value, lambda_witness = solve_min_sum()
    beta_value, supp_u, supp_v, beta_witness = compute_beta()
    maybe_make_crop()

    print("lambda+", as_fraction(lambda_value), lambda_witness)
    print("beta", as_fraction(beta_value), supp_u, supp_v, beta_witness)
    if as_fraction(lambda_value) != Fraction(4, 3):
        raise SystemExit("lambda+ check failed")
    if as_fraction(beta_value) != Fraction(3, 2):
        raise SystemExit("beta check failed")


if __name__ == "__main__":
    main()

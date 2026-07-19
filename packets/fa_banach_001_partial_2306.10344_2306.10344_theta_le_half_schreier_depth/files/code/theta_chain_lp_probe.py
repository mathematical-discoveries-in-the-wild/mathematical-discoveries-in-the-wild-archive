#!/usr/bin/env python3
"""Finite LP probe for the unpromoted theta > 1/2 chain route.

This script is diagnostic only.  It checks whether the simple depth-d chain
functional on coordinates 2,...,d+2 beats every functional of depth < d on
some positive vector.  The packet proof does not rely on this computation.
"""

from __future__ import annotations

from fractions import Fraction
from scipy.optimize import linprog


def prune_with_depth(vectors, n):
    items = list(vectors.items())
    kept = {}
    for i, (v, d) in enumerate(items):
        dominated = False
        for j, (w, dw) in enumerate(items):
            if i == j or dw > d:
                continue
            if all(w[k] >= v[k] for k in range(n)) and any(w[k] > v[k] for k in range(n)):
                dominated = True
                break
        if not dominated:
            kept[v] = d
    return kept


def generate_positive_norming_vectors(n, theta, max_depth):
    vectors = {}
    for i in range(n):
        v = tuple(Fraction(1 if j == i else 0) for j in range(n))
        vectors[v] = 0
    vectors = prune_with_depth(vectors, n)

    for m in range(max_depth):
        current = sorted(
            vectors,
            key=lambda v: (
                next((i for i, a in enumerate(v) if a), n),
                next((i for i in range(n - 1, -1, -1) if v[i]), -1),
                v,
            ),
        )
        supports = []
        for v in current:
            idx = [i for i, a in enumerate(v) if a]
            supports.append((idx[0] + 1, idx[-1] + 1))

        new = dict(vectors)
        seq = []

        def rec(last_max, max_len):
            if seq:
                vv = tuple(theta * sum(v[i] for v in seq) for i in range(n))
                if vv not in new or new[vv] > m + 1:
                    new[vv] = m + 1
            if len(seq) >= max_len:
                return
            for v, (mn, mx) in zip(current, supports):
                if mn > last_max:
                    next_max_len = mn if not seq else max_len
                    if len(seq) + 1 <= next_max_len:
                        seq.append(v)
                        rec(mx, next_max_len)
                        seq.pop()

        rec(0, n)
        vectors = prune_with_depth(new, n)
    return vectors


def chain_functional(n, theta):
    depth = n - 2
    v = [Fraction(0) for _ in range(n)]
    v[1] = theta
    v[2] = theta
    for k in range(2, depth + 1):
        v = [theta * a for a in v]
        v[k + 1] = theta
    return tuple(v), depth


def margin_for_chain(n, theta):
    f, depth = chain_functional(n, theta)
    vectors = generate_positive_norming_vectors(n, theta, depth - 1)
    lower = [v for v, d in vectors.items() if d < depth]

    # Variables are x_1,...,x_n, epsilon.  Maximize epsilon subject to
    # (f-h).x >= epsilon for every lower-depth h, x >= 0, and sum x_i = 1.
    objective = [0.0] * n + [-1.0]
    aub = []
    bub = []
    for h in lower:
        aub.append([float(h[i] - f[i]) for i in range(n)] + [1.0])
        bub.append(0.0)
    aeq = [[1.0] * n + [0.0]]
    beq = [1.0]
    bounds = [(0, None)] * n + [(0, None)]
    result = linprog(
        objective,
        A_ub=aub,
        b_ub=bub,
        A_eq=aeq,
        b_eq=beq,
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        return None
    return -result.fun


def main():
    for theta in [Fraction(1, 2), Fraction(3, 5), Fraction(2, 3), Fraction(3, 4), Fraction(9, 10)]:
        print(f"theta={float(theta):.3f}")
        for n in range(4, 9):
            print(f"  n={n}, depth={n-2}, margin={margin_for_chain(n, theta)}")


if __name__ == "__main__":
    main()

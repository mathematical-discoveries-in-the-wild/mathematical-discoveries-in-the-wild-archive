#!/usr/bin/env python3
"""Regression checks for the arXiv:1901.03777 pair-projection counterexample.

The mathematical proof is piecewise exact.  This script checks the formulas on
breakpoints, a deterministic grid, and seeded random samples.
"""

from __future__ import annotations

import random


TOL = 1.0e-11


def rho(x: float) -> float:
    if x > 1.0:
        return x - 1.0
    if x < -1.0:
        return x + 1.0
    return 0.0


def alpha(x: float) -> float:
    return rho(x) / 3.0


def beta(x: float) -> float:
    return x - 2.0 * rho(x) / 3.0


def phi(x: float) -> float:
    return 2.0 * alpha(x)


def psi(x: float) -> float:
    return alpha(x) + beta(x)


def inv_phi(y: float) -> float:
    if y > 0.0:
        return 1.0 + 1.5 * y
    if y < 0.0:
        return -1.0 + 1.5 * y
    return 0.0


def inv_psi(y: float) -> float:
    if y > 1.0:
        return (3.0 * y - 1.0) / 2.0
    if y < -1.0:
        return (3.0 * y + 1.0) / 2.0
    return y


def add(u: tuple[float, ...], v: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(a + b for a, b in zip(u, v))


def sub(u: tuple[float, ...], v: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(a - b for a, b in zip(u, v))


def dot(u: tuple[float, ...], v: tuple[float, ...]) -> float:
    return sum(a * b for a, b in zip(u, v))


def close(u: tuple[float, ...], v: tuple[float, ...]) -> bool:
    return max(abs(a - b) for a, b in zip(u, v)) <= TOL


def maps(s: tuple[float, float, float]) -> tuple[tuple[float, ...], ...]:
    s12, s13, s23 = s
    t1 = (alpha(s12), alpha(s13), beta(s23))
    t2 = (alpha(s12), beta(s13), alpha(s23))
    t3 = (beta(s12), alpha(s13), alpha(s23))
    return t1, t2, t3


def pair_sum(pair: tuple[int, int], s: tuple[float, float, float]) -> tuple[float, ...]:
    ts = maps(s)
    return add(ts[pair[0]], ts[pair[1]])


def pair_sum_inverse(pair: tuple[int, int], y: tuple[float, float, float]) -> tuple[float, ...]:
    if pair == (0, 1):
        return inv_phi(y[0]), inv_psi(y[1]), inv_psi(y[2])
    if pair == (0, 2):
        return inv_psi(y[0]), inv_phi(y[1]), inv_psi(y[2])
    if pair == (1, 2):
        return inv_psi(y[0]), inv_psi(y[1]), inv_phi(y[2])
    raise ValueError(pair)


def verify_sample(s: tuple[float, float, float], t: tuple[float, float, float]) -> None:
    ts = maps(s)
    tt = maps(t)
    total = add(add(ts[0], ts[1]), ts[2])
    assert close(total, s), (s, total)

    diffs = tuple(sub(ts[i], tt[i]) for i in range(3))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        assert dot(diffs[i], diffs[j]) >= -TOL, (i, j, s, t)

    for i in range(3):
        j, k = tuple(q for q in range(3) if q != i)
        assert dot(diffs[i], add(diffs[j], diffs[k])) >= -TOL


def main() -> None:
    grid = (-4.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0)
    for x in grid:
        assert abs(2.0 * alpha(x) + beta(x) - x) <= TOL
        assert abs(phi(inv_phi(x)) - x) <= TOL
        assert abs(psi(inv_psi(x)) - x) <= TOL

    for x in grid:
        for y in grid:
            if x <= y:
                assert alpha(x) <= alpha(y) + TOL
                assert beta(x) <= beta(y) + TOL

    random.seed(190103777)
    samples = 50_000
    pairs = ((0, 1), (0, 2), (1, 2))
    for _ in range(samples):
        s = tuple(random.uniform(-20.0, 20.0) for _ in range(3))
        t = tuple(random.uniform(-20.0, 20.0) for _ in range(3))
        verify_sample(s, t)

        y = tuple(random.uniform(-20.0, 20.0) for _ in range(3))
        for pair in pairs:
            preimage = pair_sum_inverse(pair, y)
            assert close(pair_sum(pair, preimage), y), (pair, y, preimage)

    zero = (0.0, 0.0, 0.0)
    witnesses = {
        (0, 1): (0.5, 0.0, 0.0),
        (0, 2): (0.0, 0.5, 0.0),
        (1, 2): (0.0, 0.0, 0.5),
    }
    for pair, s in witnesses.items():
        ts = maps(s)
        assert s != zero
        assert close(ts[pair[0]], zero)
        assert close(ts[pair[1]], zero)
        assert not close(add(add(ts[0], ts[1]), ts[2]), zero)

    print(f"verified {samples} random samples plus deterministic breakpoints")
    print("identity partition: PASS")
    print("pair/c-cut monotonicity: PASS")
    print("pair-sum surjectivity via explicit inverses: PASS")
    print("deleted-origin pair witnesses: PASS")


if __name__ == "__main__":
    main()

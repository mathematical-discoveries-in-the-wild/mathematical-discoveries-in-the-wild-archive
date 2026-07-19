#!/usr/bin/env python3
"""Finite checks for the odd-cycle cocycle ONB packet.

The script verifies the Gram matrix and derivative coefficient formulas for the
real Fourier-mode basis used in the solution packet.
"""

from __future__ import annotations

import argparse
import itertools
import math
from typing import Dict, Iterable, Tuple

Vector = Dict[Tuple[int, ...], float]


def elem_zero(n: int) -> Tuple[int, ...]:
    return (0,) * n


def add(a: Tuple[int, ...], b: Tuple[int, ...], N: int) -> Tuple[int, ...]:
    return tuple((x + y) % N for x, y in zip(a, b))


def sub(a: Tuple[int, ...], b: Tuple[int, ...], N: int) -> Tuple[int, ...]:
    return tuple((x - y) % N for x, y in zip(a, b))


def psi(g: Tuple[int, ...], N: int) -> float:
    return float(sum(min(x % N, N - (x % N)) for x in g))


def inner_delta(g: Tuple[int, ...], h: Tuple[int, ...], N: int) -> float:
    return 0.5 * (psi(g, N) + psi(h, N) - psi(sub(g, h, N), N))


def inner_vec(v: Vector, w: Vector, N: int) -> float:
    total = 0.0
    for g, ag in v.items():
        for h, bh in w.items():
            total += ag * bh * inner_delta(g, h, N)
    return total


def q_formula(r: int, N: int) -> float:
    x = math.pi * r / N
    return (1.0 - ((-1) ** r) * math.cos(x)) / (2.0 * math.sin(x) ** 2)


def q_fourier(r: int, N: int) -> float:
    theta = 2.0 * math.pi * r / N
    m = (N - 1) // 2
    return -2.0 * sum(a * math.cos(theta * a) for a in range(1, m + 1))


def coordinate_vector(n: int, j: int, a: int, N: int) -> Tuple[int, ...]:
    out = [0] * n
    out[j] = a % N
    return tuple(out)


def basis_vector(n: int, N: int, j: int, r: int, kind: str) -> Vector:
    theta = 2.0 * math.pi * r / N
    q = q_formula(r, N)
    scale = 2.0 / math.sqrt(N * q)
    vec: Vector = {}
    for a in range(N):
        if kind == "c":
            coeff = -scale * math.cos(theta * a)
        elif kind == "s":
            coeff = scale * math.sin(theta * a)
        else:
            raise ValueError(kind)
        if abs(coeff) > 1e-15:
            vec[coordinate_vector(n, j, a, N)] = coeff
    return vec


def all_basis(n: int, N: int) -> Iterable[Tuple[Tuple[int, int, str], Vector]]:
    m = (N - 1) // 2
    for j in range(n):
        for r in range(1, m + 1):
            yield (j, r, "c"), basis_vector(n, N, j, r, "c")
            yield (j, r, "s"), basis_vector(n, N, j, r, "s")


def predicted_pairing(g: Tuple[int, ...], N: int, j: int, r: int, kind: str) -> float:
    theta = 2.0 * math.pi * r / N
    q = q_formula(r, N)
    t = g[j] % N
    if kind == "c":
        return math.sqrt(q / N) * (1.0 - math.cos(theta * t))
    if kind == "s":
        return math.sqrt(q / N) * math.sin(theta * t)
    raise ValueError(kind)


def check_case(n: int, N: int, tol: float) -> float:
    labels_vectors = list(all_basis(n, N))
    max_err = 0.0

    for r in range(1, (N - 1) // 2 + 1):
        max_err = max(max_err, abs(q_formula(r, N) - q_fourier(r, N)))

    for idx, (label_i, vec_i) in enumerate(labels_vectors):
        for jdx, (label_j, vec_j) in enumerate(labels_vectors):
            expected = 1.0 if idx == jdx else 0.0
            got = inner_vec(vec_i, vec_j, N)
            max_err = max(max_err, abs(got - expected))

    group = list(itertools.product(range(N), repeat=n))
    for label, vec in labels_vectors:
        j, r, kind = label
        for g in group:
            delta = {g: 1.0}
            got = inner_vec(delta, vec, N)
            expected = predicted_pairing(g, N, j, r, kind)
            max_err = max(max_err, abs(got - expected))

    if max_err > tol:
        raise AssertionError(f"N={N} n={n} max_err={max_err:.3e} exceeds {tol}")
    return max_err


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=5)
    parser.add_argument("--max-n", type=int, default=3)
    parser.add_argument("--tol", type=float, default=1e-10)
    args = parser.parse_args()

    worst = 0.0
    for m in range(1, args.max_m + 1):
        N = 2 * m + 1
        for n in range(1, args.max_n + 1):
            err = check_case(n, N, args.tol)
            worst = max(worst, err)
            print(f"checked N={N:2d}, n={n}: max_err={err:.3e}")
    print(f"all checks passed; worst max_err={worst:.3e}")


if __name__ == "__main__":
    main()

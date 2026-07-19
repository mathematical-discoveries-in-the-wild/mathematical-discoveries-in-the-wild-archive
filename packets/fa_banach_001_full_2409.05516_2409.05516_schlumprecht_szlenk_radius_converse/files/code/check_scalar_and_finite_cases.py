"""Numerical checks for the Schlumprecht Szlenk-radius packet.

These checks are not used as a substitute for the proof. They verify:

1. the scalar logarithmic inequalities used in the majorant lemma on a large
   finite grid and random sample;
2. finite-support interval-DP approximations of the Schlumprecht norm for
   representative one-coordinate perturbations.
"""

from __future__ import annotations

import math
import random
from functools import lru_cache


MAJORANT_CUTOFF = 3000
RANDOM_TRIALS = 500
K_GRID_MAX = 150


def phi(n: int) -> float:
    return math.log2(n + 1)


PHI_CACHE = [phi(n) for n in range(MAJORANT_CUTOFF + 2)]


def acrit(alpha: float, cutoff: int = 100_000) -> float:
    return min((phi(n + 1) - alpha) / phi(n) for n in range(1, cutoff))


def majorant(s: float, alpha: float, cutoff: int = MAJORANT_CUTOFF) -> float:
    best = max(s, alpha)
    for m in range(1, cutoff):
        best = max(best, (PHI_CACHE[m] * s + alpha) / PHI_CACHE[m + 1])
    return best


def check_scalar_lemma() -> None:
    random.seed(1)
    for alpha in [0.001, 0.01, 0.05, 0.25, 0.5, 0.7, 0.9, 0.99]:
        a_alpha = acrit(alpha, 20_000)
        worst_weak = -10.0
        worst_strong = -10.0
        for k in range(2, K_GRID_MAX):
            for frac_t in [0.0, 0.05, 0.2, 0.5, 0.9, 1.0]:
                t = frac_t * a_alpha
                for frac_s in [0.0, 0.1, 0.33, 0.5, 0.9, 1.0]:
                    s = frac_s * t
                    rem = min(phi(k - 1) * t, phi(k) * t - s)
                    lhs = majorant(s, alpha) + rem
                    gap_weak = lhs - phi(k)
                    gap_strong = lhs - phi(k) * majorant(t, alpha)
                    worst_weak = max(worst_weak, gap_weak)
                    worst_strong = max(worst_strong, gap_strong)
                    if gap_weak > 1e-8 or gap_strong > 1e-8:
                        raise RuntimeError((alpha, a_alpha, k, s, t, gap_weak, gap_strong))
        for _ in range(RANDOM_TRIALS):
            k = random.randint(2, 500)
            t = random.random() * a_alpha
            s = random.random() * t
            rem = min(phi(k - 1) * t, phi(k) * t - s)
            lhs = majorant(s, alpha) + rem
            gap_weak = lhs - phi(k)
            gap_strong = lhs - phi(k) * majorant(t, alpha)
            worst_weak = max(worst_weak, gap_weak)
            worst_strong = max(worst_strong, gap_strong)
            if gap_weak > 1e-8 or gap_strong > 1e-8:
                raise RuntimeError((alpha, a_alpha, k, s, t, gap_weak, gap_strong))
        print(
            f"scalar alpha={alpha:.3f} a_alpha={a_alpha:.6f} "
            f"worst_weak_gap={worst_weak:.6g} worst_strong_gap={worst_strong:.6g}"
        )


@lru_cache(maxsize=None)
def intervals(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(i, n))


@lru_cache(maxsize=None)
def interval_partitions(n: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    result: list[tuple[tuple[int, int], ...]] = []

    def rec(start: int, current: list[tuple[int, int]]) -> None:
        if len(current) >= 2:
            result.append(tuple(current))
        for i in range(start, n):
            for j in range(i, n):
                current.append((i, j))
                rec(j + 1, current)
                current.pop()

    rec(0, [])
    return tuple(result)


def schl_norm(vec: list[float], iters: int = 70) -> float:
    n = len(vec)
    current = {
        (i, j): max(abs(vec[k]) for k in range(i, j + 1))
        for i, j in intervals(n)
    }
    for _ in range(iters):
        updated: dict[tuple[int, int], float] = {}
        diff = 0.0
        for i, j in intervals(n):
            best = max(abs(vec[k]) for k in range(i, j + 1))
            length = j - i + 1
            for part in interval_partitions(length):
                value = sum(current[(i + a, i + b)] for a, b in part)
                best = max(best, value / phi(len(part)))
            updated[(i, j)] = best
            diff = max(diff, abs(best - current[(i, j)]))
        current = updated
        if diff < 1e-10:
            break
    return current[(0, n - 1)]


def check_finite_cases() -> None:
    for eps in [0.1, 0.5, 1.0, 1.4, 1.8]:
        alpha = eps / 2
        a_eps = acrit(alpha, 20_000)
        worst = 0.0
        for m in range(1, 8):
            unit_norm = m / phi(m)
            x = [0.995 * a_eps / unit_norm] * m
            value = schl_norm(x + [0.0, 0.0, alpha])
            worst = max(worst, value)
            if value > 1.0001:
                raise RuntimeError((eps, m, value))
        print(f"finite eps={eps:.3f} a_eps={a_eps:.6f} worst_norm={worst:.6f}")


if __name__ == "__main__":
    check_scalar_lemma()
    check_finite_cases()
    print("checks passed")

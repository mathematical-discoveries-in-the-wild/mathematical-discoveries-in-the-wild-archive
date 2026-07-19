"""Monte Carlo probes for aggregate-law groupings in finite ell_q.

All models use the same aggregate jump law on coordinate atoms but group the
atoms into independent variables differently.  Signs are symmetric, so the
original Banach-valued increments are mean zero.
"""

from __future__ import annotations

import math
import random
from collections.abc import Callable


def ell_norm(vec: list[int], q: float) -> float:
    return sum(abs(x) ** q for x in vec) ** (1.0 / q)


def moment(
    sampler: Callable[[random.Random], list[int]],
    q: float,
    p: float,
    trials: int,
    rng: random.Random,
) -> float:
    total = 0.0
    for _ in range(trials):
        total += ell_norm(sampler(rng), q) ** p
    return total / trials


def deterministic_basis(n: int) -> Callable[[random.Random], list[int]]:
    def sample(rng: random.Random) -> list[int]:
        return [1 if rng.randrange(2) else -1 for _ in range(n)]

    return sample


def iid_occupancy(n: int) -> Callable[[random.Random], list[int]]:
    def sample(rng: random.Random) -> list[int]:
        out = [0] * n
        for _ in range(n):
            k = rng.randrange(n)
            out[k] += 1 if rng.randrange(2) else -1
        return out

    return sample


def block_occupancy(n: int, block: int) -> Callable[[random.Random], list[int]]:
    """Partition coordinates into blocks; each variable chooses within a block.

    There are n variables total.  Each coordinate has aggregate mass one.
    block=1 is deterministic_basis; block=n is iid_occupancy.
    """

    assert n % block == 0
    groups = [list(range(start, start + block)) for start in range(0, n, block)]

    def sample(rng: random.Random) -> list[int]:
        out = [0] * n
        for group in groups:
            for _ in range(block):
                k = group[rng.randrange(block)]
                out[k] += 1 if rng.randrange(2) else -1
        return out

    return sample


def paired_diagonal(n: int) -> Callable[[random.Random], list[int]]:
    """Aggregate has mass one on each coordinate, grouped in disjoint pairs."""

    assert n % 2 == 0

    def sample(rng: random.Random) -> list[int]:
        out = [0] * n
        for start in range(0, n, 2):
            for _ in range(2):
                k = start + rng.randrange(2)
                out[k] += 1 if rng.randrange(2) else -1
        return out

    return sample


def main() -> None:
    rng = random.Random(19071158819)
    trials = 4000
    cases = [
        (1.5, 1.1),
        (1.5, 3.0),
        (3.0, 1.5),
        (3.0, 5.0),
        (4.0, 2.5),
        (4.0, 8.0),
    ]
    ns = [64, 256, 1024]
    print("q p n model moment_ratio_vs_deterministic")
    for q, p in cases:
        for n in ns:
            base = moment(deterministic_basis(n), q, p, trials, rng)
            for name, sampler in [
                ("pair", paired_diagonal(n)),
                ("block8", block_occupancy(n, 8) if n % 8 == 0 else None),
                ("iid", iid_occupancy(n)),
            ]:
                if sampler is None:
                    continue
                val = moment(sampler, q, p, trials, rng)
                print(f"{q:g} {p:g} {n} {name} {val / base:.4f}")
        print()


if __name__ == "__main__":
    main()

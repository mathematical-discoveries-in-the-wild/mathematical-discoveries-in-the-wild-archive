"""Finite sanity check for the old c0 occupancy construction in ell_q.

The c0 counterexample uses eta_k = +/- e_k and xi_j = +/- e_{I_j}.
In fixed finite q, both sums have ell_q size of order N^(1/q), so this
construction does not give a growing obstruction to the ell_q natural exponent.
"""

from __future__ import annotations

import random


def trial_ratio(n: int, q: float, trials: int, rng: random.Random) -> float:
    eta_norm = n ** (1.0 / q)
    total = 0.0
    for _ in range(trials):
        counts = [0] * n
        for _ in range(n):
            index = rng.randrange(n)
            sign = 1 if rng.randrange(2) else -1
            counts[index] += sign
        xi_norm = sum(abs(c) ** q for c in counts) ** (1.0 / q)
        total += xi_norm / eta_norm
    return total / trials


def main() -> None:
    rng = random.Random(190711588)
    trials = 1500
    print("q n mean_ratio_xi_over_eta")
    for q in (1.25, 1.5, 2.0, 3.0, 4.0, 8.0):
        for n in (100, 1000):
            ratio = trial_ratio(n, q, trials, rng)
            print(f"{q:g} {n} {ratio:.4f}")


if __name__ == "__main__":
    main()

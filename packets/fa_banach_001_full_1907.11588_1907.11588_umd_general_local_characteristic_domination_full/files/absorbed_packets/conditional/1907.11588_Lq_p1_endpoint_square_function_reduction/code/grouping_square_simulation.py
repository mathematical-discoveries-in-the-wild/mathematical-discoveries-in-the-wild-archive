"""Monte Carlo checks for the L^q endpoint square-function regrouping lemma.

The script builds a finite aggregate law in R^d, partitions the same atoms into
two different independent families, and estimates

    E ||(sum_i |X_i|^2)^{1/2}||_q

for each partition.  It is evidence only, not a proof.
"""

from __future__ import annotations

import math
import random
import statistics

import numpy as np


def estimate(groups, q: float, trials: int = 6000) -> float:
    values = []
    for _ in range(trials):
        square_sum = None
        for atoms in groups:
            r = random.random()
            acc = 0.0
            chosen = None
            for prob, vector in atoms:
                acc += prob
                if r < acc:
                    chosen = vector
                    break
            if chosen is not None:
                if square_sum is None:
                    square_sum = chosen * chosen
                else:
                    square_sum = square_sum + chosen * chosen
        if square_sum is None:
            values.append(0.0)
        else:
            values.append(float((square_sum ** (q / 2.0)).sum() ** (1.0 / q)))
    return statistics.mean(values)


def random_partition(atoms, groups_count: int, max_mass: float = 0.95):
    groups = [[] for _ in range(groups_count)]
    totals = [0.0 for _ in range(groups_count)]
    order = atoms[:]
    random.shuffle(order)
    for prob, vector in order:
        choices = [i for i, total in enumerate(totals) if total + prob <= max_mass]
        if not choices:
            return None
        idx = random.choice(choices)
        groups[idx].append((prob, vector))
        totals[idx] += prob
    return groups


def random_atoms(dimension: int, count: int):
    atoms = []
    for _ in range(count):
        vector = np.zeros(dimension)
        support_size = random.randint(1, min(3, dimension))
        for coord in random.sample(range(dimension), support_size):
            vector[coord] = math.exp(random.uniform(-1.5, 1.5))
        prob = 10 ** random.uniform(-2.2, -0.15)
        atoms.append((prob, vector))
    return atoms


def run_one(q: float, dimension: int = 8, atom_count: int = 30, groups_count: int = 20):
    atoms = random_atoms(dimension, atom_count)
    first = random_partition(atoms, groups_count)
    second = random_partition(atoms, groups_count)
    if first is None or second is None:
        return None
    first_value = estimate(first, q)
    second_value = estimate(second, q)
    if min(first_value, second_value) == 0:
        return None
    return max(first_value / second_value, second_value / first_value)


def main() -> None:
    random.seed(20260616)
    np.random.seed(20260616)
    for q in [1.1, 1.2, 1.5, 1.8, 2.0, 3.0, 5.0, 10.0, 20.0]:
        best = 0.0
        for _ in range(300):
            ratio = run_one(q)
            if ratio is not None:
                best = max(best, ratio)
        print(f"q={q:4.1f} best_ratio={best:.4f}")


if __name__ == "__main__":
    main()

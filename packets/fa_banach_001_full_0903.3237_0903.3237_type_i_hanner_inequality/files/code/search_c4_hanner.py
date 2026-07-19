"""Random and local search for Hatami's Type-I Hanner conjecture on C4.

For a real matrix F and s >= 1, the Type-I C4 hypergraph norm is

    N_s(F) = tr((A A^T)^2)^(1/(4s)),  A = |F|^s.

The conjectured q-Hanner inequality has q = 4s.
"""

from __future__ import annotations

import argparse

import numpy as np
from scipy.optimize import differential_evolution


def c4_norm(matrix: np.ndarray, s: float) -> float:
    a = np.abs(matrix) ** s
    gram = a @ a.T
    fourth_power = float(np.sum(gram * gram))
    return fourth_power ** (1.0 / (4.0 * s))


def hanner_defect(f: np.ndarray, g: np.ndarray, s: float) -> float:
    q = 4.0 * s
    nf = c4_norm(f, s)
    ng = c4_norm(g, s)
    lhs = c4_norm(f + g, s) ** q + c4_norm(f - g, s) ** q
    rhs = (nf + ng) ** q + abs(nf - ng) ** q
    scale = max(rhs, np.finfo(float).tiny)
    return (lhs - rhs) / scale


def random_search(size: int, s: float, samples: int, seed: int) -> tuple[float, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    best = (-np.inf, np.empty((size, size)), np.empty((size, size)))
    for _ in range(samples):
        f = rng.normal(size=(size, size))
        g = rng.normal(size=(size, size))
        defect = hanner_defect(f, g, s)
        if defect > best[0]:
            best = (defect, f.copy(), g.copy())
    return best


def optimized_search(size: int, s: float, seed: int) -> tuple[float, np.ndarray, np.ndarray]:
    count = size * size

    def objective(vector: np.ndarray) -> float:
        f = vector[:count].reshape(size, size)
        g = vector[count:].reshape(size, size)
        return -hanner_defect(f, g, s)

    result = differential_evolution(
        objective,
        bounds=[(-2.0, 2.0)] * (2 * count),
        seed=seed,
        maxiter=800,
        popsize=20,
        polish=True,
        workers=1,
        updating="immediate",
        tol=1e-10,
    )
    vector = result.x
    return -float(result.fun), vector[:count].reshape(size, size), vector[count:].reshape(size, size)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=2)
    parser.add_argument("--s", type=float, default=3.0)
    parser.add_argument("--samples", type=int, default=200_000)
    parser.add_argument("--seed", type=int, default=4)
    parser.add_argument("--optimize", action="store_true")
    args = parser.parse_args()

    if args.optimize:
        defect, f, g = optimized_search(args.size, args.s, args.seed)
    else:
        defect, f, g = random_search(args.size, args.s, args.samples, args.seed)

    np.set_printoptions(precision=10, suppress=True)
    print(f"size={args.size} s={args.s} best_normalized_defect={defect:.16g}")
    print("F=")
    print(f)
    print("G=")
    print(g)


if __name__ == "__main__":
    main()

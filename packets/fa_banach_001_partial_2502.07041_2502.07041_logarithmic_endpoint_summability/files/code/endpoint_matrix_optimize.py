"""Local optimization probe for the endpoint matrix inequality.

This complements exact random enumeration by minimizing the largest signed
Lorentz norm after normalizing the column Lp energy.  The objective remains
nonsmooth (maximum over signs and decreasing rearrangement), so output is
diagnostic only.  Any ratio above one is independently rechecked by the exact
routine from endpoint_matrix_probe.py.
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
from scipy.optimize import differential_evolution, minimize

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


PROBE_PATH = Path(__file__).with_name("2502.07041_endpoint_matrix_probe.py")
SPEC = spec_from_file_location("endpoint_matrix_probe", PROBE_PATH)
assert SPEC is not None and SPEC.loader is not None
PROBE = module_from_spec(SPEC)
SPEC.loader.exec_module(PROBE)


def normalized_matrix(flat: np.ndarray, atoms: int, columns: int, p: float) -> np.ndarray:
    matrix = np.asarray(flat, dtype=float).reshape(atoms, columns)
    numerator = np.sum(np.mean(np.abs(matrix) ** p, axis=0)) ** (1.0 / p)
    if numerator < 1e-14:
        return matrix
    return matrix / numerator


def denominator(flat: np.ndarray, atoms: int, columns: int, p: float) -> float:
    matrix = normalized_matrix(flat, atoms, columns, p)
    signs = np.asarray(
        list(itertools.product((-1.0, 1.0), repeat=columns)), dtype=float
    )
    return float(np.max(PROBE.xp_norm_rows(signs @ matrix.T, p)))


def run(args: argparse.Namespace) -> None:
    dimension = args.atoms * args.columns
    bounds = [(-1.0, 1.0)] * dimension
    result = differential_evolution(
        denominator,
        bounds,
        args=(args.atoms, args.columns, args.p),
        seed=args.seed,
        maxiter=args.iterations,
        popsize=args.population,
        polish=False,
        workers=1,
        updating="immediate",
        tol=1e-9,
    )
    polished = minimize(
        denominator,
        result.x,
        args=(args.atoms, args.columns, args.p),
        method="Powell",
        options={"maxiter": 5000, "xtol": 1e-11, "ftol": 1e-11},
    )
    winner = polished if polished.fun < result.fun else result
    matrix = normalized_matrix(winner.x, args.atoms, args.columns, args.p)
    ratio, numerator, exact_denominator = PROBE.exact_ratio(matrix, args.p)
    np.set_printoptions(precision=12, suppress=True)
    print(f"p={args.p} atoms={args.atoms} columns={args.columns}")
    print(f"ratio={ratio:.12f} numerator={numerator:.12f} denominator={exact_denominator:.12f}")
    print(matrix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=float, default=1.5)
    parser.add_argument("--atoms", type=int, default=3)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--iterations", type=int, default=500)
    parser.add_argument("--population", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260721)
    run(parser.parse_args())

"""Finite atomic probes for Conjecture 4.6 of arXiv:2502.07041.

For an N by n matrix A, columns represent functions on N equal atoms.  The
script computes exactly (over all 2^n signs) the ratio

    (sum_i ||A_i||_Lp^p)^(1/p)
    / max_eps ||A eps||_Xp,

where Xp = Lambda_{p,W}, W(t)=log(e/t)^(1-p).  A growing ratio would disprove
the conjectured dimension-free inequality.  Finite searches are diagnostic,
not a proof.
"""

from __future__ import annotations

import argparse
import itertools
import math

import numpy as np


def xp_norm_rows(values: np.ndarray, p: float) -> np.ndarray:
    """Xp norm of each row of values, with columns viewed as equal atoms."""
    values = np.asarray(values, dtype=float)
    atom_count = values.shape[1]
    ranks = np.arange(atom_count + 1, dtype=float)
    w = np.zeros(atom_count + 1, dtype=float)
    w[1:] = np.log(math.e * atom_count / ranks[1:]) ** (1.0 - p)
    increments = np.diff(w)
    ordered = np.sort(np.abs(values), axis=1)[:, ::-1]
    return np.sum(ordered**p * increments[None, :], axis=1) ** (1.0 / p)


def exact_ratio(matrix: np.ndarray, p: float) -> tuple[float, float, float]:
    matrix = np.asarray(matrix, dtype=float)
    atom_count, column_count = matrix.shape
    numerator = np.sum(np.mean(np.abs(matrix) ** p, axis=0)) ** (1.0 / p)
    signs = np.asarray(
        list(itertools.product((-1.0, 1.0), repeat=column_count)), dtype=float
    )
    signed_sums = signs @ matrix.T
    denominator = float(np.max(xp_norm_rows(signed_sums, p)))
    return numerator / denominator, numerator, denominator


def random_regular_sparse(
    rng: np.random.Generator,
    atom_count: int,
    column_count: int,
    degree: int,
    p: float,
) -> np.ndarray:
    matrix = np.zeros((atom_count, column_count), dtype=float)
    for j in range(column_count):
        rows = rng.choice(atom_count, size=min(degree, atom_count), replace=False)
        matrix[rows, j] = rng.choice((-1.0, 1.0), size=len(rows))
    column_lp = np.mean(np.abs(matrix) ** p, axis=0) ** (1.0 / p)
    matrix[:, column_lp > 0] /= column_lp[column_lp > 0]
    return matrix


def run(args: argparse.Namespace) -> None:
    rng = np.random.default_rng(args.seed)
    best: list[tuple[float, str, int, int, int]] = []

    for n in args.columns:
        for atom_count in args.atoms:
            if n > 16:
                raise ValueError("exact sign enumeration is capped at 16 columns")

            dense = rng.normal(size=(atom_count, n))
            dense /= np.mean(np.abs(dense) ** args.p, axis=0) ** (1.0 / args.p)
            ratio, _, _ = exact_ratio(dense, args.p)
            best.append((ratio, "gaussian", atom_count, n, atom_count))

            for degree in args.degrees:
                for _ in range(args.trials):
                    matrix = random_regular_sparse(
                        rng, atom_count, n, degree, args.p
                    )
                    ratio, _, _ = exact_ratio(matrix, args.p)
                    best.append((ratio, "sparse", atom_count, n, degree))

    best.sort(reverse=True)
    print(f"p={args.p} seed={args.seed} cases={len(best)}")
    for ratio, kind, atom_count, n, degree in best[: args.report]:
        print(
            f"ratio={ratio:.8f} kind={kind:8s} atoms={atom_count:3d} "
            f"columns={n:2d} degree={degree:3d}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=float, default=1.5)
    parser.add_argument("--seed", type=int, default=20260721)
    parser.add_argument("--trials", type=int, default=30)
    parser.add_argument("--report", type=int, default=20)
    parser.add_argument("--columns", type=int, nargs="+", default=[6, 8, 10, 12])
    parser.add_argument("--atoms", type=int, nargs="+", default=[8, 16, 32])
    parser.add_argument("--degrees", type=int, nargs="+", default=[1, 2, 4, 8, 16])
    run(parser.parse_args())

"""Finite L1 cut-metric LP checks for truncations of arXiv:1311.4584.

This is exploratory evidence only.  It computes the least distortion of the
finite metric M_n into L1 by optimizing over cut metrics.  For n=4 a
symmetry-reduced LP is used.
"""

from __future__ import annotations

import collections
import itertools

import numpy as np
from scipy.optimize import linprog


def points(n: int):
    return [("0", 0)] + [("n", i) for i in range(n)] + [
        ("A", mask) for mask in range(1, 1 << n)
    ]


def distance(p, q) -> int:
    if p == q:
        return 0
    tp, x = p
    tq, y = q
    if {tp, tq} == {"0", "n"}:
        return 1
    if {tp, tq} == {"0", "A"}:
        return 2
    if tp == tq == "n":
        return 2
    if tp == "n" and tq == "A":
        return 1 if (y >> x) & 1 else 3
    if tp == "A" and tq == "n":
        return 1 if (x >> y) & 1 else 3
    if tp == tq == "A":
        return 2 if x & y else 4
    raise ValueError((p, q))


def solve_full_cut_lp(n: int) -> float:
    pts = points(n)
    pairs = [(i, j) for i in range(len(pts)) for j in range(i + 1, len(pts))]
    ds = np.array([distance(pts[i], pts[j]) for i, j in pairs], dtype=float)
    cuts = [mask << 1 for mask in range(1, 1 << (len(pts) - 1))]
    cut_matrix = np.zeros((len(pairs), len(cuts)), dtype=float)
    for k, cut in enumerate(cuts):
        for r, (i, j) in enumerate(pairs):
            cut_matrix[r, k] = ((cut >> i) & 1) != ((cut >> j) & 1)
    return solve_cut_lp(cut_matrix, ds)


def solve_cut_lp(cut_matrix: np.ndarray, ds: np.ndarray) -> float:
    objective = np.zeros(cut_matrix.shape[1] + 1)
    objective[-1] = 1
    lower = np.hstack([-cut_matrix, np.zeros((len(ds), 1))])
    upper = np.hstack([cut_matrix, -ds[:, None]])
    result = linprog(
        objective,
        A_ub=np.vstack([lower, upper]),
        b_ub=np.concatenate([-ds, np.zeros(len(ds))]),
        bounds=[(0, None)] * cut_matrix.shape[1] + [(1, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.fun)


def solve_symmetric_n4() -> float:
    n = 4
    pts = points(n)
    index = {p: i for i, p in enumerate(pts)}
    perms = list(itertools.permutations(range(n)))

    def permute_mask(mask: int, perm) -> int:
        out = 0
        for i, j in enumerate(perm):
            if (mask >> i) & 1:
                out |= 1 << j
        return out

    permuted_indices = []
    for perm in perms:
        arr = []
        for kind, value in pts:
            if kind == "0":
                arr.append(0)
            elif kind == "n":
                arr.append(index[("n", perm[value])])
            else:
                arr.append(index[("A", permute_mask(value, perm))])
        permuted_indices.append(arr)

    def canonical_cut(cut: int) -> int:
        best = None
        for arr in permuted_indices:
            moved = 0
            for i in range(len(pts)):
                if (cut >> i) & 1:
                    moved |= 1 << arr[i]
            best = moved if best is None or moved < best else best
        return best

    def pair_type(i: int, j: int):
        p, q = pts[i], pts[j]
        tp, x = p
        tq, y = q
        if {tp, tq} == {"0", "n"}:
            return ("0n",)
        if tp == "0" and tq == "A":
            return ("0A", y.bit_count())
        if tq == "0" and tp == "A":
            return ("0A", x.bit_count())
        if tp == tq == "n":
            return ("nn",)
        if tp == "n" and tq == "A":
            return ("nA", y.bit_count(), int((y >> x) & 1))
        if tp == "A" and tq == "n":
            return ("nA", x.bit_count(), int((x >> y) & 1))
        if tp == tq == "A":
            a, b = sorted([x.bit_count(), y.bit_count()])
            return ("AA", a, b, (x & y).bit_count())
        raise ValueError((p, q))

    pair_reps = []
    seen = set()
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            kind = pair_type(i, j)
            if kind not in seen:
                seen.add(kind)
                pair_reps.append((i, j, kind, distance(pts[i], pts[j])))

    orbit_counts = collections.Counter()
    sep_counts = collections.defaultdict(lambda: np.zeros(len(pair_reps)))
    for mask0 in range(1, 1 << (len(pts) - 1)):
        cut = mask0 << 1
        orbit = canonical_cut(cut)
        orbit_counts[orbit] += 1
        row = sep_counts[orbit]
        for r, (i, j, _, _) in enumerate(pair_reps):
            row[r] += ((cut >> i) & 1) != ((cut >> j) & 1)

    orbits = list(orbit_counts)
    cut_matrix = np.zeros((len(pair_reps), len(orbits)))
    for k, orbit in enumerate(orbits):
        cut_matrix[:, k] = sep_counts[orbit] / orbit_counts[orbit]
    ds = np.array([d for _, _, _, d in pair_reps], dtype=float)
    return solve_cut_lp(cut_matrix, ds)


if __name__ == "__main__":
    print("n=2", solve_full_cut_lp(2))
    print("n=3", solve_full_cut_lp(3))
    print("n=4 symmetric", solve_symmetric_n4())

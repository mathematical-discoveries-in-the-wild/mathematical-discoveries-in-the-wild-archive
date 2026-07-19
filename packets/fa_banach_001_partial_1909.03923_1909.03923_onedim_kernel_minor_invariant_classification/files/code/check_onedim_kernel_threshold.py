#!/usr/bin/env python3
"""Exact finite checks for the one-dimensional-kernel minor threshold.

For the normal-form direction D_r, the script builds the derivative map from
order-s minors to order-(s-1) minors and checks that its kernel is nonzero
exactly when 2*s <= m+n-r.
"""

from fractions import Fraction
from itertools import combinations


def combs(n, k):
    return list(combinations(range(n), k))


def rank_fraction(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    for col in range(n):
        pivot = None
        for row in range(rank, m):
            if rows[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [x / pivot_value for x in rows[rank]]
        for row in range(m):
            if row != rank and rows[row][col]:
                factor = rows[row][col]
                rows[row] = [
                    rows[row][j] - factor * rows[rank][j] for j in range(n)
                ]
        rank += 1
        if rank == m:
            break
    return rank


def derivative_matrix(m, n, r, s):
    row_sets_s = combs(m, s)
    col_sets_s = combs(n, s)
    row_sets_sm1 = combs(m, s - 1)
    col_sets_sm1 = combs(n, s - 1)

    domain = [(i_set, j_set) for i_set in row_sets_s for j_set in col_sets_s]
    codomain = {
        (i_set, j_set): idx
        for idx, (i_set, j_set) in enumerate(
            (pair for pair in ((i, j) for i in row_sets_sm1 for j in col_sets_sm1))
        )
    }

    matrix = [[0 for _ in domain] for _ in codomain]
    active = set(range(r))
    for col, (i_set, j_set) in enumerate(domain):
        i_lookup = {value: pos for pos, value in enumerate(i_set)}
        j_lookup = {value: pos for pos, value in enumerate(j_set)}
        for a in sorted(set(i_set).intersection(j_set).intersection(active)):
            i0 = tuple(x for x in i_set if x != a)
            j0 = tuple(x for x in j_set if x != a)
            sign = -1 if (i_lookup[a] + j_lookup[a]) % 2 else 1
            matrix[codomain[(i0, j0)]][col] += sign
    return matrix, len(domain)


def main():
    checked = 0
    failures = []
    for m in range(3, 7):
        for n in range(3, 7):
            for s in range(2, min(m, n)):
                for r in range(1, min(m, n) + 1):
                    matrix, domain_dim = derivative_matrix(m, n, r, s)
                    kernel_dim = domain_dim - rank_fraction(matrix)
                    expected_nonzero = 2 * s <= m + n - r
                    actual_nonzero = kernel_dim > 0
                    checked += 1
                    if actual_nonzero != expected_nonzero:
                        failures.append(
                            {
                                "m": m,
                                "n": n,
                                "r": r,
                                "s": s,
                                "kernel_dim": kernel_dim,
                                "expected_nonzero": expected_nonzero,
                            }
                        )

    if failures:
        print("FAIL")
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print(
        "PASS: checked",
        checked,
        "cases for 3 <= m,n <= 6, all ranks, and 2 <= s < min(m,n).",
    )


if __name__ == "__main__":
    main()

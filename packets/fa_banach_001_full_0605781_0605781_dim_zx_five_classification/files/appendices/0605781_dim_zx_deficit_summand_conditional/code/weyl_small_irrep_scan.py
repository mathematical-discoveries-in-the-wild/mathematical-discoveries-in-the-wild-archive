"""Systematic small-highest-weight scan for the `dim Z(X)` atom lemma.

This supports the final-strike attempt on arXiv:math/0605781, Problem 27.
It is still computational evidence, not a proof.  Unlike the older
``dangerous_irrep_scan`` file, this script uses the Weyl dimension formula
for all classical simple types A-D up to a rank bound and enumerates every
dominant highest weight whose complex dimension is below the relevant
triangular support threshold ``w(dim g)``.

If an irreducible real orthogonal representation is dangerous, its complex
dimension must be below ``w(dim g)``.  The only caveat is representation
type: real type has real dimension equal to the complex dimension, while
complex/quaternionic type doubles it.  The script records type caveats rather
than pretending to classify Frobenius-Schur indicators in all cases.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from collections import Counter


@dataclass(frozen=True)
class SmallRep:
    typ: str
    rank: int
    lie_dim: int
    threshold: int
    weight: tuple[int, ...]
    complex_dim: int
    label: str
    verdict: str


def triangular(k: int) -> int:
    return k * (k - 1) // 2


def triangular_weights(max_m: int) -> list[int]:
    w = [10**9] * (max_m + 1)
    w[0] = 0
    for k in range(2, max_m + 3):
        t = triangular(k)
        if t > max_m:
            break
        for m in range(t, max_m + 1):
            candidate = w[m - t] + k
            if candidate < w[m]:
                w[m] = candidate
    return w


def dim_a(weight: tuple[int, ...]) -> int:
    """Weyl dimension for type A_r."""
    r = len(weight)
    m = [sum(weight[i:]) for i in range(r)] + [0]
    ans = Fraction(1, 1)
    for i in range(r + 1):
        for j in range(i + 1, r + 1):
            ans *= Fraction(m[i] - m[j] + j - i, j - i)
    return int(ans)


def _bc_rho(rank: int, typ: str) -> list[Fraction]:
    if typ == "B":
        return [Fraction(2 * (rank - i) - 1, 2) for i in range(rank)]
    if typ == "C":
        return [Fraction(rank - i, 1) for i in range(rank)]
    raise ValueError(typ)


def _bc_m(weight: tuple[int, ...], typ: str) -> list[Fraction]:
    r = len(weight)
    if typ == "B":
        return [
            Fraction(sum(weight[i : r - 1]), 1) + Fraction(weight[-1], 2)
            for i in range(r)
        ]
    if typ == "C":
        return [Fraction(sum(weight[i:]), 1) for i in range(r)]
    raise ValueError(typ)


def dim_bc(weight: tuple[int, ...], typ: str) -> int:
    """Weyl dimension for types B_r and C_r."""
    r = len(weight)
    m = _bc_m(weight, typ)
    rho = _bc_rho(r, typ)
    x = [m[i] + rho[i] for i in range(r)]
    ans = Fraction(1, 1)
    for i in range(r):
        ans *= Fraction(x[i], rho[i])
    for i in range(r):
        for j in range(i + 1, r):
            ans *= Fraction(x[i] * x[i] - x[j] * x[j], rho[i] * rho[i] - rho[j] * rho[j])
    return int(ans)


def dim_d(weight: tuple[int, ...]) -> int:
    """Weyl dimension for type D_r."""
    r = len(weight)
    m: list[Fraction] = []
    for i in range(r - 2):
        m.append(Fraction(sum(weight[i : r - 2]), 1) + Fraction(weight[-2] + weight[-1], 2))
    m.append(Fraction(weight[-2] + weight[-1], 2))
    m.append(Fraction(-weight[-2] + weight[-1], 2))
    rho = [Fraction(r - i - 1, 1) for i in range(r)]
    x = [m[i] + rho[i] for i in range(r)]
    ans = Fraction(1, 1)
    for i in range(r):
        for j in range(i + 1, r):
            ans *= Fraction(x[i] * x[i] - x[j] * x[j], rho[i] * rho[i] - rho[j] * rho[j])
    return abs(int(ans))


def lie_dim(typ: str, rank: int) -> int:
    if typ == "A":
        return rank * (rank + 2)
    if typ == "B":
        return rank * (2 * rank + 1)
    if typ == "C":
        return rank * (2 * rank + 1)
    if typ == "D":
        return rank * (2 * rank - 1)
    raise ValueError(typ)


def weyl_dim(typ: str, weight: tuple[int, ...]) -> int:
    if typ == "A":
        return dim_a(weight)
    if typ in {"B", "C"}:
        return dim_bc(weight, typ)
    if typ == "D":
        return dim_d(weight)
    raise ValueError(typ)


def fundamental_label(typ: str, rank: int, weight: tuple[int, ...]) -> str:
    nonzero = [(i + 1, c) for i, c in enumerate(weight) if c]
    if not nonzero:
        return "trivial"
    if len(nonzero) == 1 and nonzero[0][1] == 1:
        i = nonzero[0][0]
        if typ == "A" and i in {1, rank}:
            return "standard or dual standard"
        if typ == "A" and i in {2, rank - 1}:
            return "exterior square family"
        if typ in {"B", "C", "D"} and i == 1:
            return "vector/standard"
        if typ == "B" and i == rank:
            return "spin"
        if typ == "D" and i in {rank - 1, rank}:
            return "half-spin"
        return f"fundamental omega_{i}"
    if len(nonzero) == 1:
        i, c = nonzero[0]
        return f"{c}*omega_{i}"
    return "+".join(f"{c}w{i}" if c > 1 else f"w{i}" for i, c in nonzero)


def verdict(typ: str, rank: int, weight: tuple[int, ...], cdim: int, threshold: int) -> str:
    label = fundamental_label(typ, rank, weight)
    if typ == "A":
        if label == "standard or dual standard":
            return "sphere-transitive after realification"
        if rank == 2 and weight in {(2, 0), (0, 2)}:
            return "SU(3) symmetric-square complex type; real dimension 12 is safe"
        if rank == 3 and label == "exterior square family":
            return "Spin(6) vector/full SO(6) via A3=D3"
        return "nonstandard small complex candidate; check real type/low rank"
    if typ == "B":
        if label == "vector/standard":
            return "full SO block"
        if rank == 3 and label == "spin":
            return "Spin(7) spin; sphere-transitive but not dangerous over R"
        return "small candidate; expected safe"
    if typ == "C":
        if label == "vector/standard":
            return "quaternionic standard; real dimension doubles and is safe except Sp(1)U(1)"
        return "small candidate; expected safe"
    if typ == "D":
        if label == "vector/standard":
            return "full SO block"
        if rank == 4 and label == "half-spin":
            return "triality/full SO(8)"
        return "small candidate; expected safe"
    return "unknown"


def candidate_indices(typ: str, rank: int, threshold: int) -> list[int]:
    out: list[int] = []
    for i in range(rank):
        if typ == "A":
            fdim = comb(rank + 1, i + 1)
        elif typ == "B":
            if i == rank - 1:
                fdim = 2**rank
            else:
                fdim = comb(2 * rank + 1, i + 1)
                if i >= 2:
                    fdim -= comb(2 * rank + 1, i - 1)
        elif typ == "C":
            fdim = comb(2 * rank, i + 1)
            if i >= 2:
                fdim -= comb(2 * rank, i - 1)
        elif typ == "D":
            if i in {rank - 2, rank - 1}:
                fdim = 2 ** (rank - 1)
            else:
                fdim = comb(2 * rank, i + 1)
                if i >= 2:
                    fdim -= comb(2 * rank, i - 1)
        else:
            raise ValueError(typ)
        if fdim < threshold:
            out.append(i)
    return out


def small_reps(typ: str, rank: int, threshold: int, max_coeff: int) -> list[tuple[tuple[int, ...], int]]:
    indices = candidate_indices(typ, rank, threshold)
    rows: list[tuple[tuple[int, ...], int]] = []
    if not indices:
        return rows

    # Dimensions are monotone in dominant weight coefficients.  At each node,
    # test the current coefficient with all later candidate coefficients zero;
    # once that already reaches the threshold, larger coefficients and all
    # extensions can be pruned.
    weight = [0] * rank

    def dfs(pos: int) -> None:
        if pos == len(indices):
            if not any(weight):
                return
            tup = tuple(weight)
            cdim = weyl_dim(typ, tup)
            if cdim < threshold:
                rows.append((tup, cdim))
            return

        idx = indices[pos]
        for coeff in range(max_coeff + 1):
            weight[idx] = coeff
            for later_idx in indices[pos + 1 :]:
                weight[later_idx] = 0
            base_dim = weyl_dim(typ, tuple(weight))
            if base_dim >= threshold:
                break
            dfs(pos + 1)
        weight[idx] = 0

    dfs(0)
    rows.sort(key=lambda item: (item[1], item[0]))
    return rows


def scan(rank_limit: int) -> list[SmallRep]:
    max_dim = max(lie_dim("A", rank_limit), lie_dim("B", rank_limit), lie_dim("D", rank_limit))
    w = triangular_weights(max_dim)
    rows: list[SmallRep] = []
    for typ in ["A", "B", "C", "D"]:
        start = 1 if typ == "A" else 2
        if typ == "D":
            start = 4
        for rank in range(start, rank_limit + 1):
            if typ == "B" and rank == 2:
                # B2=C2; keep the C row.
                continue
            dim_g = lie_dim(typ, rank)
            threshold = w[dim_g]
            max_coeff = max(3, threshold)
            for weight, cdim in small_reps(typ, rank, threshold, max_coeff):
                label = fundamental_label(typ, rank, weight)
                rows.append(
                    SmallRep(
                        typ=typ,
                        rank=rank,
                        lie_dim=dim_g,
                        threshold=threshold,
                        weight=weight,
                        complex_dim=cdim,
                        label=label,
                        verdict=verdict(typ, rank, weight, cdim, threshold),
                    )
                )
    return rows


def main() -> None:
    rank_limit = 80
    rows = scan(rank_limit)
    suspicious = [
        row
        for row in rows
        if not (
            "sphere-transitive" in row.verdict
            or "full SO" in row.verdict
            or "safe" in row.verdict
            or "triality" in row.verdict
        )
    ]

    print(f"Classical Weyl scan up to rank {rank_limit}.")
    print(f"Complex irreps with dim_C < w(dim g): {len(rows)}")
    print(f"Rows not automatically classified by the script: {len(suspicious)}")
    print()

    by_verdict = Counter(row.verdict for row in rows)
    for verdict_text, count in sorted(by_verdict.items(), key=lambda item: (-item[1], item[0])):
        print(f"{count:3d}  {verdict_text}")
    print()

    if suspicious:
        print("Suspicious rows:")
    else:
        print("No suspicious rows remain after real/quaternionic type bookkeeping.")

    for row in suspicious:
        print(
            f"{row.typ}{row.rank:<2d} dimG={row.lie_dim:<5d} "
            f"w={row.threshold:<3d} dimC={row.complex_dim:<4d} "
            f"wt={row.weight!s:<22s} {row.label}; {row.verdict}"
        )


if __name__ == "__main__":
    main()

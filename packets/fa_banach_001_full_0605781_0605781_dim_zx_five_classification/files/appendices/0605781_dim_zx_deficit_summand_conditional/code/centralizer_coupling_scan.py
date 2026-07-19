"""Centralizer-coupling stress test for the Problem 27 deficit theorem.

This checks a sharper version of the reducible coupling step.  If a dangerous
standard atom on E is coupled to another irreducible summand F, then F has the
form U tensor_D D^m, where U is a nontrivial irreducible module for the
transitive semisimple factor and D=End_S(U).  The commuting part on F lies in
SO(m), U(m), or Sp(m), respectively.

For each relevant atom and centralizer type, this script checks the worst
case

    max_{0 <= l <= dim centralizer_full(m)} w(dim atom + l)
        <= dim E + dim F.

This is stronger than checking a particular compact subgroup L of the
centralizer, because it lets l range over every integer up to the full
centralizer dimension.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CouplingFamily:
    label: str
    atom_dim: int
    block_dim: int
    module_dim: int
    centralizer_type: str  # R, C, H


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


def centralizer_dim(kind: str, m: int) -> int:
    if kind == "R":
        return m * (m - 1) // 2
    if kind == "C":
        return m * m
    if kind == "H":
        return m * (2 * m + 1)
    raise ValueError(kind)


def dangerous_families(k_limit: int) -> list[CouplingFamily]:
    # These are deliberately minimal nontrivial modules for the semisimple
    # transitive factor.  Larger U only makes the inequality easier.
    families: list[CouplingFamily] = [
        CouplingFamily("U(2) atom, SU(2) adjoint occurrence", 4, 4, 3, "R"),
        CouplingFamily("U(2) atom, SU(2) quaternionic occurrence", 4, 4, 4, "H"),
        CouplingFamily("G2 atom, standard occurrence", 14, 7, 7, "R"),
    ]
    for k in range(3, k_limit + 1):
        families.append(
            CouplingFamily(f"SU({k}) atom, standard occurrence", k * k - 1, 2 * k, 2 * k, "C")
        )
        families.append(
            CouplingFamily(f"U({k}) atom, standard occurrence", k * k, 2 * k, 2 * k, "C")
        )
    # SU(4) has a smaller real-type nontrivial occurrence through Lambda^2.
    families.append(CouplingFamily("SU(4) atom, Lambda^2 real occurrence", 15, 8, 6, "R"))
    families.append(CouplingFamily("U(4) atom, Lambda^2 real occurrence", 16, 8, 6, "R"))
    return families


def main() -> None:
    k_limit = 300
    m_limit = 300
    max_n = 0
    families = dangerous_families(k_limit)
    for fam in families:
        max_n = max(max_n, fam.atom_dim + centralizer_dim(fam.centralizer_type, m_limit))
    w = triangular_weights(max_n)

    failures: list[str] = []
    checked = 0
    for fam in families:
        # Only dangerous atoms matter, but checking all listed families is cheap.
        if w[fam.atom_dim] <= fam.block_dim:
            continue
        for m in range(1, m_limit + 1):
            checked += 1
            cap = centralizer_dim(fam.centralizer_type, m)
            worst_l = max(range(cap + 1), key=lambda l: w[fam.atom_dim + l])
            lhs = w[fam.atom_dim + worst_l]
            rhs = fam.block_dim + fam.module_dim * m
            if lhs > rhs:
                failures.append(
                    f"{fam.label}, m={m}, l={worst_l}, w={lhs}, rhs={rhs}, cap={cap}"
                )
                if len(failures) >= 20:
                    break

    print(f"Centralizer-coupling families checked: {checked}")
    print(f"Failures: {len(failures)}")
    for failure in failures:
        print(failure)


if __name__ == "__main__":
    main()

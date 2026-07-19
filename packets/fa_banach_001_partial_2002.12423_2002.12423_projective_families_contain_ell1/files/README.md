# Candidate Partial Result: Principal Projective Families Contain `ell_1`

Source paper: A. Aviles, G. Martinez-Cervantes, and J. D. Rodriguez Abellan,
*On projective Banach lattices of the form `C(K)` and `FBL[E]`*,
arXiv:2002.12423.

Result type: `partial`

Status: candidate partial result, likely valid, pending human review.

## Source Problem

Problem 2 asks:

> If `X` is `infty`-projective and infinite-dimensional, must `X`
> contain a Banach subspace isomorphic to `ell_1`?

The packet does not solve the full arbitrary Banach lattice problem.

## Candidate Contribution

Two natural families from the source paper have a positive answer.

1. If `dim E >= 2`, then `FBL[E]` contains an isomorphic copy of `ell_1`.
   Hence every infinite-dimensional free Banach lattice of the form `FBL[E]`
   satisfies the conclusion of Problem 2, regardless of projectivity.

2. If a compact Hausdorff space `K` has a non-singleton connected component,
   then `C(K)` contains an isomorphic copy of `ell_1`. De Pagter--Wickstead
   prove that compact Hausdorff ANRs have only finitely many components.
   Since the source paper proves `C(K)` is `1^+`-projective exactly when
   `K` is a compact Hausdorff ANR, every infinite-dimensional projective
   lattice of the form `C(K)` satisfies the conclusion of Problem 2.

The first item is an agent-identified implication of Remark 9.32 in
Oikhberg--Taylor--Tradacete--Troitsky, *Free Banach lattices*,
arXiv:2210.00614. The second combines a short standard `C(K)` argument with
the finite-components theorem from de Pagter--Wickstead, *Free and Projective
Banach Lattices*, arXiv:1204.4282.

## Why This Is Only Partial

Problem 2 remains open for a general infinite-dimensional
`infty`-projective Banach lattice. The packet does not prove that an arbitrary
projective Banach lattice reduces to one of these source-paper families, or
that every lattice-homomorphic retract of a free Banach lattice contains
`ell_1`.

## Files

- `source_paper.pdf`: original arXiv PDF for arXiv:2002.12423.
- `supporting_paper_1204.4282.pdf`: supporting de Pagter--Wickstead paper.
- `supporting_paper_2210.00614.pdf`: supporting free Banach lattice paper.
- `figures/open_problem_crop.png`: crop of Problems 1--3 from the source.
- `figures/supporting_remark_crop.png`: crop of Remark 9.32.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates.

## Literature Check

On June 20, 2026, exact web searches for the Problem 2 wording and nearby
phrases found the source paper and nearby work on strong Nakano,
semiprojective, and free/projective Banach lattices, but no later paper
explicitly resolving Problem 2 in full. Remark 9.32 of arXiv:2210.00614 gives
the free-lattice subcase only after identifying that `ell_1` is separable.

## Human Review

Recommended checks: verify the use of Remark 9.32 for `FBL[E]`, the
one-dimensional free-lattice exception, and the de Pagter--Wickstead
finite-components theorem for compact Hausdorff ANRs.

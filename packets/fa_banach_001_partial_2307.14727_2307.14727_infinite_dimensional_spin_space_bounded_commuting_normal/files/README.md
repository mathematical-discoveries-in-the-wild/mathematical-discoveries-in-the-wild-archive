# Infinite-dimensional spin space for mild generalized spin-boson models

Status: `partial_result_likely_valid`.

Source: Sascha Lill and Davide Lonigro, *Self-adjointness and domain of
generalized spin-boson models with mild ultraviolet divergences*,
arXiv:2307.14727.

## Claim

The source paper proves its Case 1 self-adjointness/domain and norm-resolvent
regularization theorem for finite-dimensional spin space. Remark 1.5 says that
the infinite-dimensional spin-space case for bounded commuting normal
interaction operators should follow by spectral calculus, but is postponed.

This packet supplies that missing proof under a conservative hypothesis:

- the spin space is separable;
- the free spin Hamiltonian `K` is bounded self-adjoint;
- the finitely many interaction operators `B_j` are bounded, normal, pairwise
  commuting, and have zero common kernel;
- the source paper's mild-divergence Case 1 hypotheses on the form factors are
  unchanged.

Under these assumptions, the source paper's Theorem 1.3 remains valid with the
same domain formula and norm-resolvent convergence conclusion.

## Mechanism

The proof leaves Posilicano's abstract theorem and the source paper's
regularization estimates unchanged. The only missing point is the density of
`Ran A|_{H_2}` when there is no common eigenbasis. The joint spectral theorem
represents the commuting normal tuple as multiplication by coordinate functions.
Fiberwise, the operator `A` becomes an annihilation operator for a nonzero
linear combination of the `H`-independent form factors. The source paper's
annihilation-operator range lemma applies on almost every fiber, and a standard
orthogonal-complement argument gives global density of the range.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: source page containing Remark 1.5.

Ledger:
`runs/fa_banach_001/ledger/results/2307.14727_infinite_dimensional_spin_space_bounded_commuting_normal.json`

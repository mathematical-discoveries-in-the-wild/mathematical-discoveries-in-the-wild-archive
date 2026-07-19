# Type-(B) compact self-commutators

Status: **candidate full solution, likely valid; human review requested**

Source: Daniel Belti\c{t}\u{a}, Sasmita Patnaik, and Gary Weiss,
*$B(H)$-Commutators: A Historical Survey II and recent advances on
commutators of compact operators*, arXiv:1303.4844, Definition 4.1,
Question 4.10, and the open-problem discussion on PDF pages 12-13.

## Result

Let `J` be a conjugation on a separable infinite-dimensional complex Hilbert
space and set

`o_J = {X in K(H) : X = -J X* J}`.

Every self-adjoint `T in o_J` has a representation

`T = [Y*,Y]` with `Y in o_J`,

and one may choose `||Y|| <= sqrt(2) ||T||^(1/2)`.

Thus the type-(B) eigenvalue sequences are exactly the real null multisets in
which every nonzero `lambda` and `-lambda` have equal multiplicity.

## Proof Intuition

A single eigenvalue pair lives in `so(2,C)`, which is abelian. Grouping two
pairs gives an explicit `so(4,C)` self-commutator formula; if a finite-rank
operator leaves one pair over, a fixed kernel vector gives an `so(3,C)`
block. The block solutions obey a square-root norm estimate, so their norms
tend to zero with the eigenvalues and the infinite direct sum is compact.

## Packet Contents

- `solution_packet.pdf` / `main.tex`: theorem, explicit block formulas,
  compact direct-sum proof, spectral corollary, and novelty limits;
- `source_paper.pdf`: the arXiv PDF used for extraction;
- `figures/open_problem_crop.png`: the source's type-(B) open-problem passage;
- `code/verify_blocks.py`: symbolic formula checks and 1,000 randomized
  orthogonal-conjugacy tests;
- `verification.md`: adversarial proof review and verifier output.

## Human Review Recommendation

Check the signs and cross-term cancellation in the `so(3)`/`so(4)` formulas,
the `J`-real spectral basis, the lone-pair kernel-vector case, and compactness
of the block direct sum. No unproved mathematical dependency remains.
Novelty remains provisional because the bounded primary-literature search is
not an exhaustive historical-priority search.

# Partial Result Packet: Quantifier-Free Oscillation Stability in Hilbert Operator Structures

Run: `fa_banach_001`

Status: `partial_result`

Source target: James Hanson, *Indiscernible Subspaces and Minimal Wide Types*,
arXiv:2004.03062.

## Source Question

Hanson asks in Question 4.3 whether model-theoretic stability implies
oscillation stability: if `T` is a stable Banach theory, must every unary
formula be oscillation stable on models of `T`?

The arXiv metadata says this preprint was absorbed into arXiv:2011.00610,
*Strongly Minimal Sets and Categoricity in Continuous Logic*. The corrected
absorbing paper keeps the same question in Section 6.

## Result

This packet proves a positive operator-Hilbert subcase and then transfers it to
several named stable Hilbert-operator theories.

Base theorem:

> Let `H` be an infinite-dimensional Hilbert space in the standard many-sorted
> Banach/Hilbert operator language, expanded by any collection of bounded
> linear operator symbols. For every quantifier-free unary formula `phi(x,a)`
> whose one-variable atoms are norms of operator-linear terms, every
> infinite-dimensional closed subspace `Y` of `H`, and every `epsilon>0`, there
> is an infinite-dimensional closed subspace `Z subset Y` such that `phi` has
> oscillation at most `epsilon` on the unit sphere of `Z`.

The base theorem does not require model-theoretic stability.

Transfer theorem:

> If a complete Hilbert-operator theory has quantifier elimination, or uniform
> reduction of unary formulas, to the quantifier-free operator formulas handled
> above, then every unary formula in that theory is oscillation stable.

Named stable classes covered:

- Hilbert spaces expanded by a bounded normal operator `T`, in the language
  with `T` and `T*`. Berenstein--Cuervo Ovalle--Goldbring prove QE and
  stability/superstability for the completions.
- The self-adjoint and unitary one-operator subcases in the original language.
- Hilbert spaces expanded by a unitary representation of a finite group.
  Berenstein--Perez prove QE and `aleph_0`-stability.

## Idea

A unary quantifier-free formula only sees finitely many Hilbert norms of terms
`Sx+b`, where `S` is a finite linear combination of operator words and `b` is a
parameter vector. On an infinite-dimensional subspace one first removes the
linear terms by passing to a finite-codimensional subspace. The remaining
variation is controlled by finitely many quadratic forms
`<S^*Sx,x>`. A diagonal orthonormal-subsequence argument gives an
infinite-dimensional subspace on which all those quadratic forms are
simultaneously almost scalar. Uniform continuity of the formula then gives
small oscillation.

## Scope And Limitations

- This is not a full answer to Question 4.3.
- It covers quantifier-free unary formulas in the standard operator-linear
  Hilbert/Banach language.
- It gives full positive answers for the named stable Hilbert-operator
  quantifier-elimination classes above.
- It does not cover arbitrary stable Banach theories or arbitrary stable
  expansions by wild unary predicates.

## Evidence

- `source_paper.pdf`: arXiv:2004.03062.
- `supporting_absorbing_paper_2011.00610.pdf`: corrected absorbing paper.
- `supporting_normal_operator_qe_2507.21894.pdf`: normal-operator QE and
  stability support.
- `supporting_finite_group_actions_qe_2409.03923.pdf`: finite-group-action QE
  and stability support.
- `figures/open_problem_crop.png`: crop of Question 4.3 from source PDF page 8.
- `main.tex` / `solution_packet.pdf`: proof packet.

## Novelty Check

Local indexes were searched for `2004.03062`, `Indiscernible Subspaces`,
`minimal wide`, `oscillation stability`, and related phrases. Web searches for
the exact stability/oscillation-stability question and close variants found the
source paper but no later explicit answer. Further literature search found
arXiv:2507.21894 and arXiv:2409.03923 as named stable Hilbert-operator QE
classes to which the transfer theorem applies.

## Human Review Recommendation

Review as a strengthened partial result. The key points to check are the
simultaneous quadratic-form flattening lemma, the QE transfer step, and that
the cited normal-operator/finite-group-action quantifier-elimination theorems
indeed reduce unary formulas to the operator-linear atoms handled here.

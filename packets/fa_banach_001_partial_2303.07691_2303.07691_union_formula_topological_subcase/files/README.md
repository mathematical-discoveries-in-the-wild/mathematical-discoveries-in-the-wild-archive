# Strengthened Partial Packet: Union Formula For `(I)`-Envelopes

Source paper: Ondrej F. K. Kalenda and Matias Raja, *Topologies related to
`(I)`-envelopes*, arXiv:2303.07691.

Result type: `partial`

Status: stronger partial result, likely valid, pending human review. The full
Question 5.1 remains open.

## Source Question

Question 5.1 asks whether, for convex sets `A,B subset X^*` with `A union B`
also convex, one always has

```text
(I)-env(A union B) = (I)-env(A) union (I)-env(B).
```

The packet does not answer this in full generality.

## Upgrade Summary

The earlier active packet recorded only the topological/no-`ell^1` subcase:
if `(I)-env(S)` is the closure of `co S` in a fixed topology for every
`S subset X^*`, then finite-union closure gives the formula; by Theorem 3.3
of the source paper this applies when `X` contains no isomorphic copy of
`ell^1`.

The June 22 report confirms that this topological argument is correct but is
already the implication `(1) => (2)` in the source paper's Theorem 4.3, with
the no-`ell^1` case supplied by Theorem 3.3. It then adds stronger positive
cases:

- the formula holds when `A union B` is already `(I)`-closed;
- the formula holds when `A union B` is norm separable;
- the formula holds in every Banach space when `A union B` is an affine
  subspace of the underlying real vector space of `X^*`.

Thus any counterexample must live in a space containing `ell^1`, have
non-norm-separable union, have genuinely non-affine union, and fail to be
`(I)`-closed.

## Files

- `main.tex`: consolidated strengthened partial packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 5.1 from the source paper.
- `evidence/2026_06_22_union_formula_I_envelopes/`: supplied TeX/PDF report.
- `history/2026_06_22_pre_upgrade/`: previous June 14 topological-subcase
  packet files.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Literature Status

The supplied report records a literature search through June 22, 2026 and did
not locate a full proof or counterexample. The packet therefore keeps the
classification as partial, not full.

## Human Review

Recommended checks:

- verify the source-paper citations for Theorems 3.3 and 4.3;
- check the sequential separation criterion used for `(I)`-envelopes;
- review the geometric lemma that two proper closed convex sets covering a
  Banach space must be parallel half-spaces with possible slab overlap;
- verify the affine-union proof, especially the cancellation of the two
  separating sequences.

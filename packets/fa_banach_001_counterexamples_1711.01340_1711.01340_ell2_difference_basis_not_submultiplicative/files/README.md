# Rejected Packet: `ell_2` Difference Basis Counterexample

Run: `fa_banach_001`

Status: human reviewed; rejected as a solution to the intended problem.

Source paper: Pavlos Motakis, Daniele Puglisi, Andreas Tolias,
*Algebras of diagonal operators of the form scalar-plus-compact are Calkin
algebras*, arXiv:1711.01340.

Source target: Section 8, Problem 7 asks whether, if a Banach space `X` has a
convex block homogeneous basis `(e_i)`, then the difference sequence

```text
d_1 = e_1,   d_{i+1} = e_{i+1} - e_i
```

makes `X` submultiplicative when endowed with `(d_i)`.

## Claimed Counterexample

The automatic packet takes `X = ell_2` with its usual unit vector basis and
checks that the associated difference sequence is not submultiplicative. The
finite coefficient calculation is correct.

## Human Review

The candidate is rejected because `ell_2` with its usual unit vector basis does
not satisfy the source hypothesis.

The packet treats convex block homogeneity as equivalence to normalized block
sequences. In the source context, following Argyros--Motakis--Sari, a convex
block homogeneous sequence is equivalent to its convex block sequences
themselves. These convex blocks are not renormalized.

For the `ell_2` unit vector basis, long equal-average convex blocks

```text
y_k = |B_k|^{-1} sum_{i in B_k} e_i,   |B_k| -> infinity
```

have norm `|B_k|^{-1/2} -> 0`, so they are not equivalent to the normalized
unit vector basis. Thus the proposed example fails the defining hypothesis.

There is also a secondary warning: the difference sequence in `ell_2` is not a
Schauder basis of `ell_2`, since the inverse coordinate map involves unbounded
partial summation.

## Files

- `source_paper.pdf`: local copy of arXiv:1711.01340.
- `figures/open_problem_crop.png`: crop containing Problem 7.
- `main.tex`: original automatic packet source.
- `solution_packet.pdf`: rendered automatic packet.
- `human_review.tex`: human rejection note source.
- `human_review.pdf`: rendered human rejection note.
- `bundle_with_review.pdf`: original packet followed by the human review.
- `code/verify_triangular_counterexample.py`: finite sanity check for the
  packet's coefficient calculation.

## Review Outcome

Reject this candidate as a proposed counterexample to Problem 7. It may be
archived as a cautionary example showing that the precise definition of
`convex block homogeneous` must be preserved.

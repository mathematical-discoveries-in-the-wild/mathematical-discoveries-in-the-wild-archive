# Full solution packet: normability of the higher complex Sobolev quasinorm

## Source

- Paper: Thai Duong Do and Duc-Bao Nguyen, *Higher complex Sobolev spaces on
  complex manifolds*
- arXiv: `2405.06385`
- Source location: Remark 2.4, page 8 of the arXiv PDF.

## Classification

- Status: `full_solution_likely_valid`
- Result type: positive answer to the equivalent-norm question.
- Scope: both local and global higher complex Sobolev spaces `W_q^*` with the
  source paper's quasinorm `||.||_{*,q}`.

## Result

Let `B = {phi in W_q^* : ||phi||_{*,q} <= 1}`. The convex hull `co(B)` is
bounded in the same quasinorm. Therefore the Minkowski functional of `co(B)`
is a genuine norm equivalent to `||.||_{*,q}`.

In particular, contrary to the suspicion in Remark 2.4, an equivalent norm
does exist for every `q >= 1`; when the source's completeness proposition is
used, this norm makes `W_q^*` a Banach space.

## Proof Idea

The unit ball controls each level of a defining sequence separately: the
mass/constant at level `j` is at most one. If `phi` is a convex combination of
unit-ball elements, take the same convex combination at every defining level.
Convex combinations of psh/qpsh functions stay psh/qpsh, and Jensen's
inequality for positive `(1,1)`-forms gives

```text
d(sum theta_i phi_i) wedge d^c(sum theta_i phi_i)
  <= sum theta_i d phi_i wedge d^c phi_i.
```

Thus the level-`j` mass/constant of the convex combination is still at most
one. The quasinorm of every point in `co(B)` is consequently bounded by
`q+1`. Kolmogorov's normability criterion, or directly the Minkowski
functional of `co(B)`, gives the equivalent norm.

## Files

- `main.tex`: expert-facing solution packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/remark_2_4_normability_question_crop.png`: crop of the source
  question.
- `code/verify_convex_bound.py`: finite-dimensional sanity check for the
  Jensen and convex-hull bounds.
- `tmp/`: render/build intermediates.

## Novelty Check

The run indexes had no exact prior packet for `2405.06385` or this
normability question. A bounded web search on 2026-07-03 for the exact title,
the phrase "It is interesting to know if we can build a norm", and
`W^*_q`/complex Sobolev quasinorm terms found only the arXiv source paper and
no later answer.


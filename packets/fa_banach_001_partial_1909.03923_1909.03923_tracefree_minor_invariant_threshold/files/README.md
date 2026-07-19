# Partial result: trace-free scalar-shift minor invariants

Status: partial result, subject to human review.

Source paper: arXiv:1909.03923, Andre Guerra and Bogdan Raita,
*Quasiconvexity, null Lagrangians, and Hardy space integrability under
constant rank constraints*.

## Source Question

Question 5.17 asks for conditions on a projection

```text
T:R^{m x n}->V
```

under which there is a nonzero linear combination `H_s` of `s`-minors,
`2 <= s < min{m,n}`, satisfying

```text
H_s(X)=H_s(X+Y) for every X and every Y with T(Y)=0.
```

Equivalently, `H_s` is a minor-combination depending only on the coordinates of
`V`. The source page is included as `figures/open_question_page.png`.

## Result Proved

This packet solves a natural one-dimensional-kernel slice. Let

```text
T(X)=X-(tr X/n)I
```

be the orthogonal projection from `R^{n x n}` onto the trace-free matrices.
Then, for `2 <= s < n`, there is a nonzero `s`-minor combination satisfying

```text
H_s(X)=H_s(X+tI) for every X and t
```

if and only if

```text
2s <= n.
```

When `2s <= n`, any `s`-minor whose row and column sets are disjoint is an
example. When `2s > n`, every invariant linear combination is zero.

## Proof Idea

Adding `tI` only changes diagonal entries. If `2s <= n`, one can choose
disjoint row and column sets of size `s`, so the corresponding minor never sees
the diagonal and is invariant.

For the converse, write `H_s` as a sum of minors `M_{I,J}`. Invariance under
`X+tI` implies that the derivative in the identity direction vanishes. The
coefficient of an `(s-1)`-minor `M_{A,B}` in this derivative is a signed sum of
the coefficients `c_{A union {a}, B union {a}}` over indices outside
`A union B`. If `2s > n`, every pair `I,J` of `s`-sets intersects. A descending
induction on `|I union J|` first kills coefficients with full union and then
isolates all remaining coefficients.

## Scope and Limitations

This is not a full answer to Question 5.17. It handles the trace-free
projection, equivalently a one-dimensional kernel spanned by the identity in
the square case. It does not classify arbitrary projections `T`, nor does it
describe the full invariant space when `2s <= n`.

## Novelty Check

Cheap run indexes were searched for `1909.03923`, `trace-free`, `traceless`,
`scalar-shift`, `minor invariant`, and the source question keywords. No
duplicate packet was found.

A bounded web check on July 19, 2026 searched exact phrases from Question 5.17,
the arXiv id, and trace-free/scalar-shift minor keywords. I found the source
paper and preprint records but no exact answer to this slice.

## Verification

- `main.tex` contains the proof.
- `solution_packet.pdf` was compiled from `main.tex`.
- `code/check_tracefree_threshold.py` checks the contraction-kernel threshold
  for `3 <= n <= 7` using exact rational row reduction.
- Source PDF: `source_paper.pdf`.
- Source question page: `figures/open_question_page.png`.

## Human-Review Recommendation

Check the derivative coefficient formula and the descending-union induction.
Those are the entire proof of the nonexistence direction.

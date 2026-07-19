# Partial result: one-dimensional kernel minor invariants

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

This packet solves the full one-dimensional-kernel case. Let

```text
T:R^{m x n}->V
```

be a linear projection whose kernel is `span{A}`, with `A` nonzero of rank
`r`. For `2 <= s < min{m,n}`, there is a nonzero linear combination of
`s`-minors satisfying

```text
H(X)=H(X+tA) for every X and t
```

if and only if

```text
2s <= m+n-r.
```

The previous trace-free scalar-shift packet is the special case
`m=n`, `A=I_n`, and `r=n`.

## Proof Idea

Invertible row and column changes reduce the kernel generator `A` to
`diag(I_r,0)`, and Cauchy-Binet preserves the vector space spanned by
`s`-minors. In that normal form, adding `tA` changes only the first `r`
diagonal entries.

If `2s <= m+n-r`, one can choose row and column sets of size `s` with no
common active index among `1,...,r`; the corresponding minor never sees a
shifted diagonal entry and is invariant.

If `2s > m+n-r`, every pair of row and column `s`-sets has a common active
index. Differentiating in the direction `diag(I_r,0)` gives linear equations
whose terms add the same active index to row and column sets. A descending
induction on the active union size first isolates the coefficients with full
active union and then all remaining coefficients.

## Scope and Limitations

This is a partial answer to Question 5.17. It fully classifies projections with
one-dimensional kernel, but it does not classify arbitrary higher-dimensional
kernels.

In the positive range, the packet proves existence by giving one invariant
minor. It does not describe the full dimension or basis of the invariant
subspace.

## Novelty Check

Cheap run indexes were searched for `1909.03923`, `trace-free`, `scalar-shift`,
`minor invariant`, `one-dimensional kernel`, `rank threshold`, and the source
question keywords. The only overlapping run result was the earlier trace-free
slice, which is strictly subsumed by this packet.

A bounded web check on July 19, 2026 searched exact phrases from Question 5.17,
the arXiv id, and minor-invariant/projection keywords. I found the source paper
and preprint records but no exact answer to this one-dimensional-kernel
classification.

## Verification

- `main.tex` contains the proof.
- `solution_packet.pdf` was compiled from `main.tex`.
- `code/check_onedim_kernel_threshold.py` checks the derivative-kernel
  threshold for small rectangular dimensions and all ranks using exact rational
  row reduction.
- Source PDF: `source_paper.pdf`.
- Source question page: `figures/open_question_page.png`.

## Human-Review Recommendation

Check three points:

- Cauchy-Binet really preserves the space of `s`-minor combinations under
  invertible row and column changes.
- The pigeonhole threshold for avoiding a common active index is exactly
  `2s <= m+n-r`.
- The descending induction on active union size isolates every coefficient in
  the nonexistence range.

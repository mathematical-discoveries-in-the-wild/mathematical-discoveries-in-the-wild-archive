# Dual log-BM equality-case counterexample

Status: `counterexample_likely_valid`

Source paper: Christos Saroglou, *More on logarithmic sums of convex
bodies*, arXiv:1409.4346; published in *Mathematika* 62 (2016), 818-841.

## Result

The source paper proves the dual logarithmic Brunn-Minkowski inequality and
then says that its equality cases seem likely to match the equality cases in
the log-Brunn-Minkowski conjecture, with non-symmetric bodies allowed.  The
packet gives a planar equality example outside the natural source-style
product/dilate pattern.

Let

```text
x1 = (2,0),       x2 = (0,1),
x3 = (-1,1/2),   x4 = (0,-1),
P_t = conv{x1, e^t x2, x3, e^t x4}.
```

Put `K = P_0^circ` and `L = P_1^circ`.  Then for every `0 < lambda < 1`,

```text
| (lambda K +_0 (1-lambda) L)^circ |
  = |K^circ|^lambda |L^circ|^(1-lambda).
```

The equality holds because `area(P_t) = e^t area(P_0)`.  The true logarithmic
sum has polar containing `P_{1-lambda}`, while Saroglou's dual inequality gives
the reverse volume bound, so equality is forced.

At the same time `K` is not a two-dimensional product body in the source-style
sense: `P_0 = K^circ` does not split into two pairs of vertices on two lines
through the origin.  Also `L` is not a dilate of `K`.

## Scope

This is not a counterexample to Saroglou's dual log-Brunn-Minkowski
inequality.  It is a counterexample to the proposed equality-case analogy if
that analogy is read as excluding non-product, non-homothetic planar pairs.
The packet does not attempt a full classification of equality cases.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: source page crop showing Theorem 6.1 and
  the equality-case comment.
- `code/check_quadrilateral_equality.py`: exact/rational sanity checks for the
  polygon area and non-product obstruction.
- `tmp/`: LaTeX build intermediates.

## Novelty Check

Cheap run indexes were searched for `1409.4346`, the source title,
`log-Brunn`, `dual log-Brunn-Minkowski`, `equality cases`, `B-conjecture`,
`cone-volume`, and related log-Minkowski terms.  No prior packet for this
paper or this equality-case route was found.

A bounded web search on 2026-07-18 for exact and nearby phrases including
`dual log-Brunn-Minkowski equality cases`, `Saroglou dual B-conjecture equality
cases polytopes`, and the source title found the source article and later
general log-BM literature, but no existing equality-case classification or
counterexample for this Section 6 comment.

## Human Review

Recommended verdict: likely valid counterexample to the equality-case analogy,
with narrow scope.  Reviewers should mainly check whether their intended
interpretation of the source's informal equality-case comment is indeed the
source-style product/dilate equality pattern addressed here.

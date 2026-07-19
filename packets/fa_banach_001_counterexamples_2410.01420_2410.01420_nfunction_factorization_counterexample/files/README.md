# 2410.01420 N-function factorization counterexample

- `status`: candidate counterexample likely valid; construction tightened on 2026-07-03
- `agent_id`: `agent_lane_08`
- `lane`: 8
- `date`: 2026-07-03
- `source arXiv`: 2410.01420
- `source paper`: Tomasz Kiwerski and Jakub Tomaszewski, *A few last words on pointwise multipliers of Calderon-Lozanovskii spaces*
- `target`: Problem 6.a.1
- `packet`: `solution_packet.pdf`

## Claim

Problem 6.a.1 asks whether, if `F`, `G`, and `G ominus F` are all N-functions, one must have

```tex
F^{-1}(G \ominus F)^{-1} \approx G^{-1}.
```

The packet gives a negative answer.

The counterexample takes `G(t)=t^2` and constructs an N-function `F` through a concave inverse
`A=F^{-1}`. The inverse `A` is chosen to satisfy `A(u)/sqrt(u) -> 0`, so `F` grows faster than
quadratically and `H=G ominus F` is again an N-function, but `A` has arbitrarily long almost-linear
stretches. Along those stretches,

```tex
F^{-1}(u_n) H^{-1}(u_n) / G^{-1}(u_n) -> 0,
```

so the desired equivalence fails.

## Verification

The proof is analytic and constructive; no computation is needed. A follow-up validation pass
tightened the piecewise-linear inverse construction so that interval control, unboundedness, and
the right-continuous inverse convention are explicit. The key estimate is

```tex
H^{-1}(u) <= inf_s sqrt(F(s)+u)/s
```

for `H=G ominus F` and `G(t)=t^2`. Taking `s=F^{-1}(u_n y_n)` on a long linear stretch of
`F^{-1}` gives the failure of lower comparability.

## Search Notes

Local run indexes had no exact packet for `2410.01420`. Web searches for the exact inverse relation,
`G ominus F`, N-functions, and the paper title found the source arXiv record but no later answer to
Problem 6.a.1. Novelty confidence is moderate-to-high pending human review of the constructed
piecewise-linear inverse.

## Files

- `source_paper.pdf`: source paper PDF from arXiv.
- `figures/open_problem_crop.png`: crop of Problem 6.a.1 on page 25.
- `main.tex`: packet source.
- `solution_packet.pdf`: rendered packet.

# Counterexample: weak-to-strong Hardy norm law below `p=2`

status: likely_valid_counterexample
run_id: fa_banach_001
agent_id: agent_lane_07
arxiv_id: 1505.01945
created_at: 2026-06-14T20:22:00Z

## Source Problem

Source: Jussi Laitila and Hans-Olav Tylli, *Composition operators on
vector-valued analytic function spaces: a survey*, arXiv:1505.01945.

Question 19(a), on PDF page 17, asks whether the norm estimate in part (2) of
Theorem 18 extends from `2 < p < infinity` to `1 <= p < 2`.  Part (2) says
that for infinite-dimensional complex Banach spaces `X`,

```text
||C_phi : wH^p(X) -> H^p(X)|| is equivalent to ||C_phi||_{HS}^{2/p}
```

for `2 < p < infinity`.

## Result

The extension to `1 <= p < 2` is false, already for `X=ell_2`.

For the radial symbols `phi_r(z)=rz`, `0<r<1`, and every `1 <= p <= 2`,

```text
||C_{phi_r} : wH^p(ell_2) -> H^p(ell_2)|| = ||C_{phi_r}||_{HS}
                                               = (1-r^2)^(-1/2).
```

When `1 <= p < 2`, this is not comparable to
`||C_{phi_r}||_{HS}^{2/p}` as `r -> 1`.

## Packet Contents

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1505.01945.
- `figures/open_problem_crop.png`: crop of Theorem 18 and Question 19.

## Novelty Check

Local run indexes had no hit for `1505.01945`, the weak-to-strong Hardy
question, or the radial-dilation counterexample.  Bounded web searches on
2026-06-14 for exact phrases around `wH^p(X)`, `H^p(X)`,
`Hilbert-Schmidt`, `1 <= p < 2`, `radial dilation`, and the paper title found
the source paper but no later exact answer.  Human review should still check
non-arXiv operator-theory literature, since the argument is short enough that
it may have been observed informally.

## Human Review Recommendation

Check that the source question intended uniform equivalence constants
independent of the symbol.  Under that standard reading, the family
`phi_r(z)=rz` is a direct negative answer to Question 19(a).

# Harmonic counterexample for the power-profile `f`-greedy question

Status: `counterexample_likely_valid`

Source paper: Pablo M. Berna and Hung Viet Chu, *On Some Characterizations of
Greedy-type Bases*, arXiv:2201.12029.

## Target

The first future-research question in the source asks which functions `f` make
the `f`-greedy inequality

```text
||x - G_m(x)|| <= C_f D_m^f(x)
```

equivalent to ordinary greediness.  The source proves this for regular `f`,
constructs non-greedy examples for sparse `f`, and explicitly points to
`f(n)=1/n^p`, `p>0`, as an example outside both classes.

## Counterexample

For every `p>0`, let

```text
X = { x in c0 : sum_n |x_n|/n < infinity },
||x|| = max( sup_n |x_n|, sum_n |x_n|/n ).
```

The canonical unit vector basis is normalized, 1-unconditional, and Schauder.
It is not democratic: initial intervals `{1,...,m}` have norm comparable to
`log m`, while `m`-point sets far out have norm `1`.

Nevertheless the basis is `f_p`-greedy for `f_p(n)=n^{-p}`.  If `Lambda` is
the order-`m` greedy set of `x`, and `A` is any `m`-point competitor set, then
for `z=x-alpha 1_{f_p,A}` one has

```text
||x-P_Lambda x|| <= (3+2/p) ||z||.
```

Taking the infimum over `alpha` and `A` gives the `f_p`-greedy inequality.
Thus `f_p`-greediness does not imply greediness for any `p>0`.

## Relation to the Earlier Partial

This packet supersedes the earlier partial theorem as the answer to the named
power-profile subproblem.  That partial packet is now kept under
`history/log_democracy_partial/`.  The partial theorem remains true and
explains why the counterexample has exactly harmonic/logarithmic democracy
growth.

## Novelty / Duplicate Check

Cheap run indexes were searched for `2201.12029`, `f-greedy`, `D_m^f`,
`power-profile`, `1/n^p`, and the earlier partial packet.  Web searches on
2026-06-21 for exact phrases around `f-greedy n^{-p} counterexample`,
`D_m^f harmonic greedy basis`, and the source title with `1/n^p` found no
matching later answer.  The construction appears to be new in the run memory.

## Files

- `main.tex`: full proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `history/log_democracy_partial/`: earlier partial theorem showing the
  logarithmic democracy obstruction, retained as proof history.

Human-review recommendation: check the weighted `ell_1(1/n)` estimate in the
proof of `f_p`-greediness, especially the matching of a missed competitor
coordinate with a selected coordinate outside the competitor set.

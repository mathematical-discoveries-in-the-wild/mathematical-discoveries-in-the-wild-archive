# Full projection classification for the operator alpha-ratio/Reiter questions

Status: `candidate_full_solution_likely_valid_needs_human_review`

Source paper: arXiv:1701.05537, Nicolas Monod, *Fixed points in convex
cones*.

## Claim

Problems 47 and 48 ask to clarify the operator `alpha`-ratio and
`alpha`-Reiter properties for unitary representations on Hilbert space,
especially when `alpha` ranges over nonzero projections.

This packet gives the full projection classification:

- For every unitary representation and every bounded nonzero operator
  `alpha`, the operator `alpha`-ratio property holds. Hence every unitary
  representation satisfies the projection-ratio side of Problem 48.
- For arbitrary bounded `alpha`, the operator `alpha`-Reiter property is
  exactly absence of an `alpha`-spectral gap:

```text
sum_{s in S} ||alpha(pi(s)v - v)||^2 >= c ||alpha v||^2 for all v
```

  must fail for every finite `S` and every `c > 0`.
- A unitary representation satisfies the operator `P`-Reiter property for
  every nonzero orthogonal projection `P` if and only if the representation is
  trivial.

The last item also settles the convention where "projection" means an
arbitrary bounded idempotent: orthogonal projections are included among those,
and trivial representations satisfy Reiter for every operator.

## Key mechanism

If `pi(g)` is not the identity, the spectral theorem gives a nonzero spectral
projection `P` for `pi(g)` on a Borel set separated from `1`. Since `P`
commutes with `pi(g)`,

```text
||P(pi(g)v - v)|| = ||(pi(g)-I)Pv|| >= delta ||Pv||
```

for all `v`. Thus `P`-Reiter fails for the one-element set `{g}`.

## Relation to the Earlier Partial Packet

The earlier packet
`solutions/partial/1701.05537_operator_alpha_ratio_reiter_clarification/`
proved the automatic ratio property, the general spectral-gap criterion, and
finite-rank projection criteria. It is now absorbed into this full packet under
`absorbed_packets/partial/`.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - crop containing Problems 47 and 48.
- `code/crop_open_problem.py` - script used to create the crop.

## Novelty check

The local run indexes were searched for arXiv:1701.05537 and the terms
`operator alpha-ratio`, `operator alpha-Reiter`, `fixed points in convex cones`,
and `projection alpha classification`. Web searches for exact phrases such as
`"operator alpha-ratio"`, `"operator alpha-Reiter"`,
`"operator alpha-Reiter" "projection"`, and `"Fixed points in convex cones"
"Problem 48"` returned the source paper but no later explicit solution of
Problems 47/48. Human review should still check for terminology variants in
the representation-theory literature.

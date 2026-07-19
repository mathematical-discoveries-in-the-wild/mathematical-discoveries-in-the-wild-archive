# Counterexample: sigma-directional porosity is not separably determined

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source paper: arXiv:1309.2174, Marek Cuth, Martin Rmoutil and Miroslav
Zeleny, *On Separable Determination of Sigma-P-Porous Sets in Banach
Spaces*.

## Claim

For the fixed-direction convention for `sigma`-directional porosity cited in
the source paper's Question after Remark 4.8, separable determination in the
sense of Corollary 5.11 fails.

Let `Gamma` be uncountable, let `X = ell_2(Gamma)`, and set

```text
A = {x in X : x_gamma = 1 for at least one gamma in Gamma}.
```

Then `A` is closed, hence Suslin.  It is not `sigma`-directionally porous in
`X`, but for every separable linear subspace `V` of `X`, the section `A cap V`
is `sigma`-directionally porous in `V`.

## Key mechanism

Any countable cover by fixed-direction porous pieces uses only countably many
direction vectors.  In `ell_2(Gamma)`, those vectors have countable coordinate
support, so there is a coordinate `gamma` invisible to all of them.  The affine
hyperplane `{x : x_gamma = 1}` is contained in `A`; inside it all proposed
directions are tangent, and the porous pieces become nowhere dense.  Baire's
theorem gives the contradiction.

On the other hand, every separable subspace of `ell_2(Gamma)` is supported on
countably many coordinates, so it sees `A` as only a countable union of proper
affine hyperplanes.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - page 11 crop containing the open question.

## Novelty check

Before promotion, the local run indexes and local arXiv source corpus were
searched for `1309.2174`, `sigma-directional porosity`, `directional porosity`,
and `separably determined`; no packet or later local answer to this exact
question was found.  Web searches for exact phrases around
`"sigma-directional porosity" "separably determined"` and close variants did
not return an explicit later solution.  Human review should still verify the
definition in Zajicek's cited paper, since the source explicitly warns that the
LPT convention is different outside separable spaces.

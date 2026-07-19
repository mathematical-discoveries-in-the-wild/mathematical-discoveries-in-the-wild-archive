# Almost exposed points in real L1 are atomic

Status: candidate partial result, likely valid. This is not a full solution of the
open problem about extremality of surjective isometries of the closed unit ball
of `L^1[0,1]`.

Source paper: Christian Bargetz, Michael Dymond, Katriin Pirk, "On extremal
nonexpansive mappings", arXiv:2409.04292.

Packet files:

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/l1_gap_crop.png`: source crop showing the explicit `L^1[0,1]`
  extremality gap.
- `figures/almost_exposed_definition_crop.png`: source crop of Definition 3.6.
- `figures/open_problem_crop.png`: source crop of Remark 3.7.
- `figures/method_condition_crop.png`: source crop showing why almost exposed
  points are used for the nonlinear extremality theorem.

## Claim

Let `(Omega,Sigma,mu)` be a real measure space and let `B` be the closed unit
ball of `L^1(mu)`. If `f` is a unit vector and `A={f != 0}`, then the
intersection of all hyperplanes supporting `B` at `f` consists exactly of
the functions `g=sign(f) q`, where `q >= 0`, `q` is supported in `A`, and
`int_A q dmu = 1`.

Consequently, `f` is almost exposed in `B` if and only if `A` is a measure
atom. In that case `f` is also exposed. Thus, in real `L^1(mu)` spaces, every
almost exposed point of the unit ball is exposed. In particular, the closed
unit ball of atomless `L^1[0,1]` has no almost exposed points.

## Relevance

The source paper asks whether almost exposed points may differ from exposed
points and uses the closed convex hull of almost exposed points as the key
hypothesis in its nonlinear theorem. The characterization above answers that
almost-exposed/exposed comparison inside the broad class of real `L^1(mu)`
spaces and shows that the source paper's almost-exposed convex-hull method
cannot settle the remaining classical `L^1[0,1]` case: for Lebesgue measure
there are no almost exposed points at all.

## Verification and novelty notes

The proof is analytic and self-contained. No computational verifier is needed.
The bounded duplicate check searched the run indexes for `2409.04292`,
`extremal nonexpansive`, `almost exposed`, and `L^1[0,1]`, with no exact
packet hit. A web search on 2026-06-19 for exact phrases around
`almost exposed L^1 unit ball` and the source paper's `L^1[0,1]` extremality
gap did not reveal a later answer. Novelty is therefore plausible but still
requires human mathematical review.

Primary review focus: check the support-functional description and the
singleton criterion for probability densities on a measurable support. The
packet is deliberately stated for real `L^1`; a complex version would need a
separate convention for real supporting hyperplanes and unimodular signs.

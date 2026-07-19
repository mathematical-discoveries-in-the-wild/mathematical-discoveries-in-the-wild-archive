# Surjective isometries of the real L1[0,1] ball are extremal

Status: candidate full solution, likely valid, pending human review.

Source paper: Christian Bargetz, Michael Dymond, Katriin Pirk, "On extremal
nonexpansive mappings", arXiv:2409.04292.

## Claim

Let `B` be the closed unit ball of real `L^1[0,1]`. The identity map on `B`
is an extreme point of the convex set of nonexpansive self-maps `B -> B`.
Consequently, by the source paper's reduction lemma, every surjective isometry
`B -> B` is extremal among nonexpansive self-maps.

More generally, the proof works for real `L^1(mu)` over an atomless probability
space.

## Mechanism

Assume

```text
id = (1-lambda)F + lambda G,  0 < lambda < 1,
```

with `F,G` nonexpansive. The source paper already observes that `F` and `G`
must be isometries. For any unit vector `f`, norming functionals force `F(f)`
and `G(f)` to stay in the minimal norming face of `f`: same sign and no mass
outside `supp(f)`.

This face preservation plus isometry first fixes all signed normalized
indicators, then all signed simple unit vectors, hence the whole unit sphere.
Finally, an isometry of the ball that fixes the sphere is forced to fix the
interior, because distances to signed normalized indicators recover the
positive and negative parts locally on an atomless measure space.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered full-solution candidate.
- `source_paper.pdf`: local copy of arXiv:2409.04292.
- `figures/open_problem_crop.png`: source crop showing the `L^1[0,1]` gap.
- `figures/method_condition_crop.png`: source crop showing the prior
  almost-exposed method condition.
- `history/packets/partial_packet_2409.04292_l1_almost_exposed_atoms_2026_06_21/`:
  earlier almost-exposed-points partial packet preserved as superseded history.

## Verification and novelty notes

The proof is self-contained apart from the source paper's standard reduction
from surjective isometries to the identity and its observation that the two
summands in a decomposition of an isometry must themselves be isometries.

The bounded duplicate check found only the earlier lane-8 partial packet
`2409.04292_l1_almost_exposed_atoms`, which is superseded by this full
candidate. Web searches on 2026-06-19 for the exact `L^1[0,1]` extremality
phrases and related "extreme nonexpansive mappings L1" terms found no later
answer. Human review should focus especially on Lemma 3, where distances to
signed normalized indicators are used to recover an arbitrary interior point.

Scope limitation: this packet is stated for real `L^1`; the complex case would
need a separate formulation using real supporting hyperplanes and phase
functions.

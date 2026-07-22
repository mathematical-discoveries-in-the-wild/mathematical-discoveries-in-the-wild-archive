# Finite primitive sets are synthetic for p-adic unipotent Orlicz algebras

Status: `candidate_partial_likely_valid`  
Agent: `agent_lane_02`  
Model: `GPT5.6`  
Date: 2026-07-21

## Source

Max Carter, *Weighted Orlicz \(*\)-algebras on locally elliptic groups*,
arXiv:2503.20735v2, Question 8.12, page 29; Studia Mathematica 287(2)
(2026), 145-180.

Question 8.12 asks which geometric properties of a subset of the coadjoint
orbit/primitive spectrum imply spectral synthesis for a Hermitian weighted
Orlicz algebra on a unipotent p-adic group.

## Upgraded result

Let `G` be a locally elliptic CCR group and let
`A = L^Phi(G,omega)` satisfy Carter's Section 7 hypotheses:
`Phi in Delta_2`, `1/omega in L^Psi(G)`, and `A` Hermitian. Then every finite
subset of `Prim_*(A)` is a set of synthesis.

Consequently, for every p-adic unipotent matrix group `N`, every finite subset
of

`n^*/Ad^*(N) = Prim_*(L^Phi(N,omega))`

is a set of synthesis. This includes finite sets of genuinely
infinite-dimensional irreducible representations for nonabelian `N`.

The previous abelian result is retained: if `G` is abelian and locally
elliptic, every compact-open subset of the Pontryagin dual is also synthetic.

## Proof mechanism

1. Compact-open idempotents form an approximate identity in the weighted
   Orlicz algebra.
2. If `G` is CCR, an irreducible representation maps each such idempotent to
   a compact projection, hence a finite-rank fixed-vector projection.
3. After smoothing by a fixed compact-open subgroup, the evaluation map at a
   finite primitive set therefore has finite-dimensional range. A bounded
   finite-dimensional lift corrects dense test functions so that they vanish
   exactly at every chosen primitive point.
4. Every compactly supported locally constant test function belongs to a
   finite-dimensional Hecke algebra. Its central support projection is
   annihilated by the chosen representations and Carter's smooth functional
   calculus puts that projection exactly in `m(C)`. Hence the corrected test
   function lies in `j(C)`.

## Scope

This gives a complete geometric criterion--finiteness--for every nonabelian
p-adic unipotent group in the source question. The question itself is
open-ended, so the packet remains classified as a substantial partial answer:
it does not classify infinite subsets of a nontrivial coadjoint-orbit space.

## Files

- `main.tex` - upgraded theorem and proof
- `solution_packet.pdf` - compiled review packet
- `source_paper.pdf` - original arXiv paper
- `figures/open_problem_crop.png` - full-width crop of Question 8.12
- `verification.md` - proof audit
- `history/abelian_finite_compact_open_packet_2026-07-21/` - superseded narrower packet
- `tmp/` - LaTeX and rendering intermediates

## Novelty check

Local run indexes and bounded arXiv searches on 2026-07-21 used the exact
arXiv id and combinations of `spectral synthesis`, `p-adic unipotent`,
`finite sets`, `singleton`, `primitive spectrum`, and `weighted Orlicz`.
No exact prior finite-set theorem was located. Carter explicitly says that
even treating the full group algebra of a p-adic unipotent group would be
novel. Novelty confidence remains moderate pending expert citation review.

## Human review recommendation

Check the finite-corner lifting lemma and the central-support projection step
inside a finite Hecke algebra. Also confirm that Carter's CCR statement makes
every compact-open fixed-vector projection finite rank. These are the only
new ingredients beyond the source functional calculus and approximate
identity.


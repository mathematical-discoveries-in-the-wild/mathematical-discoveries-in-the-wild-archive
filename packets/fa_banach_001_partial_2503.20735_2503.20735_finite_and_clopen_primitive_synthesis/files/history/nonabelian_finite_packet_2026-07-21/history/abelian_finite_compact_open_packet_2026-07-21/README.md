# Finite and compact-open synthesis for abelian locally elliptic Orlicz algebras

Status: `candidate_partial_likely_valid`  
Agent: `agent_lane_02`  
Model: `GPT5.6`  
Date: 2026-07-21

## Source

Max Carter, *Weighted Orlicz \(*\)-algebras on locally elliptic groups*,
arXiv:2503.20735v2, Question 8.12, page 29; Studia Mathematica 287(2)
(2026), 145-180.

Question 8.12 asks which geometric properties of a subset of the coadjoint
orbit/primitive spectrum imply that it is a set of synthesis for the
Hermitian weighted Orlicz algebra.

## Result

Let `G` be an abelian locally elliptic group and let
`A = L^Phi(G, omega)` satisfy the source paper's Section 7 hypotheses:
`Phi in Delta_2`, `1/omega in L^Psi(G)`, and `A` Hermitian. Under
`Prim_*(A) = dual(G)`, the packet proves:

1. every finite subset of `dual(G)` is a set of synthesis;
2. every compact-open subset of `dual(G)` is a set of synthesis.

Consequently, both criteria hold for the additive unipotent group
`U_2(k) = (k,+)` over every non-archimedean local field `k`.

The key lemma constructs the inverse Fourier transform of a compact-open
indicator as an exact element of Carter's generating set `m(C)`, via the
paper's smooth functional calculus.

## Scope

This is a partial answer to the broad question. It does not treat nonabelian
unipotent groups, nontrivial coadjoint orbit spaces, or arbitrary closed sets.

## Files

- `main.tex` - theorem and proof
- `solution_packet.pdf` - compiled review packet
- `source_paper.pdf` - original arXiv paper
- `figures/open_problem_crop.png` - full-width crop of Question 8.12
- `verification.md` - independent proof checklist
- `tmp/` - LaTeX and rendering intermediates

## Novelty check

On 2026-07-21, bounded arXiv searches combined the terms `weighted Orlicz`,
`spectral synthesis`, `p-adic`, `finite sets`, and `compact open sets`, and
the source's nearby cited discussion was checked. No exact prior statement of
this weighted-Orlicz criterion was found. Novelty confidence is moderate, not
definitive.

## Human review recommendation

Review the `Delta_2` density argument and the exact membership of the Fourier
cutoff in the source-defined set `m(C)`. The rest is a finite interpolation
or compact-open projection argument.


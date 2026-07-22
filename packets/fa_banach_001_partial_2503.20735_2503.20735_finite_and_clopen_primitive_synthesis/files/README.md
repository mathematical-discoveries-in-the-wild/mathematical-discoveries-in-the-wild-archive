# Finite and clopen primitive sets are synthetic

Status: `candidate_partial_likely_valid`  
Agent: `agent_lane_02`  
Model: `GPT5.6`  
Date: 2026-07-21

## Source

Max Carter, *Weighted Orlicz \(*\)-algebras on locally elliptic groups*,
arXiv:2503.20735v2, Question 8.12, page 29; Studia Mathematica 287(2)
(2026), 145-180.

The question asks which geometric properties of a subset of the
coadjoint-orbit/primitive spectrum imply spectral synthesis for a Hermitian
weighted Orlicz algebra on a unipotent p-adic group.

## Strongest result

Let `G` be locally elliptic and let `A=L^Phi(G,omega)` satisfy Carter's
Section 7 hypotheses: `Phi in Delta_2`, `1/omega in L^Psi(G)`, and `A`
Hermitian.

1. Every clopen subset of `Prim_*(A)` is a set of synthesis.
2. Every finite closed set consisting of admissible primitive points is a set
   of synthesis.
3. If `G` is CCR, every finite subset of `Prim_*(A)` is covered by (2).

Consequently, for every p-adic unipotent matrix group `N`, every finite or
clopen subset of

`n^*/Ad^*(N) = Prim_*(L^Phi(N,omega))`

is a set of synthesis. This includes finite sets of genuinely
infinite-dimensional irreducible representations and clopen subsets in
non-Hausdorff orbit spaces.

This is close to the strongest possible statement based only on elementary
size/topology conditions.  Malliavin's theorem implies that already for the
unweighted abelian algebra `L^1(k)` on `U_2(k)=(k,+)`, there is a compact
closed coadjoint-spectrum subset which is not synthetic.  Thus compactness
or closedness alone is insufficient.

## New clopen mechanism

For a compact-open subgroup `H`, the corner `e_H*A*e_H` is a unital
Hermitian semisimple Banach star algebra. A clopen primitive subset splits its
primitive spectrum into two closed pieces. Their kernel ideals are
complementary, producing a central self-adjoint idempotent `p_H` which is zero
on the chosen set and one on its complement.

The idempotent need not be compactly supported. Approximate it in the Orlicz
norm by self-adjoint Hecke functions. Riesz projections of those approximants
remain inside finite-dimensional Hecke algebras, vanish exactly on the chosen
primitive set, and converge to `p_H`. Carter's smooth functional calculus
already puts every algebraic kernel element in `j(C)`, so `p_H in j(C)`.
Compact-open smoothing then gives `ker(C)=j(C)`.

## Scope

This supplies two broad geometric criteria--finiteness and clopenness--for
the complete nonabelian class in Question 8.12. The source question is an
open-ended research program rather than a binary conjecture, so the packet
remains a substantial partial result. Infinite closed subsets with nonempty
boundary in a nonabelian orbit space are not classified. The added Malliavin
obstruction proves that a universal all-closed or all-compact extension is
false even for the one-dimensional abelian member of the class.

## Files

- `main.tex` - unified theorem and proof
- `solution_packet.pdf` - compiled review packet
- `source_paper.pdf` - original arXiv paper
- `figures/open_problem_crop.png` - full-width crop of Question 8.12
- `verification.md` - independent proof audit
- `references/` - Malliavin and de Leeuw--Mirkil source papers for the compact
  nonsynthesis obstruction
- `history/nonabelian_finite_packet_2026-07-21/` - superseded finite-only packet
- `tmp/` - LaTeX and rendering intermediates

## Novelty check

Local run indexes and bounded arXiv searches on 2026-07-21 used the exact
arXiv id and combinations of `spectral synthesis`, `p-adic unipotent`,
`clopen`, `compact-open`, `finite sets`, `central idempotent`, `primitive
spectrum`, and `weighted Orlicz`. No exact finite-or-clopen theorem for these
algebras was located. Novelty confidence is moderate pending expert citation
review.

## Human review recommendation

First check the standard primitive-spectrum correspondence for the idempotent
corner `e_H*A*e_H`. Then check the complementary-kernel construction of
`p_H` and the claim that finite-Hecke Riesz projections converge to `p_H` in
the Orlicz norm while remaining in `ker(C)`. These are the decisive new steps.

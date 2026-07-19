# Extreme Points of `Ext(F)`

Status: `candidate_full_solution_likely_valid`

Source: Palle Jorgensen, Steen Pedersen, and Feng Tian, "Extensions of Positive Definite Functions: Applications and Their Harmonic Analysis", arXiv:1507.02547.

## Result

Question 3.1 asks for a characterization of the extreme points of the compact convex set `Ext(F)` of positive-definite extensions.

This packet gives an exact characterization in the locally compact Abelian / Bochner-measure formulation used in the question:

> `mu in Ext(F)` is extreme iff there is no nonzero real `h in L^\infty(mu)` such that the signed measure `h dmu` has Fourier transform zero on the observed set `Omega^{-1} Omega`.

Equivalently, the real linear span of the observed characters is dense in `L^1(mu; R)`.

The earlier compact-support theorem is retained as a corollary: in the Euclidean case, every compactly supported extension measure is extreme, and there is at most one compactly supported extension measure for a fixed local `F`.

## Scope

This is a full abstract characterization of the measure-valued `Ext(F)` in the locally compact Abelian setting of Question 3.1. It is not a parametrization by a smaller list of named measures, and it does not claim to classify non-Abelian unitary-representation extension triples outside the Bochner-measure model.

## Files

- `main.tex` - solution packet source
- `solution_packet.pdf` - rendered packet
- `source_paper.pdf` - arXiv source paper
- `figures/open_problem_crop.png` - crop of Question 3.1 from page 65

## Verification

No computational verification is needed. Human review should focus on whether the source's Question 3.1 is intended in this measure-valued LCA sense; under that reading, the bounded-perturbation/density criterion is necessary and sufficient.

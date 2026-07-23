# Rieffel-deformed completely positive maps: full resolution

Status: `candidate_full_solution_likely_valid` (new proof, subject to human
review).

## Source questions

Adam Skalski and Ami Viselter, *Convolution semigroups on Rieffel
deformations of locally compact quantum groups*, arXiv:2311.04630;
*Letters in Mathematical Physics* 114 (2024), article 52.

Questions 4.7 and 4.8 on PDF page 26 ask whether an equivariant
nondegenerate completely positive map remains nondegenerate after Rieffel
deformation, and whether a point-norm continuous semigroup of such maps
remains point-norm continuous after deformation.

## Full answer

Both questions have affirmative answers for every locally compact abelian
deformation group.

For Question 4.7, Landstad duality identifies the source's nondegenerate
crossed-product extension with `S^Psi cross Gamma`. Crossing once more and
using Takai duality identifies the double extension with
`S^Psi tensor id_K`. The double extension is nondegenerate, and
nondegeneracy of a stabilization reflects to the original completely
positive map.

For Question 4.8, the crossed-product extensions form a point-norm continuous
semigroup on the whole crossed product by an `L1` estimate on
`C_c(Gamma,A)`. The Landstad algebra is a generalized fixed-point algebra.
On its dense compactly supported averaging core, continuity follows from the
bounded averaging maps of Buss--Echterhoff, Lemma 2.5(4); contractivity
extends continuity to the full deformed algebra.

## Files and verification

- `solution_packet.pdf`: review-ready full proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original open-question paper.
- `supporting_paper_1304.5697.pdf`: Buss--Echterhoff generalized
  fixed-point machinery.
- `figures/open_questions_crop.png`: full-width crop of Questions 4.7--4.9.
- `code/make_open_questions_crop.py`: reproducible crop script.
- `tmp/`: isolated LaTeX and page-render artifacts.

The six-page packet was compiled twice without warnings, rendered page by
page, and visually inspected. Human review should focus on Takai naturality for completely
positive maps and the identification of the Landstad algebra with the
generalized fixed-point completion used by the averaging argument.

## Novelty check

A bounded search on 23 July 2026 used the exact question wording, source
title and authors, citation searches for arXiv:2311.04630, and combinations
of Takai duality, crossed-product completely positive maps, generalized
fixed-point algebras, nondegeneracy, and point-norm continuity. No explicit
answer or prior statement of these arguments was found. This is not an
exhaustive novelty certification.

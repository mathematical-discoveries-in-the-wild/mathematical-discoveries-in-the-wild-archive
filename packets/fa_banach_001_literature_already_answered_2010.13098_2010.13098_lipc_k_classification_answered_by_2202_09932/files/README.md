# Literature Status: Lip0(C(K)) Classification

Status: `literature_already_answered (Lip_0 half of Question 1)`

Target paper:

- Leandro Candido and Pedro L. Kaufmann, "On the geometry of Banach spaces of the form Lip_0(C(K))", arXiv:2010.13098, Proc. Amer. Math. Soc. 149 (2021), 3335-3345.
- Source location: Section 3, p. 3, Question 1.
- Local PDF: `source_paper.pdf`.

Supporting answer:

- Leandro Candido and Hector H. T. Guzman, "On large ell_1-sums of Lipschitz-free spaces and applications", arXiv:2202.09932, Proc. Amer. Math. Soc. 151 (2023), 1135-1145.
- Answer location: Introduction, p. 2, Theorem 3 and Corollary 4.
- Local PDF: `supporting_paper_2202.09932.pdf`.

## Identification

Question 1 in arXiv:2010.13098 asks, for an infinite Hausdorff compactum
`K` of weight `kappa`, when one can guarantee either
`F(C(K)) ~ F(c_0(kappa))` or, at the dual level,
`Lip_0(C(K)) ~ Lip_0(c_0(kappa))`. The source paper proves partial
dual-level cases, including compacta in its class `B` with cellularity equal
to the weight.

Candido and Guzman later prove a complete classification of `Lip_0(X)` for
`L_p` spaces. In the case `p = infinity`, their Theorem 3 gives
`Lip_0(X) ~ Lip_0(c_0(kappa))` for every `L_infty` space `X` of density
`kappa`. Since every `C(K)` is an `L_infty` space and
`dens(C(K)) = weight(K)` for infinite compact Hausdorff `K`, their Corollary 4
states directly that
`Lip_0(C(K)) ~ Lip_0(c_0(kappa))` for every infinite Hausdorff compact `K` of
weight `kappa`.

The supporting authors explicitly knew the connection: the supporting paper
cites the Candido-Kaufmann paper as reference [5] and says Corollary 4 extends
the main result of [5] in the dual setting.

## Scope

This packet clears the "at least Lip_0" half of Question 1. It does not claim
that the free-space half
`F(C(K)) ~ F(c_0(kappa))` is answered in general.

## Search Evidence

Cheap run indexes had no exact row for arXiv:2010.13098. Local source
inspection isolated Question 1. Web/arXiv search for `Lip(C(K))`,
`Lip(c_0(kappa))`, and the paper title found arXiv:2202.09932, whose abstract
and p. 2 corollary give the general `Lip_0(C(K))` classification. The
supporting paper cites the target paper explicitly, so this is recorded as
`literature_already_answered`.

Ledger record:
`runs/fa_banach_001/ledger/results/2010.13098_lipc_k_classification_answered_by_2202_09932.json`

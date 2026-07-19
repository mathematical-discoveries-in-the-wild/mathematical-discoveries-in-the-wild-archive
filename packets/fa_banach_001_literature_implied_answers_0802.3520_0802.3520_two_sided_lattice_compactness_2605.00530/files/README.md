# Literature-Implied Status: arXiv:0802.3520

Status: `literature_implied_answer (two-sided lattice compactness conjecture; recent preprint; human verification recommended)`.

## Source Question

Michael Cwikel, "Complex interpolation of compact operators mapping into lattice couples," arXiv:0802.3520, 2008.

The target is the subsection "Two sided interpolation of compactness" near the end of the paper. In the local TeX source `data/parsed/arxiv_sources/0802.3520/source.tex`, lines 1005--1021, Cwikel observes that even the two-sided endpoint assumption
`T: A_j -> B_j` compact for both `j=0,1` was not known to imply compactness
`T: [A_0,A_1]_theta -> [B_0,B_1]_theta`. He then conjectures the implication for arbitrary source couples `A` whenever the range couple `B` is an arbitrary lattice couple, without Fatou or sigma-order-continuity assumptions.

## Supporting Literature

Evgeniy Pustylnik, "A new approach to interpolation of compact linear operators," arXiv:2605.00530, posted 2026-05-01.

The decisive local source passages are in `data/parsed/arxiv_sources/2605.00530/Pustilnyk-Arxiv.tex`:

- lines 270--284: the paper states that compactness is interpolated automatically whenever one has standard interpolation of bounded operators, first for two-sided compactness, while one-sided compactness requires an additional condition;
- lines 342--344: the complex interpolation functor is explicitly included, with `W(alpha,beta)=alpha^(1-theta) beta^theta` for the one-sided condition;
- lines 592--596: the same proof is said to apply to two-sided compactness of embedding operators without the one-sided inequality;
- lines 598--610: the paper passes from embeddings to arbitrary operators by factoring through image spaces.

## Identification

Cwikel's conjecture is a two-sided compactness statement for the complex interpolation functor, restricted on the range side to arbitrary lattice couples. Pustylnik's 2026 preprint claims a broader abstract interpolation result: two-sided compactness for embeddings under standard interpolation of bounded operators, and then a reduction from embeddings to arbitrary operators. Applying that reduction to a two-sided compact operator `T` gives compact image embeddings at both endpoints; combining this with the two-sided embedding statement yields compactness on the interpolated spaces. Since complex interpolation is explicitly covered, the claimed theorem implies Cwikel's two-sided lattice-couple conjecture, and in fact more, if the preprint proof is accepted.

This is an agent-identified implication. The supporting paper does not appear, from the checked text, to explicitly cite arXiv:0802.3520 or announce that it resolves this particular conjecture. Because arXiv:2605.00530 is a very recent broad preprint about a long-standing compactness-interpolation problem, this packet should be human-reviewed before being treated as settled.

## Packet Contents

- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:0802.3520.
- `supporting_paper_2605.00530.pdf`: arXiv:2605.00530.
- ledger: `runs/fa_banach_001/ledger/results/0802.3520_two_sided_lattice_compactness_2605.00530.json`.

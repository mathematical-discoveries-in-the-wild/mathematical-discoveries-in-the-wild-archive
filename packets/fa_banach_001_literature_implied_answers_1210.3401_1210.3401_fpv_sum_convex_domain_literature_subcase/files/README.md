# Literature-Implied Answer: FPV Sum Problem With Convex Domain

## Source Question

- Source paper: J. M. Borwein and L. Yao, *Recent progress on Monotone Operator Theory*, arXiv:1210.3401.
- Location: Section "Open problems in Monotone Operator Theory", p. 33 of the arXiv PDF.
- Source question: Let `A, B: X -> X*` be maximally monotone with `dom A cap int dom B != empty`. Assume that `A` is of type (FPV). Is `A+B` necessarily maximally monotone?

## Status

`literature_implied_answer (partial subcase)`.

The later paper J. M. Borwein and L. Yao, *Sum theorems for maximally monotone operators of type (FPV)*, arXiv:1305.6691, proves Corollary 4.3, "Convex domain": if `A` and `B` are maximally monotone, `dom A cap int dom B != empty`, and `A` is of type (FPV) with convex domain, then `A+B` is maximally monotone.

Thus the 1210.3401 FPV sum problem is answered affirmatively in the convex-domain subcase. The unqualified source problem remains open in this packet: arXiv:1305.6691 immediately asks whether the star-shaped/domain hypothesis in its theorem can be relaxed or dropped, and a later claimed full answer, arXiv:1411.6199, is withdrawn by the author because of an error in Lemma 1.

## Scope

- This is not an original proof.
- This does not settle the source problem without the added convex-domain hypothesis on `dom A`.
- It also gives the corresponding normal-cone subcase when the same theorem's star-shaped hypothesis applies, but it does not settle the full Simons normal-cone question as stated in arXiv:1210.3401.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source arXiv paper 1210.3401.
- `supporting_paper_1305.6691.pdf`: supporting arXiv paper proving the convex-domain subcase.

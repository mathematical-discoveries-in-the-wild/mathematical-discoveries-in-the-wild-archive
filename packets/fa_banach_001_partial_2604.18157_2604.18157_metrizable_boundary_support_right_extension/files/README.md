# Metrizable boundary support for the Right-topology extension question

Status: `partial_likely_valid`

Source paper: Stepan Ondrej and Jiri Spurny, "Operators on injective tensor products of L1-preduals", arXiv:2604.18157v1, 2026.

Source question: Question 6.7 asks whether Theorem 6.5(b) holds without the assumption that the L1-predual `X` is separable. Equivalently, for the extension `S:C(B_{X^*},E)->F` of a strongly bounded operator `T:X \hat{\otimes}_\varepsilon E -> F`, does `T` being pseudo weakly compact or Right completely continuous imply that `S` has the same property in the nonseparable case?

Partial result: The missing implication `T => S` holds if the representing measure has semivariation uniformly tight on compact metrizable homogeneous subsets of `ext B_{X^*}`. More precisely, for every `eta>0` there is compact metrizable homogeneous `L_eta subset ext B_{X^*}` with `||G||(B_{X^*}\setminus L_eta)<eta`.

Scope: This recovers the source paper's separable proof mechanism and also covers nonseparable cases with metrizable boundary support for the control/semivariation. It does not settle Question 6.7 for arbitrary nonseparable L1-preduals and arbitrary maximal control measures.

Novelty check: Local run indexes were searched for `2604.18157`, `Operators on injective tensor products of L1-preduals`, `pseudo weakly compact`, `Right completely continuous`, `q:metriz`, and nearby injective tensor product terms. No duplicate packet for this question was found. A web search on 2026-06-28 for the title, exact question label/phrase, and the Right-topology terms found only the source arXiv paper and no later answer.

Files:

- `main.tex`: expert-facing partial proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2604.18157v1.
- `figures/open_problem_crop.png`: crop of Question 6.7 from page 28 of the source PDF.

Human-review recommendation: Check the selection lemma under the compact-metrizable boundary support hypothesis and the use of antihomogeneous representing measures in the approximation estimate. These are the only delicate points; the Right-topology argument then follows the source proof of Theorem 6.5(b).

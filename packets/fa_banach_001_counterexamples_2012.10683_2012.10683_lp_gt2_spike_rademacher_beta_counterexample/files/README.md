# Counterexample packet: 2012.10683 Question 4

Status: `candidate_counterexample_likely_valid`

Source: Manuel Gonzalez, Antonio Martinez-Abejon, and Antonio Martinon, "Disjointly non-singular operators on Banach lattices", arXiv:2012.10683.

Question addressed: Question 4 on PDF page 9 asks whether, for `2 < p < infinity`, every dispersed subspace `M` of `L_p` satisfies `beta(Q_M)=1` for the quotient map `Q_M:L_p -> L_p/M`.

Claim: The answer is negative for every `2 < p < infinity`. For any `0 < eta < 1` there is a dispersed subspace `M` of `L_p(0,1)` such that `beta(Q_M) <= eta`.

Construction: split the interval into a disjoint spike region and a Rademacher region. Let `f_n` be normalized disjoint indicators in the first region and let `u_n` be normalized Rademacher functions on the second region. For `0 < b < a`, set `g_n = a f_n + b u_n` and `M = [g_n]`. The Rademacher part makes `[g_n]` isomorphic to `ell_2`, hence dispersed by Propositions 3.4 and 3.5 of the source paper. But `a^{-1}g_n` is within `b/a` of `f_n`, so the disjoint normalized sequence `(f_n)` witnesses `beta(Q_M) <= b/a < 1`.

Packet contents:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of PDF page 9 containing Question 4.

Novelty check: Cheap indexes were searched for `2012.10683`, `disjointly non-singular`, `DNS`, and `beta(Q_M)`. The only relevant exact source hits were the original paper and one later paper citing the positive `p<2` case. Later DNS papers arXiv:2101.06566 and arXiv:2302.04514 were checked locally and by web search; they record/order-continuous positive DNS results and further questions, but no `p>2` quotient counterexample was found in this bounded search.

Human review focus: check that the cited source result "isomorphic to `ell_2` implies strongly embedded/dispersed in `L_p` for `p>2`" is being applied in the intended isomorphic form, and that the quotient-distance estimate correctly uses the same normalized disjoint spike sequence.

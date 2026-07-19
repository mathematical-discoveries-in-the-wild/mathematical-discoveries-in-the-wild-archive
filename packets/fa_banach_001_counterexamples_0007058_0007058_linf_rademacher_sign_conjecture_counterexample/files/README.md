# Counterexample to the printed sign conjecture in arXiv:math/0007058

Status: `candidate_counterexample_likely_valid`

Source paper: S. J. Montgomery-Smith and E. M. Semenov, *Embeddings of rearrangement invariant spaces that are not strictly singular*, arXiv:math/0007058, Positivity 4 (2000), 397-404.

Targeted source statement: Conjecture 3 on PDF page 2 asks for a constant \(c\) such that, for every rearrangement invariant space \(E\) on \([0,1]\) and every \(x_1,\ldots,x_n\in L_1\), some choice of signs satisfies
\[
\left\|\sum_i \epsilon_i x_i\right\|_{L_1}
\ge c^{-1}\left\|\sum_i r_i\|x_i\|_1\right\|_E.
\]

Counterexample: take \(E=L_\infty[0,1]\) and \(x_i=r_i\), the first \(n\) Rademacher functions. Then the right side equals \(c^{-1} n\), while for every sign choice the left side is at most \(\sqrt n\). No fixed finite \(c\) can work for all \(n\).

Important scope note: this packet refutes Conjecture 3 as printed. It does not refute Conjecture 2; in fact, later literature records the Conjecture 2 classification as known for symmetric/rearrangement invariant spaces.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:math/0007058.
- `supporting_paper_2406.14175.pdf`: local later-paper context for the known Conjecture 2 classification.
- `figures/source_conjectures_crop.png`: crop of Conjectures 2 and 3 in the source.
- `code/make_conjecture_crop.py`: reproducible crop script.

Novelty/literature check: local run indexes and web searches did not show an existing packet for arXiv:0007058 or this sign-conjecture counterexample. The later 2024 paper `2406.14175` records Conjecture 2's classification as known, but it does not address this printed Conjecture 3 edge case.

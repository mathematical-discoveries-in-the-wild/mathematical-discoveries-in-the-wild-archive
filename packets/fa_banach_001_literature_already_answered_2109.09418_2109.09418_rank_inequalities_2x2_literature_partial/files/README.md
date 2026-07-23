# Literature correction: the 2-by-2 rank-order subcase

Status: `literature_already_answered (partial subcase)`.

For the orbit-closure/rank-inequality question at the end of Section 6 of
Derksen--Klep--Makam--Volčič, arXiv:2109.09418, the later paper of
Domokos--Miklósi, arXiv:2604.22609, explicitly proves the full equivalence for
tuples of `2 x 2` matrices over an algebraically closed field (Corollary 3.3).
Their Theorem 5.4 also covers all nilpotent `3 x 3` tuples.

The independent proof developed in this run translates rank inequalities into the Hom order and classifies the
possible two-dimensional module `M_B`. If it is semisimple, two elementary
Hom tests force isomorphism. If it is a nonsplit extension `0 -> S -> M_B ->
T -> 0`, tests with `S` and `M_B` force either isomorphism or the split module
`S direct-sum T`, which is the unique boundary degeneration needed.

Review focus: verify the rank-pencil-to-Hom-order implication with the source's
rectangular matricization/padding convention, and the self-extension case in
the final paragraph of the proof.

Files:

- `solution_packet.pdf`: literature-corrected review document with the independent proof
- `main.tex`: source
- `source_paper.pdf`: arXiv source paper
- `supporting_paper_2604.22609.pdf`: later paper containing Corollary 3.3
- `figures/open_problem_crop.png`: source question on paper page 15

The earlier novelty assessment was incorrect because it missed arXiv:2604.22609.
The proof remains valid, but it is not a new partial result. The general
stabilized/virtual-degeneration question remains open.

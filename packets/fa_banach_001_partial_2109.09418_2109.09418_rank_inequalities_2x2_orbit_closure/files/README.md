# Rank inequalities imply orbit degeneration for 2-by-2 tuples

Status: `partial_result_likely_valid` (human review requested).

For the orbit-closure/rank-inequality question at the end of Section 6 of
Derksen--Klep--Makam--Volčič, arXiv:2109.09418, this packet proves the full
equivalence for tuples of `2 x 2` matrices over an algebraically closed field.
In fact no zero stabilization is needed: the rank inequalities imply that
`A` itself lies in the orbit closure of `B`.

The proof translates rank inequalities into the Hom order and classifies the
possible two-dimensional module `M_B`. If it is semisimple, two elementary
Hom tests force isomorphism. If it is a nonsplit extension `0 -> S -> M_B ->
T -> 0`, tests with `S` and `M_B` force either isomorphism or the split module
`S direct-sum T`, which is the unique boundary degeneration needed.

Review focus: verify the rank-pencil-to-Hom-order implication with the source's
rectangular matricization/padding convention, and the self-extension case in
the final paragraph of the proof.

Files:

- `solution_packet.pdf`: review document
- `main.tex`: source
- `source_paper.pdf`: arXiv source paper
- `figures/open_problem_crop.png`: source question on paper page 15

Novelty confidence is modest. A bounded exact-phrase search through
2026-07-22 found no later resolution of the general virtual-degeneration/hom-
order question, but this elementary dimension-two subcase may be folklore.

# Positive answer for Kaufmann's cusp question

Status: `full_solution_candidate_likely_valid`

Source: Pedro L. Kaufmann, *Products of Lipschitz-free spaces and applications*, arXiv:1403.6605.

Question addressed: on page 14, after Proposition 5.1, the source asks whether
`F(Cusp)` is isomorphic to a subspace of `L1`, where
`Cusp = {(x,0): x >= 0} union {(x,x^2): x >= 0}` with the Euclidean metric.

Claim: yes. The packet proves that `F(Cusp)` is isomorphic to a subspace of an
`L1` space.

Proof mechanism: replace the Euclidean cusp, up to bi-Lipschitz equivalence, by
the two rails of a weighted ladder graph. The ladder has rungs at
`{1/n}` near the origin and at the positive integers at infinity. The rails are
1-complemented in the full ladder free space by linear extension across the
rungs. The ladder free space is an `L1` edge space modulo its cycle space; a
chosen fundamental-cycle basis gives a bounded projection onto that cycle
space, so the quotient is isomorphic to a subspace of `L1`.

Novelty check: cheap run indexes had no direct `1403.6605` packet. Local later
source citation search for Kaufmann/`1403.6605` found citations but no cusp
answer. Exact web searches for `"F(Cusp)" "L^1"`, `"1403.6605" "Cusp"
"Lipschitz-free"`, and related phrases found no direct later answer. This is a
bounded search, not a full bibliographic review.

Files:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: downloaded arXiv source PDF.
- `figures/open_problem_crop.png`: crop of the source problem.

# Full Packet: Height `omega_2` Scattered Compact `r`-Trees Are Valdivia

Run: `fa_banach_001`

Result type: `full`

Status: claimed full positive solution, likely valid, needs human review.

## Source Problem

- Tommaso Russo and Jacopo Somaglia, *Banach spaces of continuous functions
  without norming Markushevich bases*, arXiv:2305.11737.
- Source location: page 15, Problem 5.9.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Problem 5.9 asks whether every scattered compact `r`-tree `T` with
`ht(T)=omega_2` must be Valdivia.

## Claimed Answer

Yes. The packet proves the slightly stronger induction statement needed at the
boundary: a scattered compact `r`-tree of height at most `omega_2` is Valdivia.
The case `ht(T)<omega_2` is Russo--Somaglia Corollary 5.7; the new part is the
exact boundary `ht(T)=omega_2`.

## Proof Mechanism

The proof uses Cantor-Bendixson rank instead of height. Assume a minimal-rank
counterexample at height `omega_2`. Russo--Somaglia's decomposition of
scattered trees splits the tree into pairwise disjoint clopen lower-rank
subtrees plus a finite union of chains. Collapse each lower-rank clopen piece
to a marker node. The quotient is a scattered compact `r`-tree of height
strictly below `omega_2`, hence Valdivia by the source paper's lower-height
theorem.

By minimality, all collapsed clopen pieces are Valdivia. A clopen replacement
lemma then pulls back a point-countable clopen separating family from the
quotient and combines it with point-countable separating families inside the
fibers. This reconstructs a dense Sigma-subset of the original tree, so the
original tree is Valdivia, contradiction.

## Files

- `README.md`: this summary.
- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original paper with Problem 5.9.
- `supporting_somaglia_1803.11107.pdf`: supporting compact-tree criterion.
- `figures/open_problem_crop.png`: crop of Problem 5.9.
- `code/check_packet_assets.py`: lightweight structural checker.
- `history/partial_root_split_height_omega2_valdivia/`: earlier root-split
  partial packet, kept as proof-development provenance.
- `tmp/`: LaTeX build intermediates and disposable files.

## History

The first successful push produced a partial result for the root-splitting
subcase, where all immediate-successor subtrees above the root have height
strictly below `omega_2`. After the full Cantor-Bendixson rank argument was
found, that partial packet was nested here under `history/` and its ledger
status was changed to `superseded_by_full`.

## Verification Notes

The packet checks that the proof uses:

- the source paper's lower-height theorem and scattered-tree decomposition;
- Somaglia/Kalenda's zero-dimensional clopen separating-family criterion for
  Valdivia compact trees;
- a new clopen replacement lemma whose hypotheses match the decomposition.

The cheap run indexes were searched for `2305.11737`, `Problem 5.9`,
`scattered compact r-tree`, `height omega_2`, `Valdivia compact tree`, and
nearby norming-M-basis keywords. A web search on 2026-06-16 for the exact
problem phrase, source title, arXiv id, and Somaglia compact-tree criterion
found the source paper and the cited Somaglia paper, but no later full answer.

## Human Review Recommendation

Review the quotient-collapse step in Lemma 2. The central point is that the
Russo--Somaglia lower-rank clopen pieces can be collapsed to successor/minimal
marker nodes, producing a compact scattered `r`-tree quotient of height
strictly below `omega_2`, and that every basic clopen of the quotient has
clopen preimage in the original tree. If Lemma 2 is accepted, the rest of the
argument is a direct minimal-rank contradiction.

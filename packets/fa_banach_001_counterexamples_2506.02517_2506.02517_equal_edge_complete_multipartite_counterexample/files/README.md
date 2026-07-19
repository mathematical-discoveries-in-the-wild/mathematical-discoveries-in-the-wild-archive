# Equal-edge complete multipartite counterexample

Status: `candidate_counterexample_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_06`  
Date: 2026-07-03

## Source Target

Patrick Oliveira Santos, Raghavendra Tripathi, and Pierre Youssef,
"Khintchine inequalities, trace monoids and Turan-type problems",
arXiv:2506.02517.

The source asks in Section 6 whether, for graphs `G,G'` on `[L]` with the
same clique number and `|E(G)| <= |E(G')|`, one necessarily has
`||T_G|| <= ||T_{G'}||`.

## Result

The packet gives a counterexample with equality of edge counts. Let `G` be the
complete 4-partite graph with part sizes `(1,1,4,4)` and let `H` be the complete
4-partite graph with part sizes `(1,2,2,5)`. Both graphs have:

- `L = 10` vertices,
- clique number `4`,
- `33` edges.

For complete multipartite graphs with part sizes `n_1,...,n_r`,
`||T_G|| = (2/sqrt(L)) sum_k sqrt(n_k)`. Hence

- `||T_G|| = 12/sqrt(10)`,
- `||T_H|| = 2(1 + 2sqrt(2) + sqrt(5))/sqrt(10)`.

These are unequal. Since the proposed monotonicity would apply in both
directions when the edge counts are equal, it would force equality, contradiction.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/verify_partitions.py`: arithmetic verifier for the two examples.

## Novelty Check

Bounded search performed 2026-07-03:

- Cheap indexes searched for `2506.02517`, exact title terms, trace monoids,
  Turan, Khintchine, and monoid. No existing packet for this target was found.
- Local source inspection found that the first Turan question is answered in the
  same paper, but the Section 6 edge-count monotonicity question remains open.
- Web searches for exact phrases from the question and title did not reveal a
  separate later answer.

Novelty confidence: bounded local and web search, not exhaustive.

## Human Review Focus

Check the normalization in the complete multipartite norm formula. The source
states the formula in the surrounding argument; the packet proves the normalized
version directly from the decomposition into classically independent sums over
the parts.

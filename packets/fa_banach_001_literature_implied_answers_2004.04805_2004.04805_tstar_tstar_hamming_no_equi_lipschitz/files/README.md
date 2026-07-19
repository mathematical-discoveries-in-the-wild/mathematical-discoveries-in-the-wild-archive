# Literature-Implied Partial Subcase: Hamming Graphs in `T^*(T^*)`

Status: `literature_implied_answer (partial subcase)`

Source problem paper: F. Baudier, G. Lancien, P. Motakis, and
Th. Schlumprecht, *The geometry of Hamming-type metrics and their embeddings
into Banach spaces*, arXiv:2004.04805.

Supporting paper: A. Fovelle, *Hamming graphs and concentration properties in
non-quasi-reflexive Banach spaces*, arXiv:2106.04297.

## Target

Problem 5.1 in the source asks whether Hamming graphs fail to equi-coarsely
embed into any reflexive asymptotic-subsequential-`c0` space, and in
particular whether they fail to equi-coarsely embed into `T^*(T^*)`.

The full equi-coarse question remains open in this packet.

## Result

Fovelle proves that `T^*(T^*)` has property `HFC_{p,d}` for every
`1 < p < infinity`. This concentration property prevents equi-Lipschitz
embeddings of the Hamming graphs.

Therefore, the Hamming graphs do not equi-Lipschitz embed into `T^*(T^*)`.
This gives a literature-implied partial subcase of the source problem: the
stronger linear-scale version of the desired non-embeddability holds for the
specific space `T^*(T^*)`.

## Proof Summary

Fix `1 < p < infinity` and let `lambda` witness `HFC_{p,d}` for `T^*(T^*)`.
If `f_k : H_k^omega -> T^*(T^*)` were equi-Lipschitz with lower constant `A`
and upper constant `B`, then each directional Lipschitz constant of `f_k`
would be at most `B`. Applying `HFC_{p,d}` gives an infinite subgraph on which
all image distances are at most `lambda B k^{1/p}`. Two disjoint `k`-sets in
that subgraph have Hamming distance `k`, so the lower Lipschitz bound gives
image distance at least `A k`, a contradiction for large `k`.

## Evidence

- `figures/open_problem_crop.png`: source final remarks, including Problem 5.1.
- `figures/supporting_theorem_crop.png`: Fovelle's corollary that
  `T^*(T^*)` has `HFC_{p,d}` for every finite `p`.
- `source_paper.pdf`: local copy of arXiv:2004.04805.
- `supporting_paper_2106.04297.pdf`: local copy of arXiv:2106.04297.

## Search Bounds

Before packaging, the cheap run indexes were searched for `2004.04805`,
`Hamming graphs`, `Johnson graphs`, `T^*(T^*)`, `asymptotic-subsequential`,
and `HFC` keywords. No prior packet or attempt for this exact source problem
or subcase was found. Local corpus and web searches for the Hamming/Johnson
and `T^*(T^*)` phrases found the source paper and later concentration-property
papers, with arXiv:2106.04297 providing the relevant supporting theorem.

## Human Review Notes

Recommended review focus:

- Check that `HFC_{p,d}` in Fovelle is being applied with the same Hamming
  graph convention as in the source paper.
- Check the short implication from `HFC_{p,d}` to failure of equi-Lipschitz
  embeddings.
- Count this only as a literature-implied partial subcase. It does not answer
  the source paper's equi-coarse problem.


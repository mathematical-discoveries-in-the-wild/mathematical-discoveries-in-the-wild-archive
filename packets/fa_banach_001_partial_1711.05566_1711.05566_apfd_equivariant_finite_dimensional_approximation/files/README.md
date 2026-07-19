# APFD for AP modules with equivariant finite-dimensional approximation

Status: `partial_result_likely_valid`

Source paper: Yves Cornulier and Romain Tessera, "On the vanishing of reduced 1-cohomology for Banach representations", arXiv:1711.05566.

Target question: Questions 4.6 and 4.7 ask whether Property AP_fd holds for arbitrary locally compact groups, equivalently whether every non-almost-coboundary cocycle into an almost periodic Banach module has an unbounded finite-dimensional quotient.

## Result

Question 4.7 has a positive answer for almost periodic Banach `G`-modules `V` admitting a net of `G`-equivariant finite-rank projections `P_i:V -> V` with finite-dimensional ranges and `P_i v -> v` for every `v in V`.

Equivalently, in this class, if `b in Z^1(G,V)` is not an almost coboundary, then for some `i` the finite-codimensional submodule `ker P_i` gives an unbounded quotient cocycle in `V/ker P_i`.

This covers AP modules with equivariant finite-dimensional decompositions whose partial-sum projections are uniformly bounded, including `c0`- and `ell_p`-sums of finite-dimensional modules. Thus the usual diagonal direct-sum constructions cannot yield a counterexample to Question 4.7.

## Proof idea

Assume every projected cocycle `P_i b` is bounded. Since `P_i V` is finite-dimensional and has precompact linear `G`-action, a bounded affine orbit has a fixed point after taking the compact closure of the affine action and averaging over Haar measure. Hence `P_i b` is an actual coboundary.

For a compact set `K subset G`, the compactness of `b(K)` and strong convergence `P_i -> I` give `sup_{g in K} ||(I-P_i)b(g)|| -> 0`. The transfer vector solving `P_i b` is therefore an almost fixed point for the original affine action on `K`. This proves `b` is an almost coboundary, a contradiction. Hence some finite-dimensional quotient is unbounded.

## Novelty / Search Notes

- Cheap run indexes were searched for `1711.05566`, `WAPFD`, `WAPAP`, `APFD`, `almost periodic Banach`, and `reduced 1-cohomology`; no prior packet or attempt for this target was found.
- A targeted web search for the exact WAPFD/WAPAP/APFD terminology did not reveal an obvious later answer to Questions 4.6 or 4.7.
- The packet does not claim the full APFD problem. The remaining obstruction is precisely the absence, in a general compact-group Banach module, of controlled finite-dimensional equivariant projections approximating the identity.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1711.05566.
- `figures/open_problem_crop.png`: crop of the source questions on PDF page 19.

Human review recommendation: check the finite-dimensional bounded-cocycle lemma and the final compact-uniform convergence step. If those pass, this is a useful partial theorem/reduction for Question 4.7.

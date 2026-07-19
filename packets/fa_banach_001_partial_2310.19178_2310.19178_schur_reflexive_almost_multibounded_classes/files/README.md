# Schur, WSC, And c0 Classes For Almost Multi-Boundedness

Status: `partial_result_likely_valid`

Source: Hung Le Pham, *A combinatorial characterisation of amenable locally compact groups*, arXiv:2310.19178.

Targeted source problem: Problem 4.8 asks for classes of Banach spaces in which relative weak compactness implies and/or is implied by almost `(p,q)`-multi-boundedness.

## Result

For every `1 <= p,q < infinity`:

- In any Banach space, norm relatively compact sets are almost `(p,q)`-multi-bounded.
- In any Schur Banach space, relative weak compactness is equivalent to almost `(p,q)`-multi-boundedness.
- In any weakly sequentially complete Banach space, almost `(p,q)`-multi-boundedness implies relative weak compactness. This includes reflexive spaces.
- If a Banach space contains an isomorphic copy of `c0`, then the implication from almost `(p,q)`-multi-boundedness to relative weak compactness fails.
- Hence finite-dimensional spaces satisfy the equivalence in both directions.

This does not solve Pham's broad classification problem. It records exact positive families, a broad negative family, and a reusable obstruction: any set containing a basic sequence equivalent to the `ell_1` unit vector basis is not almost `(p,q)`-multi-bounded. The remaining frontier for the `almost => weak compact` direction lies among non-weakly-sequentially-complete spaces that do not contain `c0`.

## Files

- `main.tex` - full proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - source paper.
- `figures/open_problem_crop.png` - crop of Problem 4.8 in the source PDF.
- `code/finite_set_bound_check.py` - small arithmetic check for the finite-set estimate.

## Verification

The proof is deterministic. The external sequence tools used beyond the source definitions are Rosenthal's `ell_1` theorem and Eberlein--Smulian.

Bounded novelty search on 2026-06-20 checked exact phrases around `almost (p,q)-multi-bounded`, `Schur`, `weak sequentially complete`, `c0`, `weak compactness`, `c_{p,q}(B)`, and arXiv:2310.19178; no exact existing statement was found.

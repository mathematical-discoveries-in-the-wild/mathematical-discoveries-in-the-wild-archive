# Reverse Coordinate Inclusion Obstruction

Status: `partial_result_likely_valid`

Source target: arXiv:2204.00672, Castillo--Moreno, *The Kalton-Peck space is the complexification of the real Kalton-Peck space*.

## Claim

For the concluding conjecture in Section 3 of the source paper, singularity of the interpolation differential rules out mutual coordinate comparability. More precisely, in the standard complex/CKMR-derived setting used by the paper, if `(X^*, X)_{1/2} = ell_2`, the coordinate inclusion `X^* -> X` is bounded, and the differential is singular, then the reverse coordinate inclusion `X -> X^*` cannot be bounded.

## Scope

This is not claimed as a full solution of broad Banach-space incomparability. It does not rule out arbitrary non-coordinate isomorphic embeddings, nor does it settle all interpretations of "X and X* are incomparable." It gives the clean obstruction forced by the hypotheses already containing one coordinate inclusion.

## Proof Idea

If both coordinate inclusions are bounded, the endpoint norms are equivalent. The interpolation couple is then equivalent to a diagonal couple `(E,E)`. For a diagonal couple, a fixed scalar selector gives a bounded selector whose derivative is a bounded linear map. Selector-independence of derived interpolation spaces then makes the original differential linear plus bounded on all of `ell_2`, contradicting singularity.

## Files

- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2204.00672.
- `figures/open_problem_crop.png`: crop of the source page containing Proposition 3 and the conjecture.

## Novelty Check

Local lightweight indexes had no exact result for `2204.00672`. Web searches for the exact arXiv id, the title, "singular differential incomparable", and the source conjecture wording found the source arXiv/JMAA paper and related Kalton--Peck interpolation papers, but no later explicit resolution of this conjecture.

Human review should focus on the selector-independence/functoriality step for the exact interpolation framework intended by the source conjecture.

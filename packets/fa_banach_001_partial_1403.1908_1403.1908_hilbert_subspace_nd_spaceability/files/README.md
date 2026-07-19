# Hilbert-Subspace Spaceability for Non-Differentiable Pettis Primitives

Status: `partial_result_likely_valid`.

Source paper: B. Bongiorno, U. B. Darji, and L. Di Piazza,
*Lineability of non-differentiable Pettis primitives*, arXiv:1403.1908.

## Result

Let `ND_X` be the set of strongly measurable Pettis integrable functions
`f:[0,1]->X` whose Pettis primitive is nowhere weakly differentiable, equipped
with the Pettis norm topology. If the infinite-dimensional Banach space `X`
contains a subspace isomorphic to `ell_2`, then `ND_X` is spaceable.

This gives a solved subcase of the source paper's Problem 1, "Is `ND`
spaceable?"

## Idea

The source paper proves lineability by choosing many generators whose
coordinate choices are eventually almost disjoint. For spaceability in the
Hilbert case, the construction can be made cleaner: use the source's dyadic
sets `A(sigma,i)` and the orthonormal coordinates `e(sigma,i)`, but make the
`n`th generator live only in the `i=n` column and only from levels `k>=n`.
The normalizing factor `sqrt(n+1)` makes the Pettis norm of the resulting
series equivalent to the `ell_2` norm of the coefficients.

The resulting operator `T:ell_2 -> P([0,1],ell_2)` is an isomorphic embedding,
so its range is closed. Every nonzero vector in the range still has primitive
difference quotients with unbounded norm at every point, because the first
nonzero coefficient contributes on every sufficiently fine dyadic scale.

If `X` contains an isomorphic copy of `ell_2`, compose the Hilbert-valued
construction with the embedding into `X`.

## Scope

This is not a full answer to the source problem for arbitrary infinite
dimensional Banach spaces. It also does not address the stronger source
Problem 2 asking whether every separable Banach space embeds isometrically
into `ND_X union {0}`.

## Novelty / Search Notes

Cheap run indexes were searched for `1403.1908`, `Pettis primitives`,
`non-differentiable Pettis`, and related spaceability phrases; no duplicate
packet was found. Web searches for exact title and the phrases
`Pettis primitives spaceable`, `nowhere weakly differentiable Pettis
spaceability`, and `Pettis integrable spaceability primitive` surfaced only
the source paper. A local full-source search found citations to the source and
general Pettis-integration papers, but no later exact answer to the
spaceability problem.

## Files

- `source_paper.pdf`: source paper arXiv:1403.1908.
- `figures/open_problem_crop.png`: rendered first page containing the open
  problems.
- `main.tex` and `solution_packet.pdf`: proof packet.

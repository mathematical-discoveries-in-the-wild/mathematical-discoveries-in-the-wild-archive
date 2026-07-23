# Strong diameter for generalized limits: complete characterization

Status: `candidate_full_solution_likely_valid` (new proof, subject to human
review).

## Source question

Paolo Leonetti and Cihan Orhan, *On generalized limits and ultrafilters*,
arXiv:2505.23263; J. Math. Anal. Appl. 556 (2026), 130090.

Section 6, PDF page 14 asks for a characterization of the ideals
`I` for which the conclusion of Theorem 2.4 holds: for every
`f in SL(I)` there is `g in SL(I)` with `||f-g||=2`.

## Candidate full answer

The conclusion holds exactly when `Ult(I)`, the compact space of free
ultrafilters extending the dual filter of `I`, is infinite. Equivalently,
`I` has infinitely many maximal-ideal extensions, or `I` is not a finite
intersection of maximal ideals.

The proof identifies `SL(I)` isometrically with the probability measures on
`K=Ult(I)`. An infinite closed subset of `beta omega` is uncountable, whereas
one probability measure has at most countably many atoms. A zero-mass point
`u in K` therefore exists and its Dirac/ultrafilter functional is at distance
two. If `K` is finite, its uniform probability measure is at distance strictly
less than two from every probability measure on `K`.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: full-width evidence crop from PDF page 14.
- `code/make_open_problem_crop.py`: reproducible renderer/cropper.
- `code/verify_finite_distance.py`: finite-simplex sanity check.
- `tmp/`: LaTeX and rendered-page verification artifacts.

## Verification

The formal proof is self-contained apart from the source definitions. The two
topological steps that merit close review are proved explicitly: `beta omega`
has no nontrivial convergent sequence, and every infinite countable compact
Hausdorff space has one. The finite obstruction is also checked directly by
the total-variation formula and by the included finite-grid script.

Bounded novelty searches on 22 July 2026 used the exact concluding-question
wording, the source title/authors, `Ult(I)`, `SL(I)`, strong diameter, and
finite maximal-ideal extensions. They found the arXiv and 2026 journal versions
of the source, both retaining the question, but no later resolution. This is
not an exhaustive novelty claim.

Human review recommendation: verify the measure representation on
`Ult(I)`, the no-convergent-sequence lemma for `beta omega`, and the finite
intersection equivalence. These are all supplied in full in the packet.


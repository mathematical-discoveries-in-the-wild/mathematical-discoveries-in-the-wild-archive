# Hilbert relative spear operators are one-dimensional

Status: `full_solution_likely_valid`

Source paper: Lakshmi Kanta Dey and Subhadip Pal, "On the geometry of G-norm", arXiv:2603.20796.

Target question: Question 1 on PDF page 13 asks for the infinite-dimensional version of the paper's finite-dimensional Hilbert theorem that every relative spear operator is a partial isometry.

## Result

For Hilbert spaces `H_1,H_2` and a norm-one operator `G:H_1 -> H_2`, the exact infinite-dimensional statement is stronger:

`G` is relative spear, meaning `nu_G(T)=||T||_G` for every bounded operator `T:H_1 -> H_2`, if and only if `H_2` is one-dimensional and `G` is a rank-one partial isometry onto `H_2`.

Consequently, under the paper's standing assumption that `||.||_G` is a genuine norm on `L(H_1,H_2)`, this happens if and only if both Hilbert spaces are one-dimensional and `G` is a surjective isometry.

## Proof Idea

Write `A=G*G`. If `A` has spectrum in `(0,1)`, spectral subspaces give an operator `T` with `||T||_G=1` but `nu_G(T)<1`. If the top spectral value is isolated, use a rank-one map from the norm-one eigenspace into a lower spectral image. If spectral values below `1` accumulate at `1`, use alternating near-top spectral slices and a nilpotent shift; its numerical radius is at most `1/2`.

Thus `A` must be a projection, so `G` is a partial isometry. If the final space of `G` is not all of `H_2`, mapping an initial vector into the orthogonal complement again gives `||T||_G=1` and `nu_G(T)=0`. If the final space has dimension at least two, a two-dimensional nilpotent block inside the initial space gives `||T||_G=1` but `nu_G(T)<=1/2`. Hence `H_2` is one-dimensional. The converse is immediate from the one-dimensional formula.

## Novelty / Search Notes

- Cheap run indexes were searched for `2603.20796`, `G-norm`, `relative spear`, `partial isometry`, and Hilbert keywords. No prior run packet for this target was found.
- A targeted web search for `"relative spear operator" "Hilbert" "partial isometry"`, `"On the geometry of G-norm" "relative spear operator"`, and close variants did not reveal an obvious later answer.
- The theorem fully answers Question 1. The source paper's broader Questions 2 and 3 about general Banach spaces remain outside the scope of this packet.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2603.20796.
- `figures/open_problem_crop.png`: crop of the source questions on PDF page 13.

Human review recommendation: check the spectral-slice construction in the non-isolated top-spectrum case and the final one-dimensional converse. If those pass, this is a full answer to the Hilbert infinite-dimensional question.

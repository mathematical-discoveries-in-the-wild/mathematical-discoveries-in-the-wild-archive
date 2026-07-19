# Counterexample for Closed Bounded Generalized Radii

Result type: `counterexample`

Status: human reviewed; correct obstruction, not a full characterization.

Source paper:

- Syamantak Das and Tanmoy Paul, "A study on various generalizations of
  Generalized centers `(GC)` in Banach spaces", arXiv:2311.15818.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper answers its Problem 1.1 for finite subsets: for a subspace
`Y` of `X`, equality `rad_Y(F)=rad_X(F)` for every finite `F subset Y` is
equivalent to the corresponding finite intersection property.

In the observations section, the authors say they do not know the solution
of the same question for closed bounded subsets, outside trivial cases such
as `1`-complemented subspaces or ranges of quasi-linear projections.

This packet shows that the finite-subset equality cannot be extended to all
closed bounded subsets. Take

`Y = c_0`, `X = ell_infty`,

with the canonical inclusion. Then every finite subset `F subset c_0` has
the same Chebyshev radius in `c_0` and `ell_infty`, but the closed bounded
set

`A = {e_n : n in N}`

satisfies

`rad_{ell_infty}(A)=1/2`, while `rad_{c_0}(A)=1`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `human_review.tex`: human verification note.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: rendered packet followed by the human review.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  closed-bounded discussion from page 6 of the source paper.
- `code/check_radii.py`: simple exact/numerical sanity check for the
  standard-basis radius computation.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Literature Check

A web search on June 8, 2026 for exact phrases around `c_0`, `ell_infty`,
`Chebyshev radius`, `closed bounded`, and the source-paper title found the
source paper and conference abstracts, but no later paper explicitly giving
this closed-bounded counterexample.

## Human Review Notes

This packet has been manually checked. The argument is correct, but it is not
a full solution to the stated characterization problem. It is best described
as a natural counterexample or obstruction: finite-radius equality for all
finite subsets does not imply closed-bounded-radius equality.


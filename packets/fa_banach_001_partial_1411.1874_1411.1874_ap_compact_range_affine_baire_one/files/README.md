# AP compact-range partial answer for affine Baire-one maps

Status: `partial_result_likely_valid`

Source target: Ondrej F. K. Kalenda and Jiri Spurny, *Baire classes of affine vector-valued functions*, arXiv:1411.1874.

## Result

Question 10.1 asks whether, for a compact convex set `X` and a Banach space `E` with the approximation property, or compact approximation property, every affine `f in C_1(X,E)` belongs to the first affine Baire class `A_1(X,E)`.

This packet proves the following scoped positive result:

> If `E` has the approximation property and the affine Baire-one map `f:X -> E` has norm-relatively compact range, then `f in A_1(X,E)`.

The proof uses the approximation property only on the compact set `closure f(X)`. Finite-rank operators approximate the identity uniformly on that compact set; after composition with `f`, the resulting finite-dimensional affine Baire-one maps are in `A_1` by the source paper's finite-dimensional Mokobodzki lemma. They converge to `f` inside one bounded ball, so the source paper's `C_1 cap A_2 => A_1` descent corollary finishes the argument.

## Scope

This is not a full solution of Question 10.1. The extra hypothesis is norm-relative compactness of `f(X)`, and the proof handles the approximation-property half. It does not address the compact-approximation-property-only case, where the available approximating operators need not have finite-dimensional range, and it does not remove the compact-range assumption for general AP spaces.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 10.1 from the source paper.
- `code/make_open_problem_crop.py`: reproducible crop helper for the figure.

## Novelty Check

Before promotion, the cheap run indexes were searched for `1411.1874`, the source title, `Baire classes of affine vector-valued functions`, `approximation property`, `compact approximation property`, `affine Baire-one`, and `Question 10.1`. No existing local packet for this target was found. Bounded web searches for the exact question text and nearby phrases found the source paper and related approximation-property background, but no exact public answer to this compact-range subcase. Novelty confidence is moderate: the observation is natural once the source paper's finite-dimensional lemma and descent corollary are isolated.

# Property P for finite angular locus planes

Status: `partial_result_likely_valid`.

Source paper: Kalidas Mandal, Jayanta Manna, Kallol Paul, Debmalya
Sain, *On approximate preservation of orthogonality and its application to
isometries*, arXiv:2501.10719; Colloquium Mathematicum 179 (2025), 189-211.

## Result

This packet proves a positive criterion beyond the polyhedral case:

> Let `X` be a two-dimensional real Banach space.  If the projective
> nonsmooth, or angular, locus
> `A_X = {[x] : J(x) is not a singleton}` is finite and contains at least
> three projective lines, then `X` has Property P.

This subsumes the previous lane-16 two-dimensional polyhedral positive result
for polygons with at least six vertices, and also covers non-polyhedral planes
whose unit circle has finitely many corners in at least three antipodal pairs.

## Main Mechanism

The new ingredient is a compactness argument using Chmielinski--Stypka's
bounded-below estimate for additive maps satisfying the same approximate
Birkhoff--James preservation condition.  A norm-one sequence of epsilon
preservers with epsilon tending to zero has an isometric subsequential limit.
If a small preserver sent an angular line to a smooth line, the unique support
functional at the image would have to annihilate two independent limiting
directions, an impossibility.

Thus all sufficiently small preservers permute the finite angular locus.  Three
projective lines in a two-dimensional space rigidify a linear map up to scalar
once the induced line permutation is fixed.  A finite positive-gap argument
then excludes every remaining nonsimilarity by the exact
Blanco--Koldobsky--Turnsek theorem.

## Scope

This is not a full classification of all two-dimensional spaces.  It leaves
open the infinite angular-locus case and the finite one-line/two-line angular
cases.  Smooth two-dimensional spaces are already covered negatively by the
separate lane-16 uniformly smooth packet.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `supporting_paper_chmielinski_stypka_2025.pdf`: supporting open-access
  Aequationes Mathematicae paper used for the bounded-below theorem.
- `figures/open_problem_crop.png`: rendered source page containing the Property
  P query and definition.

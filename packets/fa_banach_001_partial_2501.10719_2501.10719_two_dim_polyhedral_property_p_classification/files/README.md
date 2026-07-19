# Two-Dimensional Polyhedral Classification for Property P

Status: `partial_result_likely_valid`.

Source paper: Kalidas Mandal, Jayanta Manna, Kallol Paul, Debmalya Sain,
*On approximate preservation of orthogonality and its application to
isometries*, arXiv:2501.10719; Colloquium Mathematicum 179 (2025), 189-211.

## Result

This packet gives a complete answer for two-dimensional real polyhedral Banach
spaces:

> A two-dimensional real polyhedral Banach space has Property P if and only if
> its unit sphere has at least six extreme points.

Equivalently, the only two-dimensional polyhedral failures are parallelogram
unit balls, i.e. spaces linearly isometric to `ell_infty^2`/`ell_1^2`.

## Why This Extends the Source

The source proves that regular `2n`-gon planes have Property P for `n>2`, and
notes that the regular 4-gon case fails.  The proof here removes the regularity
assumption entirely.  The source's finite-polyhedral machinery already forces
every sufficiently small epsilon-preserver to send vertex rays to vertex rays.
For a polygon with at least three projective vertex lines, the set of linear
maps preserving those finitely many rays is discrete modulo scalars.  Hence any
sequence of nonsimilarity approximate preservers with epsilon tending to zero
would have a normalized subsequence converging to an exact orthogonality
preserver, contradicting the Blanco-Koldobsky-Turnsek theorem unless the limit
is a similarity.

The parallelogram case is different because preserving the two vertex lines
allows a continuous family of diagonal nonsimilarities, matching the source's
negative `ell_1^2` result.

## Scope

This is a full classification only inside the two-dimensional polyhedral
subclass.  It does not classify higher-dimensional polyhedral spaces or general
Banach spaces.  It complements the separate lane-16 packet proving that every
real uniformly smooth Banach space of dimension greater than one fails Property
P.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: rendered source page containing the Property
  P query and definition.

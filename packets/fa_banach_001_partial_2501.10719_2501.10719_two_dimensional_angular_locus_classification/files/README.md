# Two-dimensional angular-locus classification for Property P

Status: `partial_result_likely_valid`.

Source paper: Kalidas Mandal, Jayanta Manna, Kallol Paul, Debmalya
Sain, *On approximate preservation of orthogonality and its application to
isometries*, arXiv:2501.10719; Colloquium Mathematicum 179 (2025), 189-211.

## Result

This packet gives a claimed full classification of real two-dimensional Banach
spaces for the source paper's Property P:

> A real two-dimensional Banach space `X` has Property P if and only if its
> projective angular locus
> `A_X = {[x] : J(x) is not a singleton}` contains at least three lines.

Equivalently, the only two-dimensional failures are smooth planes and planes
with one or two antipodal nonsmooth directions.

## Why This Is Stronger Than The Previous Packets

Earlier lane-16 packets proved:

- every real uniformly smooth Banach space of dimension greater than one fails
  Property P;
- a two-dimensional real polyhedral Banach space has Property P iff its unit
  sphere has at least six extreme points;
- a two-dimensional real Banach space with finite angular locus of size at
  least three has Property P.

This packet removes the finiteness restriction from the positive theorem and
adds the missing negative cases with one or two angular lines.

## Main Mechanism

For the positive direction, assume a sequence of nonsimilarity epsilon
preservers exists with epsilon tending to zero.  Chmielinski--Stypka's
bounded-below theorem lets us normalize and pass to operators converging to the
identity.  Dividing by the distance to the scalar line gives a non-scalar
first-order operator `A`.

At every angular line, one-sided convex-geometry of planar support functionals
forces `A` to fix that projective line.  A non-scalar operator on a plane has
at most two projective eigenlines, so three angular lines rule out such a
failure sequence.

For the negative direction, if the angular locus has at most two lines, choose
a small diagonal perturbation fixing all angular lines.  A finite-locus
one-sided continuity lemma shows these perturbations preserve arbitrary
epsilon-orthogonality for sufficiently small parameter, while the perturbations
are not scalar multiples of isometries.

## Scope

This is still a partial result for the global source question, because it
classifies only real two-dimensional Banach spaces.  It is intended to
supersede the previous two-dimensional polyhedral and finite-angular-locus
packets if human review accepts the one-sided support-functional lemma.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `supporting_paper_chmielinski_stypka_2025.pdf`: supporting open-access
  Aequationes Mathematicae paper used for the bounded-below theorem.
- `figures/open_problem_crop.png`: rendered source page containing the Property
  P query and definition.

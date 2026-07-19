# 1209.0055 -- two-dimensional Mazur-Ulam-property subcase

Status: literature_implied_answer (partial subcase)

## Source question

Original paper: Dongni Tan and Rui Liu, *A Note on The Mazur-Ulam
Property of Almost-CL-spaces*, arXiv:1209.0055.

In the introduction, Tan--Liu recall Tingley's isometric extension problem as
Problem 1: if `T:S_X -> S_Y` is a surjective isometry between unit spheres, must
there be a linear isometry `\widetilde T:X -> Y` extending `T`?  They then use
Cheng--Dong's Mazur-Ulam property formulation and state that the problem is
still open in general, even in two dimensions.

The paper itself proves positive results for spaces with the `(T)`-property,
almost-CL spaces admitting smooth points, a particular two-dimensional
hexagonal norm, and some vector-valued/stability constructions.  Those are
same-paper results, not new literature answers.

## Supporting literature

Supporting paper: Taras Banakh, *Every 2-dimensional Banach space has the
Mazur-Ulam property*, arXiv:2103.09268, later published in Linear Algebra and
its Applications 632 (2022), 268--280.

Banakh's abstract says that every isometry between the unit spheres of
2-dimensional Banach spaces extends to a linear isometry and that this resolves
Tingley's problem in the class of 2-dimensional Banach spaces.  Theorem 1
states exactly that every 2-dimensional Banach space has the Mazur-Ulam
property.  This answers the two-dimensional subcase flagged as still open in
the Tan--Liu introduction.

## Scope limitation

This is not a full answer to Tingley's problem or to the generalized
Mazur-Ulam question "whether every Banach space admits the Mazur-Ulam
property."  The supporting theorem settles the 2-dimensional case.  Later
operator-algebra literature still describes Tingley's problem as open in
finite dimensions at least 3, while citing Banakh for the 2-dimensional
positive answer.

The relation is agent-identified rather than presented by Banakh as a direct
answer to arXiv:1209.0055.  The supporting paper cites Cheng--Dong's
Mazur-Ulam-property formulation and the named Tingley problem, but does not
appear to cite Tan--Liu's almost-CL paper.

## Search evidence

Cheap run indexes were searched for `1209.0055`, `Mazur-Ulam property`,
`Mazur Ulam`, `Tingley`, `almost-CL`, `MUP`, and `sphere isometry`; no exact
duplicate packet for arXiv:1209.0055 was found.  Existing nearby packets cover
C*-algebra/Schatten, uniform-algebra, and Schreier-space Tingley/MUP subcases.

External web search on 2026-06-29 for "Tingley's problem two-dimensional Banach
spaces solved all two dimensional" and related Mazur-Ulam queries located
arXiv:2103.09268.  Local parsed source for arXiv:2103.09268 verifies the
abstract and Theorem 1.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source/open-problem paper, arXiv:1209.0055.
- `supporting_paper_2103.09268.pdf`: supporting answer paper.
- `source_1209.0055.tex.gz`, `supporting_source_2103.09268.tex.gz`: local
  arXiv source archives.
- `source_metadata_1209.0055.json`, `supporting_metadata_2103.09268.json`:
  local arXiv source download metadata.
- Ledger: `runs/fa_banach_001/ledger/results/1209.0055_two_dimensional_mup_banakh_2021.json`.

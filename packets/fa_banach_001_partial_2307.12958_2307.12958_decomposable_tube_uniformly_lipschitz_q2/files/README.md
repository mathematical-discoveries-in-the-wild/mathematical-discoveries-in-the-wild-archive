# Partial Solution Packet: Decomposable-Space Tube Construction for arXiv:2307.12958 Q2

Result type: `partial`

Status: human reviewed; proof appears correct as a partial solution.

## Source

- arXiv:2307.12958
- Title: "Retraction methods and fixed point free maps with null minimal displacements on unit balls"
- Authors: Cleon S. Barroso and Valdir Ferreira
- Source PDF: `source_paper.pdf` (`arXiv:2307.12958v2`, 3 September 2024)
- ArXiv evidence crop: `figures/open_problem_crop.png`
- Journal/published-formulation crop supplied in the review thread: `figures/journal_question_crop.png`

## Extracted Question

The arXiv introduction asks:

`(Q2)` Is there a uniformly Lipschitz map `T:K -> K` with no fixed point?

The journal screenshot phrases the unit-ball version more strongly:

`(Q2)` Is there a uniformly Lipschitz map `T:B_X -> B_X` satisfying
`d(T,B_X)=0` and `Fix(T)=empty`?

## Claimed Partial Result

If `X=Y \oplus Z` as a topological direct sum, where both `Y` and `Z` are
infinite-dimensional closed subspaces, then the journal-style `(Q2)` has an
affirmative answer on `B_X`.

This is a partial result only. It does not cover arbitrary Banach spaces,
especially spaces with no infinite-dimensional complemented decomposition.
Nevertheless, the human review regards the result as quite general and
ingenious: decomposable spaces form a large natural class, while genuinely
indecomposable examples are comparatively exotic.

## Addendum: Universal Eta-Approximation

The packet also records a weaker universal observation: for every
infinite-dimensional Banach space `X` and every `eta>0`, there is a
fixed-point-free uniformly Lipschitz self-map `T_eta:B_X -> B_X` with
`d(T_eta,B_X)<eta`.

This does **not** answer `(Q2)`, because the map depends on `eta`; it only
shows that the displacement can be made arbitrarily small by changing the
map. The remaining full-Q2 gap is to build one single map with
`d(T,B_X)=0`.

Novelty caveat: this exact eta-approximation statement was not found in the
source paper or in a targeted quick search, but it should be treated as a
pipeline observation rather than a certified literature-original theorem
until a proper literature review is done.

## Proof Idea

Use the complemented splitting as a base/fiber coordinate system. The base is
retracted onto a small sphere `aS_Y`. A positive Lipschitz gauge on `S_Y`
with infimum zero supplies a variable fiber radius `r(y)>0`.

The fiber direction is selected using the Benyamini--Sternfeld Lipschitz
retraction `B_Z -> S_Z`. The map sends

`x` to `y(x) - r(y(x)) z(x)`.

After the first iterate, the base and radius are unchanged and the fiber sign
flips. Thus the iterates alternate between two Lipschitz maps. The radius is
always positive, so there are no fixed points; its infimum is zero, giving
null minimal displacement.

## Verification Notes

No computational verification was used. The proofs are analytic. Human review
completed: the proof appears correct.

The review focused on:

- the 2-Lipschitz radial clipping estimate;
- the variable-radius estimate for `r R_Z(kappa(q/r))`;
- the identity `T^2=S`, `T^3=T`;
- the fixed-point-free argument;
- the sequence witnessing `d(T,B_X)=0`.
- in the addendum, the explicit Lipschitz retraction from `B_X` onto the small
  cap and the distinction between `d<eta` and `d=0`.

Human review files:

- `human_review.tex`: human verification note source.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: solution packet followed by the human verification
  note.

## Relation To Previous Packets

This is independent of the Hilbert and rotational/unconditional-basis
packets for the same source paper. It removes basis/rotation assumptions but
adds a complemented decomposition assumption.

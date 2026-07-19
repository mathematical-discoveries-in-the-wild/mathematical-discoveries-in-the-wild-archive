# Partial Solution Packet: Hilbert-Ball Q2 for arXiv:2307.12958

Result type: `partial`

## Source

- arXiv:2307.12958
- Title: "Retraction methods and fixed point free maps with null minimal
  displacements on unit balls"
- Authors: Cleon S. Barroso and Valdir Ferreira
- Source PDF: `source_paper.pdf`
- ArXiv evidence crop: `figures/open_problem_crop.png`
- Journal/published-formulation crop supplied in the review thread:
  `figures/journal_question_crop.png`

No separate public journal PDF was located. This packet keeps the arXiv PDF
as `source_paper.pdf` and includes the user-supplied journal screenshot to
document the stronger ball formulation.

## Extracted Question

The arXiv introduction asks:

`(Q2)` Is there a uniformly Lipschitz map `T:K -> K` with no fixed point?

The journal screenshot phrases the unit-ball version more strongly:

`(Q2)` Is there a uniformly Lipschitz map `T:B_X -> B_X` satisfying
`d(T,B_X)=0` and `Fix(T)=empty`?

## Claimed Partial Result

If `H` is an infinite-dimensional Hilbert space, then there exists a
uniformly Lipschitz self-map `T:B_H -> B_H` such that

- `Fix(T)=empty`;
- `d(T,B_H)=0`;
- `sup_n Lip(T^n)<infinity`.

Thus the journal-style `(Q2)` has an affirmative answer for Hilbert spaces.
This is only a partial result for the paper's general Banach-space question.

## Proof Idea

Choose an isometry `U:H -> e_0^\perp` with no nonzero fixed vector and with
approximate fixed points on the unit sphere. Define a Lipschitz collar map
`T:B_H -> S_H` by

`T(x)=a(||x||)e_0+b(||x||)Ux`,

where `a(r)^2+b(r)^2 r^2=1`, `a(r)=1,b(r)=0` near `r=0`, and
`a(1)=0,b(1)=1`. Then `T` maps the whole ball to the sphere and agrees with
`U` on the sphere.

Consequently, for every `n>=1`,

`T^n = U^{n-1} T`,

so the iterates are uniformly Lipschitz. Fixed points would have to lie on
the sphere and satisfy `Ux=x`, impossible. The null minimal displacement is
witnessed by the usual long averages of the shift basis.

## Relation to the Paper

The paper proves several Hilbert and `L_p` fixed-point-free results, including
Lipschitz or Holder maps with asymptotic-regularity properties. This packet
records a direct uniformly-Lipschitz-iterate construction for the Hilbert
unit ball. It does not remove the general Banach-space obstruction: outside
Hilbert/shift geometries one still needs a replacement for the fixed-free
isometry on the sphere or a Lipschitz retractable shift model.

## Verification Notes

No numerical verification is needed. The proof is explicit and uses only
orthogonal Hilbert-space geometry, a Lipschitz scalar collar, and the unilateral
shift. The `code/` folder contains only a note for this reason.


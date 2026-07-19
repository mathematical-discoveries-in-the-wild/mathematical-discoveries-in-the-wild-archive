# Partial Solution Packet: Rotational-Structure Q2 for arXiv:2307.12958

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

The journal-style `(Q2)` has an affirmative answer in the following cases:

- complex Banach spaces with an unconditional basis;
- real Banach spaces admitting a two-dimensional Schauder block decomposition
  whose blockwise Euclidean rotations are uniformly bounded as block diagonal
  operators;
- Banach spaces containing a complemented infinite-dimensional subspace of
  one of the preceding types.

This is a broad partial result, not a full solution for arbitrary
infinite-dimensional Banach spaces.

## Proof Idea

The core criterion is: if there is a bounded linear isomorphism `A` with
uniformly bounded positive and negative powers, no positive real eigenvector,
and unit vectors `z_k` with `||Az_k-z_k|| -> 0`, then

`U(x)=Ax/||Ax||`

is a fixed-point-free sphere map with null minimal displacement and uniformly
bounded Lipschitz iterates. Composing `U` with the Benyamini--Sternfeld
Lipschitz retraction `B_X -> S_X` gives the required map on the whole ball.

For complex unconditional bases, take a diagonal unimodular multiplier
`Ae_j=exp(i theta_j)e_j` with `theta_j -> 0` and `theta_j in (0,pi)`.
Unconditionality gives uniform boundedness of all powers.

For real rotational block decompositions, take block rotations by angles
`theta_k -> 0`. The stated block hypothesis gives the uniform power bounds.

## Relation to Previous Packets

This strengthens the Hilbert-only Q2 packet:

`solutions/partial/2307.12958_hilbert_uniformly_lipschitz_q2/`

It does not supersede the full Q1 packet, and it does not solve the remaining
general Q2 for Banach spaces with no compatible unconditional or rotational
block structure.

## Verification Notes

No computational verification was used. The proof is analytic. The main
human-review points are:

- uniform power boundedness of the chosen multiplier or block-rotation
  operator;
- absence of positive real eigenvectors;
- the Lipschitz estimate for the normalization map `x -> Ax/||Ax||`;
- the transfer from sphere dynamics to ball dynamics via the
  Benyamini--Sternfeld sphere retraction.

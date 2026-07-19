# Solution Attempt Log

Candidate: arXiv:1905.09592, Problems 2.6 and 2.8.

## Attempt 1: extend the adjoint-representation proof fully

Idea: apply the adjoint representation of a Banach--Lie group, reduce a small
candidate element to the center, and use a local logarithm.

Result: needs context; no full proof.

Details: the adjoint step reduces the obstruction to recurrence in a central
abelian quotient of a Banach space by a discrete subgroup.  Unlike the
finite-dimensional case, the relevant central subgroup need not be a
Banach--Lie subgroup with a usable lattice decomposition, and a one-parameter
subgroup need not be embedded.  This is the obstruction already signaled by
the source's Remark 4.1.

## Attempt 2: construct an infinite-dimensional torus counterexample

Idea: use a Banach quotient `E/Gamma` with increasingly badly conditioned
finite-dimensional lattice blocks, so selected powers return close to the
identity with no uniform neighborhood.

Result: no result.

Details: standard sequence-space lattices fail immediately because coordinate
characters retain the uniform scalar Jamison separation.  A viable distorted
lattice would require simultaneous spectral separation and growing additive
girth; no rigorous fixed-group construction was completed.

## Attempt 3: transfer NSS through differences

Idea: if `m_j=a_j-b_j` with both exponents selected, then closeness of the two
selected powers forces closeness of the `m_j`-th power.

Result: works as a partial result.

Details: choose `U` with `U^{-1}U` inside an NSS witness neighborhood for
`(m_j)`.  This gives an abstract transfer lemma.  Taking paired exponents
`A_j` and `A_j+2^j` imports the source theorem for the bounded-ratio sequence
`(2^j)` while allowing arbitrarily large gaps between successive pairs.

## Candidate result

Claim type: partial result.

Known gap: an arbitrary Jamison sequence need not visibly have a known NSS
sequence inside its difference set.  No structural theorem guaranteeing such
a difference sequence is proved here.

Recommended verifier focus: the order of `a_j,b_j`, the choice
`U^{-1}U subset V`, and the jump quotient
`A_{j+1}/(A_j+2^j)`.


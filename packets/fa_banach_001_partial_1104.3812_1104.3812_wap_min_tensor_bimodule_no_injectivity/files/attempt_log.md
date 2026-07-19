# Solution Attempt Log

Candidate: arXiv:1104.3812, source question on whether
`WAP(M_*)` is always a C*-subalgebra.

## Attempt 1: elementary Hopf coproducts

Idea: seek a counterexample among trivial coproducts, finite-dimensional
quantum semigroups, direct sums, and classical group/semigroup coproducts.

Result: fails as a counterexample route.

Details: trivial and finite-dimensional examples make every relevant orbit map
weakly compact; commutative semigroup cases fall under the classical WAP
algebra theorem.  Direct-sum variants did not produce a coassociative
noncommutative obstruction.

## Attempt 2: exploit nonreflexivity of Haagerup products

Idea: use the source's example
`H_c tensor_h (K_c)^* = K(K,H)` to force a product of weakly compact slice
maps to fail weak compactness.

Result: needs context; not a construction.

Details: failure of reflexivity of one factorization space only shows that the
source's sufficient factorization theorem does not apply.  It does not imply
that the product slice map is non-weakly-compact, and no coassociative
coproduct realizing the obstruction was found.

## Attempt 3: remove injectivity from the mixed-product corollary

Idea: compute slices after multiplying by an elementary tensor directly,
instead of invoking the source's factorization theorem.

Result: works as a partial result.

Details: the direct formulas factor the new slice map through the old weakly
compact map using bounded pre- and post-composition.  Algebraic-tensor
linearity and minimal-tensor norm approximation finish the proof.  This gives
the theorem in `main.tex` and its Hopf--von Neumann corollary.

## Candidate result

Claim type: partial result.

Known gap: the proof does not control a product when both coproducts merely
have weakly compact slice maps and neither is in the minimal tensor product.

Recommended verifier focus: slice orientation; normality of multiplication on
the predual; norm-closedness of weakly compact operators; and the canonical
embedding of `M tensor_min N` into `M bar-tensor N`.


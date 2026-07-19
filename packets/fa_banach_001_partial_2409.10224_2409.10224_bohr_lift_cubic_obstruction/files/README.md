# Partial packet: Bohr-lift zero incomparability

Status: candidate partial result, likely valid.

Source: Jeet Sampat, "Shift-cyclicity in analytic function spaces",
arXiv:2409.10224. The target is Problem 2.23 on PDF page 20, asking how
`f(D)` and `Bf(D_2^infty)` are related and, in particular, how to classify
those `f in H^2_0(D)` whose Bohr transform is non-vanishing on the Hilbert
multidisk.

Result: for the cubic positive-index polynomial
`f(z)=a z + b z^2 + c z^3`, the Bohr lift is
`Bf(w)=a+b w_1+c w_2`. It is non-vanishing on `D_2^infty` if and only if
`a != 0` and `|a| >= |b|+|c|`.

First obstruction: `f(z)=z+z^2+z^3` has no zeros in `D \ {0}`, since
`1+z+z^2` only vanishes at primitive third roots of unity, but
`Bf(-1/2,-1/2,0,...) = 0`. Thus ordinary one-variable disk zero behavior, even
after removing the forced zero at the origin in `H^2_0(D)`, does not capture
Bohr-lift nonvanishing.

Reverse obstruction: `g(z)=z-z^2-z^3+z^6` has Bohr lift
`Bg(w)=(1-w_1)(1-w_2)`, which is non-vanishing on `D_2^infty`. However
`g(z)=z h(z)` with `h(z)=1-z-z^2+z^5`, and
`h(0)=1`, while `h(3/4)=-77/1024 < 0`; hence `h` has a real zero in
`(0,3/4)`. Thus Bohr-lift nonvanishing also does not imply ordinary
one-variable nonvanishing away from the forced zero at the origin.

Together, the two examples show that the two zero conditions are logically
independent. They do not give the full classification requested by Problem
2.23, which would amount to classifying zero-free functions in the full
infinite-polydisk Hardy space under the unitary Bohr transform.

Novelty check: local run indexes were searched for arXiv:2409.10224, Bohr
transform, Hilbert multidisk, and non-vanishing phrases; no prior packet or
attempt for this target was found. Web/arXiv searches on 2026-06-28 for
phrases such as `"Bohr transform" "non-vanishing" "Hilbert multidisk"` and
`"H^2_0" "Bohr transform" "non-vanishing"` found no exact duplicate of these
finite-polynomial obstructions.

Human review recommendation: verify the indexing convention in the Bohr
transform: the coefficient of `z^1` maps to the constant monomial because
`1` has the empty prime factorization. Under that convention, the results are
elementary finite-dimensional calculations.

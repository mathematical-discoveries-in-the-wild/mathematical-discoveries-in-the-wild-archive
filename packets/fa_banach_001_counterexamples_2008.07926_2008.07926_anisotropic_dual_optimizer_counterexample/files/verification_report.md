# Verification report

Verdict: `candidate counterexample, likely valid`

## Target match

After displaying the symmetric family
`(f_A(x,y), f_A(x,z), f_A(y,z))`, arXiv:2008.07926v1, Example 2.20,
states: “We believe that there are no other dual solution, but can not prove
this.” The construction supplies an additional polynomial triple for the same
planar multistochastic problem.

The published JMAA version removes that sentence. The result is therefore
scoped to the arXiv-version belief and is not presented as a counterexample to
a published theorem.

## Proof audit

1. For `s=x+y+z`, the source formula satisfies
   `xyz-sum f_A=(s-1)^2(s+A)/6`. This follows by direct expansion.
2. The proposed pair polynomials satisfy
   `h12+h13+h23=(s-1)^2(x-y)`. Direct expansion gives no monomial involving
   all three variables; equivalently its `xyz` mixed derivative is zero.
3. With `A=1` and `epsilon=1/12`, subtracting the perturbation from the
   source gap gives
   `(s-1)^2(2+x+3y+2z)/12`.
4. This expression is nonnegative throughout `[0,1]^3`, so the perturbed
   triple is dual feasible.
5. The gap vanishes on `s=1`, the support plane of the primal measure in
   Example 2.11. Integrating against that primal measure gives equality
   between the perturbed dual value and the primal value, proving dual
   optimality.
6. Gauge transformations have identically zero total contribution.
   The perturbed total differs from the `A=1` total by the nonzero polynomial
   `(s-1)^2(x-y)/12`.
7. It cannot coincide with an `f_B` total for another parameter `B`: comparing
   exact gaps would require
   `2+x+3y+2z=2(s+B)` identically, which is impossible because the
   coefficients of `x` and `y` disagree.

The checker `code/verify_polynomials.py` verifies Steps 1-3 and 7 over the
exact rational polynomial ring.

## Limitations

The packet disproves only exhaustiveness of the displayed one-parameter
symmetric family. It does not classify all dual optimizers and does not answer
Open Problem 2 concerning general sufficient conditions for the representation
of optimal maps.

## Reviewer focus

Confirm that the planar primal measure used in Example 2.11 has precisely the
pair marginals used by Example 2.20, so equality of the new dual sum with
`xyz` on `s=1` gives complementary optimality exactly as stated.

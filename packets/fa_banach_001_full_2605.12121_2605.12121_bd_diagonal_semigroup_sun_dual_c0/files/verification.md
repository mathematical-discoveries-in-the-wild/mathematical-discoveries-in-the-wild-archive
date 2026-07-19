# Verification Report

Candidate: arXiv:2605.12121, Remark 4.15(2)

## Claim Checked

The classical Bourgain--Delbaen space `Y` admits a `C_0`-semigroup with
unbounded generator whose sun-dual dual contains a complemented copy of
`ell_infinity`, and hence contains `c_0`.

## Verdict

Likely valid.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| `Y` has a Schauder basis | external, verified | Tarbard arXiv:1309.7469, Chapter 2, identifies the original Bourgain--Delbaen construction and states that its biorthogonal vectors form a normalized basis. |
| `Y'` is isomorphic to `ell_1` | external, verified | The source states this in Remark 4.15(2); Tarbard's Corollary 2.5.7 also records it for every original Bourgain--Delbaen space in class `mathcal Y`. |
| Diagonal multipliers are bounded | valid | Abel summation gives `T(t)=sum_n (e^{-nt}-e^{-(n+1)t})P_n` in operator norm for `t>0`; the coefficient differences are positive and sum to `e^{-t}`. |
| Semigroup law | valid | It holds on every basis vector and hence on the dense finite-support span; boundedness extends it to all of `Y`. |
| Strong continuity at zero | valid | It holds on finite-support vectors and the semigroup is uniformly bounded near zero. |
| Generator is unbounded | valid | Every basis vector lies in the generator domain and `Ay_n=-n y_n`, contradicting boundedness of `A`. |
| Sun dual is infinite dimensional | valid | Every biorthogonal functional is an adjoint eigenvector and hence norm-continuous at zero. |
| Infinite-dimensional subspaces of `ell_1` contain complemented `ell_1` | valid | The packet gives a full gliding-hump, small-perturbation, and explicit-projection proof. |
| Dual contains `ell_infinity` | valid | A complemented `ell_1` summand dualizes to a complemented `ell_infinity` summand. |
| Original question is fully answered | valid, with interpretation note | The construction has an unbounded generator, which is stronger than merely excluding the identity/scalar semigroups and matches the Lotz-property discussion. |

## Counterexample Search

The argument was tested against the main edge cases conceptually:

- conditional Schauder bases: monotonicity of the scalar coefficients and
  Abel summation use only bounded partial-sum projections, not unconditionality;
- non-shrinking bases: shrinking is not used; only the individual coordinate
  functionals are put in the sun dual;
- merely isomorphic `Y'` to `ell_1`: the complemented-subspace conclusion is
  invariant under isomorphism;
- real versus complex scalars: the multiplier and gliding-hump arguments work
  over either field.

No counterexample was found; finite computation is not applicable.

## External Dependencies

- Tarbard, arXiv:1309.7469, for the normalized Schauder basis and `ell_1` dual
  properties of the original Bourgain--Delbaen spaces. Verified from the local
  source/PDF.
- No unproved mathematical dependency remains. The `ell_1` structural lemma
  is proved inside the packet.

## Gaps

No proof gap identified. Novelty is not certified globally: the literature
search was bounded and the source is recent.

## Confidence

Score: 94/100.

The core proof is short and uses only explicit basis-multiplier estimates and
a self-contained classical `ell_1` lemma. The remaining uncertainty is source
identification/novelty rather than the functional-analytic argument.

## Human Review Recommendation

Send to human. Verify the identification of the source's `Y` with the class
`mathcal Y` in Tarbard/Bourgain--Delbaen notation and confirm that the authors
intend "non-trivial" to include (or mean) an unbounded-generator semigroup.


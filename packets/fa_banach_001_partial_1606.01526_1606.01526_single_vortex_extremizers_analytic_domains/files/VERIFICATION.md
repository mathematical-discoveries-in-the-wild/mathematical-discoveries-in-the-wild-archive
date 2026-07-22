# Verification report

Status: `likely valid; independent human review requested`.

## Structural audit

1. **Class and degree.** The model map `w_(a,d)` belongs to `W^{1,1}` in two
   dimensions because its gradient is `|d|/|x-a|`. Multiplication by a
   `W^{1,1}` phase does not change the degree on almost every centered circle,
   so all slices have degree `d`.

2. **Sharp lower bound.** In polar coordinates inside the largest centered
   ball, the pointwise inequality

   ```text
   sqrt(rho^2 |partial_rho u|^2 + |partial_theta u|^2)
       >= |partial_theta u|
   ```

   and the length-degree inequality for circle-valued loops give exactly
   `2 pi |d| r`. This agrees with the source's formula
   `Sigma(w_(a,d))=2 pi |d| r`.

3. **Equality conditions.** Equality of the total energy with the lower bound
   forces all three nonnegative losses to vanish: energy outside the ball,
   radial energy inside the ball, and excess tangential length. Only the first
   two are needed for the geometric rigidity.

4. **Internal trace step.** At a point of the inscribed circle which is not on
   `boundary Omega`, a small two-sided neighborhood lies in `Omega`.
   `W^{1,1}` functions have a unique trace across the internal smooth arc.
   The exterior side has zero gradient and is locally constant, hence the
   angular trace is locally constant there.

5. **Positive contact measure.** The angular trace has degree `d != 0`, so its
   derivative cannot be supported on a null set. Since it is locally constant
   away from the contact set, that contact set has positive arc length.

6. **Analytic rigidity.** Restricting `x -> |x-a|^2-r^2` to the connected
   real-analytic boundary gives a real-analytic function. Its zero set has
   positive measure and therefore an accumulation point, so the identity
   principle makes it identically zero. The boundary is the centered circle;
   boundedness and simple connectivity select its interior.

7. **Converse.** On the centered disk the explicit map `w_(a,d)` has energy
   `2 pi |d| r`, so the infimum is attained.

## Main reviewer focus

The key point to check is the equality-to-trace argument at the internal
portion of the inscribed circle. It uses only standard Sobolev slicing and
trace uniqueness; it does not assume continuity of the two-dimensional map.

## Scope audit

The proof says nothing about classes with multiple point singularities or
general singular Jacobians. The packet therefore does not claim that a
noncircular ellipse fails property `(P1)` outright.

# Adversarial verification report

Status: passed symbolic and computational audit; candidate counterexample,
likely valid.

## Claim-to-source match

- Source PDF page 54 defines `omega_2`, proves the sufficient implication in
  Corollary 9.15, and asks whether it is necessary.
- Proposition 9.16 on the same page gives the exact one-dimensional weighted
  Muckenhoupt criterion used to negate the conclusion.
- A one-dimensional counterexample suffices to answer the unqualified
  question negatively.

## Step audit

1. **Homeomorphism and density.** The positive branch is continuous, strictly
   increasing, locally absolutely continuous, and divergent.  Its odd
   extension is therefore an increasing homeomorphism.  Since its derivative
   is positive almost everywhere, the pushforward has a positive density
   satisfying `h(T(t))=(1/2)exp(-t)/T'(t)` for positive `t`.

2. **Lipschitz estimate.** The square-root background has derivative at most
   `1/2`.  The unit ramps are disjoint and contribute derivative at most one,
   so the global Lipschitz constant is at most `3/2`, including across zero.

3. **One-half-Holder estimate.** On an interval of length `d<1`, at most one
   ramp contributes and its increment is at most `d<=sqrt(d)`.  For `d>=1`,
   if `N>=2` ramp intervals meet it, exponential spacing implies
   `d>=16(16^(N-1)-1)-1>=N^2`; hence their total increment is at most
   `N<=sqrt(d)`.  Adding the square-root background gives `2 sqrt(d)` on each
   half-line.  The triangle inequality across zero gives `2 sqrt(2) sqrt(d)`.

4. **Transport contraction.** If `delta=|s-t|` and
   `Delta=|T(s)-T(t)|`, the two regularity bounds give
   `delta^2 >= (4/9) Delta^2` and `delta >= Delta^2/8`.  Therefore
   `min(delta^2,delta) >= Delta^2/8`.  Contracting the source's mixed-cost
   transport inequality for the two-sided exponential law yields `T_2` for
   `mu`.

5. **Muckenhoupt divergence.** At `x_n=T(a_n+1)`, the exact positive tail is
   `(1/2)exp(-(a_n+1))`.  Restricting the weighted reciprocal-density integral
   to the ramp and changing variables gives at least
   `8 b(a_n)^2 exp(a_n)(e-1)`, where `b(a)=sqrt(a+1)-1`.  Their product is
   `4(1-exp(-1))b(a_n)^2`, which diverges.  Proposition 9.16 therefore rules
   out Poincare inequality for `(omega_2)#mu`.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1003.3852_t2_not_omega2_poincare_counterexample/code/verify_sparse_ramp.py
```

The script samples 100,000 pairs, including points on both sides of the first
five ramp endpoints, checks the three metric inequalities, and prints the
first five divergent Muckenhoupt lower bounds.  This supports but is not used
in the proof.

## Literature boundary

Bounded primary-source searches used the exact source sentence, the source
authors and arXiv id, `omega_2` pushforward terminology, and combinations of
Talagrand `T_2` with weighted Poincare necessity/counterexample.  They found
the original survey and unrelated weighted-Poincare results, but no explicit
answer or this construction.  This is not an exhaustive citation search.

## Human review recommendation

Send to a transport-inequality specialist.  In particular, verify that the
normalization convention for `T_2` only changes the finite constant, and audit
the Muckenhoupt change of variables at the piecewise-smooth ramp endpoints.


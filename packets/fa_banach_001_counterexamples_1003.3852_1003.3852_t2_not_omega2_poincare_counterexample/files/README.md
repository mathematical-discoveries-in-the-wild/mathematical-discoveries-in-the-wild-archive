# A `T_2` measure whose quadratic-tail image has no Poincare inequality

Status: `candidate_counterexample_likely_valid`

Source: Nathael Gozlan and Christian Leonard, *Transport Inequalities. A
Survey*, arXiv:1003.3852, Corollary 9.15 and the paragraph immediately after
it, PDF page 54.

## Source question

For

```text
omega_2(x) = sign(x) max(|x|, |x|^2),
```

the survey proves that Poincare inequality for `(omega_2)#mu` is sufficient
for `mu` to satisfy Talagrand's quadratic transport inequality `T_2`.  It asks
whether this condition is necessary.

## Counterexample

Let `lambda(dt)=(1/2)exp(-|t|)dt`, put `a_n=16^n`, and for `t>=0` set

```text
r_n(t) = min(max(t-a_n,0),1),
F(t)   = sqrt(t+1)-1 + sum_n r_n(t).
```

Extend `F` oddly to a homeomorphism `T:R->R`, and let `mu=T#lambda`.

The packet proves:

- `T` is `3/2`-Lipschitz and `2 sqrt(2)`-Holder of order `1/2`;
- contraction of the two-sided exponential mixed transport inequality gives
  `mu` the `T_2` property;
- on every sparse unit ramp, the weighted Muckenhoupt quantity for
  `(omega_2)#mu` is at least
  `4(1-exp(-1))(sqrt(a_n+1)-1)^2`, which tends to infinity.

Consequently `(omega_2)#mu` has no Poincare inequality.  This gives a negative
answer already in dimension one.

See `solution_packet.pdf` for the proof, `verification.md` for the adversarial
audit, and `code/verify_sparse_ramp.py` for numerical sanity checks.

## Scope and novelty

The example is an absolutely continuous, symmetric probability measure with a
positive density.  The proof uses only the mixed transport inequality for the
two-sided exponential law and the one-dimensional Muckenhoupt criterion, both
quoted in the source survey.

The run's cheap indexes and bounded exact-phrase/arXiv searches for the source
question, `omega_2` image Poincare necessity, and weighted-Poincare
counterexamples found the survey and general weighted-Poincare literature but
not this sparse-ramp construction or an explicit resolution of the question.
This is not an exhaustive novelty certification.

Human review recommendation: **high-priority review by a specialist in
transport inequalities**.  The main checks are the global one-half-Holder
bound for `T`, the contraction constant, and the change of variables in the
Muckenhoupt product.


# Adversarial Verification Report

Candidate: `2103.00294_envelope_santalo_full_extension`

## Verdict

`likely valid`

Confidence: **93/100**

## Theorem audit

| Component | Verdict | Adversarial check |
| --- | --- | --- |
| Inner radial envelope | valid | Ludwig's affine isoperimetric inequality applies only to centered competitors, exactly as defined. Volume inclusion gives the correct tail domain. |
| Inner attainment | valid | A degenerate maximizing sequence has value at most `n|B_n|L_phi`; the strict tail gap produces a smaller centered ball with strictly larger value. |
| Outer radial envelope | valid | `h_{phi*}(t)=h_phi(1/t)` and circumscribed volume inclusion give the parameter domain `u >= vrad(K)^(2n)`. |
| Outer non-escape | valid | A sequence with unbounded volume has limsup at most `n|B_n|L_phi`, while a sufficiently large centered ball containing `K` has value strictly above that threshold. |
| Outer compactness | valid | Every competitor contains a fixed centered ball. The cone estimate converts bounded volume into a uniform diameter bound, enabling Blaschke selection. |
| Two-sided dilation | valid | After scaling, concavity gives `theta(lambda u) >= lambda theta(u)` and positivity plus concavity forces monotonicity, giving the other inequality. |
| Hausdorff continuity | valid | Scaling inclusions and the two-sided dilation estimate give a two-sided squeeze for both the inclusion-increasing inner functional and inclusion-decreasing outer functional. |
| Unit-ball universal bounds | valid | The interior-peak hypothesis makes every envelope value at most `M_phi=H_phi(1)`, and both ball formulas attain this value. |
| Two product inequalities | valid | Each individual factor is bounded by the same positive ball constant, so no unproved polar-family identity or volume-product step is used. |
| Exact inner equality | valid | Attainment forces equality in both the affine-isoperimetric and one-dimensional maximum steps; strict increase of `phi` makes the maximizer an ellipsoid. |
| Exact outer equality | valid | The same chain applies directly to an attained outer maximizer, requiring strict increase of `phi*`. |

## Example audit

### Logarithmic function

- `q(t)=2t/(1+t)-log(1+t)` has derivative `(1-t)/(1+t)^2`, hence one
  positive root after `1`.
- `h_phi` tends to zero at both endpoints, so the root is the unique global
  maximum and the tail-gap condition holds.
- `(phi*)'(t)=log(1+1/t)-1/(1+t)>0` follows from
  `log(1+x)>x/(1+x)`.
- The capsule inclusions are stable under polarity and supply both the inner
  and outer maximizing ellipsoids for the body and its polar.

### Source ellipsoid equality counterexample

For `phi_m(t)=arctan(t^(1/m))`, the source itself proves the quotient is
decreasing and

```text
phi_m(s) phi_m(1/s) < phi_m(1)^2 for s != 1.
```

The exact ball formula therefore makes every scaled ball `rB_n`, `r != 1`, a
strict case of the source product inequality even though it is an ellipsoid.
This directly refutes only the printed equality characterization, not the
inequality.

### Polar-centroid counterexample

The four polar vertices were obtained by intersecting adjacent defining
half-planes. The polygon centroid formula gives exactly

```text
g(C)       = (0,0),
g(C polar) = (0,9/140).
```

Thus the source's centered competitor-family bijection fails under its
printed definitions. The new outer proof is independent of this identity.

## Failure-mode checks

- If `L_phi=infinity`, arbitrarily small inner balls or arbitrarily large
  outer `phi*` balls can make the extrema infinite.
- If the strict tail gap fails, the compactness proofs may permit collapse or
  escape. No necessity theorem is claimed.
- A tail-gapped function need not obey the normalized ball product bounds;
  the extra global interior-peak condition is explicitly retained.
- Equality need not be rigid in the new class. The packet states containment
  criteria rather than repeating the source's incorrect ellipsoid-only claim.
- The outer theorem concerns the source's original centered circumscribed
  competitors, not a modified polar-compatible definition.

## Reproducibility

Run:

```bash
python code/check_examples.py
```

Expected key output:

```text
t_star=3.921553634568
arctangent_scaled_ball_strictness=verified
body_centroid=(0,0)
polar_centroid=(0,9/140)
```

## Novelty audit

The four local run indexes were searched by arXiv id, title, and core terms.
Exact-title, exact-phrase, arXiv, and journal searches through 2026-07-19
found no erratum, later solution of the stated open problem, envelope theorem,
or notice of these two corrections. This is a bounded search and does not
certify absolute novelty.

Human recommendation: **send to specialist review**.

# Envelope-Santalo full extension

Status: `candidate_full_likely_valid`

Source: Steven Hoehner, *Extremal general affine surface areas*, Journal of
Mathematical Analysis and Applications 505 (2022), 125506,
arXiv:2103.00294v4.

Source location: Section 7.4, page 21. The paper asks for its results for a
richer function class than the classes where `phi(t)/sqrt(t)` is globally
decreasing or globally increasing.

## Full result

For

```text
h_phi(t) = phi(t)/sqrt(t),
L_phi = limsup_{t -> infinity} h_phi(t),
H_phi(a) = sup_{t >= a} h_phi(t),
```

call `phi` tail-gapped when `L_phi` is finite and `H_phi(a) > L_phi` for
every `a > 0`. Call it interior-peaked when it is tail-gapped and

```text
sup_{t > 0} h_phi(t) = H_phi(1) =: M_phi.
```

For every tail-gapped function, the packet proves directly that both the
original inner and outer maximal functionals are finite, attained, and
Hausdorff-continuous, with sharp envelopes

```text
IS_phi(K)      <= n |B_n| H_phi(vrad(K)^(-2n)),
OS_{phi*}(K)   <= n |B_n| H_phi(vrad(K)^( 2n)).
```

Both bounds are equalities on centered balls. For the interior-peaked class,
both functionals are universally bounded by their unit-ball values. Hence

```text
IS_phi(K) IS_phi(K polar) <= IS_phi(B_n)^2,
OS_{phi*}(K) OS_{phi*}(K polar) <= OS_{phi*}(B_n)^2.
```

Exact equality conditions are given in terms of containment in centered
ellipsoids whose volume-radius parameter maximizes `h_phi`.

## Strictly new class member

`phi(t)=log(1+t)` is interior-peaked but its quotient by `sqrt(t)` first
increases and then decreases. It therefore belongs to neither source class.
Its unique maximizing parameter is the solution of

```text
log(1+t_*) = 2t_*/(1+t_*),
t_* = 3.921553634568...
```

This example has many non-ellipsoidal equality cases. If
`r_*=t_*^(-1/(2n))`, every sufficiently small capsule
`B_n + epsilon[-e_1,e_1]` and its polar saturate both product inequalities.

## Source corrections

The full push found two independent problems in the published statements:

1. The claimed ellipsoid equality condition in Theorem 6.4 is false. For the
   paper's own `phi_m(t)=arctan(t^(1/m))`, a scaled ball `rB_n`, `r != 1`, is
   an ellipsoid but gives strict inequality.
2. The claimed polarity bijection between centered inner and centered outer
   competitors is false because centroid zero is not preserved by polarity.
   The packet gives an exact rational quadrilateral whose centroid is zero
   while its polar has centroid `(0,9/140)`.

The outer theorem in this packet is proved directly, so it does not rely on
the invalid polarity identity.

## Packet contents

- `main.tex`: full theorem, proof, equality classification, examples, and
  source corrections.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page-21 source evidence.
- `verification.md`: adversarial verification report.
- `code/check_examples.py`: exact/numerical checks of the examples; no
  computation is used as a substitute for proof.

Human review recommendation: **send to a convex-geometric analyst**. The
highest-value checks are the direct outer compactness argument, the two-sided
dilation estimate for general affine surface area, and the classification of
the result as a full corrected answer to the intended concave-side program.


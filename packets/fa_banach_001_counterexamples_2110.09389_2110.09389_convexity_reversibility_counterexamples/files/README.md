# Convexity and reversibility counterexamples to Conjecture 4.1

Status: `candidate_counterexample_likely_valid`;
`terminology_independent_positive_curvature_counterexample`;
`full_translation_invariant_classification`.

Source: D. S. Winterrose, *Algebras of pseudo-differential operators acting on
holomorphic Sobolev spaces*, arXiv:2110.09389v3 / JFA 285 (2023), Conjecture
4.1 (printed page 8).

## Main counterexample: positive curvature still does not suffice

On the analytic flat torus, for `0 < c < 1`, take

```text
P = (-Delta)^(1/2) + c D_1,
q(xi) = |xi| + c xi_1.
```

This is a nonnegative self-adjoint analytic classical multiplier of order one.
Its unit co-ball is an ellipsoid, so it has positive curvature everywhere and
satisfies either meaning of “strictly convex.” The imaginary-flow map is

```text
Phi(x,xi) = x + i grad(q^2/2)(xi).
```

The conjectured tube contains `x + i epsilon e_1`. But for the Fourier modes
`k = -m e_1`, the analytically continued Poisson coefficient at that point has
modulus

```text
exp[-epsilon m(1-c)] exp[epsilon m] = exp[c epsilon m].
```

It grows exponentially, so it cannot be the Fourier coefficient even of a
distribution. Conclusion (4) fails for every radius. This counterexample is
independent of the strict-versus-strong convexity terminology.

The mechanism is nonreversibility. The positive imaginary Hamilton flow gives
the tube `{q*(v) < epsilon}`, while Fourier convergence gives the reflected
tube `{q*(-v) < epsilon}`.

## Second counterexample: literal strict convexity is too weak

For

```text
P = partial_1^4 + partial_2^4
```

the `l^4` unit co-ball is strictly convex in the standard no-segments sense,
but `D^2(q^2/2)` is singular at axial covectors. The flow map loses rank and
the dual `l^(4/3)` tube boundary is not `C^2`. Conclusions (1) and (2) fail.

## Exact flat-torus repair

For every positive translation-invariant classical multiplier with principal
root `q`, including arbitrary classical lower-order terms, all six conclusions
of the printed conjecture hold if and only if:

1. `D^2(q^2/2)` is positive definite away from zero; and
2. `q(-xi) = q(xi)`.

Without reversibility, all six hold after changing the flow from positive to
negative imaginary time. Thus the packet gives a full characterization for
the translation-invariant class.

## Terminology audit

All arXiv source versions, the published paper, Boutet de Monvel’s original
note, and Winterrose’s thesis Sections 7.1–7.2 were inspected. Neither author
defines “strictly convex” by a Hessian or curvature condition. The printed
wording is set-theoretic, while the claimed smooth perturbative geometry
strongly suggests that positive curvature was intended. The Randers
counterexample makes that ambiguity immaterial for Winterrose’s broader
pseudodifferential formulation.

The original note is about differential operators, whose positive principal
symbols are automatically even in the covector. Therefore the new
nonreversibility obstruction specifically diagnoses the published extension
to general pseudodifferential operators. If the intended theorem silently
retains both positive curvature and the original differential scope, the
packet is a precise statement correction plus a full flat-torus theorem, not a
refutation of that narrower intended theorem.

## Files

- `main.tex` and `solution_packet.pdf`: full audit, both counterexamples, and
  the if-and-only-if theorem.
- `source_paper.pdf`: arXiv:2110.09389v3.
- `supporting_boutet_1979.pdf`: original note.
- `figures/open_problem_crop.png`: complete source Conjecture 4.1.
- `figures/original_boutet_condition_crop.png`: original condition (C).

Bounded literature searches found no prior occurrence of either
counterexample or the characterization. Human review should first check the
Randers example and the Hamilton-flow sign.

Model: GPT5.6.

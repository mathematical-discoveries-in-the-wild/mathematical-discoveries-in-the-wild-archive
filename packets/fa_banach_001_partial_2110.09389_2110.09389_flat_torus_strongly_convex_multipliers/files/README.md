# Boutet de Monvel conjecture for strongly convex flat-torus multipliers

> Superseded as the standalone record by
> `solutions/counterexamples/2110.09389_convexity_reversibility_counterexamples/`.
> The proof here is retained as the reversible homogeneous sufficiency
> component of that packet's stronger classification, which also permits
> arbitrary classical lower-order terms.

Status: `superseded_and_absorbed`; `partial_result_likely_valid`.

Source: D. S. Winterrose, *Algebras of pseudo-differential operators acting on
holomorphic Sobolev spaces*, arXiv:2110.09389, Conjecture 4.1 (printed page 8).

## Result

This packet proves all six conclusions of Boutet de Monvel's conjecture for a
new translation-invariant class. Let `q` be an even, real-analytic,
one-homogeneous norm on `R^n` such that the Hessian of `q^2/2` is positive
definite away from zero, and define the torus multiplier

```text
P e_k = q(k)^d e_k.
```

For every radius `epsilon > 0`, the conjectural tube is exactly

```text
T^n + i {v : q*(v) < epsilon},
```

the imaginary-time Hamilton map is `(x,xi) -> x+i grad(q^2/2)(xi)`, the
Poisson kernel extends holomorphically, its boundary value is a PHG
complex-phase FIO of order `-(n-1)/4`, and it is a homeomorphism

```text
H^s(T^n) -> O^{s+(n-1)/4}(boundary)
```

for every real `s`.

The class is genuinely larger than the source's proved Laplacian case. For all
sufficiently small `delta > 0`, the fourth-order differential operator

```text
(-Delta)^2 + delta partial_1^2 partial_2^2
```

on `T^2` satisfies the theorem, while its principal symbol is not the square
of a quadratic form.

## Proof mechanism

Legendre duality turns the explicit imaginary Hamilton flow into the dual-norm
tube. On the boundary, Poisson summation gives the positive complex phase

```text
(x-y).xi + i(epsilon q(xi) + v.xi).
```

Strong convexity makes its zero set a nondegenerate canonical graph. The phase
dimension formula gives order `-(n-1)/4`. Independently, Laplace's method gives
`S* S` elliptic of order `-(n-1)/2`, which yields the exact Sobolev shift.
Closed range plus density of holomorphic Fourier polynomials gives surjectivity.

## Scope and review focus

This is a candidate full solution of the flat-torus multiplier subcase, not of
the general conjecture on curved manifolds or for variable symbols. A bounded
registry and arXiv/web search on 21 July 2026 found no exact treatment of this
anisotropic class, but that is not an exhaustive novelty certification.

The primary expert-review point is the standard complex-phase FIO and graph
composition step for arbitrary real Sobolev exponents. The packet also supplies
an independent Gram-operator/Laplace ellipticity calculation.

## Files

- `main.tex` and `solution_packet.pdf`: theorem, proof, checks, limitations,
  and literature-search bounds.
- `source_paper.pdf`: arXiv:2110.09389.
- `figures/open_problem_crop.png`: complete Conjecture 4.1 on printed page 8.

Model: GPT5.6.

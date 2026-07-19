# No dimension-only stability constant for m-star-convexity

Status: `candidate_counterexample_likely_valid`

Source: Geanina Maria Lăchescu and Ionel Rovența, *The
Hardy-Littlewood-Pólya inequality of majorization in the context of
omega-m-star-convex functions*, arXiv:2207.08058; Aequationes Mathematicae
97 (2023), 523-535.

Source location: Section 5, Definition 4 and Problem 1, page 8.

## Result

Problem 1 asks whether every `delta-omega-m-star-convex` function on a convex
subset of `R^N` is within `k_N delta` in uniform norm of an exact
`omega-m-star-convex` function, where `k_N` depends only on the dimension.
The answer to this literal dimension-only statement is **no**.

Fix `0<m<1`, take `C=R^N` and `omega=0`, and let

```text
Phi(x) = delta/(1-m).
```

This constant function is `delta-m-star-convex`, because its defining defect
is exactly `lambda delta`, which is absorbed by the allowed `delta`.
Conversely, every exact `m-star-convex` function `Psi` satisfies `Psi(0)<=0`:
substitute `x=y=0` in the exact inequality.  Therefore

```text
||Phi-Psi||_infinity >= Phi(0)-Psi(0) >= delta/(1-m).
```

Thus any stability constant valid at a fixed `m` must be at least
`1/(1-m)`.  Since `m` can approach one, no finite constant depending only on
`N` can satisfy Problem 1 as stated.

## Scope

The counterexample uses a full-dimensional domain and the zero modulus, so it
does not rely on a degenerate convex set or unusual behavior of `omega`.

It does **not** rule out a corrected theorem with a constant `k_{N,m}` that is
allowed to depend on `m`; it proves that such dependence must blow up at least
as fast as `1/(1-m)` as `m` approaches one.  If the authors intended hidden
dependence on a fixed `m` despite writing that `k_N` depends only on `N`, the
packet should be read as a sharp necessary-parameter obstruction rather than a
disproof of that revised formulation.

## Verification and novelty

The proof is algebraic and has no computational dependency.  The verifier
report separately checks the approximate inequality, the exact inequality at
the origin, and the quantifier order.

The run indexes were searched for arXiv:2207.08058 and the core stability,
approximate-convexity, and `m`-star-convex terms.  A bounded web/arXiv search
used the exact Problem 1 wording and close Hyers-Ulam stability phrases.  It
found restricted or parameter-dependent results for related `m`-convexity,
but no answer to the stated dimension-only `omega-m` problem.  Lăchescu's
doctoral thesis *Convex Analysis and Majorization Theory* (defended 2024,
confirmed 2025) reproduces Problem 1 in Section 2.3.4 as open.  This is strong
recent status evidence, not an exhaustive novelty guarantee.

## Packet contents

- `main.tex`: self-contained counterexample and quantitative obstruction.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop containing Definition 4
  and Problem 1.
- `verification.md`: adversarial verifier report.
- `attempt_log.md`: target selection and construction history.

Human review recommendation: **verify the intended dependence of `k_N`**.
The mathematics is immediate once “depends only on the dimension” is read
literally; the main review question is whether the source intended to suppress
dependence on a fixed `m`.


# Range-Core Obstruction and Weighted-Shift Dichotomy

Status: `partial_result_likely_valid`

Source: Friedrich M. Philipp, *On Differential-Algebraic Equations with
Bounded Spectrum in Banach Spaces*, arXiv:2504.10346v1. Open Problem 4.3 asks
for which quasinilpotent bounded operators `T` the DAE

```text
(T x)' = x
```

has only the zero continuous solution on `[0,infinity)`.

## Partial answer

Every solution satisfies

```text
x(t) in intersection_{n>=1} closure(ran(T^n))
```

for every `t`. It also generates a nonzero closed invariant subspace `M` with
`M = closure(T(M))`. Thus any of the following forces triviality:

- the intersection of the closed ranges of the powers is zero;
- the generalized kernel `union_n ker((T*)^n)` is total in `X*`;
- `T` has no nonzero closed invariant subspace on which its range is dense.

The proof is a finite-difference argument: `T^n x` is `C^n` and its `n`th
derivative is `x`.

## Sharp explicit model

On `l2(N_0)`, let

```text
F e_n = e_{n+1}/(n+1),    B = F*.
```

Both operators are compact, nonnilpotent, and quasinilpotent, with
`||F^m|| = ||B^m|| = 1/m!`. Nevertheless:

- `(F x)' = x` has only the zero solution;
- `(B x)' = x` has an infinite-dimensional family of nonzero compactly
  supported global solutions.

For a continuous seed `f` supported in `[0,a]`, `a<1`, the latter solutions
are

```text
x_0(t) = f(t),
x_n(t) = (-1)^n n integral_t^a (s-t)^(n-1) f(s) ds.
```

The packet also gives a sufficient summability criterion for general
backward weighted shifts. The adjoint pair proves that compactness, spectrum,
singular values, and all power norms do not determine DAE triviality.

## Scope

This is not a full characterization. The source's Volterra operator has
dense range but only the zero global solution, so the range-core obstruction
is sufficient, not necessary.

A bounded search through 2026-07-21 found no prior statement of the
range-core theorem or the explicit adjoint-shift dichotomy in this DAE
setting. Publication-level novelty remains subject to expert review. The
recommendation is human review as a candidate partial result, focused on the
novelty of the combined range criterion and explicit weighted-shift family.

Files:

- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: readable crop of Open Problem 4.3.
- `main.tex`, `solution_packet.pdf`: complete partial-result packet.
- `VERIFICATION.md`: adversarial mathematical checks.

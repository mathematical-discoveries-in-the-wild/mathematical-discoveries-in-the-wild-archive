# Partial result: regular Santaló gradient-flow curves exist

Status: partial result, subject to human review.

Source paper: arXiv:2409.05541, Dario Cordero-Erausquin, Matthieu Fradelizi, and Dylan Langharst, *On a Santaló point for Nakamura-Tsuji's Laplace transform inequality*.

## Source Question

Section 5.2 asks whether the time-dependent gradient-flow equation

```text
s'(t) = -(p/(2q)) nabla_z Q(t,s(t))
```

has at least one sufficiently smooth solution on `R_+` with `lim_{t->infty} s(t)=0`, where `0<p<1`, `q=p/(p-1)<0`, and

```text
Q(t,z)=log int L_p(tau_z f_t)
```

for the Fokker-Planck or heat evolution `f_t`.

The source passage is included as `figures/open_problem_crop.png`; the source PDF is included as `source_paper.pdf`.

## Result Proved

This packet proves the open-question existence statement for the regular class used in the source paper's core semigroup theorem:

```text
f >= 0, f not identically zero, bounded and compactly supported,
0 < p < 1,
f_t = P_t f under the Fokker-Planck flow.
```

For such `f`, there is a `C^1` curve

```text
s:(0,infty) -> R^n
```

such that

```text
s'(t)=-(p/(2q)) nabla_z Q(t,s(t)),
lim_{t->infty} s(t)=0.
```

The curve is smooth for `t>0` wherever the source `Q` is smooth, and it belongs to the source paper's admissible class `tilde S_p(f)` because the gradient equation makes condition (58) hold with equality.

Sign note: this packet uses the source's displayed gradient equation `s'=-(p/(2q)) nabla_z Q`, which is the sign forced by condition (58). Under the paper's translation convention `tau_a f(x)=f(x-a)`, the equivalent tilted-mean formula should carry the opposite sign from the informal expectation rewrite printed after that equation.

## Proof Idea

For bounded compactly supported `f`, the Fokker-Planck flow converges exponentially on compact sets, with derivatives, to a centered Gaussian. The associated log-double-Laplace field satisfies

```text
nabla_z Q(t,z) = z/(1-p) + exponentially small error
```

on compact `z`-sets as `t -> infinity`. Hence the proposed ODE is a small nonautonomous perturbation of

```text
s'(t)=s(t)/2.
```

That limiting equation has a terminal-at-infinity solution only at `0`, but the exponentially small forcing admits a unique small terminal solution by the integral equation

```text
s(t) = - int_t^infty exp((t-u)/2) R(u,s(u)) du.
```

This gives a solution on a tail `[T,infty)`. Standard ODE continuation extends it backward to every compact subinterval of `(0,T]`; Gaussian bounds for the regularized heat/Fokker-Planck flow prevent finite-time blow-up away from `0`.

## Scope and Limitations

This is not a full answer to every possible reading of the source question. It does not handle:

- arbitrary nonnegative functions without regularity or integrability assumptions;
- the endpoint `p=0` volume-product equation;
- uniqueness of all terminal-at-infinity solutions;
- a compact-region description for all Santaló curves.

It does answer the natural regular case directly tied to Theorem 3.1 of the source paper.

## Novelty and Literature Check

Cheap run indexes were searched for `2409.05541`, `Santal`, `Nakamura`, `Tsuji`, `gradient flow`, `Laplace`, and related convex-geometric keywords. No duplicate packet was found.

A bounded web check on July 19, 2026 searched exact combinations of `Santaló curves`, `time-dependent gradient flow`, `Laplace`, and `2409.05541`. I found the source paper and open-problem summaries, but no later exact answer to this gradient-flow existence question.

## Verification

- `main.tex` contains the proof.
- `solution_packet.pdf` was compiled from `main.tex`.
- Source crop: `figures/open_problem_crop.png`.
- Source context page: `figures/open_problem_context_page32.png`.
- Source PDF: `source_paper.pdf`.
- Ledger record: `runs/fa_banach_001/ledger/results/2409.05541_santalo_gradient_flow_regular_existence.json`.

## Human-Review Recommendation

Check the asymptotic-field lemma and the backward continuation step. These are the two real analytical inputs; the terminal fixed-point argument is standard once the exponential `C^1` convergence to the Gaussian vector field is accepted.

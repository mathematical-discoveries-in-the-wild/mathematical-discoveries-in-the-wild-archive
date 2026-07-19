# Counterexample: heavy tails make the Santaló gradient field undefined

Status: counterexample to the literal arbitrary-data formulation, subject to
human review.

Source paper: arXiv:2409.05541, Dario Cordero-Erausquin, Matthieu Fradelizi,
and Dylan Langharst, *On a Santalo point for Nakamura-Tsuji's Laplace transform
inequality*.

## Source Question

Section 5.2 asks whether the time-dependent gradient-flow equation

```text
s'(t)=-(p/(2q)) nabla_z Q(t,s(t))
```

has at least one sufficiently smooth solution on `R_+` with
`lim_{t->infty}s(t)=0`, where `0<p<1`, `q=p/(p-1)<0`, and

```text
Q(t,z)=log int L_p(tau_z f_t).
```

The source passage is included as `figures/open_problem_crop.png`.

## Counterexample

For the literal reading "fixed nonnegative `f`", take dimension one and

```text
f(x)=1/(1+x^2).
```

For every `t>0`, under either the heat flow or the Fokker-Planck flow, the
evolved function `f_t` remains comparable to `(1+x^2)^(-1)`. Hence
`f_t^(1/p)` is integrable but has no nonzero exponential moments. Therefore
the Laplace transform

```text
H_t(x)=int f_t(y)^(1/p) exp(xy) dy
```

is finite only at `x=0` and is infinite for every `x != 0`. Since `q<0`,

```text
L_p(f_t)(x)=H_t(x)^q
```

is zero for every `x != 0`, and its possible nonzero value at `x=0` is invisible
to Lebesgue integration. Consequently

```text
int L_p(tau_z f_t)=0,    Q(t,z)=log 0=-infinity
```

for every `t>0` and every `z`. The vector field `nabla_z Q(t,z)` is not
defined anywhere, so no smooth solution of the proposed gradient-flow ODE
exists.

## Relation to the Positive Packet

This does not contradict
`solutions/partial/2409.05541_santalo_gradient_flow_regular_existence/`.
That packet proves existence for bounded compactly supported data, where the
Fokker-Planck tail is Gaussian enough for the double Laplace field to be finite
and smooth. The present packet shows that some such domain or tail hypothesis
is genuinely necessary.

## Novelty and Literature Check

The source paper already includes heavy-tail examples showing that `L_p(f)` can
collapse to zero away from the origin. The additional observation here is that
the collapse persists after positive heat/Fokker-Planck time for polynomial
tails, so the Section 5.2 gradient equation cannot be posed for all
nonnegative data.

Cheap run indexes were searched for `2409.05541`, `Santalo`, `gradient flow`,
`heavy tail`, and `Laplace transform`; no duplicate packet for this obstruction
was found. A web check on July 19, 2026 found the source paper and an
open-problem summary, but no later exact answer.

## Verification

- `main.tex` contains the detailed proof.
- `solution_packet.pdf` was compiled from `main.tex`.
- Source PDF: `source_paper.pdf`.
- Source crop: `figures/open_problem_crop.png`.

## Human-Review Recommendation

Check that the intended reading of the source question did not silently impose
finite-domain/Gaussian-tail hypotheses. Under the literal all-nonnegative-data
wording, the domain-collapse argument is straightforward.

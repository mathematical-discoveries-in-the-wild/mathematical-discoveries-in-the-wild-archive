# Counterexample: critical quadratic growth can destroy attainment

status: `counterexample_likely_valid`

source: Noboru Isobe, *A convergence result of a continuous model of deep
learning via Lojasiewicz--Simon inequality*, arXiv:2311.15365v2.

target: Remark 7.1 on PDF page 23 says that the `p=2` case of Assumption 1.3
remains unsolved and asks for an example in which the continuous-DNN objective
has no minimizer.

## Result

The requested example exists already in one state and one parameter dimension.
Take

```text
X = R,  Y = {0},  mu_0 = delta_(0,0),  lambda = 2,
ell(x,0) = (x-1)^2,
v(x,theta) = theta^4/(1+theta^2).
```

The vector field satisfies the critical bounds with `p=2`, since
`0 <= v(x,theta) <= theta^2`, and it is independent of `x`. For an admissible
parameter curve `eta`, put

```text
R = integral theta^2 d eta_t dt,
A = integral theta^4/(1+theta^2) d eta_t dt.
```

The terminal state is `A`, so

```text
J(eta) = (A-1)^2 + R.
```

If `R>0`, then `A<R` strictly; if `R=0`, then `A=0`. Consequently every
admissible `eta` satisfies `J(eta)>3/4`. On the other hand, with `r=1/2` and

```text
eta_t^M = (1-r/M^2) delta_0 + (r/M^2) delta_M,
```

one has `R_M=r`, `A_M=r M^2/(1+M^2) -> r`, and hence
`J(eta^M) -> 3/4`. Thus `inf J=3/4` and the infimum is not attained.

## Mechanism

The velocity-to-quadratic-cost ratio is strictly below one at every finite
parameter, but tends to one at infinity. A vanishing amount of mass can escape
to infinity while retaining a fixed second moment and a fixed asymptotic
effect on the state. This is exactly the concentration-at-infinity obstruction
that the source's subcritical condition excludes.

## Verification and novelty

- The complete proof is in `main.tex` and `solution_packet.pdf`.
- `source_paper.pdf` is the official current arXiv v2 PDF.
- `figures/open_problem_crop.png` is a full-width crop of Remark 7.1 from PDF
  page 23.
- `code/check_minimizing_sequence.py` checks the exact finite-`M` formulas and
  sample values; it is a sanity check, not part of the proof.
- On 2026-07-21, the run indexes and bounded arXiv searches for the exact id,
  title, `p=2`, quadratic growth, minimizer nonexistence, and continuous-DNN
  variants found no later resolution or matching packet. This is a bounded
  novelty check, not a claim of exhaustive literature coverage.

## Human-review recommendation

Review as a full negative answer to the source's critical-`p=2` existence
question and as the explicit nonattainment example requested in Remark 7.1.
The main points to audit are the reduction of the continuity equation to a
translation and the strict inequality `A<R` for every nonzero admissible
second moment.


# Full solution: Hardy-block formula for the missing associate norm

status: full_solution_likely_valid

source: Miquel Saucedo and Sergey Tikhonov, *The Fourier transform is an
extremizer of a class of bounded operators*, arXiv:2501.17505.

target: Item (iii) on p. 36 asks for the associates of two optimal Fourier
domain functionals. The source gives a known formula for the first and says it
could not find an expression for the second.

packet: `runs/fa_banach_001/solutions/full/2501.17505_hardy_block_associate_norm/`

ledger: `runs/fa_banach_001/ledger/results/2501.17505_hardy_block_associate_norm.json`

## Result

For `1 <= q < 2`, write the second source functional as

```text
N_a(F)^q = integral a(t) [integral_0^t
             (integral_0^(1/r) F*(s) ds)^2 dr]^(q/2) dt.
```

Let `K(t,r)` be a positive kernel on `0 < r < t`, with mixed
`L^(q')(a(t)dt;L^2(0,t))` norm. Define

```text
(T_a^* K)(s) = integral a(t)
                 integral_0^min(t,1/s) K(t,r) dr dt.
```

Then the requested associate is exactly

```text
N_a'(G) = min ||K||
```

over positive kernels satisfying

```text
integral_0^x G*(s) ds <= integral_0^x (T_a^*K)(s) ds
```

for every `x > 0`. The minimum is attained. The formula also covers `q=1`,
where the kernel norm is `L^infinity(a(t)dt;L^2(0,t))`.

## Main idea

The nested source functional is the norm of a positive linear Hardy operator
into a mixed `L^q(L^2)` space. Mixed-norm duality produces the kernel. Because
associate functionals can be tested on decreasing rearrangements, pointwise
adjoint equality is replaced by cumulative Hardy majorization. A closed-cone
separation argument proves that this condition is both necessary and
sufficient without loss of norm.

## Verification and novelty

- The printed source statement and both displayed functionals were checked on
  p. 36 of the PDF.
- The adjoint and cumulative constraint were checked directly by Tonelli.
- The formula reduces to the known associate in the source's simplifying
  regime `xi approximately U`.
- Run indexes and current arXiv literature were searched using the exact
  phrase, authors, defining integral, Hardy/Copson associate terminology, and
  citations to arXiv:2501.17505. No exact answer was found.
- Novelty confidence is moderate; proof confidence is high, subject to review
  of the conic separation step.

## Scope

This is an exact two-variable Hardy-block representation, not necessarily a
single weighted Lorentz formula. It covers the Banach associate range
`1 <= q < 2`; it does not claim a Banach-dual result for `q < 1`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: compiled and visually verified packet.
- `source_paper.pdf`: arXiv:2501.17505.
- `figures/open_problem_crop.png`: the printed p. 36 problem.

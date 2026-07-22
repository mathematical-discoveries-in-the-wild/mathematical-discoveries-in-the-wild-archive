# Verification report

Verdict: `PASS - candidate partial result likely valid`

## Analytic audit

- The centered simplex model
  `K={x: sum x_i=0, x_i>=-1}` has gauge `-min_i x_i`.
- Uniform points are exactly `mP-1` for flat Dirichlet `P`, giving
  `||X+Y||_K=2-m min_i(P_i+Q_i)` with `m=n+1`.
- For iid `Gamma(2,1)` variables, the survival expansion
  `e^{-z}(1+z)=1-z^2/2+O(z^3)` gives the Rayleigh limit at scale
  `sqrt(m)`.
- The two displayed tail inequalities in the proof imply uniform first and
  second moments.
- On the Gamma-sum concentration event, the normalized Dirichlet minimum is
  squeezed between `W_m/(1+delta_m)` and `W_m/(1-delta_m)`.
- The complement has probability at most `4 exp(-c sqrt(m))`; together with
  `A_m<=2 sqrt(m)`, this makes its expectation contribution vanish.
- The resulting deficit scaling and the comparison with the source's exact
  cube formula are dimensionally consistent.
- For a centered `N`-facet polytope, each normalized facet deficit is
  nonnegative, log-concave, and has mean one.
- Convexity of minus the logarithm of its survival function proves
  `P(U<=t)<=2t` for `t<=1/2`.
- The identity `2-||X+Y||_K=min_j(U_j+V_j)` and independence give
  `P(2-||X+Y||_K<=t)<=4Nt^2`, hence the constant `3/(16 sqrt(N))`.

No missing assumption or circular dependency was found.

## Numerical sanity check

Command:

```text
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python -u \
  code/verify_simplex_asymptotic.py --samples 20000
```

Selected output:

```text
Rayleigh limiting mean: 1.253314137
m= 256  Gamma scaled_mean=1.295381619
m=1024  Gamma scaled_mean=1.274248566
m=4096  Gamma scaled_mean=1.263756190
m= 512  Dirichlet scaled_mean=1.286609048  se=4.827e-03
sqrt(n) cube deficit at n=4096: 1.772291599
limit sqrt(pi): 1.772453851
simplex/cube limiting deficit ratio: 0.707106781
PASS
```

The numerical check is not used in the proof.

## PDF QA

The upgraded six-page packet was rendered to PNG at 150 dpi.  Every page was visually
inspected.  The source question, equations, theorem statement, proof ending,
limitations, and reference are legible; no clipping, overlap, broken glyphs,
or misplaced build artifacts were found.

# 2209.07058 -- the log-free ratio conjecture fails for atomic isotropic measures

Status: full counterexample likely valid.

## Source conjecture

Daniel Bartl and Shahar Mendelson, *Structure preservation via the
Wasserstein distance*, arXiv:2209.07058, Theorem 2.4 and Remark 2.5.

For the class `U` of inverse images of generalized real intervals under
linear functionals on `R^d`, Theorem 2.4 proves, at sample size
`m >= c d/Delta`, the simultaneous estimate

`|mu_m(A)-mu(A)| <= sqrt(Delta mu(A)) log(e/mu(A))`

for all `A` with `mu(A) >= Delta`, with high probability. Remark 2.5
conjectures that the logarithmic factor can be removed.

## Counterexample

For each `N`, let `mu_N` be uniform on the vertices of the regular `N`-gon,
scaled by `sqrt(2)`. This is a centered isotropic probability measure on
`R^2`. Every vertex singleton is exposed by a halfspace and therefore belongs
to `U`.

Set `Delta=1/N` and take `m=ceil(alpha N)`, where `alpha` is any sufficiently
large fixed constant. If a log-free estimate with universal constant `C`
held, applying it to the `N` singleton sets would imply

`max_j K_j <= (alpha+1)(1+C)`,

where `(K_1,...,K_N)` are the occupancy counts of `m` uniform samples in
`N` bins.

This is impossible with the conjectured probability. A self-contained
Poissonization argument shows that `max_j K_j` tends to infinity in
probability: use a Poisson number of samples with mean `alpha N/2`; the bin
counts become independent `Poisson(alpha/2)` variables, whose maximum
exceeds every fixed bound with probability tending to one. The Poisson sample
has at most `m` points with probability tending to one, so monotonicity
transfers the conclusion to the fixed-size sample.

Meanwhile `Delta*m -> alpha`, so the conjectured high-probability lower bound
stays bounded away from zero. This contradiction disproves the log-free
conjecture under its stated arbitrary-measure hypotheses.

## Scope

The obstruction is atomic. It does not rule out a version restricted to
nonatomic measures, bounded marginal densities, log-concave measures, or
other regularity hypotheses. It does show that some factor diverging as
`mu(A)` tends to zero is unavoidable in the full generality of Theorem 2.4.
The classical maximum-load asymptotic suggests a necessary loss of at least
order `log(1/Delta)/log log(1/Delta)` along this example.

## Verification and files

- `main.tex`: self-contained counterexample proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: current arXiv source paper PDF.
- `figures/source_conjecture.png`: source-page crop of Theorem 2.4 and
  Remark 2.5.
- Ledger: `runs/fa_banach_001/ledger/results/2209.07058_logfree_ratio_bound_regular_polygon.json`.

Cheap run indexes contained no duplicate for arXiv:2209.07058. The current
source revision still states the conjecture. Bounded exact-title, exact-phrase,
and author/topic searches found no later explicit resolution.


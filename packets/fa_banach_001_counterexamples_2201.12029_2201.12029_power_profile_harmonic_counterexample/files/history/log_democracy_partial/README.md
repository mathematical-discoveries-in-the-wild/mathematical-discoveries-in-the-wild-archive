# Power-profile `f`-greedy bases are logarithmically democratic

Status: `superseded_by_counterexample` (historical partial result retained
inside `solutions/counterexamples/2201.12029_power_profile_harmonic_counterexample/history/`)

Source paper: Pablo M. Berna and Hung Viet Chu, *On Some Characterizations of
Greedy-type Bases*, arXiv:2201.12029.

Target question: the first item in the source paper's "Future research" section
asks for a characterization of the functions `f` for which the `f`-greedy
inequality

```text
||x - G_m(x)|| <= C_f D_m^f(x)
```

forces ordinary greediness.  The source proves this for regular `f`, gives
counterexamples for sparse `f`, and explicitly lists `f(n)=1/n^p`, `p>0`, as
an uncovered class.

## Result

For every `p>0`, if a semi-normalized Schauder basis is `f_p`-greedy for
`f_p(n)=n^{-p}`, then it is suppression unconditional and satisfies a
logarithmic democracy estimate:

```text
||1_A|| <= C log_2(|A|+1) ||1_B||
```

for all finite sets `A,B` with `|A|=|B|`.  The constant depends only on `p`,
the `f_p`-greedy constant, and the semi-normalization constants of the basis.

Equivalently, any counterexample to the full power-profile problem must be
unconditional and can fail democracy by at most a logarithmic factor.

Update 2026-06-21: the harmonic counterexample packet realizes this logarithmic
failure and proves that `f_p`-greediness does not imply greediness for any
`p>0`.

## Proof idea

The source already proves that `f`-greediness implies unconditionality whenever
`f(n)` is never zero.  The new point is a tail-block test.  If `C` sits before
`A`, and `|C|>=|A|=|B|`, then the vector

```text
x = 1_{f_p,C union A} + eta 1_B
```

with `f_p(|C|+1)<eta<f_p(|C|)` has greedy set `C union B`.  The greedy error
is the power-weighted copy of `A`, while `D_m^f(x)` is bounded by
`eta ||1_B||`.  For `f_p(n)=n^{-p}`, the ratio between the first and last
coefficients on a dyadic tail block is bounded by `2^p`, giving uniform
control of every dyadic tail block of `A` by `B`.  Summing over the dyadic
blocks gives the logarithm.

## Historical limitation

At the time this partial result was written, it did not settle the source's
full characterization question for `f(n)=1/n^p`.  The parent harmonic packet
now realizes the logarithmic failure and supplies the full counterexample.

## Novelty / duplicate check

Cheap run indexes were searched for `2201.12029`, `f-greedy`, `D_m^f`,
`power-profile`, and `1/n^p`; only the earlier failed attempt
`attempts/2201.12029_f_greedy_power_profile_push.md` was found.  Web searches
on 2026-06-21 for exact phrases around `2201.12029`, `f-greedy`, `D_m^f`, and
`1/n^p` found no later resolution or matching logarithmic-democracy theorem.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.

Human-review recommendation: check the dyadic decomposition constants and the
use of suppression unconditionality to pass from disjoint to arbitrary equal
sets.  The result is intentionally scoped as partial.

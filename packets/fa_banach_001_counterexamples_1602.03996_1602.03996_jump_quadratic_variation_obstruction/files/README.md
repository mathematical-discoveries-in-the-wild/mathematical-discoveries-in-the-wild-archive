# Jump obstruction to quadratic-variation-only estimates

Status: `counterexample_likely_valid` for the quadratic-variation-only
noncontinuous extension route.

Source paper: Mark Veraar and Ivan Yaroslavtsev, *Cylindrical continuous
martingales and stochastic integration in infinite dimensions*,
arXiv:1602.03996.

## Target

The source asks what structure a cylindrical noncontinuous local martingale
must have in order to support a stochastic integration theory with two-sided
estimates.  In the continuous theory, the decisive size datum is the
quadratic-variation measure `[[M]]` together with its operator derivative.

## Counterexample / obstruction

For every `p>2`, the scalar compensated Poisson martingales

```text
M^R_t = R (N^R_t - R^{-2} t),     0 <= t <= 1,
```

where `N^R` is a Poisson process of intensity `R^{-2}`, all have the same
predictable second characteristic:

```text
<M^R>_t = t.
```

Thus any jump theory whose integrand norm sees only this second-order
quadratic/intensity datum assigns the constant integrand `1` the same size for
all `R`.  But

```text
E |M^R_1|^p >= c_p R^{p-2} -> infinity.
```

So no uniform upper two-sided `L^p` estimate can depend only on the predictable
quadratic variation/intensity measure of scalar projections.  Additional jump
structure, such as optional quadratic variation, jump-size data, or
Rosenthal/Poisson-type norms, is genuinely necessary.

## Scope

This does not solve the full noncontinuous cylindrical integration program.
It rules out one natural extension of the continuous `[[M]]` philosophy:
second-characteristic-only data are too poor once jumps are allowed.  The
obstruction already occurs in the scalar real-valued case, hence also in every
cylindrical setting containing the one-dimensional case.

## Novelty / Duplicate Check

Cheap run indexes were searched for `1602.03996`, the source title,
`cylindrical noncontinuous`, `two-sided estimates`, `scalar quadratic
variation`, and related jump/quadratic-variation phrases.  No durable packet
for this source was found.  Web searches on 2026-06-21 for the exact
`[[M]]`/scalar-quadratic-variation implication and `c0` variants did not find
a matching packet-level answer.  The Poisson obstruction itself is elementary
and should be treated as a sharp run result or folklore-level clarification,
not as a claim that the phenomenon was unknown to probability specialists.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `code/poisson_lower_bound.py`: optional numerical sanity check for the
  lower-bound growth.

Human-review recommendation: check that the scoped target is read narrowly as
"quadratic/intensity-only jump estimates fail"; do not read the packet as a
negative result for richer jump theories based on optional quadratic variation
or Rosenthal-type norms.

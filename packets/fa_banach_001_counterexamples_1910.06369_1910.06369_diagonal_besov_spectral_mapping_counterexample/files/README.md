# A diagonal counterexample to Besov spectral mapping

Status: `candidate_counterexample_likely_valid`

Source: Charles Batty, Alexander Gomilko, and Yuri Tomilov, *The theory of
Besov functional calculus: developments and applications to semigroups*,
arXiv:1910.06369, Section 8.2, page 43.

## Result

The final question in the source has a negative answer.  On `ell_2(N)` take

```text
A e_n = i n e_n,                     f(z) = z/(1+z).
```

Then `-A` generates a unitary `C_0`-semigroup, `f` belongs to the analytic
Besov algebra, and `t -> f(tA)` is operator-norm continuous on
`(0,infinity)`.  Nevertheless, for every `t>0`,

```text
sigma(f(tA)) = {itn/(1+itn): n>=1} union {1},
```

whereas

```text
f(t sigma(A)) union {0}
  = {itn/(1+itn): n>=1} union {0}.
```

The extra point `1` is the limit of the diagonal entries and is not attained
at any finite spectral value of `A`.

## Mechanism

The source's positive spectral-mapping theorem assumes that `f` vanishes at
infinity.  Our rational function has `f(infinity)=1`.  Applying it to an
unbounded discrete spectrum produces a nonzero cluster point in the spectrum
of the bounded diagonal operator.  Norm continuity under positive dilations
does not remove this point because the exact difference estimate is

```text
||f(tA)-f(sA)|| <= |t-s|/min(s,t).
```

## Scope caveat

The packet answers the final printed formulation, which explicitly assumes
`f in B` and norm continuity of `f(dot A)`.  The paragraph first refers to
Theorem 8.8, where a resolvent-decay condition is used as a sufficient
criterion for norm continuity.  This example does not satisfy that stronger
decay condition, so it does not settle a strengthened interpretation that
imports the condition in addition to the assumptions restated in the final
question.

## Verification and novelty

The proof is exact.  The included checker verifies the scalar identities,
continuity estimate, and convergence to the missing spectral point over
several deterministic scales.  See `verification.md`.

The run indexes and a bounded primary arXiv search found no explicit answer to
this question and no occurrence of this counterexample.  Searches included
the exact question, title, authors, and related arXiv papers 2311.18757,
2202.03143, and 2101.05083.  This is not an exhaustive novelty certification.

Human review recommendation: **send to a functional analyst**.  The primary
review issue is the interpretive scope described above; the operator and
spectrum calculations themselves are elementary.

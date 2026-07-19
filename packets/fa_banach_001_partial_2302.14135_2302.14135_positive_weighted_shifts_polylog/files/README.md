# Positive strongly Kreiss weighted shifts have polylogarithmic powers

Status: `partial_result_likely_valid`

## Source question

Loris Arnold and Christophe Cuny, "On the growth rate of powers of a
strongly Kreiss bounded operator on Lp-spaces", arXiv:2302.14135; published
online in *Studia Mathematica* (2026), DOI 10.4064/sm230303-29-10.

Question 5.8 asks whether every positive strongly Kreiss bounded operator on
`L^p`, `1 < p < infinity`, has polylogarithmic power growth.  The question is
shown in `figures/open_problem_crop.png` from page 19 of the arXiv PDF.

## Result

The answer is affirmative for a natural class containing the standard
non-power-bounded positive weighted-shift examples.  Let

```text
(Tx)_j = w_j x_{j+1}  on ell^p(N_0),
```

where `w_j >= 1` and `sup_j w_j < infinity`.  If `T` is strongly Kreiss
bounded, then there are `C,kappa > 0` such that

```text
||T^N|| <= C log(N+2)^kappa.
```

The proof works for every `1 <= p <= infinity`.

Write `a_0=1` and `a_n=w_0...w_{n-1}`.  Strong Kreiss boundedness controls the
normalized Poisson semigroup `P_N=e^{-N}e^{NT}`.  Testing `P_N` between two
coordinate blocks of length comparable to `sqrt(N)` gives, uniformly in the
base index `n`,

```text
a_(n+N) / a_(n+c sqrt(N)) <= C_0.
```

Consequently, for `b_N=||T^N||`,

```text
b_N <= C_0 b_(floor(c sqrt(N))).
```

Only `O(log log N)` iterations are needed to reach a fixed scale, yielding a
power of `log N`.

## Verification

- The formal proof is in `main.tex` and `solution_packet.pdf`.
- `code/weighted_shift_probe.py` computes finite-section induced norms of the
  normalized Poisson semigroup for polynomial cumulative weights
  `a_n=(n+1)^beta`.  It tests 36 `(p,beta,radius)` cases and shows increasing
  norms, consistent with the theorem's obstruction to polynomial growth.
- Verification command:

  ```bash
  conda run --no-capture-output -n sandbox python code/weighted_shift_probe.py
  ```

  For every tested pair (`p` in `1.5,2,4`, `beta` in `0.05,0.1,0.2`), the
  finite-section norm increased at radii `20,80,320,1280`; for example, at
  `p=2`, `beta=0.2`, the values were `1.17125, 1.31642, 1.50094, 1.72158`.
- The computation is a sanity check only; the proof uses the uniform local
  lower bound for Poisson probabilities and does not depend on numerics.

## Scope and novelty

This does not settle Question 5.8 for arbitrary positive operators, nor for
weighted shifts whose cumulative products are not monotone.  A bounded search
through 2026-07-19 for strongly Kreiss bounded positive weighted shifts and
polylogarithmic power bounds found the source paper, Cohen--Cuny--Eisner--Lin
(2020), and adjacent Cesaro/Kreiss weighted-shift literature, but no statement
of this square-root recurrence.  Novelty confidence is moderate; the result
may be a useful folklore consequence not isolated in the searched sources.

Human review should focus on the Poisson-window lower bound and the block
indexing in Lemma 3.  If those are accepted, the recurrence and its
polylogarithmic iteration are elementary.

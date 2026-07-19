# The constancy hypothesis in the stability-radius formula is necessary

Status: candidate_counterexample_likely_valid

Source: C. Badea and M. Mbekhta, "The stability radius of linear
operator pencils", arXiv:math/0011229v2; published as "The stability
radius of Fredholm linear pencils", Journal of Mathematical Analysis and
Applications 260 (2001), 159-172.

## Result

The source asks whether its spectral-radius representation

`d(T;S) = sup{1/r(SL): TLT=T} = sup{1/r(SL): TLT=T, LTL=L}`

remains true without requiring `dim N(T-lambda S)` to be constant near
zero, equivalently without `k(T;S)=0`. The answer is no, already on
`C^2`.

Let

```
T = [[1,0],[0,0]],  S = I_2.
```

Then `T-lambda S=diag(1-lambda,-lambda)`. It is invertible for all
`lambda` except `0` and `1`; at `lambda=1` its nullity and deficiency
are one. The punctured-disk definition therefore gives `d(T;S)=1`.

For every `epsilon>0`, set

```
L_epsilon = [[1,1],[-1+epsilon,-1+epsilon]].
```

Direct multiplication gives `T L_epsilon T=T` and
`L_epsilon T L_epsilon=L_epsilon`. Moreover,
`L_epsilon^2=epsilon L_epsilon`, so its eigenvalues are `0` and
`epsilon`; hence `r(S L_epsilon)=epsilon`. Both proposed suprema are
at least `1/epsilon` for every positive `epsilon`, and thus both are
infinite, whereas `d(T;S)=1`.

At `epsilon=0`, the same construction gives a nilpotent generalized
inverse. The positive-epsilon family shows that the argument does not
depend on how `1/0` is interpreted.

## Scope

This counterexample answers only the source's explicit question about
dropping the local-nullity constancy hypothesis. It does not affect the
source theorem under `k(T;S)=0`, and it does not rule out modified formulas
that impose additional compatibility conditions on generalized inverses.

## Novelty check

The run's registry, solution, attempt, and proof-gap indexes and the parsed
source corpus were searched for arXiv:math/0011229, the exact title, the
formula involving `r(SL)`, and the constancy hypothesis. No prior answer was
found. Bounded web searches used the exact title, DOI, open-problem wording,
and formula fragments; they returned the source and later generalized-
resolvent papers citing it, but no reported resolution or matching
counterexample. This is not an exhaustive citation review, so novelty remains
subject to expert confirmation.

## Files

- `solution_packet.pdf`: complete counterexample and verification note.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:math/0011229v2.
- `figures/open_problem_crop.png`: source page 2 with the formula and question.
- `code/verify_matrices.py`: exact rational matrix checks.


# Local Bishop-beta sum counterexample

Status: `counterexample_likely_valid`

Source paper: Salah Mecheri, *On the stability of the Bishop's
property(beta) under compact perturbations*, arXiv:2510.09289.

## Result

The packet gives a negative answer to the localized question printed on page 5
of the source paper:

```text
If S,T in B(X) have Bishop's property (beta) at lambda_0, does S+T
have Bishop's property (beta) at lambda_0?
```

Let `B` be the backward unilateral shift on `ell_2(N_0)`, set

```text
S = 2 I,        T = B - 2 I.
```

Then `S` and `T` commute and both have Bishop's property `(beta)` at `0`,
because `0` lies in the resolvent sets of both operators.  Their sum is `B`.
The vector field

```text
z |-> (1, z, z^2, ...)
```

is a nonzero analytic eigenvector field for `B` on the unit disk, so `B` fails
SVEP at `0`; since Bishop's property `(beta)` implies SVEP, `B` fails
Bishop's property `(beta)` at `0`.

## Scope

This answers the fixed-base-point localized sentence as printed.  It does not
settle the deeper global commuting-sum problem where both summands are assumed
to have Bishop's property `(beta)` everywhere.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: source page crop showing the localized
  question.
- `source/PerturbationStabilty.tex`: local copy of the arXiv source TeX used
  to inspect the question text.
- `tmp/`: LaTeX build intermediates.

## Novelty Check

Cheap run indexes were searched for `2510.09289`, the source title,
`Bishop's property`, `Bishop beta`, `localized Bishop`, `SVEP`, `commuting
perturbation`, and `backward shift`.  No prior packet or attempt for this
localized question was found.

A bounded web search found the source preprint and older/global formulations
by the same author, but no existing scalar-shift counterexample to the exact
fixed-base-point localized sentence.  This is not an exhaustive literature
search, and the elementary observation may be folklore.

## Human Review

Recommended verdict: likely valid counterexample to the localized question.
Reviewers should mainly check that the source sentence really asks for the sum
at the same `lambda_0`, and that the packet does not overclaim anything about
the global Bishop-beta sum problem.

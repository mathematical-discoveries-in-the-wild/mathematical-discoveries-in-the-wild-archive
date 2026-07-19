# The displayed three-dimensional gradient representation fails Weak C6

Status: `candidate_counterexample_likely_valid`

Source: Wen Qi Zhang, *Stein-Weiss, and power weight Korn type
Hardy-Sobolev Inequalities in L1 norm*, arXiv:2412.09987v2 (2025).

Source location: Section 6, Question 6.4, page 18.

## Result

The answer to Question 6.4 is **no**.  For the source's precise choices

```text
L(D) = [partial_2 partial_3, partial_1 partial_3,
        -2 partial_1 partial_2]

K(y) = (y_2 y_3, y_1 y_3, -y_1 y_2/2)^T,
```

there are no maps `T(x)` and `P(y)` satisfying property (Weak C6) for all
nonzero `x`.

For fixed `x`, put `Q_x(y)=T(x)P(y)`.  The three independent coefficient
rows in `L(D)` force Weak C6 to prescribe `partial_23 Q_x`,
`partial_13 Q_x`, and `partial_12 Q_x` separately.  The first two prescribed
right-hand sides must satisfy

```text
partial_1 R_23 = partial_2 R_13,
```

because both sides equal the same distributional derivative
`partial_123 Q_x`.  If `H` is the Hessian of `1/(4 pi |x|)`, the prescribed
right-hand sides instead give

```text
partial_1 R_23 - partial_2 R_13 = H_22(x) - H_11(x).
```

At `x=(1,0,0)`, these diagonal entries are `-1/(4 pi)` and `2/(4 pi)`.
This contradiction is independent of the tentative cubic factorization in
the paper and rules out every possible finite-dimensional factorization.

## Scope

This is a full negative answer to the displayed Question 6.4 only.  It does
not answer the broader question in the same section of whether every elliptic
canceling operator admits some representation satisfying Weak C6 (or a
similar property).  In particular, it does not rule out different choices of
`L(D)` and `K(y)` for the gradient.

## Verification and novelty

The proof uses only equality of mixed distributional derivatives and the
elementary Hessian of the Newtonian kernel.  The included SymPy checker
independently expands the Weak C6 right-hand sides, verifies the compatibility
obstruction, proves inconsistency of a general cubic at `x=(1,0,0)`, and checks
that the paper's tentative cubic does not satisfy the system.

Cheap run indexes were searched for arXiv:2412.09987, `Weak C6`, `WTP`, and
the core gradient-representation terms.  A bounded arXiv/web search used the
exact question phrase, the source title and id, and close Weak C6 terms.  It
found the source paper, whose current v2 (2025-05-15) still poses the question,
and no separate answer.  This is not an exhaustive novelty claim.

## Packet contents

- `main.tex`: self-contained result, proof, scope, and verification notes.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop of Question 6.4 on page 18.
- `code/check_weak_c6.py`: exact symbolic audit.
- `verification.md`: adversarial verifier report.

Human review recommendation: **send to an analyst familiar with canceling
operators**.  The highest-value checks are the componentwise extraction from
Weak C6 and the composition order of `G`, `K`, and the coefficient rows of
`L(D)`.

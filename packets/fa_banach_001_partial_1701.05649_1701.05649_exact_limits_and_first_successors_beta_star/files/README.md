# Characteristic Witnesses at Limits and Their First Successors

Status: `partial_result_likely_valid`; human verification recommended.

Model: `GPT5.6`.

Source paper: D. H. Leung, H.-W. Ng, and W.-K. Tang, *On ordinal ranks of Baire class functions*, arXiv:1701.05649.

## Upgraded Partial Result

Let `(X,tau)` be an uncountable Polish space and let `2 <= xi < omega_1`.
There is a characteristic Baire class `xi` function with exact extended
oscillation rank `theta` whenever `theta` is one of:

- `1`;
- `2`;
- a nonzero countable limit ordinal `lambda`;
- the first successor `lambda+1` of a nonzero countable limit ordinal.

The new part is the characteristic realization of every limit and every
first successor of a limit.  The source paper already realizes limits by
general functions, and the predecessor packet proves rank two.

The proof chooses a set of exact length `theta` in the strict Hausdorff
difference hierarchy over `Pi^0_xi` on a closed Cantor subset.  For a
characteristic function, potential separation rank and potential oscillation
rank agree exactly.  Theorem 5.17 of arXiv:1406.5724 gives

```text
alpha^*_xi(f) <= alpha_xi(f) <= 2 alpha^*_xi(f).
```

At a limit, `2 eta < eta+omega <= theta` for every `eta<theta`; at
`theta=lambda+1`, a strict drop is at most `lambda` and
`2 lambda=lambda`.  Thus the factor-two comparison cannot permit a strict
drop.  Lemma 3.5 of the source paper transfers the witness from the closed
Cantor subset to `X` without changing these ordinals.

This does **not** solve the full question.  The unresolved cases are finite
ranks `3,4,...` and, more generally, finite tails `lambda+n` with `n>=2`.

## Verification and Search Scope

The packet checks the difference-hierarchy orientation, the equality of the
ordinary derivatives for characteristic functions, ordinal multiplication,
and closed-subspace transfer.  The main external input needing human review
is strictness at every countable level of the Hausdorff difference hierarchy
over `Pi^0_xi` on Cantor space.

A bounded novelty search covered the run indexes, the full sources of
arXiv:1701.05649 and arXiv:1406.5724, exact-rank/range keyword searches, and
citation metadata.  No explicit later full solution or this first-successor
statement was located.  The search was not exhaustive.

## Files

- `main.tex`: proof and adversarial verification packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1701.05649.
- `ekv_source_paper.pdf`: arXiv:1406.5724.
- `figures/open_problem_crop.png`: source question on page 11.
- `code/render_source_crop.py`: reproducible crop renderer.

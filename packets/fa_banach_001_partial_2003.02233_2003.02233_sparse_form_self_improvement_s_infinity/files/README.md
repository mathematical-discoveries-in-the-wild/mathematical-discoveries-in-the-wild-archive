# Sparse-Form Self-Improvement at the Endpoint `s = infinity`

Status: candidate substantial partial result, likely valid.

Conjecture 6.2 of Lorist--Nieraeth (arXiv:2003.02233) asks whether sparse
form domination at exponent `q_0` automatically self-improves to every
`0 < q <= q_0`. The source explicitly says that even
`m = 1, r = 1, q_0 = 1, s = infinity` is unknown.

This packet proves the entire `s = infinity` slice: for arbitrary arity `m`,
all averaging exponents `r_j > 0`, all `q_0 > 0`, and every
`0 < q <= q_0`, the desired `q`-sparse form follows with linear dependence
on the original sparse constant.

The proof splits `F = |T(f)|` at `C_T M_r(f)`. The near part is controlled by
a pointwise sparse domination of the multilinear maximal function. On the
far part, applying the `q_0` hypothesis to

```text
h = F^(q/q_0 - 1) |g|^(q/q_0)
```

turns the `q_0` integral into the desired `q` integral. Since the exponent of
`F` on the sparse side is `q-q_0 <= 0`, the far-set inequality reverses in
exactly the useful direction.

## Packet contents

- `solution_packet.pdf`: source conjecture, theorem, maximal lemma, and proof.
- `source_paper.pdf`: arXiv:2003.02233v4.
- `figures/open_problem_crop.png`: source PDF page 25, Conjecture 6.2 and the simplest-case note.
- `code/make_open_problem_crop.py`: reproducible source crop.
- `verification.md`: proof audit, limitations, and novelty-search bounds.

There is no computational dependency.

## Scope limitation

The argument uses `s = infinity`, where the local exponent on the test
function equals the outer exponent. For finite `s`, the nonlinear test
produces a strictly larger local exponent than the conjectured target, so the
same proof does not close. The finite-`s` part of Conjecture 6.2 remains open.

## Novelty status

A bounded search on 22 July 2026 covered the run's cheap indexes, the local
deterministic source-signal corpus, exact searches for the conjecture title
and number, the quoted “simplest case” sentence, author/title variants, and
arXiv queries involving `q_0`, smaller exponents, and `s = infinity`. It found
the source paper and a later thesis restatement of the conjecture as open, but
no answer to the endpoint slice. Novelty confidence is moderate, not
definitive.

## Human review recommendation

Check the scalar multilinear-maximal stopping lemma, the monotone truncation
of the nonlinear test function, and the exponent calculation
`C_T^(q_0) C_T^(q-q_0) = C_T^q`. The proof otherwise uses only the assumed
form bound and the definition of the multilinear maximal function.

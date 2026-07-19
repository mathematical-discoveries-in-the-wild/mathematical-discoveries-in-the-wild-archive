# Partial result: properly infinite operator-algebra obstruction for finite-dimensional `Ext`

Status: `partial_result_likely_valid`

Source paper: P. Kuchment, *Three-representation problem in Banach spaces*,
arXiv:2006.07696.

## Target question

Section 4 asks whether there are infinite-dimensional Banach spaces `E` and
`F` such that

```text
0 < dim Ext^1(F,E) < infinity.
```

The source excludes several cases, including the square-isomorphic case
`E ~= E ⊕ E` or `F ~= F ⊕ F`.

## Result

The square-isomorphism assumption can be weakened to an operator-algebraic
proper-infiniteness condition.

If either `L(E)` or `L(F)` contains two orthogonal idempotents each equivalent
to the identity, then

```text
Ext^1(F,E) = 0  or  dim Ext^1(F,E) = infinity.
```

Equivalently, it is enough that `E` or `F` contain two mutually disjoint
complemented subspaces each isomorphic to the whole space. The source's
hypothesis `E ~= E ⊕ E` is the special case where the two self-copies sum to
the whole space.

## Proof idea

If `Ext^1(F,E)` were nonzero finite-dimensional, Kuchment's functoriality
gives a unital finite-dimensional representation of `L(E)` and a unital
finite-dimensional anti-representation of `L(F)`.

For an idempotent `P = UV` equivalent to the identity, with `VU = I`, the
image of `U` has a one-sided inverse. In finite dimension this inverse is
two-sided, so the representation sends `P` to the identity. Two orthogonal
such idempotents would therefore be sent both to the identity, while their
product is zero. Contradiction.

## Limitations

This is not a full answer to the finite positive-dimensional `Ext` problem.
It sharpens the source's algebraic obstruction but leaves the genuinely
Dedekind-finite/few-operators frontier open, as noted in the prior attempt.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - source paper.
- `figures/open_problem_crop.png` - crop of the Section 4 question.
- `code/render_open_problem_crop.py` - reproducible crop script.

## Human review recommendation

Recommended for human review as a small but clean partial strengthening of
Kuchment's Theorem 4.6.

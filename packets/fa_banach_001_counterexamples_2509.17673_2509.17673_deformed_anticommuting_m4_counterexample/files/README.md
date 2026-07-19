# Deformed anticommuting M4 counterexample

Status: `counterexample_likely_valid`

Source paper: David P. Blecher, *Commutativity of operator algebras*,
arXiv:2509.17673.

## Result

The packet refutes the conjecture following Example 5.2 of the source paper:

```text
up to unitary equivalence A is the only noncommutative reversible
4 x 4 matrix algebra
```

The source example is

```text
A_1 = span{ e13 + e24, e12 - e34, e14 }.
```

The counterexample is the deformed algebra

```text
A_2 = span{ U, V, W } in M4
U = e13 + 2 e24
V = e12 - 2 e34
W = e14.
```

It satisfies

```text
U^2 = V^2 = UW = WU = VW = WV = 0,
UV = -2W,   VU = 2W.
```

Hence all products anticommute, so `A_2` is noncommutative and reversible:
the map `x -> -x` is a complete isometric algebra isomorphism from the
reversed algebra onto the original algebra.

The algebra is not unitarily equivalent to `A_1`.  More generally, for

```text
A_t = span{ e13 + t e24, e12 - t e34, e14 },   t > 0,
```

unitary equivalence forces `t` to be equal.  The invariant is the constant
ratio, for all non-product elements, between the `e4 -> span{e2,e3}` component
and the `span{e2,e3} -> e1` component after the unique rank-one product line
`C e14` is fixed.  This ratio is `t`, so `A_2` and `A_1` cannot be unitarily
equivalent.

## Scope

This is a counterexample to the unitary-equivalence uniqueness conjecture as
literally stated.  It does not classify all reversible `4 x 4` matrix
algebras, and it does not rule out weaker nonunitary similarity or abstract
complete-isometric equivalence between the deformed family members.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: source page crop showing the conjecture.
- `code/check_deformed_anticommuting.py`: matrix identity and invariant sanity
  check.
- `source/3commfarx.tex`: local copy of the source TeX used for inspection.
- `tmp/`: LaTeX build intermediates and rendered verification page.

## Novelty Check

Cheap run indexes were searched for `2509.17673`, the source title,
`commutativity of operator algebras`, `reversible operator algebra`,
`anticommuting operator algebra`, and `4 x 4 matrix algebra`.  No prior packet
or attempt for this source conjecture was found.

A bounded web search for the exact conjecture phrase and nearby terms found
the source preprint and unrelated uses of anticommutation/reversibility, but no
existing counterexample to this unitary-equivalence uniqueness conjecture.

## Human Review

Recommended verdict: likely valid counterexample.  Reviewers should mainly
check the unitary-invariant ratio argument: unitary conjugacy preserves the
unique rank-one product line, hence preserves the decomposition
`C e1 + span{e2,e3} + C e4`, and therefore preserves the ratio `t`.

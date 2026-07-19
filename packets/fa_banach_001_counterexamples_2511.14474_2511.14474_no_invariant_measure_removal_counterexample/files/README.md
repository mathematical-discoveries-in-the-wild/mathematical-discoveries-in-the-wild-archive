# Counterexample to removing the invariant-measure hypothesis

Status: `counterexample_likely_valid`

Source paper: Anshu, Tattwamasi Amrutam, and Pradyut Karmakar,
*Fejer property and Galois correspondence for groupoid C*-algebras*,
arXiv:2511.14474.

## Result

Remark 3.5 of the source paper asks whether the invariant-measure assumption
in Theorem 3.4 can be removed.  The packet gives a negative answer.

There exists a compact metrizable `SL_3(Z)`-space `X` such that the
transformation groupoid `SL_3(Z) ⋉ X` is second countable, Hausdorff, etale,
principal, and has the bounded Fejer property, while `SL_3(Z)` itself does not
have the Haagerup-Kraus approximation property (AP).

Thus the implication

```text
Gamma ⋉ X has Fejer property  =>  Gamma has AP
```

is false without the existence of a Gamma-invariant probability measure on
`X`.

## Construction

Let `G = SL_3(R)`, let `P` be a minimal parabolic subgroup, and let
`Y = G/P` be the full flag manifold.  The action of `G` on `G/P` is
topologically amenable because `P` is amenable, so its restriction to
`Gamma = SL_3(Z)` is topologically amenable.

Let `Z` be the profinite completion of `Gamma`, with the left-translation
action.  Set

```text
X = Y x Z.
```

The diagonal action is still topologically amenable, and it is free because
the profinite left-translation action is free.  Therefore `Gamma ⋉ X` is a
principal amenable transformation groupoid.  Amenability of the action supplies
compactly supported positive-type multipliers converging to `1`, which gives
the bounded Fejer property of the groupoid.

Since `SL_3(Z)` is known not to have AP, the source theorem cannot remain true
after dropping the invariant-measure hypothesis.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: source page crop showing Theorem 3.4 and
  Remark 3.5.
- `tmp/`: LaTeX build intermediates.

No numerical computation is used.

## Novelty Check

Cheap run indexes were searched for `2511.14474`, the source title, `Fejer`,
`invariant measure`, `removed in general`, `amenable action`,
`transformation groupoid`, `SL_3`, and `AP`.  No prior packet for this paper or
route was found.

A bounded web search on 2026-07-18 for exact and nearby phrases including
`Fejer property invariant measure removed groupoid`, `Gamma rtimes X Fejer
property invariant measure AP`, and `SL_3(Z) approximation property exact
amenable action` found the source paper and standard background on exact
non-AP groups and amenable actions, but no existing answer to Remark 3.5.

## Human Review

Recommended verdict: likely valid counterexample.  Reviewers should check the
standard input that the `SL_3(R)` action on `SL_3(R)/P` is topologically
amenable and that amenability of a discrete transformation groupoid yields the
bounded Fejer multipliers used here.

# Five-color and high-color boundary cases for the 4x4 SAP-lunar problem

Status: **candidate partial result; likely valid; computer-assisted at the
five-color boundary**.

Source: Yong Han, Yanqi Qiu, and Zipeng Wang, *Self-absorption of Hankel
systems on monoids -- a seemingly universal property*, arXiv:2407.01048v1,
Problem 7 on PDF page 21.

## Result

Let `Phi:[4]x[4]->L` be coordinatewise injective and let
`m=|im(Phi)|`.

- If `m<=5`, then the associated Hankel system has SAP if and only if `Phi`
  is lunar.
- If `m>=14`, then `Phi` is automatically lunar, independently of SAP.

Thus the source problem has a positive answer in both boundary regimes. The
remaining unresolved color counts are `6<=m<=13`.

The low-color implication is an exact finite proof. There are 24 canonical
four-color tables, all lunar. Among 4,896 canonical five-color tables, 144 are
lunar. Row/column permutations, color relabeling, and transposition reduce the
five-color tables to 17 classes: one lunar and 16 non-lunar. For every
non-lunar class, the verifier finds coefficients in `{-3,...,3}` for which the
scalar tensor norm is strictly larger than the original norm. Each accepted
gap is certified by exact Sturm root counts for integer Gram matrices; floating
point is used only to propose a rational separating threshold.

The high-color statement is non-computational: any failed lunar implication
forces three independent identifications among the 16 cells, hence at most 13
colors.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  code/verify_five_color_boundary.py
```

Expected final line:

```text
PASS: every non-lunar five-color class fails scalar SAP exactly
```

The complete proof, verification design, representative certificate table,
limitations, and novelty check are in `solution_packet.pdf`.

## Scope and novelty

This does **not** solve Problem 7 in full. The cases with 6 through 13 colors
remain open. A bounded search on 2026-07-21 used the exact title, exact Problem
7 wording, `lunar map`, `Hankel SAP converse`, and the author names on arXiv
and general web search. It found the original v1 and a contemporaneous 2024
talk announcement mentioning unspecified progress, but no later paper or
stated theorem resolving these boundary cases. Novelty confidence is therefore
medium pending author/expert review.

## Human review recommendation

Send to a functional analyst/operator-space expert. The main review targets
are the completeness of the restricted-growth enumeration and orbit quotient,
and the exact interpretation of the Sturm counts as scalar SAP violations.


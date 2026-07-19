# Counterexample to the Reverse Exact-Dominant Narrowness Question

Result type: `counterexample`

Status: candidate counterexample, likely valid pending human review.

## Source

- Nariman Abasov, Abd El Monem Megahed, and Marat Pliev,
  *Dominated operators from a lattice-normed space to a sequence vector
  lattice*, arXiv:1508.03275.
- Source question: Remark after the theorem in Section 5, page 9 of the arXiv
  PDF.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Exact Target

The paper proves that if a dominated linear operator `T` is order narrow, then
its exact dominant `|T|` is order narrow. The subsequent remark asks whether
the converse holds: does order narrowness of the exact dominant imply order
narrowness of `T`?

## Claimed Answer

No. The inclusion

```text
T : L_infty[0,1] -> L_1[0,1]
```

with the domain viewed as the lattice-normed space
`(L_infty, |.|, L_infty)` and the range viewed as the Banach-Kantorovich space
`(L_1, ||.||_1, R)` is a counterexample.

The exact dominant is the positive functional

```text
S(e) = integral_0^1 e(t) dt,    e in L_infty[0,1]_+.
```

This `S` is order narrow because every signed bounded density on the atomless
Lebesgue interval can be bisected in integral. But `T` is not order narrow:
for `v = 1`, every mutually complemented fragment decomposition is
`1 = chi_A + chi_{A^c}`, and

```text
||T chi_A - T chi_{A^c}||_1 = 1.
```

Thus no net of such decompositions can converge to zero in the range lattice
norm.

## Novelty Check

Cheap run indexes were searched for `1508.03275`, the paper title, `exact
dominant`, `order narrow`, and related domination-problem phrases. No duplicate
packet for this target was found. Local source search found vector-lattice and
abstract-Uryson results where order narrowness of an operator is equivalent to
order narrowness of its modulus under additional range hypotheses, but not this
lattice-normed-space counterexample.

Bounded web searches on 2026-07-01 for the exact question phrase, the source
title, and `order narrow exact dominant lattice-normed` found the source arXiv
page and a related orthogonally additive paper, but no exact resolution of the
linear reverse implication.

## Files

- `main.tex`: self-contained LaTeX counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source theorem and remark.
- `code/make_crops.py`: crop-generation script.
- `tmp/`: LaTeX build intermediates and disposable rendering outputs.

## Human Review Notes

The key checks are:

- `L_infty[0,1]` over itself is an atomless Dedekind complete Banach-Kantorovich
  space with the strong Freudenthal property;
- `L_1[0,1]` over the scalar lattice `R` is a Banach-Kantorovich space;
- the integral functional is indeed the exact dominant of the inclusion;
- atomless bisection makes the exact dominant order narrow;
- the constant-one vector blocks order narrowness of the inclusion.

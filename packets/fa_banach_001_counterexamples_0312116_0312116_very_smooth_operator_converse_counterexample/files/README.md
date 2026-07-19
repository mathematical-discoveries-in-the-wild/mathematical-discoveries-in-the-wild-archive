# Counterexample Packet: `0312116_very_smooth_operator_converse_counterexample`

Status: candidate counterexample to an author-labeled converse question.

Source paper: T. S. S. R. K. Rao, "Very smooth points of spaces of operators", arXiv:math/0312116.

## Target

After Corollary 14, Rao proves that every very smooth point `T` of
`K(X,Y)` attains its norm at a unique unit vector `x_0` up to scalars and
that `T(x_0)` is a very smooth point of `Y`. The paper then asks whether
the converse is always true.

## Result

The converse is false, already for scalar-valued compact operators on
`ell_1`.

Let `Y` be the scalar field and define `T: ell_1 -> Y` by

```text
T(x) = x_1 + sum_{n>=2} (1 - 1/n) x_n.
```

Then `T` is compact, `||T||=1`, and `T` attains its norm only at scalar
multiples of `e_1`. Also `T(e_1)=1`, which is a very smooth point of the
one-dimensional range space. However, under the canonical identification
`K(ell_1,Y)=ell_infty`, the coefficient sequence
`(1, 1/2, 2/3, 3/4, ...)` is not even a smooth point of `ell_infty`: it is
normed both by first-coordinate evaluation and by any free-ultrafilter
limit functional.

## Evidence

- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of the arXiv PDF.
- `main.tex`: self-contained proof source.
- `figures/open_problem_crop.png`: crop of Corollary 14 and the converse question on page 58 of the source paper.
- `code/README.md`: notes that no computational verifier is needed.

## Novelty Check

Local cheap indexes were searched for `0312116`, `very smooth`, `unique
norm`, `norm-attain`, `Rao`, `operator converse`, and `compact operator`;
no prior run packet or attempt covered this target. The parsed source corpus
was searched for the exact question and adjacent key phrases. Web searches
for the exact converse sentence, the source title with `converse`, and
variants involving `K(X,Y)` and `unique unit vector` found the arXiv source
page but no separate erratum or known answer.

Human review recommendation: high confidence. The construction is rank-one,
and the obstruction is the elementary distinction between actual unique
norm-attainment on `ell_1` and non-unique norming functionals in `ell_infty`
coming from limiting maximum coordinates.

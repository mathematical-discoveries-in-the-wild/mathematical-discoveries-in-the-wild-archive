# Negative Answer to Ostrovskii's Projection-Factorization Problem

Status: `counterexample_likely_valid_with_sharp_dimension_partial`

Run: `fa_banach_001`

Source paper: M. I. Ostrovskii, *Compositions of projections in Banach spaces and relations between approximation properties*, arXiv:0811.1763.

## Result

Problem 3 asks whether there is a universal constant `C` such that for every triple

```text
X_1 subset X_2 subset X_3
```

with `X_1` and `X_2` finite-dimensional, one can choose projections

```text
P_1:X_2 -> X_1,  P_2:X_3 -> X_2
```

with

```text
||P_2|| <= C lambda(X_2,X_3)
||P_1 P_2|| = lambda(X_1,X_3).
```

The active packet gives a negative answer: for each `d >= 2` there are finite-dimensional real triples with `dim X_1 = d`, `lambda(X_2,X_3) <= 2`, but every such factorization with minimal product satisfies

```text
||P_2|| >= sqrt(d/6) - 2.
```

Thus no dimension-free universal constant exists.

## Positive Dimension-Dependent Theorem

The previous partial result is preserved inside the packet and in `history/`. It proves the matching upper-side theorem:

```text
C_d <= 1 + 2 sqrt(d).
```

More sharply, for arbitrary triples,

```text
||P_2|| <= (1 + 2 lambda(X_1,X_3)) lambda(X_2,X_3)
```

while preserving `||P_1 P_2|| = lambda(X_1,X_3)`.

Together the positive theorem and the counterexample show the worst-case dependence on `dim X_1` is `sqrt(d)` up to absolute constants.

## Proof Mechanism

The counterexample starts from a large-norm uniquely minimal projection. A hyperplane containing its range is chosen so that any factorization whose product is still minimal must use a projection onto that hyperplane with large norm.

The uniquely minimal projections used are the Rademacher projections

```text
R_d:L_{2d}({-1,1}^d) -> span{r_1,...,r_d}.
```

The external input is the Lewicki-Skrzypek uniqueness theorem for classical Rademacher projections in `L_p[0,1]`, transferred to the finite cube by conditional expectation. The norm lower bound is elementary:

```text
||R_d|| >= sqrt(d/6).
```

## Files

- `main.tex`: merged proof packet with source screenshot, positive theorem, and counterexample.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:0811.1763.
- `figures/open_problem_crop.png`: full-width crop of Problem 3 from the source paper.
- `history/previous_dimension_dependent_partial_2026_06_19/`: previous active partial packet.
- `evidence/supplied_ostrovskii_negative_answer_2026_06_19/`: supplied external TeX/PDF note used to build this version.

## Human Review Focus

The key external hinge is the unique minimality theorem for the classical Rademacher projection and its transfer to the finite cube. Once that is accepted, the remaining hyperplane obstruction, factorization argument, and norm-growth estimate are finite-dimensional.


# A B(c0) coefficient separating left and right Asplund/tame functionals

Status: counterexample_likely_valid.

Source target: Matan Komisarchik, *Characterizations of Asplund and Tame
Functionals using Arens Products*, arXiv:2602.14317, Remark 2.30.

## Result

The left/right Asplund and tame notions from the source paper are not
equivalent.

Let `A = L(c0)` be the Banach algebra of bounded operators on `c0`, let
`e_1` be the first unit vector, and let `e_1^*` be the first coordinate
functional. Define

```text
phi(T) = e_1^*(T e_1),   T in L(c0).
```

Then `phi` is left Asplund and left tame, but it is not right Asplund and not
right tame. Passing to the opposite Banach algebra reverses left and right, so
neither direction of implication holds in general.

## Idea

For this rank-one coefficient the two module orbits are completely explicit.

```text
B_A circledast phi = { T -> e_1^*(T y) : y in B_{c0} },
phi circledast B_A = { T -> eta(T e_1) : eta in B_{ell_1} }.
```

Both identifications are isometric. The first orbit is therefore a copy of
the unit ball of `c0`, while the second is a copy of the unit ball of `ell_1`.
The source paper recalls that `B_V` is Asplund iff `V` is Asplund, and tame iff
`V` is Rosenthal. Since `c0` is Asplund and Rosenthal, but `ell_1` is neither,
the two sides separate.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2602.14317.
- `figures/open_problem_crop.png`: source Remark 2.30 with the open question.
- `code/check_orbit_formula.py`: finite-dimensional sanity check for the two
  orbit formulas.
- Ledger: `runs/fa_banach_001/ledger/results/2602.14317_left_right_asplund_tame_b_c0_counterexample.json`.

## Novelty Check

Cheap-index searches for `2602.14317`, the exact title, left/right
Asplund/tame phrases, and `B(c_0)` found no prior durable packet or attempt for
this counterexample in the run indexes. Local source-corpus searches found the
source open remark and the source's later Example 5.5, which gives only a
left-Asplund sufficient condition for `L(c0)` matrix coefficients.

Web spot checks on 2026-06-30 for the exact title, `Quest. 7.2`, `left right
Asplund tame functionals`, and `B(c_0) tame functionals Asplund` found the
source problem and related tame-functional literature, but no exact later
resolution or this `B(c0)` coefficient counterexample.

## Human Review

Recommended review focus: check that the source paper's Asplund/tame subset
properties are used with their standard invariance under isomorphic embeddings.
For applying the example directly to the older uniformly-continuous convention,
note that `L(c0)` is unital, so the usual left/right uniformly continuous
restriction should not remove this functional.

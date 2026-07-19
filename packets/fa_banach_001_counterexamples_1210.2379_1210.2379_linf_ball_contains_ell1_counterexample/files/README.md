# Counterexample: `ell_infty` Ball Families Contain `ell_1`

## Status

`counterexample_likely_valid`

This packet answers the `ell_infty^{d}`-ball branch of Problem 1(i) in
Argyros--Manoussakis--Petrakis, `Function spaces not containing ell_1`
(arXiv:1210.2379), negatively.

For every nonempty bounded open `Omega subset R^d`, `d >= 2`, if `Q_infty`
is the family of axis-parallel `ell_infty^d` balls contained in `Omega`, then
`JF(Q_infty(Omega))` contains an isomorphic copy of `ell_1`.

The previous lane-0 partial packet is now nested in this packet at
`history/1210.2379_Q_family_nonseparable_dual/`. It proves the dual
nonseparability part for this same family, and also for Euclidean balls.
Together, the current state for `ell_infty` balls is:

- Problem 1(ii): yes, the dual is nonseparable.
- Problem 1(i): no, the space can contain `ell_1`; in fact it does for every
  nonempty bounded open `Omega` in dimension at least two.

The Euclidean-ball `ell_1`-noncontainment case is not settled by this packet.

## Construction

Inside a small axis-parallel cube contained in `Omega`, define

```text
f_n(x_1,...,x_d) = (lambda_n/L) cos(lambda_n (x_1-a_1)/L)
```

on the cube and zero outside, where `lambda_n = 2 pi 2^n`.

For any disjoint family of `ell_infty` balls of side lengths `s_j`, the
integral over the `j`-th cube is bounded by

```text
s_j^{d-1} min(2, lambda_n s_j / L).
```

Splitting at `s_j = L/lambda_n` and using `d >= 2` gives a uniform bound on
the `JF(Q_infty)` norms of the whole sequence.

On the other hand, integrals over the nested detector cubes inside the support
cube are proportional to `sin(2 pi 2^n t)`. Every subsequence has a further
subsequence and a single `t` for which these sine values oscillate between
near `1` and near `-1`. Hence the bounded sequence has no weak-Cauchy
subsequence. Rosenthal's `ell_1` theorem then gives an `ell_1` subsequence.

## Files

- `main.tex` - full counterexample proof.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:1210.2379.
- `figures/open_problem_crop.png` - crop of Problem 1 and the ball-family
  remark from the source paper.
- `code/crop_open_problem.py` - reproducible crop script using PyMuPDF.
- `history/1210.2379_Q_family_nonseparable_dual/` - earlier partial packet
  proving nonseparability of the dual for Euclidean and `ell_infty` ball
  families.

## Verification

The proof is deterministic. The main estimates are:

- the uniform cube-JF norm bound from the side-length split;
- the binary-selection lemma producing a detector cube for every subsequence;
- Rosenthal's theorem turning a bounded sequence with no weak-Cauchy
  subsequence into an `ell_1` subsequence.

Human reviewers should check the convention for `ell_infty^d` balls in the
source problem. Under the standard convention, these are axis-parallel cubes,
which is exactly the geometry used here.

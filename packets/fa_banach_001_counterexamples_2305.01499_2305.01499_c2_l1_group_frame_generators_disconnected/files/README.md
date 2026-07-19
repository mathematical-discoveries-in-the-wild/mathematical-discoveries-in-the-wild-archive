# Counterexample Packet: Group-p-USF Generators Need Not Be Path Connected

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2305.01499`
- source paper: K. Mahesh Krishna, *Group-Frames for Banach Spaces*
- target passage: PDF page 13, Problem 2.19

## Claim

Problem 2.19 asks whether `F_G(pi, X)` is path connected in the norm topology.
The answer is no in general.

Already for `G = C_2`, `X = ell_1^2(C)`, `p = 1`, and `pi` the left regular
swap representation, the full set of group-1-USF functional-vectors is exactly
the disjoint union

```text
{(a zeta_e, a^{-1} delta_e): |a| = 1}
union
{(a zeta_s, a^{-1} delta_s): |a| = 1}.
```

These two circles are separated in `X^* x X`, so the set is not path connected.

## Construction

Let `C_2 = {e,s}` and write `delta_e, delta_s` for the standard basis of
`ell_1(C_2)`. Let `zeta_e, zeta_s` be the coordinate functionals and let
`lambda_s` swap the two basis vectors.

For `f = a zeta_e + b zeta_s`, the generated analysis operator is the symmetric
matrix

```text
[ a  b ]
[ b  a ].
```

The group-1-USF condition forces this matrix to be a surjective isometry of
complex `ell_1^2`. Such isometries are monomial. The symmetry above leaves only
two cases: `b = 0, |a| = 1`, or `a = 0, |b| = 1`. The reconstruction equation
then forces the synthesis vector to be the matching inverse basis vector.

## Scope

This gives a complete negative answer to Problem 2.19 under its literal
generality. It also gives, in this example, a complete characterization of
`F_G(lambda, ell_1^2(C))`, as requested in Problem 2.18.

The packet does not claim to classify all Banach spaces, groups, or
representations satisfying the commutant or double-commutant equalities in
Problem 2.18.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2305.01499
- `figures/open_problem_crop.png`: crop of Problems 2.18 and 2.19
- `code/make_open_problem_crop.py`: script used to regenerate the crop

## Novelty Check

The local run indexes were searched for `2305.01499`, the source title,
`Group-Frames for Banach Spaces`, `group-p-USF`, `Banach frames`, `frame`,
`group representation`, `orbit`, `Schauder frame`, `path connected`, and
`\mathscr{F}_G`. No exact prior packet for this question was present.

External searches on June 28, 2026 for combinations of `2305.01499`,
`Group-Frames for Banach Spaces`, `path connected`, `group-p-USF`, and
`\mathscr{F}_G` did not locate a published answer. Human review should still
treat this as a bounded novelty check.

## Human Review Recommendation

Check the convention that `F_G(pi, X)` in Problem 2.19 is taken for the fixed
`p` from the surrounding group-p-USF context. With `p = 1`, the example is a
complete counterexample to path-connectedness.

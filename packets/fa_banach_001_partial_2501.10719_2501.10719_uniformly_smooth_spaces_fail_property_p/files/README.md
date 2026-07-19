# Uniformly Smooth Spaces Fail Property P

Status: `partial_result_likely_valid`.

Source paper: Kalidas Mandal, Jayanta Manna, Kallol Paul, Debmalya Sain,
*On approximate preservation of orthogonality and its application to
isometries*, arXiv:2501.10719; Colloquium Mathematicum 179 (2025), 189-211.

## Result

The source introduces `Property P`: a Banach space `X` has Property P if some
`epsilon in (0,1)` forces every bounded linear operator on `X` that preserves
`epsilon`-approximate Birkhoff-James orthogonality at every point to be a
scalar multiple of an isometry.

This packet proves the following broad negative theorem:

> Every real uniformly smooth Banach space of dimension greater than one fails
> Property P.

Equivalently, for every `epsilon in (0,1)` there is an invertible bounded
linear operator `T` on `X` that preserves `epsilon`-orthogonality at all points
but is not a scalar multiple of an isometry.

## Method

Choose a unit vector `v` and a norm-one functional `phi` with `phi(v)=0`, and
use the rank-one shear

`T_delta x = x + delta phi(x)v`.

Uniform smoothness makes the unit support-functional map uniformly continuous
on the relevant annulus.  Hence, for small `delta`, if `x` is Birkhoff-James
orthogonal to `y`, the unique supporting functional at `T_delta x` almost
annihilates `T_delta y`, with a uniform error bounded by the chosen `epsilon`.
The same shear is never a scalar multiple of an isometry, because it fixes
`ker phi` pointwise and translates every affine line `w + R v` with
`phi(w)=1`.

## Scope

This is a partial result for the landscape opened by the source paper, not a
full classification of spaces with Property P.  It subsumes the uniformly smooth
negative examples `ell_p` and `ell_p^n` for `1<p<infty`, and it is compatible
with the source's positive finite-dimensional polyhedral examples, which are
not smooth.

The packet records a bounded novelty check.  Local run indexes showed no prior
packet for arXiv:2501.10719 or this theorem.  Web search found the source's
published Colloquium Mathematicum entry and the 2026 Lebesgue-Bochner
continuation arXiv:2601.02786, but no statement that all uniformly smooth
spaces fail Property P.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: rendered source page containing the Property
  P query and definition.

# Partial Packet: Finite-Dimensional Quotients Obstruct Epsilon-Hypercyclicity

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- agent: `agent_lane_08`
- source arXiv id: `2103.08075`
- source paper: Sebastian Tapia-Garcia, *An epsilon-hypercyclicity criterion and its application on classical Banach spaces*
- target: the introduction asks whether every separable infinite-dimensional Banach space admits an `epsilon`-hypercyclic operator which is not hypercyclic, for `epsilon in (0,1)`.

## Claim

No nonzero finite-dimensional Banach space admits an `epsilon`-hypercyclic
operator for any `epsilon < 1`. Consequently, if `T` is `epsilon`-hypercyclic
on a Banach space `X` with `epsilon < 1`, then `T` has no nonzero
finite-dimensional invariant quotient. Equivalently, `T` has no invariant
closed subspace of finite codimension.

This explains why the most tempting construction strategy for the source
problem cannot work: one cannot take a hypercyclic operator on a hyperplane and
add a one-dimensional non-hypercyclic marker coordinate. Any such marker would
be a finite-dimensional quotient obstruction to `epsilon`-hypercyclicity.

## Scope

This is a partial obstruction, not a construction of a new
`epsilon`-hypercyclic non-hypercyclic operator. The full source question remains
open here.

The result is useful for future attempts because it says that the
non-hypercyclic obstruction must be genuinely infinite-dimensional or must avoid
passing to a finite-dimensional quotient altogether.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2103.08075
- `figures/open_problem_crop.png`: crop of the source open-question passage

## Verification

The proof is purely analytic. Human review should check the finite-dimensional
orbit dichotomy: if a finite-dimensional orbit has a subsequence converging to
zero, then the cyclic restriction has spectral radius strictly less than one,
so the orbit is bounded and cannot also see arbitrarily large scales.

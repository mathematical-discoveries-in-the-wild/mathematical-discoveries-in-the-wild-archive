# Partial Packet: Complemented-Summand Transfer for Small Gradient Cones

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- agent: `agent_lane_08`
- source arXiv id: `0002108`
- source paper: Daniel Azagra and Mar Jimenez-Sevilla, *Rolle's theorem is either false or trivial in infinite-dimensional Banach spaces*
- target: Open Problem 4.5 asks whether every separable reflexive infinite-dimensional Banach space with a `C^p` smooth Lipschitz bump has another such bump whose derivative cone has empty interior in the dual.

## Claim

The property in Open Problem 4.5 is stable under complemented direct sums:
if a complemented summand `Y` has a smooth Lipschitz bump `b` with
`C(b)` of empty interior in `Y*`, and the complementary summand has any smooth
Lipschitz bump, then `X = Y direct_sum Z` also has a smooth Lipschitz bump
with empty derivative cone in `X*`.

Consequently, every Banach space with a `C^1` smooth Lipschitz bump and a
complemented subspace isomorphic to `ell_2` satisfies the `C^1`
Lipschitz-bump conclusion of Open Problem 4.5, because the source paper proves
that case for `ell_2`.

## Scope

This is a partial transfer theorem, not a full solution of the separable
reflexive problem. It covers all spaces where a solved summand is complemented,
including `ell_2 direct_sum Z` and any smooth space containing a complemented
copy of `ell_2`.

The remaining hard case is a reflexive smooth space whose Hilbert/small-cone
substructures, if any, are not complemented.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:math/0002108
- `figures/open_problem_crop.png`: crop of Open Problem 4.5

## Verification

Human review should focus on the projection argument: if the derivative cone
of the product bump in `X* = Y* direct_sum Z*` had nonempty interior, its
projection to `Y*` would be a nonempty open subset contained in `C(b)`, which
contradicts the empty-interior hypothesis on the summand.

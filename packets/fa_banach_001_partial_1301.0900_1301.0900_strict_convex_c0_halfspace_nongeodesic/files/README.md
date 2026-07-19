# Strict-convex c0 half-space non-geodesicity

Status: `partial_result_likely_valid` / source-announced omitted proof.

Source target: Antti Rasila and Jarno Talponen, "On Quasihyperbolic Geodesics in Banach Spaces", arXiv:1301.0900, Conjecture 2.5.

## Result

The packet gives a complete proof of the strict-convex `c0` half-space example stated without proof immediately after Conjecture 2.5.  With
\[
N(x)^2=\|x\|_\infty^2+\sum_{n\ge 1}2^{-n}|x_n|^2
\]
and a positive `f=(f_n)\in \ell_1` satisfying `f_n/2^{-n}` unbounded, the open half-space
\[
\Omega=\{x\in c_0:\sum f_nx_n>0\}
\]
is not geodesic in the quasihyperbolic metric induced by `N`; in fact no two distinct points of `\Omega` are joined by a quasihyperbolic geodesic.

## Scope

This does not settle the full Rasila--Talponen conjecture, which asks whether an arbitrary strictly convex Banach space is reflexive exactly when all of its open half-spaces are quasihyperbolically geodesic.  It verifies the canonical nonreflexive strict-convex `c0` subcase and supplies the missing proof details for the source remark.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: page-7 crop with Conjecture 2.5 and the omitted-proof remark.

## Verification

No numerical computation is used.  The proof is analytic: a far-coordinate bump changes only a `2^{-m}`-weighted part of the strict convex norm but increases the half-space distance denominator by `f_m`; choosing `m` with `f_m/2^{-m}` large strictly shortens any alleged geodesic.


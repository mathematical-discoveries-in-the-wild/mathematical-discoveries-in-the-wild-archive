# Counterexample: the Lp projection-constant equality conjecture

agent_id: agent_lane_16
run_id: fa_banach_001
arxiv_id: 1503.08912
source: G. M. Ivanov, "Modulus of supporting convexity and supporting smoothness"
date: 2026-06-28
status: counterexample_likely_valid

## Result

Conjecture 1 in the source paper says that the right-hand side of inequality
(13) should be an equality for `L_p`, `1<p<infinity`. This packet gives a
finite-dimensional `L_p` counterexample:

```text
X = ell_20^2.
```

For this space,

```text
xi_X <= 2^(9/10),
```

but the right-hand side of the source upper estimate is strictly larger than
`2^(9/10)`. Hence the claimed equality fails.

## Mechanism

For `ell_20^2`, every support projection has rank one, and its norm is bounded
by a simple Holder estimate. On the other hand, an explicit almost-flat tangent
configuration shows `lambda_X^-(1) < 10^-6`, so the argument of `lambda_X^+` in
the source upper bound is at least `0.4999995`. Evaluating `lambda_X^+` on the
symmetric support pair then already forces the source upper expression above
`2^(9/10)`.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:1503.08912.
- `figures/open_problem_crop.png` - crop of Theorem 4 / Conjecture 1.
- `code/check_counterexample.py` - high-precision verifier for the strict
  scalar inequalities used in the proof.

## Novelty Check

Cheap indexes were searched for `1503.08912`, supporting convexity/smoothness,
hyperplane projection constants, and related Birkhoff-James terms. Web searches
on 2026-06-28 for the exact title, the `L_p` conjecture phrase, and hyperplane
projection constants found the source arXiv record and the later Ivanov-Martini
paper `1609.01587`, but no later explicit resolution of this conjecture. The
run already contains a packet for a different conjecture in `1609.01587`; it is
not this projection-constant conjecture.

## Review Recommendation

Likely valid counterexample. Human review should check that the source's
`L_p` wording includes finite-dimensional `ell_p^2`, and should verify the
rank-one formula for support projections in two-dimensional `ell_p`.

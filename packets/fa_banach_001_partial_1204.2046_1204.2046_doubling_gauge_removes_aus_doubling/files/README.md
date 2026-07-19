# Partial Result: Removing AUS-Doubling for Doubling Gauges

Run: `fa_banach_001`

Agent: `agent_super_01`

Status: `partial_result_likely_valid`

## Source Problem

Jean-Matthieu Auge, *Orbits of linear operators and Banach space geometry*,
arXiv:1204.2046.

The source proves Theorem 4.3 under the auxiliary hypothesis
`\bar\rho_X(2t)=O(\bar\rho_X(t))` for the modulus of asymptotic uniform
smoothness, and ends with the remark that it is not known whether this
assumption is really necessary.

## Result

The packet proves that the source's AUS-doubling hypothesis is not needed
when the comparison gauge `rho` is itself dyadically doubling at zero.

Precisely, let `f(t)=\bar\rho_X(t)`. If `rho` is nondecreasing, positive on
`(0,infty)`, satisfies `rho(2t)=O(rho(t))` as `t downarrow 0`, and
`f(t)/rho(t) -> 0`, then for every non-nilpotent bounded operator `T` on `X`
there exists `x` such that

```text
sum_n rho(||T^n x|| / ||T^n||) = infinity.
```

Thus the extra doubling assumption on `f=\bar\rho_X` can be removed for all
power gauges `rho(t)=t^q`, and more generally for regularly dyadic gauges.

## Method

The proof isolates the only place where the source uses
`\bar\rho_X(2t)=O(\bar\rho_X(t))`: constructing coefficients `alpha_i` with
all dyadic rescalings `sum_i f(2^k alpha_i)` summable while
`sum_i rho(alpha_i/2)` diverges.

For dyadically doubling `rho`, the hypothesis `f=o(rho)` implies
`f(2^k t)=o(rho(t/2))` for every fixed `k`. A diagonal repetition lemma then
produces the required coefficient sequence simultaneously for all `k`. The
rest of Auge's inductive construction is unchanged.

## Scope

This is not a full solution of the arbitrary-gauge question in the source
remark. If `rho` is allowed to decay much faster under fixed dilations, the
diagonal comparison may fail. The result settles the source's main power-gauge
use case but leaves genuinely non-doubling gauges open.

## Files

- `main.tex`: proof note.
- `solution_packet.pdf`: rendered proof note.
- `source_paper.pdf`: arXiv:1204.2046.

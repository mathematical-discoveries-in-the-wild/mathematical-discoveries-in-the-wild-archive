# Gaussian RSSI open problem: symmetric and nested subcases

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Source: arXiv:2602.07981, Emanuel Milman, Shohei Nakamura, and Hiroshi
Tsuji, "The Gaussian Conjugate Rogers-Shephard Inequality"  
Processed: 2026-07-03 by `agent_lane_04` in lane 1

## Claim

The packet records two elementary but useful subcases of the source paper's
open Gaussian Rogers--Shephard--Spingarn question:

`gamma(K) gamma(L) <= gamma(K cap L) gamma(K-L)`.

The inequality holds for convex sets with non-empty interior and Gaussian
barycenters at the origin if either:

1. one of `K,L` is centrally symmetric; or
2. the sets are nested, i.e. `K subset L` or `L subset K`.

It also records the parameter-level sign-flip observation: whenever one set is
centrally symmetric, the source paper's `sigma=+1` parameter region transfers
to the `sigma=-1` version of its general problem.

## Source Question

The open question appears on page 5 of the source paper, immediately after
Theorem 1.3.  The authors ask whether, under the same Gaussian-barycenter
assumptions,

`gamma(K) gamma(L) <= gamma(K cap L) gamma(K-L)`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of the source open question.

## Human Review Focus

1. Check that the reflection/sign-flip argument really preserves both Gaussian
   measure and the intersection factor when one set is centrally symmetric.
2. Check the centering lemma used for the nested case: after replacing convex
   sets by closures, Gaussian barycenter zero forces `0` to lie in the set.
3. Keep the status partial: this does not address the genuinely nonsymmetric,
   nonnested case of the source problem.


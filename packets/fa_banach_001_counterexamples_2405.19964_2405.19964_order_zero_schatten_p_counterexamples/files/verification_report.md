# Verification Report

Candidate: arXiv:2405.19964 p-Schatten boundedness question.

## Claim checked

There is a single real symbol `F in S^0_{rho,0}(R^4)` for every
`0 <= rho <= 1` such that its non-magnetic super Weyl quantization is bounded
on S2 but unbounded on Sp for every `p != 2`.

## Verdict

`likely valid`

Confidence: 94/100.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Khintchine-small sign blocks | valid | Pointwise Khintchine followed by integration gives an Lq norm at most `C_q sqrt(N)` for some sign choice. |
| Dirichlet lower bound | valid | On an interval of length comparable to `1/N`, the Dirichlet kernel has size comparable to `N`, giving `N^(1-1/q)`. |
| One sequence for all q | valid | Repeating every rational `q>2` infinitely often and enlarging disjoint blocks forces unbounded ratios for each such q. |
| Passage to all p != 2 | valid | L2 boundedness plus interpolation handles `p>2`; real-symbol duality handles `1<p<2`; endpoint boundedness would interpolate/dualize to a forbidden finite exponent. |
| Smooth interpolation | valid | Disjoint translates of one compactly supported plateau bump give a C-infinity function with all derivatives uniformly bounded. |
| Hoermander membership | valid | All position derivatives are bounded and all momentum derivatives vanish, giving both regular and double order-zero estimates. |
| Position-only quantization | convention-sensitive, likely valid | Tensor symbols act by left/right position multiplication; the joint distributional formula yields kernel multiplication by `F(x,y)`. This is the main source-convention check for a human. |
| Matrix compression | valid | Disjoint translates make the multiplier exactly constant `m(i-j)` on every product support, and the embedding preserves every Schatten norm. |
| Fourier-Schur transfer | external, verified | Neuwirth-Ricard arXiv:1001.5332, Theorem 2.1, bounds the Fourier multiplier norm by the associated Toeplitz Schur multiplier norm for discrete amenable groups. |
| p=infinity | valid | If the finite matrix restrictions were uniformly bounded on S-infinity, interpolation with their S2 contraction would give a forbidden finite S-q bound. |

## Counterexample and computational checks

No finite-dimensional contradiction was found. The script
`code/check_block_multiplier.py` numerically checks the expected block norm
separation. For `q=4`, 128 random trials, and a 16384-point circle grid, the
Dirichlet/random-sign norm ratio increased monotonically across the tested
sizes, from 1.6995 at `N=16` to 3.1441 at `N=256`. This is supporting evidence
only; the proof is analytic.

## External dependencies

- Lee-Lein's super Weyl convention and the tensor-symbol identity.
- Neuwirth-Ricard Theorem 2.1.
- Standard Khintchine inequality and complex interpolation/duality for Lp and
  Schatten classes.

## Gaps

No mathematical gap is currently identified. The convention-sensitive kernel
identity should be checked against the source definition before human
acceptance. Novelty confidence is lower than validity confidence because the
bounded search may miss non-arXiv or differently phrased treatments of this
standard Schur-multiplier embedding.

## Human review recommendation

`send to human`


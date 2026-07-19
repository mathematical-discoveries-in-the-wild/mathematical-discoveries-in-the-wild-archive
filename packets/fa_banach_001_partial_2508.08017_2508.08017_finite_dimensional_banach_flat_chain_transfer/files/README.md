# Partial Result: Finite-Dimensional Banach Transfer for Alberti--Marchese

Status: `partial_result_likely_valid`

Source/open-problem paper: D. Bate, E. Caputo, J. Takac, P. Valentine,
P. Wald, *Structure of Metric 1-currents: approximation by normal currents
and representation results*, arXiv:2508.08017.

Supporting theorem: G. Alberti and A. Marchese, *On the structure of flat
chains with finite mass*, arXiv:2311.06099, Theorem 1.1.

## Target

The source paper proves the one-dimensional metric flat-chain conjecture and a
Banach-space version of the Alberti--Marchese restriction theorem for
`1`-currents. In the proof discussion, lines 456--459 of the parsed source say
that for `k >= 2` strict polyhedral approximation fails in every
infinite-dimensional Hilbert space, and it is therefore unclear whether
Alberti--Marchese Theorem 1.1 extends beyond finite-dimensional Euclidean
space.

## Result

Let `E` be a `d`-dimensional Banach space and let `1 <= k < d`. Let `T` be a
real `k`-dimensional flat chain with finite mass in `E`. For every linear
isomorphism `A:E -> R^d` and every `epsilon > 0`, there are a boundaryless
normal `k`-current `N` in `E` and a Borel set `B subset E` such that

`T = N restricted to B`

and

`M_E(N) <= (2+epsilon) ||A||^k ||A^{-1}||^k M_E(T)`.

Equivalently, after taking `A` close to a Banach--Mazur minimizer, the constant
is `(2+epsilon) d(E,ell_2^d)^k`, up to the usual arbitrarily small slack in the
choice of `A`.

## Idea of the Proof

The theorem is a bi-Lipschitz transfer of Alberti--Marchese's Euclidean
restriction theorem. Push `T` forward through a linear isomorphism from `E` to
Euclidean `R^d`, apply Alberti--Marchese there, then pull the boundaryless
normal current and the Borel set back to `E`. Normality, boundarylessness, and
restriction identities are preserved by the inverse linear map. The mass is
multiplied by at most the `k`-th power of the relevant Lipschitz constants.

## Evidence

- `source_paper.pdf`: local copy of arXiv:2508.08017.
- `supporting_paper_2311.06099.pdf`: local copy of arXiv:2311.06099.
- `solution_packet.pdf`: compiled proof packet.
- No computational code was needed.

## Search Bounds

Before packaging, the cheap run indexes were searched for `2508.08017`,
`Structure of metric 1-currents`, `metric 1-currents`, `flat chain
conjecture`, `Alberti Marchese`, `finite-dimensional Banach`, `metric
currents`, and related core phrases. No prior packet for this transfer result
was found.

Web searches on June 19, 2026 for combinations including `"Alberti" "Marchese"
"finite-dimensional Banach" "flat chains"`, `"On the structure of flat chains
with finite mass" "Banach"`, and `"metric currents" "finite-dimensional
Banach" "flat chains"` found the Alberti--Marchese arXiv paper and adjacent
metric-current literature, but no direct finite-dimensional Banach transfer
statement.

## Scope Limitations

This is only a finite-dimensional Banach-space partial result and it loses the
sharp Euclidean mass constant by the `k`-th power of the selected linear
distortion. It does not address the infinite-dimensional Banach/Hilbert case
flagged in the source paper, nor does it show that arbitrary finite-mass
metric `k`-currents in Banach spaces are flat chains.

## Human Review Notes

Recommended review focus:

- Confirm that the flat-chain category used in the source is stable under
  linear bi-Lipschitz pushforward/pullback as used here.
- Check that restriction to Borel sets commutes with the pushforward by a
  bijective linear map.
- Check whether finite-dimensional normed-space versions of
  Alberti--Marchese are already explicit in the literature, in which case this
  packet should be reclassified as literature-implied rather than new partial.

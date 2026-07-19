# Stronger partial packet for Problem 3.19

Source: Jan Rozendaal and Mark Veraar, *Fourier multiplier theorems involving
type and cotype*, arXiv:1605.09340.

Status: `strong_partial_likely_valid_consolidated`.

This is the single active packet for the arXiv:1605.09340 Problem 3.19 /
Theorem 3.21 target. It is not a full intrinsic classification for arbitrary
Banach pairs, but it is a stronger partial than the previous consolidated
packet.

## Main Additions

- Complete scalar classification: the property holds exactly for
  `1<p<=2<=q<infinity`.
- Endpoint obstruction for every nonzero Banach pair `X,Y`: the faces `p=1`
  with finite `q>=2`, and `q=infinity` with `1<p<=2`, fail.
- Corrected reading of Theorem 3.21: delete the printed `p=1` endpoint and
  require the target embedding to be a closed-subspace/isomorphic embedding,
  not a merely injective continuous map.
- Endpoint correction to the positive-kernel statements: the `p=1<q` face
  fails by the same scalar Riesz-potential obstruction.
- Closed-graph uniformization for the multiplier property.
- Monotonicity in the exponent rectangle via Riesz potentials.
- Exact bilinear gamma-Pitt criterion.
- Frequency-translation obstructions for small domain blocks and large target
  blocks.
- Target cotype-index obstruction: if `X` is nonzero and the property holds,
  then the cotype index of `Y` is at most `q`.
- Complete infinite-dimensional `L^u -> L^v` and `ell^u -> ell^v`
  classification: for `1<p<=2<=q<infinity`, the property holds exactly when
  `p<=u` and `v<=q`.

## Remaining Open Core

The original arbitrary Banach-pair classification remains open. The strongest
current reduction in this packet is the exact bilinear gamma-Pitt criterion;
the remaining task is to turn that criterion into standard Banach-space
invariants such as type, cotype, Fourier type, K-convexity, or local finite
representability.

## Files

- `main.tex`: stronger partial packet source.
- `solution_packet.pdf`: compiled 9-page packet.
- `source_paper.pdf`: local copy of arXiv:1605.09340.
- `figures/`: source-paper screenshots for Problem 3.19 and Theorem 3.21.
- `history/previous_consolidated_packet_2026_06_18/`: previous active packet,
  preserved for provenance.

## Human Review Recommendation

Review the closed-graph uniformization argument, the closed-range target
embedding correction, the positive-kernel endpoint counterexample, the uniform
gamma-bounds in the frequency-translation constructions, and the
finite-representability step behind the cotype obstruction.

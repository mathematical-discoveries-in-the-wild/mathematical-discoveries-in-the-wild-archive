# Partial Packet: Indicator Constant for the `L_p` Scale

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- agent: `agent_lane_11`
- source arXiv id: `1404.2893`
- source paper: Michael Cwikel, Mario Milman, and Richard Rochberg, *An introduction to Nigel Kalton's work on differentials of complex interpolation processes for Kothe spaces*
- target: Looking Forward item (9), asking for which Kothe spaces the optimal indicator constant `delta(Phi)` equals `log 2`.

## Claim

For `1 <= p < infinity`, on any measure space with two disjoint finite
positive-measure sets, the indicator of `L_p` has optimal constant
`(log 2)/p` in Kalton's indicator inequality. For `L_infty`, the optimal
constant is `0`.

The same computation applies to weighted `L_p(w)` spaces whenever the
indicator is finite on the functions under consideration, because the weight
only contributes a linear term and linear terms cancel in `Delta_Phi`.

## Scope

This is a partial answer to the source's equality question. It shows that the
standard `L_p` scale has equality with the extremal value `log 2` only at
`p = 1` (apart from degenerate one-dimensional measure algebras, where even
the `L_1` defect can collapse).

It does not characterize all Kothe spaces with `delta(Phi) = log 2`.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local PDF rendered from the arXiv TeX source
- `figures/open_problem_crop.png`: crop of the source equality question

## Verification

Human review should focus on the entropy-defect calculation:
`Phi_{L_p}(f) = p^{-1}(int f log f - ||f||_1 log ||f||_1)`, and hence
`Delta Phi_{L_p} = p^{-1} Delta Phi_{L_1}`. The sharp upper bound is the
binary entropy bound, and equality is approached, indeed attained in the
usual rich measure spaces, by equal-mass functions with disjoint supports.

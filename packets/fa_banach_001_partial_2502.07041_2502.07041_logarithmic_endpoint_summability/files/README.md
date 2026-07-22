# Logarithmic endpoint summability for the continuous Bennett--Carl inclusion

**Status:** candidate partial result, likely valid; Conjecture 3.4 of
arXiv:2502.07041 remains open.

## Result

Fix `1<p<2` and let

`X_p = Lambda_{p,W_p}`,  `W_p(t)=log(e/t)^(1-p)`.

For every `beta>1`, let `Phi_beta` be a Young function satisfying

`Phi_beta(u) ~ u^p / log(e/u)^beta` as `u -> 0`.

Then the inclusion `J:X_p -> L^p` is `(Phi_beta,1)`-absolutely
summing. Equivalently, there is `C=C(p,beta)` such that every finite family
`(f_i) subset X_p` satisfies

`||( ||f_i||_p )||_{ell_{Phi_beta}}
 <= C max_{eps_i=+-1} ||sum_i eps_i f_i||_{X_p}`.

This gives one endpoint-scale sequence space strictly between `ell^p` and
every `ell^q`, `q>p`. It is stronger than separately knowing all the source
paper's `(q,1)` estimates, although it does not reach the conjectured
`ell^p` conclusion.

## Mechanism

The source proof can be made quantitative. Uniformly for `q` just above `p`,

`pi_{q,1}(J) <= C_p (q-p)^(-1/q)`.

The only singular factor comes from the explicit embedding
`Exp L^{p'} -> X_q`; its `q`-th power is `O((q-p)^(-1))`. Integrating these
near-endpoint estimates against `(q-p)^(beta-1)` gives the Orlicz modular
`u^p/log(e/u)^beta`. The packet includes the complete extrapolation argument,
so the result does not depend on an unproved quantitative interpolation
claim.

## Verification and limits

- The Rademacher lower estimate in `X_q` is proved directly by aligning the
  largest coefficients on events of measure `2^(-k-1)`; its constant is
  uniform for `q` in a compact interval above `p`.
- The norm of `Exp L^{p'} -> X_q` is computed explicitly from decreasing
  rearrangements.
- The final extrapolation integral converges exactly for `beta>1` by this
  route. It diverges at `beta=1`, so neither that border nor Conjecture 3.4 is
  claimed.
- A bounded web/arXiv and local-corpus search on 2026-07-21 found no later
  settlement of Conjecture 3.4 and no explicit application of the logarithmic
  extrapolation theorem to this inclusion.

The main verifier focus should be the locally uniform Rademacher constant and
the normalization in the `(Phi_beta,1)` Luxemburg estimate.

## Files

- `main.tex` and `solution_packet.pdf`: full proof and review note.
- `source_paper.pdf`: arXiv:2502.07041.
- `supporting_paper_2503.20478.pdf`: the later extrapolation template.
- `figures/open_problem_crop.png`: Conjecture 3.4 on source PDF page 12.
- `code/`: diagnostic finite-matrix searches; these are evidence only, not
  part of the proof.


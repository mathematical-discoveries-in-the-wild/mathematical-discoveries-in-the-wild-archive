# Multiplicative Equality Scaling Reduction

status: partial_result_likely_valid

## Source

- arXiv:2602.10812
- Sotiris Armeniakos and Jacopo Ulivelli, "A new infinitesimal form of the Prekopa--Leindler inequality with multiplicative structure and applications"
- Target signal: page 15, after the proof of Theorem 1.1, notes that a full characterization of equality cases in the multiplicative infinitesimal Prekopa--Leindler inequality is future work.

## Result

This packet proves an exact algebraic reduction of equality in the multiplicative inequality
\[
  \langle\rho,\varphi\rangle_I^2
  \le
  \langle\rho,\rho\rangle_P\langle\varphi,\varphi\rangle_{BL}
\]
to equality in the additive/mean inequality
\[
  \langle\rho,\varphi\rangle_I
  \le
  \frac{\langle\rho,\rho\rangle_P+\langle\varphi,\varphi\rangle_{BL}}{2}.
\]

Apart from the trivial zero/constant-kernel cases, multiplicative equality for \((\rho,\varphi)\) holds if and only if there is a scalar \(\lambda\ne0\) such that \((\lambda\rho,\varphi)\) is an equality case of the mean inequality. Equivalently, \(\lambda=\langle\rho,\varphi\rangle_I/\langle\rho,\rho\rangle_P\).

As a corollary, every nontrivial equality family from Proposition 2.8 of the source paper generates a two-scalar family of multiplicative equality cases, and the product-only cases are precisely the unequal scalar rescalings inside that family.

## Scope

This does not give the full geometric characterization of equality cases requested as future work. It reduces the multiplicative equality problem to the mean-form equality problem plus one scalar normalization. The remaining hard piece is therefore the equality characterization for the underlying Prekopa--Leindler second-variation/mean inequality.

## Verification

- The proof is purely algebraic and uses the source paper's Lemma 2.7 mechanism, applied with equality tracked in the quadratic discriminant.
- Local cheap indexes had no existing packet or attempt for arXiv:2602.10812.
- Web search for the exact title and equality-case keywords found no later equality-case resolution; the same-author follow-up arXiv:2602.23350 concerns dimensional Brunn--Minkowski and the (B)-conjecture, not equality cases for this multiplicative form.

## Files

- `main.tex`: full partial-result note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2602.10812.
- `figures/open_problem_crop.png`: page 15 crop showing the future-work/equality-case passage.
- Ledger: `runs/fa_banach_001/ledger/results/2602.10812_multiplicative_equality_scaling_reduction.json`.


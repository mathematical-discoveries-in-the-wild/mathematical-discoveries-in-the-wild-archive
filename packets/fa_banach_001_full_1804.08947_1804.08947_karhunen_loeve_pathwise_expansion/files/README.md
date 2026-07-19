# Candidate Full Result: Pathwise Karhunen-Loeve Expansion from the Separating Dual

- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_11`
- **arXiv:** `1804.08947`
- **Source paper:** Petru A. Cioica-Licht, Sonja G. Cox, Mark C. Veraar, *Stochastic integration in quasi-Banach spaces*
- **Source location:** Remark 2.26, page 14
- **Status:** `candidate_full_solution_likely_valid_needs_human_review`
- **Includes provenance:** `provenance/partial_basis_from_dual_packet/`

## Claim

Under the hypotheses of Proposition 2.25, namely for a separable `r`-Banach space `E` whose dual separates points and an `E`-valued Gaussian random variable `X`, the two questions in Remark 2.26 have positive answers.

There is an orthonormal basis `(h_n)` of Byczkowski's Gaussian Hilbert space `E^2(P_X)` with each `h_n in E^*`, and there are vectors `x_n in E` such that

```tex
\sum_{n=1}^\infty h_n(X)x_n = X
```

almost surely.

## Proof Sketch

1. The prior partial packet's density argument shows that the canonical image of `E^*` is dense in `E^2(P_X)`, hence Gram-Schmidt gives an ONB `(h_n) subset E^*`.
2. Proposition 2.25 / Byczkowski gives a Gaussian series `Y_0 = sum gamma_j y_j` with law `P_X`.
3. The source paper's finite-matrix estimate turns the coefficient sequence `(y_j)` into a bounded coefficient operator `R_0 : ell^2 -> E`; the testing-against-an-ONB theorem makes it gamma-radonifying.
4. For each `h_n`, the scalar expansion of `h_n(Y_0)` has coefficient vector `a_n=(h_n(y_j)) in ell^2`. These `a_n` are orthonormal.
5. Rotate the coefficient operator by `e_n -> a_n` and set `x_n=R_0 a_n`. Then `h_k(x_n)=delta_kn`.
6. For every `x^* in E^*`, the numbers `x^*(x_n)` are the Fourier coefficients of `x^*` in the ONB `(h_n)`, so `x^*(sum_{n<=N} h_n(X)x_n) -> x^*(X)` in `L^2`.
7. Ito-Nisio in the source paper upgrades this scalar convergence to almost-sure convergence in `E`.

## Files

- `main.tex` - source for the solution packet
- `solution_packet.pdf` - compiled packet
- `source_paper.pdf` - source arXiv paper
- `figures/open_problem_crop.png` - screenshot crop of Remark 2.26
- `provenance/partial_basis_from_dual_packet/` - earlier partial proof of the density/basis subclaim
- `provenance/partial_basis_from_dual_ledger.json` - superseded ledger record retained for provenance

## Review Notes

Human review should focus on the coefficient-operator lemma and the final Ito-Nisio step. The result uses machinery from the source paper itself; it is a proof closure of the remark, not a claim that a later external paper explicitly resolved it.

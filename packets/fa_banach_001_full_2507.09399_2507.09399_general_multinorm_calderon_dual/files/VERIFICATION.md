# Verifier report

Verdict: `likely valid`, candidate full solution pending expert review.

Date: 2026-07-21

## Checks performed

1. **Exact source match.** The statement in Section 13, item 4, page 63 of
   arXiv:2507.09399 was checked against the source PDF and source TeX. The
   theorem answers the intrinsic non-tensor Calderón-family existence question
   under exactly the three listed hypotheses.

2. **Fourier scaling.** For the source convention
   `Psi_L^{(-L)}(x) = 2^{sum l_i q_i} Psi_L(2^L x)`, its Fourier transform is
   `hat(Psi_L)(2^{-L} xi)`, as used in the proof.

3. **Tail estimate.** On each marked-partition piece `L_S`, the unmarked scale
   coordinates are determined by the marked ones. Cancellation gives
   geometric decay below each marked frequency, while Schwartz decay gives
   arbitrarily high geometric decay above any coordinate frequency. Therefore
   the off-tube sum is uniformly summable and tends to zero with the tube
   enlargement.

4. **Ellipticity.** After the off-tube sum is made less than `1/2`, the retained
   atoms have sum of modulus at least `1/2`. Bounded overlap gives one retained
   atom of modulus at least `1/(2 N_R)`, hence the Gram symbol is bounded below
   by `(2 N_R)^{-2}`.

5. **Uniform Schwartz control.** On the normalized support of the `L`th cutoff,
   only indices `P` with bounded `|P-L|` enter the denominator. All relative
   dilations are therefore uniformly bounded. The reciprocal denominator and
   all its derivatives are uniform, and the dual symbols are uniformly
   `C_c^infinity`.

6. **Cancellation.** The dual Fourier support avoids every hyperplane
   `eta_i=0` with `i in D_L`; hence all partial derivatives vanish there and
   every moment in the corresponding physical variable is zero.

7. **Exact identity.** Multiplication of the analysis and dual symbols gives
   `theta_L |a_L|^2 / A`. Summing gives exactly `1`, including for complex-valued
   families because of the conjugate in the dual.

8. **Scope control.** The packet does not claim the tensor-specific `Phi_L`
   partial-sum formula or the broader mutual `L^1` square-function equivalence.

9. **Build and visual QA.** `main.tex` compiles with `latexmk` to a five-page
   PDF. All pages and the source-question crop were rendered and inspected.

## Primary reviewer focus

Review the fixed-enlargement/off-tube summation in Lemma 1 across the finitely
many marked partitions. The frame inversion after that lemma is algebraic.


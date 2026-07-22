# Counterexample: no uniform convexity modulus as the MMD regularization vanishes

Status: `candidate_counterexample_likely_valid_full_negative_answer`

Source: Viktor Stein, Sebastian Neumayer, Nicolaj Rux, and Gabriele Steidl,
*Wasserstein Gradient Flows for Moreau Envelopes of f-Divergences in
Reproducing Kernel Hilbert Spaces*, arXiv:2402.04613, Remark 23.

## Source question

For regularization parameters \(\lambda_N\downarrow0\), the source asks
whether the MMD-regularized functionals \(D_{f,\nu}^{\lambda_N}\) admit a
uniform lower bound on their convexity moduli along generalized Wasserstein
geodesics. Such a bound would let an Ambrosio--Gigli--Savaré stability theorem
identify the limit of the regularized gradient flows.

## Result

The answer is **no in the stated generality**, already for standard data:

- dimension \(d=1\);
- Gaussian kernel \(K(x,y)=\exp(-(x-y)^2/2)\);
- Tsallis-2 entropy \(f(a)=(a-1)^2\);
- target \(\nu=\delta_0\).

Let \(E_\lambda=D_{f,\delta_0}^{\lambda}\). If \(\kappa_\lambda\) is any
convexity modulus for \(E_\lambda\) along generalized geodesics, then
\[
  \kappa_\lambda\le -\frac{1}{e\lambda(1+2\lambda)}.
\]
Consequently, for every \(\lambda_N\downarrow0\), the moduli have no finite
uniform lower bound.

The source's approximation hypotheses can simultaneously be met: take
\(\lambda_N=1/N\), \(\mu_0=\delta_0\), and
\(\mu_{0,N}=N^{-1}\sum_{i=1}^N\delta_0=\delta_0\). Then
\(E_{\lambda_N}(\mu_{0,N})=0\) for every \(N\).

## Proof in one line

On the embedded line of Dirac masses,
\[
 H_\lambda(x):=E_\lambda(\delta_x)
 =\frac{(1-e^{-x^2/2})(e^{-x^2/2}+4\lambda+1)}
        {2\lambda(1+2\lambda)},
\]
and direct differentiation gives
\(H_\lambda''(1)=-1/[e\lambda(1+2\lambda)]\). Generalized geodesics between
two Dirac masses are uniquely the ordinary Dirac interpolation, so every
global convexity modulus is at most this second derivative.

## Scope

This closes the literal uniform-modulus question negatively under the
paper's general assumptions. It does **not** show that the corresponding
gradient flows fail to converge. It only shows that a uniform global
generalized-geodesic semiconvexity bound cannot justify convergence in full
generality. Restricted questions for non-atomic targets or narrower
entropy/kernel classes remain open.

## Files

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered proof packet.
- `verification.md`: independent algebra/calculus checks.
- `source_paper.pdf`: local copy of arXiv:2402.04613.
- `figures/open_question_crop.png`: Remark 23 containing the question.
- `figures/source_tsallis2_formula_crop.png`: source's Dirac/Tsallis-2 formula.

## Search evidence

The four cheap run indexes were searched for the arXiv identifier and for
combinations of MMD, generalized geodesic convexity, Moreau envelopes,
uniform convexity moduli, Tsallis-2, and Gaussian kernels. No prior packet or
attempt was found. Bounded arXiv web searches on 2026-07-21 for the exact
question and these core terms found the source and related MMD-flow work, but
no later paper explicitly resolving this uniform-modulus question.

Human review recommendation: verify the convention for a convexity modulus
against Definition (30) in the source, then accept as a full negative answer
to Remark 23 in the paper's stated generality.

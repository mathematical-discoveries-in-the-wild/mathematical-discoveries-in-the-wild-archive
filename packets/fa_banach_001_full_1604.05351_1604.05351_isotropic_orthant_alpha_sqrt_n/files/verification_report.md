# Verification report

Packet: `1604.05351_isotropic_orthant_alpha_sqrt_n`

Date: 2026-07-21

Verdict: `candidate_full_solution_likely_valid`, suitable for human review.

## Analytic proof audit

The proof has four independent components.

1. **One-sided moment lemma.** For a nonnegative log-concave variable \(Y\),
   its survival function is log-concave. Markov's inequality at twice the mean
   therefore gives an exponential tail and
   \[
   \mathbb E Y^2\le\left(4+\frac8{(\log2)^2}\right)(\mathbb EY)^2.
   \]
2. **Centered inball.** For every marginal \(Z=\langle X,\theta\rangle\) of
   the uniform measure on \(K\), Grunbaum's inequality gives
   \(\mathbb P(Z\le0)\ge e^{-1}\). Applying the first step conditionally to
   \(-Z\) on the negative halfline shows
   \(h_K(\theta)\ge c_0\sigma\), hence \(c_0\sigma B_2^n\subset K\).
3. **Orthant lower bound.** Relative entropy against the Gaussian with the
   same covariance gives
   \(\sigma/|K|^{1/n}\ge(2\pi e)^{-1/2}\). One Euclidean-ball sector in an
   arbitrary orthant then proves \(\alpha_n\ge c/\sqrt n\).
4. **All-dimensional upper bound.** Sylvester-Hadamard cones give the source's
   simplex-volume example in every power-of-two block. Binary decomposition
   of \(n\) and a bounded entropy loss give \(\alpha_n\le4e/\sqrt n\).

No computational assertion is used to close an analytic gap.

## Reproducible finite-dimensional checks

Command run from the packet directory:

```bash
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python \
  code/verify_hadamard_blocks.py
```

Output summary:

```text
HADAMARD CHECKS: PASS
BINARY BLOCK CHECKS: PASS
tested every 1 <= n <= 100000
largest observed binary entropy per coordinate = 1.386109874246
proof bound = 2.772588722240
C0 = 20.650951848045
centered inball factor = 0.132296537209
alpha_n >= 0.064023777920/sqrt(n)
alpha_n <= 10.873127313836/sqrt(n)
ALL VERIFICATION CHECKS: PASS
```

For each \(d=1,2,4,\ldots,128\), the script verifies exactly that the
Sylvester matrix has first row all ones and \(H_d^T H_d=dI\). It checks the
log-determinant against \((d/2)\log d\), the simplex probability formula
against the factorial bound, and then checks the binary entropy and product
inequalities for every dimension through 100,000.

These checks support the algebraic bookkeeping. They do not prove the
survival-function lemma, Grunbaum's inequality, Prekopa marginal
log-concavity, or the entropy inequality; those steps are explicitly proved
or cited in `main.tex`.

## Novelty bounds

The local registry, solution, attempt, and proof-gap indexes were searched for
arXiv:1604.05351 and the core orthant/isotropic terms. Three bounded web-search
rounds used:

- the exact source phrase beginning `It may be asked what is the best
  constant`;
- `alpha_n`, `isotropic convex body`, `positive orthant`, and `orthonormal
  basis`;
- the title, authors, and arXiv id;
- `isotropic log-concave orthant probability` and the \(n^{-n/2}\) scale;
- later citations and inradius/covariance variants.

The searches found the source paper and unrelated isotropic/log-concave
results, but no later answer or matching proof. Novelty confidence is
moderate because this was not an exhaustive citation or priority search.

## Human-review focus

- Verify the use of log-concavity for the conditional negative marginal and
  the survival function.
- Verify that lower bounds on all support functions imply the centered-ball
  inclusion for a nonsymmetric body.
- Verify that the block-diagonal orthant fraction factors and that the binary
  entropy estimate loses only a universal exponential factor.
- Confirm that resolving \(\alpha_n\asymp n^{-1/2}\) is appropriately scoped
  as a full answer to the source's order-of-magnitude conjecture, while the
  exact leading constant remains open.

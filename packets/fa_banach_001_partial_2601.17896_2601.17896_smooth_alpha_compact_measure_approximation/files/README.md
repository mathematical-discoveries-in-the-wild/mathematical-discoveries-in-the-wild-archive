# Smooth approximation of compact trace measures: uniformly elliptic partial

Source: Denis Vinokurov, *Eigenvalue optimization in higher dimensions and
p-harmonic maps*, arXiv:2601.17896v3, Remark 1.3 on PDF page 4.

Status: candidate partial result, likely valid. This is not a full answer to
Remark 1.3.

## Result

Let `M` be a closed Riemannian manifold, let `alpha` be continuous with
`0 < c <= alpha <= C`, and let `mu` be a nonzero positive Radon measure such
that `H^1(M,alpha) -> L^2(M,mu)` is compact. Then there are smooth strictly
positive densities `alpha_n` and `rho_n` such that

```text
alpha_n -> alpha uniformly,
mu_n = rho_n dv_g -> mu weak-star,
mu_n(M) = mu(M),
lambda_k(alpha_n,mu_n) -> lambda_k(alpha,mu)
```

for every fixed finite variational eigenvalue. The normalized eigenvalues
converge as well.

The proof first constructs `mu_n` with convergence in the stronger Sobolev
multiplier norm. The main device is local smoothing that preserves Maz'ya's
vanishing capacitary modulus uniformly.

## Scope

This settles the source question for smooth uniformly positive `alpha`, in
particular for `alpha = 1`, and more generally allows continuous uniformly
positive `alpha` to be smoothed simultaneously. It does not treat rough or
degenerate energy densities, where weighted capacity is not stable under the
local translations used in the proof.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `verification.md`: explicit adversarial verification report.
- `source_paper.pdf`: arXiv:2601.17896v3.
- `figures/open_problem_crop.png`: Remark 1.3 and its immediate context.
- `code/make_open_problem_crop.py`: reproducible crop helper.
- `tmp/`: build and rendering intermediates.

## Human review recommendation

Send for expert review as a substantial partial theorem. The two most
important checks are the uniform capacity estimate for the localized
diffeomorphism smoothing and the collective-compactness lemma derived from
that estimate.


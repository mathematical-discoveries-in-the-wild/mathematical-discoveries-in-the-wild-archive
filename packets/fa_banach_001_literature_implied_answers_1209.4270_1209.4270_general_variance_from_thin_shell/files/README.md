# General variance conjecture from the solved isotropic thin-shell theorem

Run: `fa_banach_001`

Status: `literature_implied_answer (full; agent-identified implication)`

## Result

Conjectures 1.4 and 1.5 of Alonso-Gutierrez--Bastero,
arXiv:1209.4270, are true for every centered log-concave random vector.
More sharply, the optimal dimension-free constant in the general variance
inequality is exactly the optimal constant in the isotropic variance
inequality, when both are taken over all dimensions.

The source asks whether

```text
Var |X|^2 <= C lambda_X^2 E|X|^2
```

for every centered log-concave `X`, where `lambda_X^2` is the largest
eigenvalue of its covariance.  Klartag--Lehec, arXiv:2507.15495,
Theorem 1.1, now proves

```text
Var |Y|^2 <= C k
```

for every isotropic log-concave `Y` in every dimension `k`.  The supporting
paper does not state the anisotropic conclusion.  The implication is supplied
here by a spectral-layer/Abel-summation argument.

## Proof mechanism

Whiten `X` as `X=M^(1/2)Y`, where `M=Cov(X)` and `Y` is isotropic.  Diagonalize
`M` with eigenvalues `mu_1 >= ... >= mu_n >= 0`.  For the nested coordinate
projections `P_k`, every `P_k Y` is again isotropic and log-concave, now in
dimension `k`.  Abel summation gives

```text
<MY,Y> - tr M
  = sum_k (mu_k-mu_{k+1}) (|P_kY|^2-k).
```

Minkowski and the isotropic theorem bound its `L2` norm by

```text
sqrt(C) sum_k (mu_k-mu_{k+1}) sqrt(k).
```

Writing the last sum as the integral of the square root of the spectral
counting function and applying Cauchy--Schwarz yields

```text
(sum_k (mu_k-mu_{k+1}) sqrt(k))^2
    <= mu_1 sum_i mu_i
    = ||M||op tr M.
```

This is precisely the general variance conjecture, with no loss in the
universal constant.  The general thin-shell conjecture follows from

```text
E(|X|-sqrt(E|X|^2))^2 <= Var(|X|^2)/E|X|^2.
```

## Provenance classification

This packet is in `literature_implied_answers`, not `full`, because its only
deep input is the later Klartag--Lehec theorem and the repository protocol
assigns agent-identified implications of known theorems to this provenance
bucket.  Mathematically, however, it gives a complete answer to source
Conjectures 1.4 and 1.5, not merely a subcase.

The supporting authors prove the isotropic theorem and do not identify this
specific answer to arXiv:1209.4270.  The constant-preserving transfer proof is
the agent-identified part.

## Novelty and literature search

Searches performed on 2026-07-22:

- run indexes for `1209.4270`, `general variance conjecture`, `thin shell`,
  anisotropic quadratic forms, and covariance terminology;
- the TeX of arXiv:2507.15495 for `quadratic`, `linear image`,
  `non-isotropic`, `anisotropic`, and related terms;
- exact arXiv/web searches for the displayed general variance inequality,
  the phrase `general variance conjecture`, and quadratic-form variants;
- the later Alonso-Gutierrez--Bastero paper arXiv:1610.04023, whose
  introduction still says it was unclear whether the isotropic and general
  conjectures were equivalent and proves additional special cases only.

No later source explicitly stating the full anisotropic conclusion or this
spectral-layer implication was found.  Novelty confidence is therefore
moderate, not definitive: the short transfer lemma may be folklore.

The existing run packet
`solutions/literature_already_answered/1310.1204_slicing_thin_shell_answers_2024_2025/`
records the isotropic theorem but explicitly does not address the general
variance conjecture from arXiv:1209.4270.

## Verification

- `main.tex` contains the formal theorem and proof.
- `code/verify_spectral_layer.py` checks the Abel identity and the deterministic
  spectral inequality on 20,000 seeded random spectra.
- `solution_packet.pdf` was rendered and visually inspected page by page.
- `figures/open_problem_crop.png` shows source Conjectures 1.4 and 1.5 on
  PDF page 2.
- `figures/supporting_answer_crop.png` shows Theorem 1.1 of arXiv:2507.15495
  on PDF page 2.

## Files

- `source_paper.pdf`: arXiv:1209.4270.
- `supporting_paper_2507.15495.pdf`: Klartag--Lehec's isotropic thin-shell
  theorem.
- `main.tex`, `solution_packet.pdf`: detailed implication note.
- `figures/`: source and supporting theorem crops.
- `code/verify_spectral_layer.py`: deterministic algebra smoke test.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Human review recommendation

Review as a full literature-implied answer.  The key checks are that
orthogonal marginals of an isotropic log-concave vector remain isotropic and
log-concave, and that Minkowski is applied only to nonnegative spectral
increments.  A novelty reviewer should search specifically for the same
Abel-summation transfer after the 2025 isotropic solution.


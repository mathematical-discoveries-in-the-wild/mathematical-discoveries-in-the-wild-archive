# Milman's multi-integral norm question answered by Bizeul--Klartag

Status: `literature_already_answered`.

Source/open-problem paper: Nikos Skarmogiannis, "On a multi-integral norm
defined by weighted sums of log-concave random vectors", arXiv:2208.06365
(2022; published 2023). In the Introduction, PDF pages 2--3, the paper asks
whether the norm

\[
  \|t\|_{K^s,K}=\int_{K^s}\Big\|\sum_{j=1}^s t_jx_j\Big\|_K,dx_1\cdots dx_s
\]

is Euclidean up to a factor polylogarithmic in the dimension. Theorem 1.1
reduces this to proving
\(\sqrt n M(K_*)L_{K_*}\le C(\log n)^b\) for a volume-one isotropic
image \(K_*\); the paper says on page 3 and again in Remark 4.2 on page 9
that this estimate remained open.

Supporting answer paper: Pierre Bizeul and Boaz Klartag, "Distances between
non-symmetric convex bodies: optimal bounds up to polylog", arXiv:2510.20511
(2025). Corollary 1.7, PDF page 6, proves for every convex body \(A\) in
covariance-one isotropic position that

\[
  M(A)\le C\frac{\psi_n\sqrt{\log n}}{\sqrt n}.
\]

Together with their displayed bound \(\psi_n\le C\sqrt{\log n}\), this gives
\(M(A)\le C\log n/\sqrt n\). Applying it to
\(A=K_*/L_{K_*}\) yields exactly
\(\sqrt n M(K_*)L_{K_*}\le C\log n\). Substitution into Skarmogiannis's
Theorem 1.1 gives the affirmative estimate

\[
  c\|t\|_2\le \|t\|_{K^s,K}\le C(\log n)^6\|t\|_2
\]

for all \(s\) and all centrally symmetric \(K\) (after the source's
volume-one normalization). On PDF page 7, Bizeul--Klartag explicitly cite
Skarmogiannis and state that their corollary completes, up to
polylogarithmic factors, the conjecture attributed to V. Milman. This makes
the relation an explicit later-literature answer, not an agent-only
implication.

Scope: this answers the qualitative question and supplies an admissible
exponent \(6\); optimizing the logarithmic exponent is not claimed.

Files:

- `source_paper.pdf`: arXiv:2208.06365.
- `supporting_paper_2510.20511.pdf`: arXiv:2510.20511.
- `main.tex`: compact identification note.
- `solution_packet.pdf`: rendered status note.
- ledger: `runs/fa_banach_001/ledger/results/2208.06365_milman_multi_integral_answered_by_2510.20511.json`.

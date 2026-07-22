# Quantitative-aperture reduction for the RMF equivalence problem

Status: `conditional_result_likely_valid`.

Source: Francesco Di Plinio and Yumeng Ou, *Banach-valued multilinear singular
integrals*, arXiv:1506.05827v3, Remark 3.7 (printed page 14).

The source asks whether dyadic RMF and nontangential RMF are equivalent. This
packet proves the pointwise reduction

\[
M^\triangle f(x) \lesssim M_{\Phi,C}f(x)
+\sum_{m\ge 0}2^{-m}M_{\Phi,C2^m}f(x).
\]

Consequently, nontangential RMF implies dyadic RMF under the explicit
quantitative condition

\[
\sum_{m\ge0}2^{-m}\|M_{\Phi,C2^m}\|_{L^p(X_3)\to L^p}<\infty.
\]

Polynomial aperture growth of order strictly below one suffices. The proof
uses a smooth approximation to a cube average, differentiates in scale, and
moves the derivative to the cube boundary. The boundary layer at relative
scale `2^{-m}` has mass `O(2^{-m})` and requires aperture `O(2^m)`.

The packet is conditional because ordinary nontangential RMF is not shown to
imply the summable aperture estimate. It also does not address the reverse
dyadic-to-nontangential implication. The most important review point is the
simultaneous Rademacher-bound estimate for the boundary integrals.

Files:

- `main.tex` and `solution_packet.pdf`: theorem, proof, limitations, and search status.
- `source_paper.pdf`: arXiv:1506.05827v3.
- `figures/open_problem_crop.png`: the exact source question on printed page 14.

Model: GPT5.6.

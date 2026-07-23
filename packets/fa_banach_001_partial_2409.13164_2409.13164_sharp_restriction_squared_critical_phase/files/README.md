# Sharp restriction exponent in the squared-critical phase

Status: `candidate partial result - likely valid`

Source: Xinxin Chen, Yong Han, Yanqi Qiu, and Zipeng Wang, *Harmonic
analysis of Mandelbrot cascades -- in the context of vector-valued
martingales*, arXiv:2409.13164v3.

## Result

Let \(\mu_\infty\) be the nondegenerate canonical \(b\)-adic Mandelbrot
cascade with weight \(W\), under the moment assumptions of the source paper.
Write

\[
W^{(2)}=\frac{W^2}{\mathbb E W^2}.
\]

If

\[
\mathbb E[W^{(2)}\log W^{(2)}]\geq \log b,
\]

then, almost surely on nonextinction, the supremal exponent for

\[
\|\widehat f\|_{L^2(\mu_\infty)}
   \leq C_r\|f\|_{L^r(\mathbb R)}
\]

is exactly

\[
r_*=\frac{4}{4-D_F},
\]

where \(D_F=\dim_F(\mu_\infty)\) is the deterministic Fourier dimension
computed in the source paper.  The estimate holds for every \(1\leq r<r_*\)
and fails for every \(r>r_*\).

This settles the source question in the squared-critical and
squared-supercritical regimes as a sharp supremum statement.  Whether the
estimate holds at \(r=r_*\) is not decided.

## Mechanism

The exact Frostman exponent of the cascade is

\[
\alpha_{\mathrm{Fr}}
=\sup_{q>1}\frac{q-1-\log_b\mathbb E W^q}{q}.
\]

In the squared-critical/supercritical phase, elementary convexity shows that
the supremum is attained at some \(q_*\leq2\).  The source formula for \(D_F\)
then gives \(D_F=2\alpha_{\mathrm{Fr}}\).

Any \(L^r\to L^2(\mu)\) restriction estimate forces
\(\mu(I)\lesssim |I|^{2/r'}\) for every interval \(I\), by testing a
frequency-localized Schwartz function.  Hence
\(2/r'\leq\alpha_{\mathrm{Fr}}=D_F/2\), or
\(r\leq4/(4-D_F)\).  The reverse strict range is Corollary 1.6 of the source
paper.

## Scope and verification

- Full proof and novelty bounds: `main.tex` and `solution_packet.pdf`.
- Source question: page 9, Corollary 1.6 and the following remark.
- `source_paper.pdf` is the arXiv source paper.
- `supporting_paper_1206.5444.pdf` records the sharp Frostman/modulus
  phenomenon in the classical boundary parametrization.
- The subcritical regime and endpoint attainment remain open.

Ledger:
`runs/fa_banach_001/ledger/results/2409.13164_sharp_restriction_squared_critical_phase.json`

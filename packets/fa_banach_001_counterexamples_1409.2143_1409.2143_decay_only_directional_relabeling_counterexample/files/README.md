# Counterexample packet: decay alone cannot control a directional wavelet projection by its named Riesz transform

Status: `candidate_counterexample_likely_valid` (full negative answer to the
literal decay-only formulation on p. 4 of arXiv:1409.2143, pending human
review)

Source: Paul F. X. Muller and Stefan Muller, *Interpolatory Estimates, Riesz
Transforms and Wavelet Projections*, arXiv:1409.2143; published in *Revista
Matematica Iberoamericana* 32 (2016), no. 4, 1137-1162.

## Result

The source asks for interpolatory estimates between a directional wavelet
projection `W^(epsilon)` and `R_i` when the wavelets satisfy the localization
and decay condition (1.2a) only.

In dimension two, take the tensor Haar basis and swap the labels `(1,0)` and
`(0,1)`. The resulting family remains an orthonormal wavelet basis and obeys
the source's decay estimate with constant one and every positive decay
exponent. However, its nominal `(1,0)` projection is the actual `(0,1)` Haar
projection.

For

\[
 u_N(x_1,x_2)=\mathbf 1_{[0,N)}(x_1)
 \bigl(\mathbf 1_{[0,1/2)}-\mathbf 1_{[1/2,1)}\bigr)(x_2),
\]

we have `W^(1,0)u_N=u_N`, while Plancherel and anisotropic dilation give

\[
 \frac{\|R_1u_N\|_2}{\|u_N\|_2}\longrightarrow0.
\]

Consequently there is no uniform estimate

\[
 \|W^{(1,0)}u\|_2
 \le C\|u\|_2\,
 \Psi\!\left(\frac{\|R_1u\|_2}{\|u\|_2}\right)
\]

for any control function `Psi(t)->0` as `t->0`. This rules out all power
interpolation estimates and the logarithmic endpoint estimate appearing in
the source.

## What the counterexample identifies

Decay controls localization and unconditionality, but it does not attach the
label `epsilon_i=1` to cancellation in coordinate `i`. A label-compatible
directional condition is therefore necessary. The example does not decide the
narrower problem obtained by retaining the source's sectional oscillation
condition (1.2c) while dropping only Holder regularity.

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained counterexample proof.
- `source_paper.pdf`: the original paper.
- `figures/open_problem_crop.png`: full-width crop containing item 4 on p. 4.
- `verification.md`: proof audit, stress tests, novelty bounds, and reviewer
  focus.

## Novelty and review

The four cheap run indexes were searched for the arXiv id, exact title,
directional wavelet projections, Riesz transforms, and decay-only variants.
Two bounded web-search rounds on 2026-07-22 used the exact open-problem phrase,
the paper title and authors, and close arXiv variants. They found the source
and its published version but no later answer or matching counterexample.
This is not an exhaustive priority search, so novelty confidence is
**moderate**.

Recommended expert-review focus: confirm that the literal phrase “decay
estimates only” drops direction-specific sectional oscillation (1.2c), and
check the Fourier dominated-convergence limit for the long-strip functions.

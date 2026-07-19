# Conditional Packet: Fast exponential real-axis model

Status: `conditional_reduction_likely_valid`

Agent: `agent_lane_00`  
Run: `fa_banach_001`  
Date: 2026-07-18  
Source: Antonio Arnal and Petr Siegl, "Resolvent estimates for one-dimensional Schrodinger operators with complex potentials", arXiv:2203.15938, J. Funct. Anal. 284 (2023), 109856.

## Target

Section 7.3 of the source treats
\[
H=-\partial_x^2+i e^{x^2}
\]
and states that Theorem 4.2 does not apply to the behaviour of \(\Psi(\lambda)\)
for \(\lambda\in\mathbb R_+\); consequently the critical region next to the
real axis is left open.

## Result

This packet proves the limiting first-order model which would replace the
regular-variation model in Theorem 4.2.  If the real-axis localization step from
the source extends to this fast exponential potential with that model, then
\[
\|(H-a)^{-1}\|
= {4\over \pi} e^{-t_a^2}(1+o(1)),
\qquad
t_a e^{t_a^2}=2\sqrt a.
\]
Equivalently,
\[
\|(H-a)^{-1}\|
= {\sqrt 2\over \pi}\sqrt{{W_0(8a)\over a}}\,(1+o(1))
= {\sqrt 2\over \pi}{\sqrt{\log a}\over \sqrt a}(1+o(1)).
\]
The corresponding conditional uniform-boundedness edge is
\[
0\le b < \left({\pi\over 4}-\eta\right)e^{t_a^2}
\]
for each fixed \(\eta>0\), hence asymptotically of order
\(\sqrt a/\sqrt{\log a}\).

## Conditional Dependency

The unproved dependency is the transfer from the original Schrodinger resolvent
to the normalized local model
\[
B_t=-\partial_x+e^{t^2(x^2-1)}
\]
near the Fourier turning points \(\pm\sqrt a\).  The source proves the analogous
transfer under regular variation and symbol-class derivative hypotheses; those
hypotheses fail for \(e^{x^2}\).  The packet isolates the precise model and
constant a future proof should verify.

## Files

- `main.tex`: human-readable conditional packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: crop of the source open-question paragraph.
- `code/model_kernel_check.py`: finite-dimensional numerical check of the
  model-kernel norm convergence.  This is evidence only, not a proof.

## Human Review Recommendation

Review as a conditional reduction, not as a solved open problem.  The model
theorem and constant \(4/\pi\) are the strongest proved part; the main review
question is whether the localization/commutator machinery can be extended to
\(V_2(x)=e^{x^2}\).

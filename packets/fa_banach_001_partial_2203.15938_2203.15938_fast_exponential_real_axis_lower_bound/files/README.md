# Partial Packet: Fast exponential real-axis lower bound

Status: `partial_result_likely_valid`

Agent: `agent_lane_00`  
Run: `fa_banach_001`  
Date: 2026-07-18  
Source: Antonio Arnal and Petr Siegl, "Resolvent estimates for one-dimensional Schrodinger operators with complex potentials", arXiv:2203.15938, J. Funct. Anal. 284 (2023), 109856.

## Target

Section 7.3 of the source treats
\[
H=-\partial_x^2+i e^{x^2}
\]
and says that the real-axis theorem for regularly varying potentials is not
applicable, leaving the critical region next to the positive real axis open.

## Result

This packet proves the unconditional one-sided real-axis bound
\[
\liminf_{a\to+\infty} e^{t_a^2}\|(H-a)^{-1}\| \ge {4\over \pi},
\qquad
t_a e^{t_a^2}=2\sqrt a.
\]

Equivalently, the smallest singular value of \(H-a\) is at most
\[
\left({\pi\over 4}+o(1)\right)e^{t_a^2}
\]
along the positive real axis.

## Scope

This is a substantial partial result, not a full solution of the source open
question.  It proves the lower-bound/quasimode side of the predicted asymptotic
constant.  The matching upper bound still requires a global localization
argument replacing the source's regular-variation and symbol-class commutator
machinery.

## Relation To Existing Conditional Packet

The earlier packet
`solutions/conditional/2203.15938_fast_exponential_real_axis_model/` proves the
first-order model limit \(\|B_t^{-1}\|\to4/\pi\) and records the conditional
transfer that would imply the full asymptotic.  The present packet removes the
transfer dependency for the lower-bound direction by constructing physical
wave packets directly.

## Files

- `main.tex`: human-readable partial packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: crop of the source open-question paragraph.
- `code/quasimode_residual_check.py`: optional numerical sanity check for the
  scaling identity used in the proof.

## Human Review Recommendation

Review as a likely valid partial result.  The key technical point is Lemma 3.3
in `main.tex`, which bounds the second derivative of the first-order
quasimode by a polynomial in \(t\); this makes the second-order correction
negligible after multiplication by \(e^{-t^2}\).

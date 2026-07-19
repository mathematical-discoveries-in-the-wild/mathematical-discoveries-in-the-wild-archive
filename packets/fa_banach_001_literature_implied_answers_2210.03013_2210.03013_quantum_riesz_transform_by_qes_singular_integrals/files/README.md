# Quantum Riesz Transform Boundedness from Quantum Euclidean CZ Theory

Status: `literature_implied_answer`.

Source/open-problem signal: arXiv:2210.03013, Laurent Lafleche, *On
Quantum Sobolev Inequalities*, J. Funct. Anal. 286 (2024), 110400.

## Identification

In the subsection "Boundedness of Riesz transforms in the quantum phase
space", the source observes that separate `x` and `xi` Schur multiplier
estimates imply equivalence of the two split first-order seminorms, but it is
not clear there whether those split expressions are equivalent to
`||(-DD_h)^{1/2} op||_{L^p}`.  The source then conjectures more precisely that
`(-DD_h)^{-1/2} D_h : L^p -> (L^p)^{2d}` is bounded for every `1<p<infty`
with norm independent of `hbar`.

The supporting paper is Gonzalez-Perez, Junge, and Parcet, *Singular integrals
in quantum Euclidean spaces*, arXiv:1705.01081 / Memoirs AMS 272 (2021),
no. 1334.  Their quantum Euclidean space `R_Theta` includes the Heisenberg-Weyl
algebra when `Theta = 2 pi hbar J`, and their quantum Calderon-Zygmund
extrapolation theorem gives `L_p(R_Theta)` boundedness of Calderon-Zygmund
operators, in particular quantum Fourier multipliers, for `1<p<infty`.

Under Weyl quantization in the source paper,
`D_h op_f = op_{\nabla_z f}` and
`(-DD_h)^s op_f = op_{(-Delta_z)^s f}`.  Thus each component of
`D_h(-DD_h)^{-1/2}` is the scalar quantum Fourier multiplier with the classical
Riesz symbol `i eta_j / |eta|` on the `2d`-dimensional quantum Euclidean space
`R_{Theta_h}`.  Its Calderon-Zygmund kernel is the usual homogeneous
`z_j/|z|^{2d+1}` kernel transported by the normal homomorphism `pi_Theta`;
the constants in the supporting theorem depend on `p` and `d`, not on the
deformation matrix `Theta_h`, hence not on `hbar`.

Finally, the source paper's Appendix proposition on vector-valued Schatten
operators converts boundedness of the finitely many scalar components into
boundedness of the requested column-valued map
`L^p -> (L^p)^{2d}`.  The adjoint scalar transforms and the identity
`(-DD_h)^{1/2} = - sum_j R_j D_{h,j}` also give the reverse comparison, so the
order-one quantum Bessel and Sobolev seminorms are equivalent for fixed
dimension, with constants independent of `hbar`.

## Scope

This is not a new original proof.  It is an agent-identified implication from
the quantum Euclidean singular-integral literature.  The supporting authors do
not appear to explicitly cite arXiv:2210.03013 or phrase their theorem as an
answer to Lafleche's Riesz-transform conjecture.

The result answers the source conjecture as stated with constants allowed to
depend on the fixed phase dimension `2d` and on `p`.  It does not claim the
dimension-free noncommutative square-function estimates of Junge-Mei-Parcet,
and it does not optimize constants.

## Files

- `main.tex`: compact status note and proof of the implication.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: local copy of arXiv:2210.03013.
- `supporting_paper_1705.01081.pdf`: local copy of the decisive supporting
  quantum Euclidean singular-integral paper.
- `supporting_paper_1407.2475.pdf`: local copy of the noncommutative Riesz
  transform paper used only as surrounding context.

## Search Evidence

Cheap run indexes were searched for `2210.03013`, the paper title, quantum
Sobolev/Riesz-transform phrases, and nearby Junge/Parcet/Gonzalez-Perez
keywords.  No exact prior packet was found.  Web searches on 2026-07-18 checked
arXiv/EMS pages for arXiv:2210.03013, arXiv:1705.01081, arXiv:1407.2475, and
close phrases such as "quantum Euclidean spaces Riesz transforms" and "twisted
group von Neumann Riesz transforms".

Human review should confirm the routine but nontrivial identification between
the source's Weyl/Schatten normalization and the `R_Theta` trace normalization;
the `hbar`-independence is robust under the standard rescaling.

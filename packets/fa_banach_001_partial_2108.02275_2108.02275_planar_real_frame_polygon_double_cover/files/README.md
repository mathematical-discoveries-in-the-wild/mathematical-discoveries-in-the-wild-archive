# Planar real frame spaces as polygon double covers

Status: `partial_result_likely_valid`.

Source paper: Tom Needham and Clayton Shonkwiler, *Admissibility and Frame Homotopy for Quaternionic Frames*, arXiv:2108.02275.

## Source problem

The quaternionic admissibility and homotopy questions in the source are answered in the same paper. The residual target is the real case mentioned in the introduction and discussion:

- introduction: for real frames with nonconstant frame spectrum or vector norms, the analogue of the complex/quaternionic connectedness theorem remains open;
- discussion: some real frame spaces \(\mathcal F^{\mathbb R^d,N}_{\lambda}(r)\) are connected and others are not, and it is challenging to characterize which \(\lambda,r\) give which outcome.

## Result

For \(d=2\), the real frame space with fixed vector norms and frame spectrum is exactly a coordinatewise double cover of a labelled planar polygon level.

Let \(r_i>0\), \(\lambda_1\geq\lambda_2>0\), assume \(\sum_i r_i=\lambda_1+\lambda_2\), and put \(\delta=\lambda_1-\lambda_2\). Then
\[
\mathcal F^{\mathbb R^2,N}_{\lambda}(r)
\cong
\left\{\theta\in\mathbb T^N:
\left|\sum_{i=1}^N r_i e^{2i\theta_i}\right|=\delta
\right\}.
\]
Equivalently, if
\[
L(r,\delta)=
\left\{\phi\in\mathbb T^N:
\left|\sum_{i=1}^N r_i e^{i\phi_i}\right|=\delta
\right\},
\]
then the frame space is \(D^{-1}L(r,\delta)\), where \(D(\theta_1,\dots,\theta_N)=(2\theta_1,\dots,2\theta_N)\). For each path component \(C\) of \(L(r,\delta)\), the number of frame-space components lying over \(C\) is the index in \((\mathbb Z/2)^N\) of the mod-2 winding image of \(H_1(C;\mathbb Z/2)\) in \(H_1(\mathbb T^N;\mathbb Z/2)\).

When \(\delta>0\), \(L(r,\delta)\) is \(S^1\) times the usual labelled planar polygon space with side lengths \(r_1,\dots,r_N,\delta\) and the \(\delta\)-side fixed. When \(\delta=0\), it is the closed \(N\)-gon phasor level. Thus the \(d=2\) part of the real-frame connectedness problem reduces exactly to planar polygon components plus a finite \((\mathbb Z/2)^N\)-monodromy calculation.

## Scope

This does not solve the source's full real-frame characterization problem in dimensions \(d\geq3\). It also does not simplify all planar polygon-space cases into inequalities; rather, it gives an exact and reusable planar reduction. The theorem is intended as a sharp reduction/characterization for \(d=2\), not as a claim that every admissible planar real frame space is connected.

## Verification and novelty check

Cheap run indexes were searched for `2108.02275`, `frame homotopy`, `quaternionic frames`, `real frame spaces`, `fixed spectrum`, `polygon`, and related terms. No exact duplicate packet was found.

Web searches on 2026-07-03 for exact and close phrases found the source paper, Cahill--Mixon--Strawn's finite unit norm tight frame connectivity paper, and Needham--Shonkwiler's complex symplectic-frame paper, but no later full characterization of the source's nonconstant real-frame connectedness problem and no exact arbitrary-\((\lambda,r)\) planar double-cover statement.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2108.02275.
- `figures/open_problem_intro_page.png`: page image containing the introduction's real nonconstant-frame open-problem sentence.
- `figures/open_problem_discussion_page.png`: page image containing the discussion's real-frame characterization passage.

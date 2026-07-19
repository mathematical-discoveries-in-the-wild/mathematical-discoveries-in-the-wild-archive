# Real Parseval connectedness from Caine--Needham--Shonkwiler

Status: `literature_implied_answer (partial subcase)`.

Source/open-problem paper: Tom Needham and Clayton Shonkwiler, *Admissibility and Frame Homotopy for Quaternionic Frames*, arXiv:2108.02275, Linear Algebra and its Applications 645 (2022), 237--255.

Supporting paper: Anthony Caine, Tom Needham, and Clayton Shonkwiler, *Optimization and the Topology of Spaces of Parseval Frames*, arXiv:2505.14860, submitted 20 May 2025.

## Source Question

The source paper answers the quaternionic admissibility and connectedness questions, and notes that for real frames with nonconstant frame spectrum or vector norms the analogous path-connectedness question remains open. Its discussion asks, in effect, to characterize the real frame spaces
\[
\mathcal F^{\mathbb R^d,N}_{\lambda}(r)
\]
that are connected, noting that some are connected and others are not.

## Identification

The supporting paper gives a broad partial answer for the Parseval fixed-operator subcase \(S=I_d\), written there as
\[
\operatorname{PF}^{\mathbb R}_d(r)=\{F\in \mathbb R^{d\times n}: FF^*=I_d,\ \|f_i\|^2=r_i\}.
\]
For rational admissible \(r\), Theorem 4.5 gives explicit sufficient conditions, in terms of the constants \(k_\ell(r)\) and \(c\), under which \(\operatorname{PF}^{\mathbb R}_d(r)\) is \(q\)-connected. Corollary 4.9 specializes this to path-connectedness: if
\[
k_\ell(r)\ge c\,{n\ell\over d}\quad (1\le \ell\le d-1),
\qquad
c\ge {d\over n}{2d\over d-1},
\]
then all sufficiently small rational admissible perturbations \(s\) of \(r\) have \(\operatorname{PF}^{\mathbb R}_d(s)\) path-connected. In particular, this gives an open rational neighborhood of the equal-norm vector whenever \(n\ge 2d^2/(d-1)\).

## Scope

This is not a full solution to the 2108.02275 real-frame characterization problem. It treats only Parseval frame operator \(S=I_d\), assumes rational prescribed squared norms, and gives sufficient connectedness conditions rather than a necessary-and-sufficient characterization. The supporting paper explicitly says that a complete characterization of \(r\) for which \(\operatorname{PF}^{\mathbb R}_d(r)\) is path-connected remains open.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2108.02275 source/open-problem paper.
- `supporting_paper_2505.14860.pdf`: arXiv:2505.14860 supporting paper.

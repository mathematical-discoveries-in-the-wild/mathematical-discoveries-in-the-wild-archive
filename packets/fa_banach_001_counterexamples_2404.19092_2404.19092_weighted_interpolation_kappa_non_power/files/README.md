# Counterexample: a homogeneous Hilbertian operator space whose kappa sequence is not a power

Status: candidate counterexample, likely valid.

Source paper: Bruno M. Braga and Javier A. Chavez-Dominguez, "On the small scale nonlinear theory of operator spaces", arXiv:2404.19092.

Target question: Remark 4.7 asks whether, for every homogeneous Hilbertian operator space \(X\), the sequence \(\kappa_n(X)\) is equivalent to a power of \(n\).

Claim: No. There is an infinite-dimensional homogeneous Hilbertian operator space \(X\) such that
\[
\kappa_n(X)=\max\left\{1,\sup_{k\ge 2}2^{-k} n^{(1-1/k)/2}\right\}.
\]
This sequence is below \(\sqrt n\) by a subpower factor, but dominates \(n^c\) for every \(c<1/2\). Hence it is not equivalent to \(n^c\) for any constant \(c\).

Construction: On the common Hilbert space \(\ell_2\), take the diagonal weighted intersection of \(R\) and the interpolation spaces \((R,C)_{1-1/k}\), \(k\ge 2\):
\[
\|[x_{ij}]\|_{M_m(X)}
=\max\left\{\|[x_{ij}]\|_{M_m(R)},
\sup_{k\ge 2}2^{-k}\|[x_{ij}]\|_{M_m((R,C)_{1-1/k})}\right\}.
\]
This is a concrete operator space via the diagonal embedding into an \(\ell_\infty\)-sum. Its scalar norm is the Hilbert norm and homogeneity follows from the homogeneity of \(R\) and \((R,C)_\theta\).

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of Remark 4.7.
- `code/growth_verifier.py`: numerical sanity check for the envelope.
- `code/crop_open_problem.py`: reproduces the crop from the rendered source page.

Novelty check: local run indexes had no prior entry for arXiv:2404.19092 or this kappa/power question. A bounded web search for the exact kappa question and close phrases found the source paper but no later answer.

Human review recommendation: Check the weighted-intersection construction and the equality for \(\kappa_n(X)\). The proof is short, and these are the only substantive points.

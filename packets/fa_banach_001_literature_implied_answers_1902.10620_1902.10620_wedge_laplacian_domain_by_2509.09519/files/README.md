# Literature-Implied Answer: wedge Dirichlet Laplacian domain

Status: `literature_implied_answer_partial_scope`

Source paper: Emiel Lorist and Mark Veraar, "Singular stochastic integral operators", arXiv:1902.10620.

Supporting paper: Petru A. Cioica-Licht, Emiel Lorist, and P. Tobias Werner, "$H^\infty$-calculus for the Dirichlet Laplacian on conical domains", arXiv:2509.09519v2.

Target signal: in the appendix of the source paper, after Proposition A.2 on heat kernel estimates on a wedge, the authors note that the Dirichlet Laplacian is sectorial for
\[
  -\pi/\kappa < \theta/q < 2+\pi/\kappa,
\]
but that they do not know its domain on the full range. They quote a domain formula from Pruss--Simonett for
\[
  2-\pi/\kappa < \theta/q < 2+\pi/\kappa
\]
and say the other values of theta are harder.

Identification: Theorem A / Theorem 4.1 of arXiv:2509.09519 gives a domain and bounded \(H^\infty\)-calculus theorem for the Dirichlet Laplacian on conical domains with mixed weights. Specializing to a two-dimensional wedge, setting \(p=q\), \(\gamma=0\), and \(\nu=\theta-2\), recovers the source paper's single tip-weight space \(L^q(D,|x|^{\theta-2})\). This identifies the domain throughout the sectorial range except for the explicit resonant values \(\theta/q=2\pm n\pi/\kappa\).

Scope:
- The \(C_p\)-independence signal in the same source paper is a same-paper false positive: the paper says it was open and then settles it immediately below.
- The wedge-domain signal is answered only after a later literature identification, so it is recorded as `literature_implied_answer_partial_scope`.
- Resonant values excluded in arXiv:2509.09519 are not claimed solved here.

Files:
- `main.tex` / `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: original arXiv:1902.10620 paper.
- `supporting_paper_2509.09519.pdf`: supporting arXiv:2509.09519v2 paper.


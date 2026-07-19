# Counterexample packet: gamma-multipliers need not be gamma-radonifying

status: candidate_counterexample_likely_valid

Source: Jan van Neerven, "$\gamma$-Radonifying operators -- a survey", arXiv:0911.3788.

Target: after Theorem 5.2, the source asks whether the multiplier extension
\(\widetilde M\) actually takes values in \(\gamma(L^2(A;H),E)\) rather than
only in \(\gamma_\infty(L^2(A;H),E)\), already for \(A=(0,1)\) and
\(H=\mathbb R\). In the theorem's two-space notation, this is the evident
question with the output space as codomain.

Result: negative. Even with the same input and output Banach space
\(E=F=c_0\), there is a strongly measurable multiplier
\[
  M(t)x = x_1 \big(r_n(t)/\sqrt{\log(n+1)}\big)_{n\ge 1}
\]
whose range is \(\gamma\)-bounded, and a constant finite-rank simple
\(\phi:(0,1)\to\gamma(\mathbb R,c_0)\), such that \(T_{M\phi}\) is
\(\gamma\)-summing but not \(\gamma\)-radonifying.

Files:
- `main.tex`: full counterexample note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of the open-problem paragraph from PDF page 24.
- `code/crop_open_problem.py`: script used to regenerate the crop.

Novelty check: checked the run lightweight indexes for arXiv id and core
terms; inspected the source theorem and the preceding Linde--Pietsch diagonal
example; searched web phrases for the exact open-problem sentence and for
gamma-multiplier/gamma-infinity/c0 variants. I found the classical diagonal
\(\gamma_\infty\setminus\gamma\) example in the source itself, but no source
realizing it as a \(\gamma\)-bounded multiplier counterexample. Novelty
confidence is moderate pending expert review.

Human review recommendation: focus on the gamma-boundedness estimate for the
rank-one family \(M(t)=g(t)\otimes e_1^*\), and on the final restriction from
\(L^2(0,1)\) to the closed span of the Rademacher functions. If those two
steps check out, the example gives a negative answer to the stated open
problem.

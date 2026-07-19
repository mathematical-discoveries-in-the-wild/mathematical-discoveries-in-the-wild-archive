# 1511.09055 -- nilpotent pure parts in the Fong-Tsui problem

Status: `partial_result_likely_valid`

Source paper: Mostafa Mbekhta and Laurian Suciu, "Partial isometries and
the conjecture of C. K. Fong and S. K. Tsui", arXiv:1511.09055.

Packet path:
`runs/fa_banach_001/solutions/partial/1511.09055_nilpotent_pure_part_numerical_radius`

## Result

The packet proves that a bounded nilpotent Hilbert-space operator \(N\) of
finite nilpotency order cannot satisfy
\[
  |N| \leq |\operatorname{Re} N|
\]
unless \(N=0\). The proof uses the Haagerup--de la Harpe numerical-radius
bound for nilpotents:
\[
  w(N) \leq \|N\|\cos\frac{\pi}{m+1}, \qquad N^m=0.
\]
The Fong-Tsui inequality gives the reverse lower chain
\[
  \|N\| \leq \|\operatorname{Re}N\| \leq w(N),
\]
which is impossible for nonzero \(N\) because \(\cos(\pi/(m+1))<1\).

## Consequences for the source paper

On page 11, after Corollary 3.4, the source paper asks whether the hypothesis
\(Q^2=0\) in Proposition 3.3 can be weakened to \(Q^m=0\) for some
\(m\geq 3\), with the aim of proving \(Q=0\) under condition (1.1). The packet
gives a positive finite-nilpotent answer: the \(Q^2=0\) alternative in
Proposition 3.3 may be replaced by \(Q^m=0\) for any finite \(m\geq 2\).

Combining this with Corollary 3.5 of the source paper gives the stronger
corollary that every contractive finite \(m\)-quasi-isometry satisfying
\(|T|\leq |\operatorname{Re}T|\) is self-adjoint.

## Scope

This is not a proof of the full Fong-Tsui conjecture and does not settle the
general pure-contraction case. It eliminates the finite nilpotent obstruction
that appears in the source paper's \(m\)-quasi-isometry analysis.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet for review.
- `source_paper.pdf`: local copy of arXiv:1511.09055.
- `figures/open_problem_crop.png`: crop of the page-11 open-problem passage.

## Human review focus

Check the application of the Haagerup--de la Harpe bound to arbitrary bounded
Hilbert-space nilpotents after normalization, and check the blockwise
inheritance of \(|T|\leq |\operatorname{Re}T|\) from \(T=S\oplus Q\) to \(Q\).

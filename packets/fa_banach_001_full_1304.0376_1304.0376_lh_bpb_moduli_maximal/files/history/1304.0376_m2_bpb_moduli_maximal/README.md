# The BPB Moduli of \(M_2(\mathbb C)\) Are Maximal

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Mario Chica, Vladimir Kadets, Miguel Martin, Soledad Moreno-Pulido,
  Fernando Rambla-Barreno, "Bishop-Phelps-Bollobas moduli of a Banach
  space", arXiv:1304.0376.
- Local source PDF: `source_paper.pdf`
- Source discussion crop: `figures/source_discussion_crop.png`

## Claimed Contribution

The source paper asks whether \(L(H)\), for finite- or infinite-dimensional
Hilbert space \(H\), has the maximum Bishop-Phelps-Bollobas moduli. Its
centralizer and M-ideal criteria do not apply because \(L(H)\) has trivial
center.

This packet proves the first noncentral Hilbert-operator case:

> For \(X=M_2(\mathbb C)=L(\mathbb C^2)\),
> \[
> \Phi_X(\delta)=\Phi_X^S(\delta)=\sqrt{2\delta}
> \qquad (0<\delta\leq 1/2).
> \]

The proof constructs, for \(\varepsilon=\sqrt{2\gamma}\),
\[
x=\operatorname{diag}(1-\varepsilon,1),
\qquad
\rho=\operatorname{diag}(\varepsilon/2,1-\varepsilon/2),
\]
and shows that every norm-attaining pair \((y,T)\) is at
\(d_\infty\)-distance at least \(\varepsilon\) from \((x,\rho)\).

The key two-dimensional mechanism is:

- if \(y\) is within \(\varepsilon\) of \(x\), then \(y\) cannot be unitary;
- a nonunitary \(2\times2\) contraction of norm one has a one-dimensional
  top singular subspace, so every trace-norm-one functional norming it is
  rank one;
- \(\rho\) has trace-norm distance at least \(\varepsilon\) from every
  rank-one trace-norm-one matrix.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local rendered copy of the arXiv source.
- `figures/source_discussion_crop.png`: crop of the source discussion of
  \(L(H)\).
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The result is intentionally narrow. It answers the \(L(H)\) question only for
\(\dim H=2\). It does not prove the finite-dimensional \(M_n(\mathbb C)\)
case for \(n\geq3\), nor the infinite-dimensional \(B(H)\) case.

The main review point is the equality case in trace duality: for a
nonunitary \(2\times2\) contraction \(y\) with \(\|y\|=1\), every
trace-norm-one \(T\) satisfying \(\operatorname{Tr}(Ty)=1\) must be rank one.
The packet gives an explicit singular-value proof after reducing \(y\) to
\(\operatorname{diag}(1,s)\), \(0\leq s<1\).

The broader noncentral-projection route remains plausible, but it needs a
new higher-dimensional control of norming trace-class functionals. This
packet should be read as a verified base case and a guide to the obstruction,
not as a solution of the full \(L(H)\) problem.

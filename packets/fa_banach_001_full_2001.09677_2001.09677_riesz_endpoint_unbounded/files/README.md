# Endpoint Riesz Potential Is Unbounded

Status: full solution candidate, likely valid.

Source: Francisco L. Hernandez, Evgeny M. Semenov, and Pedro Tradacete,
*Strictly singular non-compact operators between \(L_p\) spaces*,
arXiv:2001.09677.

## Solved Question

Remark 11 asks whether the endpoint Riesz potential from Theorem 10 is bounded,
and, if it is bounded, whether it is strictly singular. The printed remark uses
an undeclared symbol \(s\) in the first exponent; the surrounding theorem and
the following sentence identify the coherent endpoint as
\[
  p=q=\frac{1-\alpha}{1-\lambda},
\]
in the Banach-relevant case \(0<\alpha<\lambda<1\).

## Result

For \(0<\alpha<\lambda<1\), the operator
\[
  T_\lambda f(t)=\int_0^1 \frac{f(u)}{|t-u|^\lambda}\,du,
  \qquad t\in\Omega_\alpha,
\]
where \(\Omega_\alpha\subset(0,1)\) is closed Ahlfors \(\alpha\)-regular and
is equipped with \(\mathcal H^\alpha\), is not bounded
\[
  L_p(0,1)\to L_p(\Omega_\alpha,\mathcal H^\alpha),
  \qquad p=\frac{1-\alpha}{1-\lambda}.
\]
Thus the endpoint is outside the \(L\)-characteristic set, and the strict
singularity follow-up is vacuous.

## Proof Mechanism

The adjoint endpoint potential of a characteristic function of a small Ahlfors
piece has exactly critical weak-\(L^{p'}\) decay near the fractal set. Since
\[
  p'=\frac{1-\alpha}{\lambda-\alpha},
\]
that weak critical decay gives a logarithmic divergence in strong
\(L^{p'}(0,1)\). Hence the adjoint is not bounded, so neither is \(T_\lambda\).

## Files

- `main.tex` contains the self-contained proof.
- `solution_packet.pdf` is the compiled proof packet.
- `source_paper.pdf` is the source paper.
- `figures/open_problem_crop.png` shows the source remark.

## Novelty Check

I checked the local run indexes for `2001.09677`, title keywords, and
strictly-singular/Riesz-potential characteristic-set terms. No exact prior
packet was found. Web searches for the exact endpoint wording, the source
paper, and Adams/Riesz trace inequality phrases found broad trace-inequality
literature but no direct answer to Remark 11 of the source paper.


# Strictly Positive Functional Subcase for the Kothe Tensor `L0` Question

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Qingying Bu, Gerard Buskes, Alexey I. Popov, Adi Tcaciuc, and
  Vladimir G. Troitsky, "The 2-concavification of a Banach lattice equals
  the diagonal of the Fremlin tensor square", arXiv:1109.5380.
- Local source PDF: `source_paper.pdf`
- Local source TeX: `source_tex/source_1109.5380.tex`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Section 4 of the source paper says that, for a Kothe space `E` on
`Omega`, the algebraic tensor product `E tensor E` embeds in
`L0(Omega^2)` by `(x tensor y)(s,t)=x(s)y(t)`, and the authors do not
know whether the completed Fremlin tensor product
`E tensor_|pi| E` can still be viewed as a sublattice of `L0(Omega^2)`.

This packet proves an affirmative subcase. If there is a strictly
positive continuous Kothe-dual functional, equivalently a function
`h>0` a.e. such that

`int |x| h dmu <= C ||x||_E`

for all `x in E`, then the canonical elementary-tensor representation
extends to an injective lattice homomorphism

`E tensor_|pi| E -> L0(Omega^2)`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `source_tex/source_1109.5380.tex`: local source TeX used to locate the
  source signal.
- `figures/open_problem_crop.png`: crop from page 13 of the source PDF.
- `tmp/`: LaTeX build intermediates.

## Human Review Notes

The key review points are:

- the use of the Fremlin universal property for the positive lattice
  bimorphism into `L1(h(s)h(t) dmu(s)dmu(t))`;
- the Fremlin positive-cone domination fact: every nonzero positive
  tensor element dominates a nonzero positive elementary tensor;
- the strict positivity of `h`, which makes every nonzero positive
  elementary tensor nonzero in the weighted product `L1`, hence proves
  injectivity.

The packet does not prove that every Kothe space in the minimal source
definition has such an `h`. Thus it is a substantial positive subcase,
not a complete resolution of the unrestricted source question.

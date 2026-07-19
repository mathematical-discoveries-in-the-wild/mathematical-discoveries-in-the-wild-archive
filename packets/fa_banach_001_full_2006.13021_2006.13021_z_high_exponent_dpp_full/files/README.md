# Full scoped packet: high-exponent DPP for `A_2^r(Z)`

Status: likely valid scoped full solution.

Source paper: Edmond E. Granirer, "Geometric Properties of some Banach Algebras
related to the Fourier algebra on Locally Compact Groups", arXiv:2006.13021.

Targeted source question: in the section on the Schur and Dunford-Pettis
properties, the source asks whether `A_p^r(G)` has the Dunford-Pettis property
when `r > max(p,p')`, even for `G=Z` and `p=2`.

Result: for `G=Z` and `p=2`, the answer is completely determined. For every
finite `1<r<infinity`, and in particular for every finite `r>2`,
`A_2^r(Z)` fails the Dunford-Pettis property. For `r=infinity`,
`A_2^infinity(Z)=A_2(Z)` is isometric to `L^1(T)`, hence has the
Dunford-Pettis property.

Proof idea: identify `A_2^r(Z)` with the graph space
`{f in L^1(T): Fourier(f) in ell^r}` inside `L^1(T) \oplus ell^r`.
The Fourier monomials `z^n` give weakly null vectors, the `n`th coordinate
functionals give weakly null dual vectors, and the pairings are always `1`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered source paper.
- `figures/dpp_question_crop.png`: crop of the source question.

Scope: this settles the discrete `G=Z`, `p=2` DPP subquestion. It does not
settle the RNP question for finite `r>2`, the `G=R` case, or the semisimple Lie
group DPP conjecture.

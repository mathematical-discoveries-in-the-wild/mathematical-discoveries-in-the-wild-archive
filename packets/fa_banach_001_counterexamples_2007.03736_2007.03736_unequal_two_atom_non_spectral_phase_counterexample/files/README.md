# Unequal two-atom counterexample for nonlinear-phase exponential bases

Status: `counterexample_likely_valid`

Source: Jean-Pierre Gabardo, Chun-Kit Lai, and Vignon Oussa,
"On exponential bases and frames with non-linear phase functions and some
applications", arXiv:2007.03736.

The packet answers the first open problem in Section 8 negatively. The source
asks whether every finite Borel measure `mu` can admit an orthogonal basis of
the form `E(Lambda, phi)` for some Borel measurable phase `phi`, and asks for a
measure admitting no orthogonal basis of nonlinear phase.

Counterexample: take the probability measure
`mu = (1/3) delta_0 + (2/3) delta_1` on `R`. For any Borel phase `phi` and any
two frequencies, the corresponding exponentials are vectors whose two
coordinates have modulus one. Their weighted inner product can vanish only if
the two atom weights are equal. Since `1/3 != 2/3`, no two distinct generalized
exponentials are orthogonal, while `L^2(mu)` is two-dimensional. Hence no
`E(Lambda, phi)` can be an orthogonal basis.

Files:

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: locally compiled source paper.
- `figures/open_problem_crop.png`: rendered source page containing the open problem.

Human review focus: confirm that the source's phrase "any finite Borel measure"
does not implicitly exclude finite atomic measures or require nonatomic
measures. Under the literal statement, the counterexample is immediate and
complete.

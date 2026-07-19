# Unconditional Support Ideals Are Non-Pathological

Status: partial result, likely valid.

Source paper: Adam Kwela and Jaroslaw Swaczyna, *Zoo of ideal Schauder bases*,
arXiv:2508.21235.

Open question: Question 11.2 asks whether every analytic P-ideal `I` can be
represented as a critical ideal `CR(X,a)` for some Banach space `X` and
sequence `a`. The paper proves this for non-pathological analytic P-ideals in
Theorem 7.1.

Partial result: the positive weighted-series route used by Theorem 7.1 cannot
reach pathological analytic P-ideals. More generally, if `X` has a
1-unconditional Schauder basis `(u_n)` and `c_n > 0`, then the support ideal

`{A subset omega : sum_{n in A} c_n u_n converges in X}`

is always `Exh(phi)` for a non-pathological lower semicontinuous submeasure
`phi`.

Why this matters: Theorem 7.1 realizes every non-pathological analytic P-ideal
by exactly this kind of weighted positive-support construction. The new
obstruction shows that extending the construction by merely changing the
unconditional Banach sequence norm cannot solve Question 11.2 for pathological
analytic P-ideals.

Packet contents:

- `source_paper.pdf`: arXiv:2508.21235.
- `figures/open_problem_crop.png`: crop of Question 11.2 on page 23.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `tmp/`: LaTeX build outputs.

Human review focus:

- Check the positive norming functional step for 1-unconditional bases.
- Check that convergence of the positive subseries is exactly
  `lim_m phi(A\\m)=0`.
- Confirm the scope is not overstated: the full Question 11.2 remains open
  outside this unconditional positive-series route.

# Boundary-cap dissipativity does not exclude support points

Status: `candidate_counterexample_likely_valid`.

This packet gives a counterexample to Question 3.10 of Filippo Bracci and
Oliver Roth, *Support points and the Bieberbach conjecture in higher
dimension*, arXiv:1603.01532 (PDF page 6).

The question asks whether strict Herglotz-field dissipativity near some subset
of the boundary of the unit ball forces the initial member of a normal Loewner
chain to lie outside `Supp(S^0) union Ex(S^0)`.

Set

\[
c=\frac{3\sqrt3}{2},\qquad
\Phi(z_1,z_2)=(z_1+c z_2^2,z_2),\qquad
f_t=e^t\Phi.
\]

The autonomous generator is

\[
G(z_1,z_2)=(-z_1+c z_2^2,-z_2).
\]

The map `Phi` is a support point of `S^0`, detected by the sharp coefficient
functional `b^1_{0,2}`. Nevertheless, on the positive-measure cap

\[
A=\{\zeta\in\partial\mathbb B^2:|\zeta_2|\le 1/4\}
\]

the dissipativity expression has limsup at most
`-1+3 sqrt(3)/32 < -3/4`. Thus the printed hypothesis holds with
`a=3/4`, while its proposed conclusion fails.

## Files

- `solution_packet.pdf`: human-readable proof and source evidence.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of Question 3.10.
- `figures/boundary_dissipativity.png`: verifier-generated cap plot.
- `code/verify_counterexample.py`: deterministic algebraic/numerical checks.
- `verification.md`: analytic and computational audit.

## Scope limitation

The counterexample addresses Question 3.10 exactly as printed, where the
condition is imposed near "some" boundary subset. It does not address a
stronger version requiring the whole boundary or an additional quantitative
largeness condition.


# Finite-slice reduction for JNP witnesses in `C_p(X,E)`

Status: `partial_result_likely_valid`

Source: Christian Bargetz, Jerzy Kakol, and Damian Sobota, *On complemented
copies of the space c_0 in spaces C_p(X,E)*, arXiv:2107.03211v3, Problem 4.8,
page 7.

## Result

Let `H=C_p(X,E)`, and write a weak-star null sequence in `H'` in its grouped
form

`Phi_n(g) = sum_{x in A_n} eta_{n,x}(g(x))`,

where `A_n` is finite and `eta_{n,x}` belongs to `E'`. If this sequence
witnesses the Josefson--Nissenzweig property of `H`, then:

- if the union of the sets `A_n` is finite, `E` has the JNP;
- if all coefficient functionals `eta_{n,x}` lie in one fixed
  finite-dimensional subspace of `E'`, `C_p(X)` has the JNP.

Thus, if Problem 4.8 has a negative answer, every counterexample witness must
escape simultaneously through infinitely many evaluation points of `X` and
through an infinite-dimensional family of coefficient functionals in `E'`.
This is an unconditional partial reduction, not a solution of the unrestricted
problem.

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2107.03211v3.
- `figures/open_problem_crop.png`: source Problem 4.8 and surrounding context.
- `verification.md`: proof and novelty checks.

Ledger record:
`runs/fa_banach_001/ledger/results/2107.03211_jnp_finite_slice_reduction.json`.


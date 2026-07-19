# Bounded Clark Cauchy Transform Need Not Imply One-Component

Result type: `counterexample`

Status: candidate counterexample, likely valid pending human review.

Source paper:

- C. Bellavita, E. Dellepiane, A. Hartmann, and J. Mashreghi,
  "Infinitely supported harmonically weighted Dirichlet spaces which are
  de Branges Rovnyak spaces", arXiv:2509.04907.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks Open Problem 4.4:

> Let `sigma` be the Clark measure associated with `u`. Is it true that if
> `C_sigma` is bounded on `L^2(sigma)`, then `u` is a one-component inner
> function?

This packet gives a negative answer.

Let `zeta_n = exp(i 2^{-n})` and let
`sigma = sum_{n>=1} 2^{-4n} delta_{zeta_n}`. By the standard Clark/Herglotz
correspondence, `sigma` is the Clark measure of an inner function `u`. The
truncated Cauchy transform is represented on `L^2(sigma)` by a matrix whose
unitarily conjugated entries are

`sqrt(sigma_i sigma_j) / (1 - conjugate(zeta_i) zeta_j)`.

These entries are square-summable, so the operator is Hilbert-Schmidt and
hence bounded. But Bessonov's characterization of Clark measures of
one-component inner functions, quoted as Theorem 3.8 in the source paper,
requires the mass of every isolated atom to be bounded below by a constant
times the adjacent atom gap. Here

`2^{-4n} / |zeta_n - zeta_{n+1}| -> 0`,

so no such lower bound exists. Therefore the associated inner function is
not one-component.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2509.04907.
- `figures/open_problem_crop.png`: crop of Open Problem 4.4 from page 20.
- `code/check_hilbert_schmidt.py`: finite partial-sum sanity check.
- `code/crop_open_problem.py`: reproduces the crop.

## Literature Check

Cheap indexes were searched for the arXiv id, title keywords, `Clark measure`,
`Cauchy transform`, and `one-component inner function`; no duplicate result
was found. Exact web searches for the open-problem wording and close variants
only surfaced the source paper. This supports treating the packet as a new
direct counterexample to the problem as stated.

## Human Review Notes

The key review points are:

- the Clark/Herglotz inverse step: every finite positive singular measure on
  the circle is a Clark measure of an inner function;
- the Hilbert-Schmidt estimate for the atomic Cauchy matrix;
- the use of Bessonov's lower mass-gap condition to rule out one-component
  inner functions.

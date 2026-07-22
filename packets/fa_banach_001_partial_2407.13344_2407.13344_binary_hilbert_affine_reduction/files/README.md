# Partial result: explicit binary affine reduction for Hilbert spheres

status: `substantial_partial_result_likely_valid`

model: `GPT5.6`

source: Itaï Ben Yaacov, Tomás Ibarlucía, and Todor Tsankov, *Extremal
models and direct integrals in affine logic*, arXiv:2407.13344v2.

target: Question 27.9 asks for an explicit way to approximate continuous
logic formulas by affine formulas modulo the Hilbert-sphere theories `HS_d`.
The introduction specifically says that no affine approximation of
`<x,y>^3` was known.

## Result

The highlighted cubic is explicitly and uniformly approximable. More
generally, every continuous logic formula with at most two free variables is
uniformly approximable by affine formulas modulo each fixed `HS_d`.

For `-1<r<1`, choose

`a_r=(sqrt(1+r)+sqrt(1-r))/2`,

`b_r=(sqrt(1+r)-sqrt(1-r))/2`.

Then the affine formula

`N_r(x,y)=sup_z (a_r<x,z>+b_r<y,z>)`

equals `sqrt(1+r<x,y>)`. Consequently,

`(8/r^3)(N_r-N_{-r}-r<x,y>) -> <x,y>^3`

uniformly, with error `O(r^2)`. Higher finite differences recover every
power `<x,y>^k`; polynomial approximation gives every continuous function of
one inner product. Since binary Hilbert-sphere types are determined by the
inner product, this covers every binary formula, including formulas with
quantifiers.

## Limitation

Question 27.9 for arbitrary tuple arity remains open. For three or more
variables, types are parametrized by a Gram matrix. The present method does
not yet construct nonlinear products of independent Gram coordinates.

## Verification and novelty

- The proof is analytic and dimension-independent for a prescribed function
  of one inner product.
- `code/check_approximants.py` numerically checks the cubic convergence and
  finite-difference formulas on a 2,001-point grid using 80-digit arithmetic.
- Cheap indexes contained no duplicate.
- Bounded exact-question and arXiv-title searches found no later explicit
  syntactic solution.

## Files

- `main.tex` / `solution_packet.pdf`: complete partial theorem and proof.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: source page 121, Question 27.9.
- `code/check_approximants.py`: numerical sanity checker.

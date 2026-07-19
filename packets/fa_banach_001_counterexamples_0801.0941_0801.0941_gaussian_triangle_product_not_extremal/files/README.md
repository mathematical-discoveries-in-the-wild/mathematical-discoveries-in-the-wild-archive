# Counterexample packet: the Gaussian-triangle product is not extremal

Status: `candidate_counterexample_likely_valid (Question 3, second clause; first clause remains open)`

## Source

- Philippe Jaming, Mate Matolcsi, and Szilard Gy. Revesz, *On the
  extremal rays of the cone of positive, positive definite functions*,
  arXiv:0801.0941; Journal of Fourier Analysis and Applications 15 (2009),
  561-582, DOI: 10.1007/s00041-008-9057-6.
- Exact location: Conclusion, Question 3, PDF page 18.
- `source_paper.pdf` is the local source; `figures/open_problem_crop.png`
  shows the complete question and its Borisov-conjecture context.

The source sets

`f = 1_[-1/2,1/2] * 1_[-1/2,1/2]` and `gamma(x) = exp(-pi x^2)`

and asks first whether `f * gamma` is extremal in the cone of continuous
nonnegative positive-definite functions, and then whether
`gamma (f * gamma)` is extremal.

## Result

The second function is **not** extremal. Define

`q(x) = (1 - 2|x|)_+ exp(-2 pi x^2)` and `gamma_2(x) = exp(-2 pi x^2)`.

Completing the square gives the exact identity

`gamma(x) (f * gamma)(x) = 2 (q * gamma_2)(x)`.

For sufficiently small `epsilon > 0`, both

`q_+(x) = q(x)(1 + epsilon x^2)` and
`q_-(x) = q(x)(1 - epsilon x^2)`

are nonnegative positive-definite functions. The key estimate comes from the
three jumps of `q'`: if `Q = Fourier(q)`, then

`Q(xi) = [1 - exp(-pi/2) cos(pi xi)]/(pi^2 xi^2) + o(xi^-2)`.

Thus `Q >= c/(1+xi^2)`. Meanwhile `u=x^2q` has a second distributional
derivative which is a finite measure, so `|Fourier(u)| <= C/(1+xi^2)`.
Small perturbations therefore keep both Fourier transforms nonnegative.
Convolving `q_+` and `q_-` with `gamma_2` gives a nonproportional decomposition
of the source's second function inside the cone.

## Scope

This is a complete negative answer to the second clause of Question 3. It does
not decide whether `f * gamma` is extremal. It also does not refute Borisov's
conjecture; instead, it proves that this proposed function cannot be the hoped
for strictly positive extremal counterexample.

## Files

- `solution_packet.pdf`: full human-review packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source evidence crop.
- `code/numerical_sanity_check.py`: auxiliary finite-grid check, not used as proof.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Human review focus

Check the completion-of-the-square identity, the signs and sizes of the three
derivative jumps of `q`, and the passage from the two-sided Fourier decay
bounds to a single sufficiently small `epsilon`. No numerical claim is needed
for the proof.


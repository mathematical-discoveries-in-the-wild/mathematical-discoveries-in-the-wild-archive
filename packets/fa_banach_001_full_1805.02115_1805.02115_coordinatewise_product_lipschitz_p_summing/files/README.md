# Coordinatewise products on ell_1 are Lipschitz p-summing

Result type: `full`

Status: candidate full solution, likely valid, pending human review.

Source paper: Jorge C. Angulo-López and Maite Fernández-Unzueta,
*Lipschitz p-summing multilinear operators*, arXiv:1805.02115v2,
J. Funct. Anal. 279 (2020), no. 4, 108572.

## Source question

On page 6, immediately after Proposition 3.5, the authors consider

`T: ell_1 x ell_1 -> ell_1,  T(x,y)=(x_j y_j)_j`

and write: “We do not know if `T` is Lipschitz `p`-summing.”

## Candidate contribution

The answer is yes for every `1 <= p < infinity`. In fact, the packet proves
the stronger arity-independent statement that for every `m >= 2`,

`M_m(x^1,...,x^m)=(x^1_j ... x^m_j)_j : ell_1^m -> ell_1`

is Lipschitz `p`-summing. If `kappa_p` denotes a lower scalar Khintchine
constant over the underlying field, then

`1 <= pi_p^Lip(M_m) <= sqrt(2)/kappa_p`.

For a tested pair of decomposable tensors, their difference becomes an array
whose flattening has rank at most two. Diagonal extraction has `ell_1` norm at
most the trace norm of this flattening, hence at most `sqrt(2)` times its
Hilbert-Schmidt norm. Independent sign arrays are norm-one multilinear forms
on `ell_1^m`; the lower Khintchine inequality recovers the Hilbert-Schmidt norm
in expectation. Summing over all tested pairs and taking a supremum over sign
arrays gives exactly the Lipschitz `p`-summing inequality.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop from source page 6.
- `code/finite_rank_sign_check.py`: finite-dimensional stress test.
- `verification.md`: proof audit and computational report.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

The run indexes were searched for arXiv:1805.02115, the exact map, and the
core Lipschitz-summing phrases; no prior packet or attempt was found. A bounded
arXiv web search used the exact source sentence, the paper title, and variants
of “coordinatewise product” and “Lipschitz p-summing.” A local full-source
search examined later arXiv papers citing the 2020 paper, including
arXiv:2010.01350, 2204.01775, 2209.03038, 2308.03491, 2406.03895, 2410.21082,
2411.11372, 2412.10527, and 2501.15863. No answer to the coordinatewise-product
question or this rank-two/random-sign proof was found.

The separate Question 7.1 of the source, asking whether two notions for
Sigma-operators coincide, is not claimed here: arXiv:2204.01775 explicitly
answers that question affirmatively. Novelty confidence for the present result
is moderate pending a specialist bibliographic search.

## Human review focus

Please check the trace-duality diagonal estimate for the infinite array, the
rank-at-most-two flattening, and the passage from the pointwise Khintchine
estimate to one common sign-array supremum for a finite family. These are the
only substantive steps.


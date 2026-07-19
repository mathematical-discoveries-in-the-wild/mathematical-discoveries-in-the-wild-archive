# Non-Atomic `L_p` Spaces Fail the SPAP

Result type: `partial`

Status: candidate partial negative result, likely valid pending human review.

Source paper:

- Luis A. Garcia, Jose Lucas P. Luiz, Vinicius C. C. Miranda, "Norm
  attainment for multilinear operators and polynomials on Banach Spaces
  and Banach lattices", arXiv:2605.12117.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Question 2 asks whether there are Banach lattices with the sequentially
positive approximation property (SPAP) beyond the known class of Banach
lattices with order-continuous norm whose order is given by a basis.

This packet proves a partial negative result: if `(Omega,Sigma,mu)` is a
non-atomic finite measure space and `1 <= p < infinity`, then `L_p(mu)`
does not have the SPAP.

The proof extends the obstruction in the source paper for `L_2([0,1])`.
It constructs dyadic signs `r_k` with `|r_k| = 1` and `r_k -> 0` weakly
in every finite `L_p`. A finite-rank positive approximant `S` sends
`r_k` to zero in norm along a tail, while the modulus inequality

`|S - I|(|r_k|) >= |(S - I)r_k|`

forces `|S-I|(1)` to stay bounded below. This contradicts SPAP
convergence at the single positive vector `1`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of Question 2
  from page 28 of the source paper.
- `code/check_dyadic_obstruction.py`: finite-grid sanity check for the
  conditional-expectation obstruction.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

This is not a full answer to Question 2 because it does not produce new
SPAP examples. It rules out a natural non-atomic `L_p` family of possible
examples.

The proof depends on standard facts: non-atomic finite measure spaces
admit dyadic equal-measure splittings, dyadic sign functions are weakly
null in finite `L_p`, finite-rank operators are compact, and regular
operator moduli satisfy `|T|(|x|) >= |Tx|`.

# Finite-block prefix retraction for the Kim--Lee stability question

Status: partial_result_likely_valid

Source paper: Sun Kwang Kim and Han Ju Lee, "Simultaneously continuous
retraction and Bishop-Phelps-Bollobas type theorem", arXiv:1308.1638.

Source question: after Proposition 2.5, the paper states that the authors do
not know whether the analogous stability result for uniformly simultaneously
continuous retractions holds for `c0` sums or `ell_p` sums, `1<p<infty`.

Partial result: if the summands are finite-dimensional Banach spaces, then the
answer is affirmative for both `c0` sums and `ell_p` sums. Equivalently, for
`X=(oplus F_n)_{c0}` or `X=(oplus F_n)_{ell_p}`, `1<p<infty`, with all `F_n`
finite-dimensional, the dual `X^*` admits a uniformly simultaneously
continuous retraction onto its unit ball.

Main mechanism: on the dual `ell_q` sum of the finite-dimensional blocks,
truncate by the first coordinate block at which the cumulative `q`-mass reaches
one. This avoids the weak-star discontinuity of radial normalization. The
finite-dimensionality of each block makes coordinate norms weak-star
continuous, while tails disappear against the `c0` or `ell_p` predual.

Limitations: this does not settle the arbitrary-summand stability problem. The
argument uses finite-dimensionality exactly to make the coordinate norms
weak-star continuous.

Packet contents:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source passage.
- `code/prefix_truncation_check.py`: small numerical stress check of the
  prefix truncation modulus; it is not used as proof.

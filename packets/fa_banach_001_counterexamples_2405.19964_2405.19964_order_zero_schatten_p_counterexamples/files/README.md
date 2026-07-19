# Order-Zero Super Symbols Can Fail on Every Schatten Class Except S2

Result type: `counterexample`

Status: candidate counterexample, likely valid pending human review.

Source:

- G. Lee and M. Lein, "A proof of L2-boundedness for magnetic
  pseudodifferential super operators via matrix representations with respect
  to Parseval frames", arXiv:2405.19964; Monatshefte fuer Mathematik 206
  (2025), 597-627.
- The open p-Schatten boundedness question is on source page 3; the
  same-hypotheses endpoint discussion is Remark 5.4 on pages 29-30.
- Local source PDF: `source_paper.pdf`.
- Evidence crops: `figures/open_problem_crop.png` and
  `figures/same_hypotheses_remark_crop.png`.

## Claimed contribution

There is one real non-magnetic symbol

`F(x_L, xi_L, x_R, xi_R) = phi(x_L - x_R)`

which belongs to `S^0_{rho,0}(R^4)` and to the double class
`S^{0,0}_{rho,0}(R^4)` for every `0 <= rho <= 1`, such that `Op^0(F)` is
bounded on Hilbert-Schmidt operators but unbounded on `S^p(L^2(R))` for every
`p != 2`, including `p=1` and `p=infinity`.

The construction starts with a single sign sequence `m: Z -> {-1,1}` whose
Fourier multiplier is unbounded on every `L^p(T)`, `p != 2`. Such a sequence
is assembled blockwise from Khintchine-small sign polynomials and the large
Dirichlet kernel, with a diagonal enumeration over rational exponents above
2. A disjoint smooth interpolation gives `phi in C_b^infinity(R)` with
`phi(n)=m(n)`.

For symbols depending only on `x_L,x_R`, non-magnetic super Weyl quantization
multiplies integral kernels by `F(x,y)`. Small disjoint translates of one
smooth vector then compress `Op^0(F)` exactly to the Toeplitz Schur multiplier

`(a_ij) -> (m(i-j) a_ij)`.

Neuwirth-Ricard Fourier-Schur transference converts boundedness on `S^p` into
boundedness of the Fourier multiplier on `L^p(T)`, a contradiction.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `verification_report.md`: adversarial step check.
- `attempt_log.md`: concise route history.
- `source_paper.pdf`: arXiv:2405.19964.
- `supporting_paper_1001.5332.pdf`: Fourier-Schur transference reference.
- `supporting_paper_2603.26455.pdf`: the closest later literature found.
- `figures/open_problem_crop.png`: source page 3 question.
- `figures/same_hypotheses_remark_crop.png`: stitched source Remark 5.4.
- `code/crop_open_problem.py`: reproduces the evidence crops from rendered
  source pages.
- `code/check_block_multiplier.py`: finite numerical sanity check of the block
  norm-growth mechanism.

## Literature check

The four run indexes were searched for arXiv:2405.19964, title terms,
`magnetic pseudodifferential super operator`, `Schatten`, `trace class`, and
`Schur multiplier`; no duplicate was found.

Bounded web searches found the published 2025 source and H. D. Cornean and
M. H. Thorn, "Magnetic Weyl Super Calculus: Schatten-class properties,
commutator criterion, and complete positivity", arXiv:2603.26455 (March
2026). That follow-up proves positive results for stronger integrable-weight
and completed projective tensor-product hypotheses. It does not state the
counterexample here or recover a universal order-zero result for `p != 2`.
No exact or close literature answer matching this construction was found.

## Human review focus

- Confirm that a position-only super symbol acts as the displayed kernel
  multiplier under the Lee-Lein right-action convention.
- Confirm the full Toeplitz-set application of Neuwirth-Ricard Theorem 2.1.
- Check the diagonal sign-block construction of one multiplier bad at every
  exponent, especially the interpolation/duality passage from rational
  exponents above 2 to all `p != 2`.


# Counterexample: finite-rank norm-attaining need not be finitely norm-attaining

Status: candidate counterexample, likely valid.

Source: arXiv:2602.23796, R. J. Aliaga, S. Dantas, J. Guerrero-Viu, M. Jung, and O. Roldan, *Integral representations of projective norm-attaining tensors*.

## Question Answered

Section 2.3 asks whether

```tex
\FNA_\pi(X \widehat\otimes_\pi Y)
=
\NA_\pi(X \widehat\otimes_\pi Y) \cap (X \otimes Y)
```

holds for arbitrary Banach spaces outside the easy cases listed in the source paper.

## Result

The equality is false.  Take `X = ell_1` and `Y = ell_2^2`.  Choose unit vectors `h_n` in pairwise distinct one-dimensional directions in `ell_2^2`, and set

```tex
u = \sum_{n=1}^\infty 2^{-n} e_n \otimes h_n.
```

Under the isometry `ell_1 \widehat\otimes_\pi ell_2^2 = ell_1(ell_2^2)`, this is norm-attaining with optimal coordinate representation and norm `1`.  It is also algebraic, because the second factor is two-dimensional:

```tex
u = (2^{-n} h_n^{(1)})_n \otimes f_1
  + (2^{-n} h_n^{(2)})_n \otimes f_2.
```

It has no finite optimal representation.  Any finite optimal representation would force equality in the coordinatewise triangle inequality at every `ell_1` coordinate.  Strict convexity of `ell_2^2` then forces every coordinate direction to be among finitely many summand lines, contradicting the choice of infinitely many distinct directions.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2602.23796.
- `figures/open_problem_crop.png`: crop of the source definition and question.
- `code/make_open_problem_crop.py`: script used to generate the crop.

## Verification

No numerical computation is needed.  The proof uses only the standard isometry `ell_1 \widehat\otimes_\pi H = ell_1(H)` and equality in the triangle inequality for strictly convex two-dimensional Hilbert space.

Local run indexes on 2026-06-18 showed no existing solution packet for this arXiv id.  Web searches for the exact source title, `FNA_pi`, and "finitely norm-attaining tensors" found the source arXiv page but no later answer to this equality question.

## Review Focus

Check the equality-chain step: finite optimality in `ell_1(H)` makes every coordinate triangle inequality sharp, and sharpness in `ell_2^2` forces a single projective line at each coordinate.

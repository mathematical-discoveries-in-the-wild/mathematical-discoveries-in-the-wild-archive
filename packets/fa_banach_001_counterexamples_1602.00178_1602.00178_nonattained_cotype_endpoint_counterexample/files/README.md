# Counterexample packet: the non-attained-cotype endpoint fails

Status: likely valid counterexample to the endpoint, epsilon-free strengthening of Theorem 2.4.

Source target: Aron, Nunez-Alarcon, Pellegrino, and Serrano-Rodriguez, "Optimal exponents for Hardy--Littlewood inequalities for m-linear operators", arXiv:1602.00178v4.

The source proves a sharp vector-valued Hardy--Littlewood theorem when the range space `Y` attains its cotype, and then gives only an `epsilon`-shifted version when one does not know whether `Y` attains the infimum of its cotypes. This packet shows that the epsilon loss is genuinely necessary in general: for an explicit infinite-dimensional Banach space `Y` with finite cotype, `cot Y = 2`, but no cotype `2`, the endpoint inequality fails already for linear maps `A: ell_4 -> Y`.

Main construction:

- Let `r_n = 2 + 1/n` and `N_n = n^(4n+2)`.
- Let `Y = (direct sum_n ell_{r_n}^{N_n})_2`.
- Then `Y` has cotype `s` for every `s>2`, but not cotype `2`; hence `cot Y=2` is not attained.
- Split `ell_4` into consecutive blocks of lengths `N_n`. On block `n`, set
  `A_n = n^{-1} N_n^{-(1/r_n-1/4)} I: ell_4^{N_n} -> ell_{r_n}^{N_n}`.
- The resulting block diagonal operator `A: ell_4 -> Y` is bounded.
- However
  `sum_j ||A e_j||_Y^4 = sum_n n^{-4} N_n^{1-4(1/r_n-1/4)} = sum_n 1 = infinity`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source arXiv PDF.
- `figures/main_theorem_crop.png`: crop of the source theorem requiring attained cotype.
- `figures/nonattained_cotype_crop.png`: crop of the source epsilon theorem for the non-attained case.
- `code/nonattained_cotype_endpoint_check.py`: arithmetic checks for the construction.
- `code/crop_source_passages.py`: reproducible crop script.

Novelty check:

- Local lightweight indexes were searched for `1602.00178`, Hardy--Littlewood, optimal exponents, multilinear forms, cotype, and non-attained cotype. No exact prior packet was found.
- Bounded web searches on 2026-06-28 for the source arXiv id, Hardy--Littlewood cotype endpoint, and non-attained-cotype epsilon language found no separate known answer beyond the source arXiv record.

Human-review recommendation: check the standard cotype facts used for the `ell_2`-sum of finite-dimensional `ell_r` blocks. The operator counterexample itself is an explicit block calculation.

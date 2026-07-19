# Weak vector-valued Hardy spaces are strong only in finite dimension

Status: `full_solution_likely_valid`

Source paper: F. J. Bertoloto, *Duality of certain Banach spaces of
vector-valued holomorphic functions*, arXiv:1203.5322.

## Result

Conjecture 5.11 asks whether
`H^p(D;F) = H^p(D;F)_w` holds exactly for finite-dimensional Banach
spaces `F`. The source has already observed that finite-dimensional `F`
works and that `p = infinity` is exceptional, since
`H^\infty(D;F)_w = H^\infty(D;F)` for every `F`.

This packet proves the conjecture for every finite `p`, `1 <= p < infinity`:
if `F` is infinite-dimensional, then there is an `F`-valued holomorphic
function whose scalar evaluations all lie in scalar `H^p`, but which is not in
Bochner `H^p(D;F)`.

## Proof Mechanism

Use the Dvoretzky-Rogers theorem to choose a weakly `ell^p` sequence
`(x_n)` in `F` whose norm sequence is not in `ell^p`. Then place these values
on an interpolating sequence for scalar Hardy space. Scalar interpolation
shows every `phi o f` belongs to `H^p`, while vector-valued Carleson evaluation
would force `(x_n)` to be norm `ell^p` if `f` were in strong `H^p(D;F)`.

## Verification

- Source PDF and a crop of Conjecture 5.11 are included.
- `solution_packet.pdf` renders from `main.tex`.
- Literature search on 2026-07-03 for the exact conjecture wording and close
  variants found the arXiv source, but no later explicit answer.

Human review should check the stated Hardy interpolation standard fact,
especially the local summability of the interpolation functions used to form
the vector-valued holomorphic series.

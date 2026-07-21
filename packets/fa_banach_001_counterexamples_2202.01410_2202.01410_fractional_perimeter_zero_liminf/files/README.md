# 2202.01410 fractional-perimeter zero-liminf counterexamples

Status: `counterexample_likely_valid`

Source: Haïm Brezis, Andreas Seeger, Jean Van Schaftingen, and Po-Lam Yung, *Sobolev spaces revisited*, arXiv:2202.01410.

## Result

For every dimension `n >= 1` and every `-1 < gamma < 0`, both negative-`gamma` BV liminf questions on page 20 of the source have negative answers.

- There is a compactly supported characteristic function `u` outside homogeneous `BV` for which
  `lambda nu_gamma(E_{lambda,1+gamma}[u]) -> 0` as `lambda -> 0+`.
- There is a nonconstant compactly supported characteristic function `v` in homogeneous `BV` for which the same limit is zero. Hence its positive BV seminorm cannot be bounded by a multiple of the liminf.

The mechanism is that, with `s=-gamma in (0,1)`, this expression for a characteristic function is bounded by `lambda` times its fractional `W^{s,1}` seminorm. The first example is an infinite union of rapidly shrinking intervals with finite fractional perimeter and infinite classical perimeter, multiplied by a cube in higher dimensions. The second is simply a cube.

## Scope

The result covers the full interval `-1 < gamma < 0` in all dimensions. It does not address `gamma <= -1` or `gamma > 0`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: page-20 source excerpt.
- `VERIFICATION.md`: concise proof and render checks.

## Novelty and review

Local indexes and bounded web searches found the source papers but no matching later resolution. Novelty confidence is moderate because the fractional-perimeter observation is elementary and could be folklore.

Recommended review status: likely valid counterexample. The primary check is the one-line domination by the fractional seminorm; the product construction then handles every dimension.

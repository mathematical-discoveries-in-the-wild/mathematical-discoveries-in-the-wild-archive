# Partial Result: Cube Dimension of Cyclic Metrics

Status: `partial_result_likely_valid` / sharp obstruction to one lower-bound route.

Source target: Paul Creutz, *Rigidity of the Pu inequality and quadratic isoperimetric constants of normed spaces*, arXiv:2004.01076, Rev. Mat. Iberoam. 38 (2022), 705-729.

## Source Problem

Creutz proves that for each finite dimension `n >= 2` and area functional `A >= A^ht`, the `A`-quadratic isoperimetric spectrum of `Ban_n` is `[1/(4*pi), r_n^A]`, where `r_n^A < 1/(2*pi)`, the numbers are nondecreasing in `n`, and they converge to `1/(2*pi)`. The paper states that explicit values of `r_n^A` beyond `n = 2` remain open, and that for `n >= 3` the extremal spaces are completely open.

In Remark 4.9(1), the paper obtains the concrete lower bound

```text
r_n^ht >= C^ht(R_infty^n) >= (1 - 2/n) * 1/(2*pi)
```

from an isometric embedding of the cyclic metric `S_{2n}` into `R_infty^n`.

## Result

Let `S_m` be the `m`-point cyclic metric with graph distance
`d(i,j)=min(|i-j|, m-|i-j|)`. The least `N` for which `S_m` embeds isometrically into `ell_infty^N` is exactly `ceil(m/2)`.

Consequently, Creutz's `S_{2n} -> R_infty^n` construction is optimal inside `ell_infty^n`: no larger cyclic metric `S_m` with `m > 2n` can be used in the same cube route to improve Remark 4.9(1).

## Scope

This does not compute `r_n^A`, identify the extremal normed spaces for `n >= 3`, or rule out sharper lower bounds from non-cube normed spaces or other filling-area arguments. It is a narrow sharp obstruction to the most direct cyclic-subset improvement of the source paper's explicit lower bound.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2004.01076.
- `figures/open_constants_crop.png`: source crop for the open constants statement.
- `figures/extremal_spaces_crop.png`: source crop for the extremal-spaces statement.
- `figures/linf_lower_bound_crop.png`: source crop for Remark 4.9(1).
- `code/cycle_linf_dimension_check.py`: small finite verifier for the coordinate construction and lower-bound counting for small cycles.

Human review recommendation: check the odd-cycle lower-bound counting lemma, especially the assertion that one real 1-Lipschitz coordinate certifies at most two diameter pairs.

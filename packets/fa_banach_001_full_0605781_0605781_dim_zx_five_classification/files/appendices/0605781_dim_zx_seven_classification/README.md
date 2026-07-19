# Internal Appendix: Seven-Dimensional `dim Z(X)` Classification

Source: V. Kadets, M. Martin, and R. Paya, "Recent progress and open questions on the numerical index of Banach spaces", arXiv:math/0605781.

Target: Problem 27 asks for the possible values of `dim Z(X)` for `n`-dimensional real Banach spaces, where `Z(X)` is the Lie algebra of skew-hermitian operators.

Canonical packet: `solutions/full/0605781_dim_zx_five_classification/`.
This file is an internal appendix to that packet, not a separate indexed
solution packet.

## Claim

For every seven-dimensional real Banach space `X`,

```text
dim Z(X) in {0,1,2,3,4,5,6,7,9,10,11,15,21}.
```

Every value in this set is attained by an `ell_infty`-sum of Euclidean blocks.

This extends the run's `n=5` and `n=6` analyses, but it is still a partial
result for the all-dimensional Problem 27.

## Main proof idea

Rosenthal's gap theorem, quoted in the source paper, reduces the seven-dimensional case to dimensions at most `15`, plus the Hilbert value `21`. The Euclidean-block construction realizes all values except `8,12,13,14`.

The exclusions use a low-dimensional compact Lie representation table for faithful orthogonal actions on `R^7`:

- dimensions `12` and `13` cannot occur as compact Lie subalgebras of `so(7)` with the needed faithful representation and center;
- dimension `8` forces the standard `su(3)` action on `C^3`, which is sphere-transitive and hence enlarges the norm symmetry to `SO(6)`;
- dimension `14` forces the standard `g_2` action on `R^7`, sphere-transitive, hence the norm is Euclidean and the symmetry algebra is `so(7)`.

## Files

- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop containing the source problem.
- `code/check_seven_dimension_values.py`: sanity check for the Euclidean-block values and missing dimensions.

## Verification

Command run:

```sh
python3 code/check_seven_dimension_values.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The script confirms that the Euclidean-block values are
`{0,1,2,3,4,5,6,7,9,10,11,15,21}` and that the missing values below the
Rosenthal threshold are `{8,12,13,14}`.

## Human review recommendation

Review as a candidate partial solution. The main thing to check is Lemma 1 in the packet: the compact Lie algebra representation table for faithful orthogonal actions on `R^7` and the stated centralizer-rank bounds.

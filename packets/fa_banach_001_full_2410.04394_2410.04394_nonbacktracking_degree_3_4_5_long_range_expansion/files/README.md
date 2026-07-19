# Full result: degree 3,4,5 random regular graphs satisfy part B

Status: `candidate_full_solution_likely_valid_needs_human_review`.

## Source target

Source: Dylan J. Altschuler, Pandelis Dodos, Konstantin Tikhomirov, and
Konstantinos Tyros, *A combinatorial approach to nonlinear spectral gaps*,
arXiv:2410.04394.

Problem 6.3 asks whether, for `d in {3,4,5}`, a uniformly random `d`-regular
graph satisfies part (B) of the paper's long-range expansion property with
high probability.

## Result

Yes. For each `d in {3,4,5}` there is `eta_d > 0` such that every `d`-regular
graph with adjacency nontrivial spectral radius at most
`2 sqrt(d-1) + eta_d` satisfies part (B) of the source long-range expansion
property, with the source parameters `epsilon=0.2`,
`alpha(d)=d^{-10^11 log d}`, and `L(d)=24 alpha(d)^{-1}`.

Friedman's theorem then gives the desired high-probability statement for
uniform random `d`-regular graphs.

## Mechanism

The source proof for `d >= 6` uses ordinary adjacency walks, whose spectral
upper bound has exponential base approximately `4(d-1)`. That base is just
too large for `d=3,4,5`.

The replacement is to count nonbacktracking walks. Nonbacktracking walk
matrices are polynomials in the adjacency matrix. Under a Friedman/Ramanujan
spectral bound, their nontrivial spectral growth is essentially
`(d-1)^{ell/2}`, so the squared upper bound has base `d-1`. The lower bound
coming from a failure of part (B) has base `(d-1-0.2)^3/(d-1)`, which is
strictly larger than `d-1` for `d=3,4,5`.

## Files

- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv PDF.
- `figures/open_problem_crop.png`: crop of Problem 6.3.
- `source_2410.04394.tex`: parsed source TeX used for inspection.
- `code/crop_open_problem.py`: reproducible crop helper.
- `code/verify_constants.py`: fixed-degree arithmetic verifier.

## Verification

Commands used:

```sh
conda run --no-capture-output -n sandbox python code/crop_open_problem.py
conda run --no-capture-output -n sandbox python code/verify_constants.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The crop and rendered PDF were visually inspected. The key human-review focus
is the nonbacktracking polynomial spectral lemma and the transfer of the
source's part (B) contradiction argument from adjacency walks to
nonbacktracking walks.

Ledger: `runs/fa_banach_001/ledger/results/2410.04394_nonbacktracking_degree_3_4_5_long_range_expansion.json`.

# Nonzero sixth trace coefficient in dimensions 9 and 11

Status: `partial_result_likely_valid`

Source: Fatima Aboud and Didier Robert, *Asymptotic expansion for nonlinear
eigenvalue problems*, arXiv:0903.0919.

## Result

For the positive elliptic quadratic polynomial `P(x)=|x|^2`, the source's
sixth semiclassical trace coefficient is explicitly nonzero in the first two
dimensions the authors leave for symbolic computation:

- `C_6^(9)((z+1)^(-15)) = 212857*pi/901943132160 > 0`;
- `C_6^(11)((z+1)^(-18)) = 84227*pi/2727476031651840 > 0`.

The two test functions satisfy the source's decay hypothesis. By the source's
trace and counting propositions, the nonlinear pencil

`-Delta + (|x|^2-lambda)^2`

has infinitely many nonlinear eigenvalues in dimensions 9 and 11. More
precisely, for every `epsilon>0`, its counting function obeys lower bounds of
orders `R^(9/2-epsilon)` and `R^(15/2-epsilon)`, respectively.

## Scope

This proves the `j=3` coefficient conjecture for the radial quadratic
polynomial, not for every positive elliptic polynomial. It does not settle the
source's all-`j`, all-polynomial conjecture.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify_c6_radial.py
```

The script reconstructs the Weyl recurrence in exact rational arithmetic,
checks its `K_2` formula against the source, evaluates all spherical and beta
integrals symbolically, and asserts both displayed constants exactly. See
`verification.md` for the recorded report.

## Files

- `main.tex`: formal proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_conjecture_crop.png`: source page 8, Conjecture (4.25).
- `figures/d9_d11_symbolic_prompt_crop.png`: source page 15.
- `code/verify_c6_radial.py`: exact symbolic verifier.

Ledger:
`runs/fa_banach_001/ledger/results/0903.0919_radial_quadratic_d9_d11_nonzero_c6.json`

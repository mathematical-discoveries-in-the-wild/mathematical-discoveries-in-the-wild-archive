# Hadamard-order FUNTFs for real ell_1^n

Status: candidate partial result, likely valid.

Source paper: J. A. Chavez-Dominguez, D. Freeman, and K. Kornelson,
*Frame potential for finite-dimensional Banach spaces*, arXiv:1804.03677.

## Result

Question 8.2 of the source paper asks whether real `ell_1^n` has a length
`N` finite unit norm tight frame (FUNTF) for every `N >= n`.

This packet proves the following partial result. If there is an `N x n` sign
matrix `H` with orthogonal columns, equivalently `H^T H = N I_n`, then real
`ell_1^n` has a length `N` FUNTF. In particular, the Sylvester Hadamard
matrices give length `2^m` FUNTFs in real `ell_1^n` for every `2^m >= n`.

The construction is explicit. For the row signs `h_{r,i}` set

```text
x_r = (1/n) (h_{r,1}, ..., h_{r,n}) in ell_1^n,
x_r^* = (h_{r,1}, ..., h_{r,n}) in ell_infty^n.
```

Then each pair is normalized and norming, and the frame operator is
`(N/n) I_n`.

## Scope

This does not answer Question 8.2 for all lengths. It supplies a general
infinite family of admissible lengths, including a dyadic length
`2^{ceil(log_2 n)}` for every `n`, and more generally every known Hadamard
order `N >= n`.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of the source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open questions on page 14.
- `code/verify_hadamard_funtf.py`: exact arithmetic sanity checker for the
  Sylvester construction.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1804.03677_hadamard_funtf_real_l1/code/verify_hadamard_funtf.py
```

The script constructs Sylvester sign matrices, selects the first `n` columns,
and checks exactly that the resulting frame operator is `(N/n) I_n` for
`2 <= n <= 20`. This is only a sanity check; the proof in `main.tex` is the
general argument.

Ledger record:
`runs/fa_banach_001/ledger/results/1804.03677_hadamard_funtf_real_l1.json`.

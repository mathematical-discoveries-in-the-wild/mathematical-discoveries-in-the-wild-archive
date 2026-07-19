# Real ell_1^n has FUNTFs of every length

Status: candidate full solution, likely valid, needs human review.

Source paper: J. A. Chavez-Dominguez, D. Freeman, and K. Kornelson,
*Frame potential for finite-dimensional Banach spaces*, arXiv:1804.03677.

## Result

Question 8.2 of the source paper asks whether real `ell_1^n` has a length
`N` finite unit norm tight frame (FUNTF) for every `N >= n`.

This packet gives a constructive positive answer.

For `n >= 3` and `N = n+k` with `0 <= k <= n-1`, set

```text
beta  = (n-k)/(2 n (n-2)),
alpha = 1 - (n-1) beta.
```

Use `n` sign rows with one positive coordinate and `k` all-positive rows:

```text
x_j   = alpha e_j - beta sum_{i != j} e_i,
x_j^* = e_j^* - sum_{i != j} e_i^*,       1 <= j <= n,

y_t   = (1/n) sum_i e_i,
y_t^* = sum_i e_i^*,                       1 <= t <= k.
```

The diagonal coefficients are `(n+k)/n`, and the off-diagonal coefficients
cancel because

```text
-alpha + (n-3) beta + k/n = 0.
```

Thus this gives a length `n+k` FUNTF for all finite-gap lengths. Taking
unions of FUNTFs gives all `N >= n`. The cases `n=1` and `n=2` are handled
separately by trivial length-1 and explicit length-2/length-3 seeds.

## Novelty check

Local cheap indexes were searched for `1804.03677`, `real ell_1^n`, `FUNTF`,
`finite unit norm tight frame`, and related terms. The only local result was
the earlier Hadamard-order partial packet produced in this run.

Web searches on 2026-06-26 for exact phrases around `real ell_1^n FUNTF`,
`finite unit norm tight frame Banach ell_1`, and the source title surfaced the
source arXiv record but no direct later answer. Novelty remains subject to
human review.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of the source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open questions on page 14.
- `code/verify_real_l1_funtf_all_lengths.py`: exact arithmetic verifier.
- `history/hadamard_order_partial_packet/`: earlier Hadamard-order partial
  packet, now superseded by this full construction.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/1804.03677_real_l1_all_lengths_funtf/code/verify_real_l1_funtf_all_lengths.py
```

The script constructs the stated frames and checks normalization, pairing, and
the frame-operator identity exactly for `1 <= n <= 10` and
`n <= N <= 4n+7`. The computation is a sanity check, not the proof.

Ledger record:
`runs/fa_banach_001/ledger/results/1804.03677_real_l1_all_lengths_funtf.json`.

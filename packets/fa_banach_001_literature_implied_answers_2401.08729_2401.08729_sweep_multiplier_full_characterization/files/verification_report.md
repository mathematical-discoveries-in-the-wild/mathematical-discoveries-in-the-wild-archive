# Verification report

Status: passed automated structural checks; human mathematical review still
recommended.

## Source and provenance

- The source question was checked in `source_paper.pdf`, PDF page 2.
- `supporting_0805.0158.pdf` is the decisive Blasco–Pott paper.
- Its PDF pages 6–7 contain Lemma 2.3,
  `pi_B^* pi_B = Lambda_{S_B}+D_B`, and Theorem 2.4,
  `||S_B||_{BMO_mult}+||B||_{SBMO^d}^2 comparable to ||pi_B||^2`.
- Under the faithful left multiplication representation on `L_2(M)`,
  `B_I^*B_I` becomes left multiplication by `b_I^*b_I`, so the cited dyadic
  theorem applies to semicommutative paraproducts.

## Mathematical checks

1. Haar orthogonality was used only to derive the exact positive identity
   `(pi_b^F)^*pi_b^F f = sum_I 1_I a_I m_I f/|I|`.
2. For `d>2`, the diagonal remainder is a `(d-1)`-mode block rather than a
   scalar block.  The proof bounds it child by child, so no simultaneous
   diagonalization or hidden commutation is used.
3. The column BMO lower bound is obtained by indicator tests followed by an
   orthogonal projection onto descendant output Haar modes.
4. Infinite symbols are handled by uniform finite coefficient truncations;
   no pointwise convergence of the positive sweep is assumed.
5. The norm inequalities are explicit:
   `P^2 <= M+C^2`, `M <= 2P^2`, and `C^2 <= P^2`.

## Finite-tree numerical sanity check

The script `code/verify_finite_tree.py` constructs random `2 x 2`
matrix-valued coefficients on finite binary and ternary trees.  It forms the
paraproduct matrix, its positive square, the sweep paraproduct, and the
diagonal remainder.  It checks that the remainder is Haar-block diagonal,
positive up to roundoff, and bounded by the computed column BMO constant.

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_finite_tree.py
```

Observed output on 2026-07-19:

```text
{'d': 2.0, 'identity_error': 0.0, 'off_block_error': 3.85e-16,
 'minimum_diagonal_eigenvalue': -6.59e-17,
 'diagonal_norm': 0.23707, 'bmo_squared': 0.32750,
 'diagonal_bound_slack': 0.09043}
{'d': 3.0, 'identity_error': 0.0, 'off_block_error': 1.02e-15,
 'minimum_diagonal_eigenvalue': -2.68e-16,
 'diagonal_norm': 0.29855, 'bmo_squared': 0.34828,
 'diagonal_bound_slack': 0.04973}
```

The tiny negative eigenvalues and off-block entries are ordinary floating
point error.

## Human review focus

- Decide whether the source authors intended “characterize” to exclude
  Haar-multiplier BMO conditions.  The packet is a full structural iff, but
  it explicitly does not claim a standard-BMO-only answer.
- Verify the extended-value convention for symbols whose Haar coefficients
  initially lie only in `L_1(M)`; boundedness forces the relevant left
  multipliers into `M`.
- Check the uniform finite-set definition against the preferred completion
  convention for formal operator-valued BMO spaces.

## PDF build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after the normal reference rerun.
- The final five-page `solution_packet.pdf` was rendered to PNG at 120 dpi.
- All five pages were inspected: the source crop, displayed formulas, theorem
  breaks, references, margins, and page numbering are legible, with no clipped
  or overlapping content.

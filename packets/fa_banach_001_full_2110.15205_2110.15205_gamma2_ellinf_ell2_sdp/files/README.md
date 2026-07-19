# SDP formula for `gamma_2` on `ell_infty^n tensor ell_2^m`

Status: full answer to the source paper's computability question, likely valid.

Source target: arXiv:2110.15205, Lee--Srinivasa--Junge--Romberg,
*Approximately low-rank recovery from noisy and local measurements by convex
program*.

The source says, in Section 3, that although the rank proxy lemma applies to
`ell_infty^n tensor ell_2^m`, it was not known whether the `gamma_2` norm there
can be computed easily as a standard convex optimization problem. This packet
answers yes.

For a real `m x n` matrix `M`, viewed as an operator `ell_1^n -> ell_2^m`,

```text
gamma_2(M) = min t
```

subject to

```text
[ P   M ] >= 0,
[ M'  Q ]

P <= t I_m,
Q_jj <= t  for every j.
```

This is a polynomial-size SDP. The proof is the standard Gram-factorization
argument: a Hilbert factorization `M = AB` gives the block Gram matrix
`[[AA', M], [M', B'B]]`; conversely any feasible block Gram matrix supplies
vectors `x_i,y_j`, hence a factorization through their Hilbert span. Balancing
the two factors turns the product norm into the single scalar `t`.

## Files

- `main.tex` - full proof packet.
- `solution_packet.pdf` - compiled human-readable packet.
- `source_paper.pdf` - local copy of the source paper.
- `source_paper.tex` - local copy of the parsed source TeX.
- `figures/open_problem_crop.png` - crop of the source passage.

## Limitations

This answers only the `gamma_2` SDP computability issue. It does not prove that
using this norm in the source estimator preserves the same statistical recovery
theorems; that would require separate entropy and concentration estimates for
the `gamma_2` SDP ball.

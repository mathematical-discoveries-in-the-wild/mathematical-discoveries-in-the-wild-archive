# Partial result: physical-space `(q,p)` matrix hypercontractivity for `q >= 2`

Status: partial; superseded by
`runs/fa_banach_001/solutions/full/2109.02600_general_qp_matrix_hypercontractivity/`
for the finite-exponent physical-space question.

Source paper: arXiv:2109.02600, Srinivasan Arunachalam and Joao F. Doriguello, *Matrix hypercontractivity, streaming algorithms and LDCs: the large alphabet case*.

## Source question

Future work item 4 asks for a general `(q,p)`-hypercontractive statement for matrix-valued functions, first over `{0,1}^n` and then over `Z_r^n`.

The previous packet

```text
runs/fa_banach_001/solutions/partial/2109.02600_coefficient_qp_matrix_hypercontractivity/
```

settled the natural Fourier-coefficient formulation. This packet pushes the stronger physical-space version.

## Result proved

For `1 <= p <= 2 <= q < infinity`, define

```text
zeta_r(p) = ((p-1)(1-(p-1)^(r-1))) / ((r-1)(2-p)),
eta_r(q)  = ((q-1)((q-1)^(r-1)-1)) / ((r-1)(q-2)),
```

with continuous endpoint values `zeta_r(2)=1` and `eta_r(2)=1`.

The packet proves that for every matrix-valued function `f: Z_r^n -> C^{m x m}`,

```text
||T_rho f||_{L_q(S_q)} <= ||f||_{L_p(S_p)}
```

whenever

```text
0 <= rho <= sqrt(zeta_r(p) / eta_r(q)).
```

For `r=2`, this recovers the classical Nelson noise threshold

```text
rho <= sqrt((p-1)/(q-1))
```

in the matrix-valued physical-space setting for all `1 <= p <= 2 <= q < infinity`.

## Proof mechanism

The source paper proves an `r`-point Ball--Carlen--Lieb convexity inequality for Schatten `p` norms, `1 <= p <= 2`.

The new ingredient here is the matching `r`-point smoothness inequality for Schatten `q` norms, `q >= 2`, obtained by the same block-diagonal Fourier device and repeated applications of the Ball--Carlen--Lieb smoothness inequality. The one-coordinate noisy estimate follows by:

1. applying the `q`-smoothness inequality to the noisy Fourier coefficients;
2. using Schatten monotonicity `||A||_q <= ||A||_p`;
3. applying the source paper's `p`-convexity inequality.

The product-space result follows by applying the one-coordinate estimate with the remaining coordinates viewed as a finite direct sum of matrix algebras, while the noise in those remaining coordinates is only used as an `L_p` contraction.

## Scope and remaining wall

This packet was a genuine physical-space upgrade beyond the coefficient packet,
but it has now been superseded. The full follow-up packet proves the
physical-space estimate for every finite `1 <= p <= q < infinity`:

```text
runs/fa_banach_001/solutions/full/2109.02600_general_qp_matrix_hypercontractivity/
```

The old "remaining range" `p < q < 2` is handled there by interpolating between
`L_1(S_1) -> L_1(S_1)` contraction and the source-derived
`L_a(S_a) -> L_2(S_2)` endpoint, avoiding the direct Hanner-type one-step
inequality that this packet tried to find.

## Verification

- Source crop: `figures/open_problem_crop.png`, rendered from PDF page 9 of `source_paper.pdf`.
- LaTeX packet: `main.tex`.
- Rendered packet: `solution_packet.pdf`.
- Literature/context checked: arXiv page for `2109.02600`; Ball--Carlen--Lieb trace-norm convexity/smoothness; searches for matrix-valued `(q,p)` hypercontractivity and Schatten two-point hypercontractivity. Related noncommutative hypercontractivity literature exists, but no exact run packet or exact `Z_r^n` physical-space statement matching this theorem was found.

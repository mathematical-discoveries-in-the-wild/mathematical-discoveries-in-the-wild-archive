# Full result: finite-exponent physical-space `(q,p)` matrix hypercontractivity

Status: full finite-exponent solution, subject to human review.

Source paper: arXiv:2109.02600, Srinivasan Arunachalam and Joao F. Doriguello, *Matrix hypercontractivity, streaming algorithms and LDCs: the large alphabet case*.

## Source Question

Future work item 4 asks whether the paper's `(2,p)` matrix-valued hypercontractive theorem can be upgraded to a general `(q,p)` hypercontractive statement, first for matrix-valued functions over `{0,1}^n` and then over `Z_r^n`.

The source passage is cropped in `figures/open_problem_crop.png`; the source PDF is included as `source_paper.pdf`.

## Result Proved

Let `G=Z_r^n`, and let `T_rho` be the usual noise multiplier

```text
(T_rho f)^hat(S) = rho^|S| fhat(S).
```

For every finite `1 <= p <= q < infinity`, the packet proves an explicit dimension-free constant `c_r(p,q) >= 0` such that, for all matrix sizes `m`, all `n`, and all `f:G -> C^{m x m}`,

```text
||T_rho f||_{L_q(S_q)} <= ||f||_{L_p(S_p)}
```

whenever

```text
0 <= rho <= c_r(p,q).
```

For `p>1`, the constant is positive. For the endpoint `p=1<q`, the theorem gives the expected degenerate constant `c_r(1,q)=0`, matching the scalar Nelson phenomenon.

The result includes the Boolean cube case `r=2` and the large-alphabet case `r>=2`.

## Constants

For `1 <= s <= 2`, set

```text
zeta_r(s) = ((s-1)(1-(s-1)^(r-1))) / ((r-1)(2-s)),
beta_r(s) = sqrt(zeta_r(s)),
```

with continuous endpoint values `zeta_r(1)=0` and `zeta_r(2)=1`.

The packet defines `c_r(p,q)` piecewise:

- if `p=q`, then `c_r(p,q)=1`;
- if `1 <= p < q <= 2`, interpolate between `L_1 -> L_1` contraction and the source-derived `L_a -> L_2` endpoint, where

```text
1/a = (1/p + 1 - 2/q) / (2 - 2/q);
```

- if `p <= 2 <= q`, use composition through Hilbert exponent `2`:

```text
c_r(p,q)=beta_r(p) beta_r(q'),
```

where `q'=q/(q-1)`;

- if `2 <= p < q < infinity`, use duality:

```text
c_r(p,q)=c_r(q',p').
```

No optimality is claimed except where already inherited from known endpoints. For `r=2` and `p <= 2 <= q`, this recovers the classical scalar threshold `sqrt((p-1)/(q-1))`; below or above `2`, the constants are generally nonsharp but dimension-free.

## Proof Mechanism

The source result implies an `L_s(S_s) -> L_2(S_2)` physical-space estimate for `1 <= s <= 2`: Parseval moves the target norm to Hilbert-Schmidt coefficients, and Schatten monotonicity gives `||A||_2 <= ||A||_s`.

The noise operator is convolution by a product probability kernel when `0 <= rho <= 1`, hence it is an `L_t(S_t)` contraction for every `t >= 1`.

Complex interpolation between `L_1 -> L_1` and `L_a -> L_2` gives the missing `1 <= p <= q <= 2` range. Duality gives `2 <= p <= q < infinity`. Semigroup composition through `2` gives the crossing range `p <= 2 <= q`.

## Relation to Earlier Packets

This packet upgrades and supersedes the physical-space partial packet:

```text
runs/fa_banach_001/solutions/partial/2109.02600_physical_qge2_matrix_hypercontractivity/
```

It also subsumes the qualitative purpose of the earlier coefficient-space packet, while the coefficient packet remains useful because it records a separate coefficient-norm formulation and a `q<2` obstruction for that different formulation:

```text
runs/fa_banach_001/solutions/partial/2109.02600_coefficient_qp_matrix_hypercontractivity/
```

## Novelty and Literature Check

Cheap run indexes were searched for `2109.02600`, `matrix hypercontractivity`, `general (q,p)`, `Schatten`, and `Z_r`. Existing run hits were exactly the earlier lane 19 partial packets.

A bounded web/literature check on July 18, 2026 searched for exact combinations of `2109.02600`, `general (q,p)`, `matrix-valued hypercontractivity`, `Schatten`, and `Z_r`. I found the source paper and standard background, but no exact later paper answering Future work item 4 with this finite-exponent physical-space theorem.

## Verification

- `main.tex` contains the self-contained proof.
- `solution_packet.pdf` was compiled from `main.tex`.
- Source crop: `figures/open_problem_crop.png`.
- Source PDF: `source_paper.pdf`.
- Ledger record: `runs/fa_banach_001/ledger/results/2109.02600_general_qp_matrix_hypercontractivity.json`.

## Human-Review Recommendation

Review the interpolation step and the endpoint reduction from the source coefficient theorem to physical `L_s(S_s) -> L_2(S_2)`. These are the only real moving parts; the rest is contraction, duality, and semigroup composition.

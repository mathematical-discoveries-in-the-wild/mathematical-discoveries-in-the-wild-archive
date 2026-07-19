# Partial result: coefficient `(q,p)` matrix hypercontractivity

Status: partial; superseded for the physical-space finite-exponent question by
`runs/fa_banach_001/solutions/full/2109.02600_general_qp_matrix_hypercontractivity/`.

Source paper: arXiv:2109.02600, Srinivasan Arunachalam and Joao F. Doriguello, *Matrix hypercontractivity, streaming algorithms and LDCs: the large alphabet case*.

## Source question

The source paper's Future work item 4 asks whether one can prove a general `(q,p)`-hypercontractive statement for matrices, first for matrix-valued functions on `{0,1}^n`, and then for functions on `Z_r^n`.

The packet addresses the Fourier-coefficient formulation naturally suggested by the source paper's Result 1 / Theorem 3.3:

```text
( sum_S rho^{2|S|} ||hat f(S)||_p^2 )^{1/2}
    <= ( E_x ||f(x)||_p^p )^{1/p}.
```

## Result proved

For `1 <= p <= 2`, let `p'` be the conjugate exponent and let `beta_r(p)` be the noise constant from the source paper's `(2,p)` theorem:

```text
beta_r(p)^2 = ((p-1)(1-(p-1)^{r-1})) / ((r-1)(2-p)),
```

with the continuous value `beta_r(2)=1`.

For every outer coefficient exponent `q >= 2`, the packet proves a dimension-free coefficient estimate

```text
( sum_S rho^{q|S|} ||hat f(S)||_p^q )^{1/q}
    <= ( E_x ||f(x)||_p^p )^{1/p}
```

for matrix-valued `f: Z_r^n -> C^{m x m}` and an explicit admissible `rho`.

The proof uses two endpoints:

- the source paper's `(2,p)` matrix hypercontractive theorem;
- a Schatten-valued Hausdorff-Young inequality obtained by interpolating the trivial `L_1(S_1)->ell_infty(S_1)` estimate with Parseval on `L_2(S_2)`.

Holder interpolation between those two endpoints gives the stated `q` family.

The packet also proves that this coefficient formulation cannot have any positive dimension-free noise parameter for `q < 2`: already scalar degree-one character sums force growth like `rho n^{1/q}` on the left and at most `sqrt(n)` on the right.

## Scope and limitations

This is a full answer for the coefficient-norm version of the future-work item, including the sharp qualitative range `q >= 2` versus `q < 2`.

It is only a partial answer to the informal source question. The packet does not prove a physical-space estimate of the form

```text
||T_rho f||_{L_q(S_q)} <= ||f||_{L_p(S_p)}
```

nor does it claim optimal noise constants in the coefficient estimate.

Follow-up packets:

```text
runs/fa_banach_001/solutions/partial/2109.02600_physical_qge2_matrix_hypercontractivity/
runs/fa_banach_001/solutions/full/2109.02600_general_qp_matrix_hypercontractivity/
```

The full packet proves the physical-space estimate for every finite
`1 <= p <= q < infinity`. This coefficient packet remains useful because it
records a different coefficient-norm formulation and the scalar obstruction to
positive dimension-free coefficient noise when the outer coefficient exponent
is `q < 2`.

## Verification

- Source crop: `figures/open_problem_crop.png`, rendered from PDF page 9 of `source_paper.pdf`.
- LaTeX packet: `main.tex`.
- Rendered packet: `solution_packet.pdf`.
- Bounded duplicate/literature check: cheap run indexes for `2109.02600`, `Matrix hypercontractivity`, `general (q,p)`, `Schatten`, and `Z_r`; web searches for exact combinations of `matrix-valued hypercontractivity`, `q,p`, `Schatten`, and `Z_r`. No existing run packet or exact later answer was found.

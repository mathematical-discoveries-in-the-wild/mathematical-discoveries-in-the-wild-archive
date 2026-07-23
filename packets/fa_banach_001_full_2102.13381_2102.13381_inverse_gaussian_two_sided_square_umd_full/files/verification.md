# Verification Report

## Verdict

`candidate full solution - likely valid`

The proof was audited against the source definitions and the exact wording of
the remark after Theorem 1.5. No unresolved mathematical dependency remains.
The final appeal is to the standard Xu-Hytönen characterization already
quoted and used by the source paper.

The 2022 open-access typeset version of the 2023 Potential Analysis article
was checked separately. The same question remains verbatim on published PDF
page 43.

## Exact-Question Audit

The proposed modification retains the first inequality in Theorem 1.5(ii),
the upper estimate for `g_A^{1,X}`. It replaces only the second inequality,
the upper estimate for `g_A^{1,X*}`, by a lower estimate for
`g_A^{1,X}`. Thus the modified condition is exactly a two-sided estimate for
the same `X`-valued lattice square function. The packet does not claim that
the lower estimate alone implies UMD.

## Scaling Audit

For `f_epsilon(x)=F(x/epsilon)` and `x=epsilon z`,

```text
epsilon^2 A = -Delta_z/2 - epsilon^2 z dot grad
```

under conjugation by dilation. The time change `t=epsilon s` leaves
`dt/t=ds/s` and `t partial_t=s partial_s`. The input and output norms both
acquire the same factor

```text
c_n^(1/p) epsilon^(n/p)
```

and the rescaled density is `exp(epsilon^2 |z|^2)`.

## Local Error Audit

The source estimate on the local region is

```text
|| t partial_t(P_t^A(x,y)-P_t(x-y)) ||_L2(dt/t)
    <= C sqrt(1+|x|) / |x-y|^(n-1/2).
```

After `x=epsilon z`, `y=epsilon u`, including the Jacobian
`dy=epsilon^n du`, the error is

```text
C epsilon^(1/2)
  integral |z-u|^(-n+1/2) |F(u,w)| du.
```

For compactly supported bounded finite tensors, the scalar majorant is bounded
near the support and is `O(|z|^(-n+1/2))` at infinity. Its relevant `p`-th
power integral is

```text
epsilon^(p/2)
integral_1^(rho/epsilon) r^(n-1-p(n-1/2)) dr.
```

It tends to zero in all cases:

- `p(n-1/2)>n`: `O(epsilon^(p/2))`;
- `p(n-1/2)=n`: `O(epsilon^(p/2) log(1/epsilon))`;
- `p(n-1/2)<n`: `O(epsilon^(n(p-1)))`.

This covers every `n>=1` and `p>1`.

## Tail Audit

Outside a fixed physical ball, the shrinking support is uniformly separated
from the output point.

- On a fixed annulus, the full Poisson square kernel is uniformly bounded:
  use the Euclidean kernel plus the local comparison estimate on the local
  part, and the source's global bound on the global part.
- For large `|x|`, the pair is global. The source's estimate `(A2)`, after
  the Poisson-to-heat square-kernel comparison, gives
  `(1+|x|)^n exp(-a|x|^2)` for inputs in a fixed small ball, with
  `a>1/p`.

This majorant belongs to `L^p(gamma_-1)`. Minkowski then contributes the
shrinking input volume `epsilon^n`; after the norm normalization
`epsilon^(-n/p)`, the tail is
`O(epsilon^(n(1-1/p)))`, which tends to zero.

## Limit and Density Audit

On the central expanding ball, the weight is bounded by `exp(rho^2)` and
converges pointwise to one. The Euclidean square function of a compactly
supported finite tensor lies in `L^p_X`, by domination by finitely many scalar
Poisson square functions. Dominated convergence therefore identifies the
limit norm.

The resulting Euclidean upper estimate makes the square-function map
continuous on a dense test class. The reverse estimate then extends to all of
`L^p_X` by density and the pointwise reverse triangle inequality for the
`L^2(dt/t)` norm.

## External-Theorem Audit

The source paper explicitly states that, for Banach lattices, a two-sided
Euclidean Poisson lattice-square estimate implies UMD, citing:

- Q. Xu, *Littlewood-Paley theory for functions with values in uniformly
  convex spaces*, J. Reine Angew. Math. 504 (1998), Theorem 4.1.
- T. P. Hytönen, *Littlewood-Paley-Stein theory for semigroups in UMD
  spaces*, Rev. Mat. Iberoam. 23 (2007), Theorem 1.6.

No stronger or unproved transference theorem is invoked.

## Computational Checks

No numerical computation is part of the proof. The exponent arithmetic,
dilation factors, and measure normalization were checked symbolically in the
displayed calculations above.

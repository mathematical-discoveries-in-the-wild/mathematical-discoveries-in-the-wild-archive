# Counterexample: One-Variable Steinhaus Decoupling Fails in `c0`

Status: `counterexample`

Source problem paper: D. Carando, F. Marceca, and P. Sevilla-Peris,
*Decoupling inequalities with exponential constants*, arXiv:2012.15293.

## Target

Remark 4.3 asks whether the `K`-convexity assumption in the reverse
one-variable Steinhaus decoupling estimate is necessary.

## Result

The reverse estimate cannot hold in all Banach spaces without a geometric
assumption. It fails for `X = c0`.

More precisely, for every `p >= 1` there is no constant `C_p` such that for
all `m`, all `n`, and all `m`-homogeneous tetrahedral polynomials
`P: C^n -> c0`,

```text
sqrt(m) (E ||M(w',w,...,w)||^p)^{1/p}
    <= C_p (E ||P(w)||^p)^{1/p}.
```

Here `M` is the symmetric `m`-linear form associated to `P`, and `w,w'` are
independent Steinhaus vectors.

## Construction

For fixed `m,n`, let the finite coordinates of `c0` be indexed by the
`m`-subsets `A` of `[n]`, and define

```text
P(z) = sum_{|A|=m} e_A z_A.
```

Then `||P(w)||_infty = 1` always. For the associated symmetric multilinear
map,

```text
M_A(w',w,...,w)
  = (1/m) sum_{j in A} w'_j prod_{i in A, i != j} w_i.
```

Writing `u_j = w'_j / w_j`, this coordinate has modulus

```text
(1/m) |sum_{j in A} u_j|.
```

For `n` large compared with `m`, with probability at least `1/2` there are
`m` coordinates `u_j` in the arc `{exp(i theta): |theta| <= pi/3}`. Choosing
those coordinates gives a set `A` for which the above modulus is at least
`1/2`. Thus `(E||M(w',w,...,w)||^p)^{1/p}` is bounded below by a positive
constant independent of `m`, while the estimate would require
`sqrt(m) <= O(1)`.

## Scope

This packet shows that the `K`-convexity hypothesis cannot simply be removed.
It does **not** settle the finer question, also mentioned in the source remark,
of whether `K`-convexity can be weakened to finite cotype: `c0` has trivial
cotype.

## Evidence

- `figures/open_problem_crop.png`: Remark 4.3 from the source paper, PDF page
  24.
- `source_paper.pdf`: local copy of arXiv:2012.15293.
- `solution_packet.pdf`: full proof packet.

## Human Review Notes

Recommended review focus:

- Check the symmetrization formula for the associated multilinear map:
  each coordinate is the average over the `m` possible positions of `w'`.
- Check the probabilistic lower bound by the arc-counting argument for iid
  Steinhaus ratios `u_j=w'_j/w_j`.
- Confirm the scope note: this is a counterexample to dropping geometric
  assumptions entirely, not a finite-cotype counterexample.

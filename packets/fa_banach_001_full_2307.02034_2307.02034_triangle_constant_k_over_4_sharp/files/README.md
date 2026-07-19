# Full Result Packet: sharp triangle constant for contractions

Run: `fa_banach_001`

Result type: `full_result`

Status: promoted proof. This packet proves the sharpness conjecture at the end
of arXiv:2307.02034, and slightly strengthens the even case recorded there.

## Source Problem

- Jean-Christophe Bourin and Eun-Young Lee, *Diagonal and off-diagonal blocks
  of positive definite partitioned matrices*, arXiv:2307.02034.
- Local source inspected: `data/parsed/arxiv_sources/2307.02034/source.tex`,
  lines 606--663.
- Local PDF: `source_paper.pdf`.

Corollary `cortriangle` in the source states that if
`A_1,...,A_k` are contractions in `M_n`, `k>1`, then

```tex
|A_1 + ... + A_k| <= (k/4) I + |A_1| + ... + |A_k|.
```

The source proves that the constant `k/4` is sharp for even `k` and `n >= 3`.
It then conjectures that the same constant is optimal for all odd integers
`k>1`. In the abstract this is stated in particular for three contractions,
where the conjectured sharp constant is `3/4`.

## Result

For every integer `k>1`, the constant `k/4` in the above triangle inequality is
optimal. In fact, over complex matrices, `2 x 2` rank-one contractions already
force the constant `k/4`.

For a real-matrix version, the same construction works in `M_3(R)` for every
odd `k >= 3` by replacing roots of unity with vertices of a regular `k`-gon.

## Construction

Let `zeta = exp(2 pi i/k)` and let `e_1,e_2` be the standard basis of `C^2`.
Set

```tex
v_j = (1/2)e_1 + (sqrt(3)/2) zeta^j e_2,
qquad
u = e_1,
qquad
A_j = u v_j^*
```

for `j=0,...,k-1`. Each `v_j` is a unit vector, hence each `A_j` is a
rank-one contraction and

```tex
|A_j| = v_j v_j^*.
```

Since `sum_j zeta^j = 0`,

```tex
sum_j A_j = (k/2) e_1 e_1^*,
qquad
|sum_j A_j| = (k/2) e_1 e_1^*,
```

while

```tex
sum_j |A_j| =
diag(k/4, 3k/4).
```

If the source inequality held with `cI` in place of `(k/4)I`, then evaluating
on `e_1` would give

```tex
k/2 <= c + k/4,
```

so `c >= k/4`. The source corollary gives the matching upper bound, hence the
constant is exactly sharp.

## Scope Notes

- This settles the odd-`k` conjecture in the source.
- It also gives a shorter complex `2 x 2` sharpness witness for even `k`; the
  source had an even-`k` witness in dimension `n >= 3`.
- The result concerns the additive identity term in Corollary `cortriangle`,
  not the separate optimal `1/4` block-matrix constant in the main theorem.

## Verification

- `main.tex` contains the proof in manuscript form.
- `tmp/verify_rank_one_construction.py` numerically checks the obstruction for
  representative values of `k`.
- `solution_packet.pdf` is the rendered proof note.

# Counterexample: the weak `(p,1)` limit case fails

Status: candidate counterexample, likely valid.

Source: Kati Ain and Eve Oja, arXiv:1409.6476, *On `(p,r)`-null sequences and their relatives*.

## Result

For every `1 <= p < infinity`, the open limit case `r=1` in Remark 4.6 has a negative answer:

```text
W_(p,1) != W_(p,1) o W.
```

Consequently, Theorem 4.8 does not extend to the limit case `r=1`.

## Counterexample

Let `j: ell_1 -> c0` be the canonical inclusion.

The unit vector basis `(e_n)` of `c0` belongs to `ell_p^w(c0)` for every finite `p`, because `(c0)^* = ell_1` and `ell_1 subset ell_p`. Therefore

```text
j(B_ell1) = B_ell1 subset (p,1)-conv(e_n),
```

so `j` is weakly `(p,1)`-compact. It is not compact.

On the other hand, every operator in `W_(p,1) o W` is compact. Indeed, every weakly `(p,1)`-compact operator factors through a quotient of `ell_1`; quotients of `ell_1` have the Schur property, so such operators are completely continuous. A completely continuous operator maps weakly compact sets to norm-compact sets. Thus composing it after a weakly compact operator gives a compact operator.

Hence `j in W_(p,1)` but `j notin W_(p,1) o W`.

For Theorem 4.8, the sequence `(e_n)` in `c0` is weakly null and relatively weakly `(p,1)`-compact, but it is not weakly `W_(p,1)`-compact; otherwise it would lie in the image of a weakly compact set under a completely continuous operator, hence in a norm-compact set, impossible.

## Novelty Check

Bounded checks performed on 2026-06-20:

- local run indexes for `1409.6476`, `p-(r)-null`, `weakly (p,1)-compact`, `W_(p,1)`, and related operator-ideal terms;
- local parsed source search around `r=1`, `Theorem 4.8`, `Proposition 4.5`, `weakly p-compact`, and `c0`;
- web searches for exact and close phrases including `Proposition 4.5 W_(p,1) p,r-null sequences`, `On (p,r)-null sequences and their relatives r=1 We do not know`, `weakly (p,1)-compact c0`, and `weakly (p,r)-null Theorem 4.8 r=1`.

These found the source paper and no prior answer to the two limit-case questions.

## Files

- `main.tex` contains the proof.
- `solution_packet.pdf` is the rendered packet.
- `source_paper.pdf` is the source paper.
- `figures/prop45_limit_crop.png` and `figures/thm48_limit_crop.png` show the source remarks.

## Human Review

Recommended review focus: verify the factorization of weakly `(p,1)`-compact operators through a quotient of `ell_1`, and the conclusion that `W_(p,1) o W` consists of compact operators.


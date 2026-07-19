# Odd-dimensional operator-space numerical index

result type: full
status: candidate full solution, likely valid, needs human review
source paper: Vladimir Kadets, Miguel Martin, Javier Meri, Antonio Perez, Alicia Quero, "On the numerical index with respect to an operator", arXiv:1905.12257
target location: page 18, immediately after Theorem 4.7; source line 1012 in the parsed TeX

## Claim

The open odd-dimensional case after Theorem 4.7 has an affirmative answer. If
`H` is a real Hilbert space of odd dimension at least `3`, then

```text
n_G(L(H),Y)=0
```

for every Banach space `Y` and every norm-one operator
`G in L(L(H),Y)`. Since finite-dimensional `K(H)=L(H)`, the same also covers
the corresponding compact-operator space in the finite odd case. Together with
Theorem 4.7 of the source paper, this removes the parity gap for all real
Hilbert spaces of dimension at least `2`.

## Proof Summary

Let `W=L(H)`. Proposition 3.10(c) of the source paper says it is enough to show
that the union of the ranges of all zero-numerical-radius operators on `W` is
dense in `W`. In fact it equals all of `W`.

For a prescribed `C in L(H)`, choose unit vectors `a,b` with `<Cb,a>=0`.
Choose skew-adjoint `A,B` with one-dimensional kernels `Ra`, `Rb` and with
disjoint nonzero rotation frequencies. The Sylvester map

```text
R(X)=AX+XB
```

has numerical radius zero because it is the infinitesimal generator of the
isometry group `X -> exp(tA) X exp(tB)`. Its kernel is exactly the line
spanned by `a tensor b*`, so its range is the Hilbert-Schmidt orthogonal
hyperplane to that line. The condition `<Cb,a>=0` puts `C` in this range.
Thus every `C` lies in the range of some zero-radius operator `R`, and
Proposition 3.10(c) applies.

## Verification

The packet includes `code/verify_sylvester_cover.py`, a numerical sanity check
for the finite-dimensional Sylvester step. It is not used as proof, but it
checks random instances in dimensions `3,5,7`.

Command run:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/1905.12257_odd_dim_operator_space_zero_index/code/verify_sylvester_cover.py --dims 3 5 7 --trials 20
```

Result: ranks were `8,24,48` respectively, i.e. `n^2-1`, with residuals below
`1.2e-13`.

## Novelty Check

Bounded check performed on 2026-06-26:

- local run indexes searched for `1905.12257`, `numerical index with respect`,
  `odd dimension`, `L(H),Y`, and `operator`;
- web/arXiv searches for `"When H has odd dimension" "n_G" "L(H),Y"`,
  `"numerical index with respect to an operator" "odd dimension" "L(H)"`,
  `"On the numerical index with respect to an operator" "odd dimension"`, and
  `"n_G(\\mathcal{L}(H),Y)=0"`.

No separate later paper or existing packet answering this exact odd-dimensional
question was found. The only direct web hit was the source arXiv record.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1905.12257.
- `figures/open_problem_crop.png`: readable crop of the source question.
- `code/verify_sylvester_cover.py`: sanity-check script.

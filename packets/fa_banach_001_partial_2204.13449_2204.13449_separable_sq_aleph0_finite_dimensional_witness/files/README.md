# 2204.13449 - finite-dimensional witnesses in the separable SQ example

Status: `partial_result_likely_valid`

Source paper: Antonio Aviles, Stefano Ciaci, Johann Langemets, Aleksei
Lissitsin, and Abraham Rueda Zoca, *Transfinite almost square Banach spaces*,
arXiv:2204.13449.

## Result

The separable `SQ_{<aleph0}` example in Section 2 of the source paper satisfies
the stronger finite-dimensional exact formulation: for every finite-dimensional
subspace `F` of the source space `X`, there is `u in S_X` such that

```text
||z + t u|| <= max{||z||, |t|}
```

for all `z in F` and all real `t`.

This gives a concrete positive subcase for the authors' comment that the
`kappa = aleph0` subspace-version of the transfinite SQ characterization is
unclear. It does not solve the general equivalence problem and does not answer
whether `c_0` itself admits an equivalent `SQ_{<aleph0}` norm.

## Proof Idea

For a finite-dimensional subspace `F`, choose a coordinate `m` larger than
`dim F`. The `m`th coordinate shadow of `F` is a finite-dimensional subspace of
odd functions on the sphere `S_{R^m}` of dimension `< m`, so Borsuk-Ulam gives a
point where all of those coordinate functions vanish. The pointwise gauge of
that coordinate shadow is an even continuous function `q`; multiplying an odd
norm-one function `h` by `1-q` gives an odd function `g` with norm one and
pointwise room exactly complementary to the entire coordinate shadow. Placing
`g` in the `m`th `c_0`-sum coordinate gives the desired vector `u`.

## Files

- `main.tex` - full proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2204.13449.

## Verification Notes

The proof uses only the source definitions and the standard Borsuk-Ulam theorem
for odd maps `S^{m-1} -> R^r` with `r < m`. The coordinate is chosen with
`m > dim F`, which is the safe dimension count.


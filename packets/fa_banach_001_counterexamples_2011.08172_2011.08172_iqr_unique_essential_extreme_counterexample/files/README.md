# Counterexample Packet: Unique Essential Extreme Point Not Recovered by Fixed IQR Sections

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2011.08172`
- source paper: Matthew J. Colbrook and Anders C. Hansen, *On the infinite-dimensional QR algorithm*
- target passage: compiled source PDF page 42 / source lines 2167-2171, the concluding conjecture that for normal operators the IQR algorithm should recover the extreme parts of the essential spectrum when the set of extremal points has size one.

## Claim

There is an invertible normal operator `T` on `ell^2(N)` such that:

- `T` is self-adjoint, positive, and non-diagonal in the canonical basis;
- `sigma_ess(T) = {1}`, so the essential spectrum has exactly one maximal-modulus extremal point;
- `T` has no eigenvalues of modulus greater than `r_ess(T)=1`;
- for every finite `m`, every IQR iterate section
  `P_m Q_n^* T Q_n |_{P_m ell^2}` stays a positive distance away from `1`, uniformly in `n`.

Thus the source conjecture is false under the natural fixed-`m`, `n -> infinity`
reading of "recovered in the limit `n -> infinity` for large enough `m`".

## Construction

Let

```text
a_k = 1 - 1/(2k),      b_k = 1 - 1/(2k+1)
```

and let `B_k` be the non-diagonal real symmetric `2 x 2` block obtained by
rotating `diag(a_k,b_k)` by the Hadamard unitary.  Set
`T = direct_sum_k B_k` on the canonical two-dimensional block decomposition
of `ell^2(N)`.

The blocks have eigenvalues `a_k < b_k < 1` and `a_k,b_k -> 1`, so
`T-I` is compact and `sigma_ess(T)={1}`.  But the finite span of the first
`m` canonical vectors is contained in the first `ceil(m/2)` reducing blocks.
The IQR identity from the source paper gives

```text
span{Q_n e_j : 1 <= j <= m} = span{T^n e_j : 1 <= j <= m},
```

so the `m`-section never leaves those finitely many reducing blocks.  Its
spectrum is therefore bounded above by `b_ceil(m/2) < 1` for all `n`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local compiled PDF of the arXiv source.
- `source_paper.tex`: local parsed TeX source.
- `figures/open_problem_crop.png`: crop of the source conjecture passage.
- `code/verify_block_counterexample.py`: small finite-block sanity checker.

## Novelty Check

The run indexes were searched for `2011.08172`, `infinite-dimensional QR`,
`QR algorithm`, `QR iteration`, and `Hessenberg`; no duplicate packet or
attempt for this paper was found.

A bounded web search on 2026-07-19 for exact phrases around `2011.08172`,
`On the infinite-dimensional QR algorithm`, `IQR algorithm`, `normal operators`,
`essential spectrum`, and `extremal points` found the source paper but no later
answer or counterexample to this exact conjecture.  Human review should focus
mainly on the interpretation of the source phrase "recovered in the limit
`n -> infinity` for large enough `m`"; the operator-theoretic obstruction is
elementary.

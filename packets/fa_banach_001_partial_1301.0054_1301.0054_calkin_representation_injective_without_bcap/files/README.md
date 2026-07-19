# Partial Packet: BCAP-Free Injectivity of the Calkin Representation

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- source arXiv id: `1301.0054`
- source paper: March T. Boedihardjo and William B. Johnson, *On Mean Ergodic Convergence in the Calkin Algebras*
- target: Remark 1 after Theorem 2.1 asks whether the theorem is true without assuming that `X` has the BCAP.

## Claim

The Calkin representation from Theorem 2.1 is always injective, even without
BCAP.

More precisely, for every infinite-dimensional Banach space `X`, if
`hat T=0` on `hat X`, then `T` is compact. Hence the map

```text
f : B(X)/K(X) -> B(hat X),   dot T |-> hat T
```

is a well-defined faithful algebra anti-homomorphism.

## Scope

This is a partial result only. It does **not** prove the bounded-below
embedding estimate in Theorem 2.1 without BCAP, and it does **not** answer
Remark 2 about whether the representation is isometric for `L_p(0,1)`,
`p != 2`.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1301.0054
- `figures/theorem_context_crop.png`: Theorem 2.1 and construction context
- `figures/open_problem_crop.png`: source remarks containing the open questions

## Verification

The proof is analytic. No computational step is used in the result.

Human review should focus on the compactness criterion
`inf_E ||Q_E T|| > 0` for noncompact `T`, where `E` ranges over finite-dimensional
subspaces of `X`, and on the construction of the weak-star-null ultrapower
vector from functionals in `E^\perp`.

# Compact-operator algebras determine the underlying Banach space

Status: **candidate full solution, likely valid**, for the explicit
compact-operator-algebra subquestion on page 40 of arXiv:2505.02338. The
broader maximal `L^p` Roe-algebra and K-theory questions remain open.

## Result

For nonzero Banach spaces `X` and `Y`,

```text
K(X) and K(Y) are isomorphic as Banach algebras
if and only if
X and Y are isomorphic as Banach spaces.
```

The forward implication is recovered from a rank-one idempotent: its minimal
left ideal is canonically isomorphic to the underlying Banach space, and a
Banach-algebra isomorphism preserves that ideal. The reverse implication is
conjugation by a Banach-space isomorphism.

Consequently, for `1 <= p < infinity`,

```text
K(L^p[0,1]) is isomorphic to K(ell^p) as a Banach algebra
exactly when p = 2.
```

For `p != 2`, the classical non-isomorphism of `L^p[0,1]` and `ell^p` is
reproved using the Schur property at `p=1`, and the complemented Rademacher
copy of `ell^2` plus Pitt's compactness theorem for `1<p<infinity`.

## Scope and review

- “Isomorphic” is interpreted in the standard Banach-algebra sense: a bounded
  linear algebra isomorphism. If the source intended only Banach-space
  isomorphism between the two operator spaces, this packet does not decide
  that different question.
- The source's sentence overlooks the Hilbert case: `L^2[0,1]` and `ell^2`
  are isometrically isomorphic.
- Recommended review focus: confirm the intended meaning of “isomorphic” in
  the source paragraph. The minimal-left-ideal proof itself is elementary and
  does not use an approximation property.

See [solution_packet.pdf](solution_packet.pdf) for the source crop, formal
theorem, proof, verification notes, novelty search, and references.


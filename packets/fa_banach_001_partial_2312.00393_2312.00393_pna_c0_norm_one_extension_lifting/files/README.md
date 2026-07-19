# Partial Result: Norm-One Extension Lifting for \(c_0\subset \mathrm{PNA}(M)\)

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_04`  
Source paper: G. Choi, M. Jung, H. J. Lee, and O. Roldan, *Embeddings of infinite-dimensional spaces in the sets of norm-attaining Lipschitz functions*, arXiv:2312.00393.

## Target

Question 4.1 in the source asks whether every infinite pointed metric space
\(M\) satisfies that \(c_0\) is isometrically contained in
\(\mathrm{PNA}(M)\), the set of pointwise norm-attaining scalar Lipschitz
functions on \(M\).

The source proves the weaker statement that every infinite \(M\) contains a
metric subspace \(M_0\subseteq M\) such that \(c_0\subset \mathrm{PNA}(M_0)\)
isometrically. The remaining obstruction is the subspace-to-ambient lifting
step: scalar norm-preserving Lipschitz extensions are not automatically
linear on a whole \(c_0\)-copy.

## Result

This packet proves a sharp extension-lifting partial result:

If \(K\subseteq M\) contains the base point and there is a norm-one linear
extension operator
\[
  E:\mathrm{Lip}_0(K)\longrightarrow \mathrm{Lip}_0(M),
  \qquad (Ef)|_K=f,
\]
then every isometric copy of \(c_0\) contained in \(\mathrm{PNA}(K)\) lifts to
an isometric copy of \(c_0\) contained in \(\mathrm{PNA}(M)\).

In particular, the same conclusion holds whenever \(K\) is a pointed
1-Lipschitz retract of \(M\).

## Scope

This does not solve Question 4.1 in full, because arbitrary metric subspaces
need not admit norm-one linear simultaneous Lipschitz extension operators.
It does give a clean sufficient condition for upgrading the source theorem's
subspace conclusion to the original ambient space.

## Files

- `main.tex`: expert-facing partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local rendering of arXiv:2312.00393 from cached source.
- `figures/open_problem_crop.png`: rendered source page containing Question 4.1.

## Verification

The proof is purely functional-analytic. The key observation is that a
norm-one linear extension preserves the norm of every lifted function because
restriction back to \(K\) gives the reverse inequality; pointwise
norm-attainment also persists because the witnessing point and slopes inside
\(K\) are still available inside \(M\).

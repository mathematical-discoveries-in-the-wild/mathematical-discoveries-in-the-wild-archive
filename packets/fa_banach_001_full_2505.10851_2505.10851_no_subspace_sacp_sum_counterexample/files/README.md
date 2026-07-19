# Full solution: no subspace counterexample to the SACP sum question

Status: `full`

Source paper: Syamantak Das, *Transfer of Approximation properties under Local Constraints and Best Simultaneous Approximation on Sums*, arXiv:2505.10851v3.

## Claim

Remark 3.12 of the source paper asks whether there can be two subspaces
\(Y\) and \(Z\) of a Banach space \(X\) such that
\((X,Y,\mathcal F(X))\) and \((X,Z,\mathcal F(X))\) have
\(\tau\)-\(\mathfrak F_{cmc}\)-SACP, \(Y+Z\) is closed, but
\((X,Y+Z,\mathcal F(X))\) fails \(\tau\)-\(\mathfrak F_{cmc}\)-SACP.

This packet gives a negative answer for the two topologies allowed in the
paper, namely the norm topology and the weak topology. Such a subspace
counterexample does not exist.

## Proof Idea

The key point is that the full class \(\mathfrak F_{cmc}\) contains the
one-variable function
\[
g(t)=\max\{t-1,0\}.
\]
For a subspace \(V\) and the one-point finite set \(F=\{0\}\), every point of
the closed unit ball of \(V\) is an exact \(g\)-minimizer, since
\(\operatorname{rad}_V^g(F)=0\) and \(g(\|v\|)=0\) for \(\|v\|\leq 1\).

Thus norm-\(\mathfrak F_{cmc}\)-SACP forces the closed unit ball of \(V\) to be
norm sequentially compact, hence norm compact, hence \(V\) is finite
dimensional. Weak-\(\mathfrak F_{cmc}\)-SACP forces the closed unit ball of
\(V\) to be weakly sequentially compact, hence weakly compact by
Eberlein--Smulian, hence \(V\) is reflexive.

The source paper's own transfer theorems then finish the problem:

- Theorem 3.10 transfers \(\tau\)-\(\mathfrak F_{cmc}\)-SACP from \(Z\) to
  \(Y+Z\) when \(Y\) is finite dimensional.
- Theorem 3.14 transfers weak-\(\mathfrak F_{cmc}\)-SACP from \(Z\) to
  \(Y+Z\) when \(Y\) is reflexive and \(Y+Z\) is closed.

## Novelty Check

Before promotion, the run indexes were searched for arXiv:2505.10851, the
exact title, the phrase from Remark 3.12, and the keywords
`\(\mathfrak F_{cmc}\)`, `SACP`, `weak-F_cmc-SACP`, and `Y+Z`.
No duplicate result packet or literature-answer packet was found.

External web/arXiv searches on 2026-06-19 for the exact remark phrase,
`Transfer of Approximation properties under Local Constraints Remark 3.12`,
`F_cmc simultaneous approximative SACP subspaces`, and
`weak-F_cmc-SACP reflexive subspace Y+Z` found the source paper and the earlier
SACP paper arXiv:2501.03347, but no later paper explicitly answering this
subspace-sum question.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2505.10851.
- `figures/function_class_crop.png`: source definition of \(\mathfrak F_{cmc}\).
- `figures/finite_dim_transfer_crop.png`: source Theorem 3.10.
- `figures/open_remark_crop.png`: source Remark 3.12.
- `figures/weak_transfer_crop.png`: source Theorem 3.14.

## Human Review Focus

Review as a short full solution. The main checks are:

1. \(g(t)=\max\{t-1,0\}\) is indeed allowed by the source definition of
   \(\mathfrak F_{cmc}\).
2. The unit-ball minimizing-sequence argument is compatible with the source
   definition of SACP for \(F=\{0\}\).
3. The source's Theorems 3.10 and 3.14 apply exactly to the norm and weak
   versions of the subspace question in Remark 3.12.


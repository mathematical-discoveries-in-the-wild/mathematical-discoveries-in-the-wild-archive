# Finite-rank aDP operators attain their norm

Status: likely valid partial result.

Source target: Kadets, Martin, Meri, and Perez, "Spear operators between Banach spaces", arXiv:1701.02977.

## Result

Let \(G:X\to Y\) be a norm-one finite-rank operator with the alternative Daugavet property. Then
\[
B_X=\overline{\operatorname{conv}}\{x\in S_X:\|Gx\|=1\}.
\]
In particular, \(G\) attains its norm. Consequently every finite-rank spear operator attains its norm.

## Source Questions Addressed

The paper's Chapter 10 asks whether the rank-one results can be extended to finite-rank operators, and separately asks whether every spear operator attains its norm. This packet does not prove the full finite-rank lushness or adjoint-lushness statements, but it proves a finite-rank norm-attainment consequence for the larger aDP class, hence for finite-rank spear operators.

## Idea of the Proof

The point is to avoid extending lushness back to the original codomain. Put \(Z=G(X)\), with the norm inherited from \(Y\), and view the same map as \(H:X\to Z\). The source paper explicitly states that the aDP is preserved when the codomain is restricted to any subspace containing the range. Since \(Z\) is finite-dimensional, the source paper's finite-dimensional codomain theorem upgrades \(H\) from aDP to lush. Finally, lush operators attain their norm, indeed with norm-attaining vectors whose convex hull is dense in \(B_X\). The norm-attaining set is unchanged because \(Z\) has the inherited norm.

## Limitations

This does not show that the original finite-rank operator \(G:X\to Y\) is lush. The source paper notes that aDP, spearness, and lushness are not stable under arbitrary codomain extension, so the quotient/range reduction cannot simply be inverted. The full finite-rank analogues of Corollary 6.6 and Proposition 7.8 remain open.

## Novelty Check

Cheap run indexes had no duplicate for arXiv:1701.02977, spear operators, finite-rank aDP/lushness, or finite-rank norm-attainment. Local later-source checks included arXiv:2306.02645 on generating operators and arXiv:2306.02638 on numerical range methods; neither records this finite-rank aDP consequence. External web searches on 2026-06-16 for quoted combinations of "finite-rank", "alternative Daugavet property", "spear operators", and "norm-attaining" returned no exact hit. Novelty confidence is modest because the proof is a short corollary obtained by combining results already present in the source paper, but the corollary is not stated there and directly advances one finite-rank/norm-attainment subcase.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1701.02977.


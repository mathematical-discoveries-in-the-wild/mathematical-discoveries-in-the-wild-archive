# Finite-rank aDP operators are lush

Status: likely valid strong partial result.

Source target: Kadets, Martin, Meri, and Perez, "Spear operators between Banach spaces", arXiv:1701.02977.

## Result

Let \(G:X\to Y\) be a norm-one finite-rank operator. Then
\[
G\text{ is lush}\quad\Longleftrightarrow\quad
G\text{ is a spear operator}\quad\Longleftrightarrow\quad
G\text{ has the alternative Daugavet property}.
\]

Equivalently, the aDP/lushness/spearness part of the finite-dimensional codomain theorem remains true when only the image \(G(X)\) is finite-dimensional.

## Source Questions Addressed

The source paper says after Proposition 6.5 that it is not known whether that finite-dimensional codomain theorem, or part of it, remains true when only the range of \(G\) is finite-dimensional. Chapter 10 asks whether the rank-one results extend to finite-rank operators.

This packet proves the core equivalence between aDP, spearness, and lushness for finite-rank operators. It does not prove the finite-rank analogue of Proposition 7.8, namely that \(G^*\) must be lush.

## Idea of the Proof

The source theorem for aDP says that for each fixed \(x^*\in X^*\), a dense \(G_\delta\) set of extreme \(y^*\in B_{Y^*}\) satisfies
\[
\|G^*y^*+\mathbb T x^*\|=1+\|x^*\|.
\]
For a finite list of \(x^*\)'s, Baire gives one \(y^*\) satisfying all corresponding equations inside any prescribed weak-star slice of \(B_{Y^*}\).

The finite-rank hypothesis then turns this finite-list information into all-list information: \(G^*(B_{Y^*})\) lives in a finite-dimensional compact set. Closed subsets indexed by \(x^*\in X^*\) have the finite-intersection property, so their total intersection is nonempty. This produces, inside a near-norming weak-star slice, a functional \(y^*\) such that \(G^*y^*\in\operatorname{Spear}(X^*)\). Hence the set of such \(y^*\)'s is norming for \(Y\), and Proposition 3.32(a) of the source paper implies that \(G\) is lush.

## Relation to Earlier Lane-19 Packet

The earlier packet
`solutions/partial/1701.02977_finite_rank_adp_norm_attainment/`
proved norm-attainment for finite-rank aDP operators. The present theorem strictly strengthens it, since lush operators attain their norm by Proposition 7.9 of the source paper.

## Limitations

This does not settle whether \(G^*\) is lush for finite-rank aDP \(G\). The source paper proves that in rank one, but the dual aDP/lushness transfer for finite-dimensional range still requires a separate argument.

## Novelty Check

Cheap run indexes had no duplicate for arXiv:1701.02977 or finite-rank aDP/lushness. Local later-source checks included arXiv:2306.02645 on generating operators and arXiv:2306.02638 on numerical range methods; neither states this finite-rank aDP/lushness equivalence. Web searches on 2026-06-16 for quoted combinations of "finite-rank", "alternative Daugavet property", "finite-dimensional range", "spear operators", and "lush" returned no exact match beyond the source and broader generating-operator paper.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1701.02977.


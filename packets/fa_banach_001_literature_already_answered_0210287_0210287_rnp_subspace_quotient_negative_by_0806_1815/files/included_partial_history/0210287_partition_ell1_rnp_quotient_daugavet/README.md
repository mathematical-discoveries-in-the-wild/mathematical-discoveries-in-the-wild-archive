# Partition `ell_1` RNP subspaces give Daugavet quotients

Status: `included_partial_history`

Source paper: Vladimir Kadets, Nigel Kalton, and Dirk Werner, *Remarks on rich subspaces of Banach spaces*, arXiv:math/0210287.

Update: the full RNP-subspace question is later answered negatively by Kadets--Shepelska--Werner, *Quotients of Banach spaces with the Daugavet property*, arXiv:0806.1815. See:

```text
runs/fa_banach_001/solutions/literature_already_answered/
  0210287_rnp_subspace_quotient_negative_by_0806_1815/
```

## Result

The source asks whether `L_1/X` has the Daugavet property whenever `X subset L_1` has the Radon-Nikodym property.

This included historical subpacket proves a positive nonreflexive subcase. If `(A_n)` is a countable measurable partition of a nonatomic probability space and

```text
X = closed span { 1_{A_n} / lambda(A_n) : n in N } subset L_1,
```

then `X` is isometric to `ell_1`, hence has the Schur property and the RNP, and `L_1/X` has the Daugavet property.

The proof decomposes the quotient as an `ell_1`-sum of the finite-codimensional quotients

```text
L_1(A_n) / span{1_{A_n}},
```

each of which has the Daugavet property by the known reflexive-subspace case cited in the source paper. An elementary slice argument shows that an `ell_1`-sum of Daugavet spaces has the Daugavet property.

## Scope

This does not solve the full RNP-subspace question and does not answer whether a rich subspace of `L_1` with the Schur property exists. It gives a concrete positive Schur/RNP, nonreflexive subspace class for the quotient problem, retained here only as provenance and contrast because the full RNP quotient question is answered negatively by arXiv:0806.1815.

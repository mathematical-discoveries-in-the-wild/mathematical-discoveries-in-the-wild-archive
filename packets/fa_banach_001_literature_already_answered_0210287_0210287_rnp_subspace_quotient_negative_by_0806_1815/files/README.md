# RNP quotient Daugavet question: partial history and later negative answer

Status: `literature_already_answered`

Source/open-problem paper: Vladimir Kadets, Nigel Kalton, and Dirk Werner, *Remarks on rich subspaces of Banach spaces*, arXiv:math/0210287.

Supporting answer paper: Vladimir Kadets, Varvara Shepelska, and Dirk Werner, *Quotients of Banach spaces with the Daugavet property*, arXiv:0806.1815, Bull. Pol. Acad. Sci. 56 no. 2 (2008), 131-147.

## Identification

The source paper asks whether, for every subspace `X` of `L_1` with the Radon-Nikodym property, the quotient `L_1/X` has the Daugavet property.

The supporting paper explicitly says that this Pelczynski question, reiterated in Shvidkoy's paper and in Kadets--Kalton--Werner arXiv:math/0210287, has a negative answer. Its Corollary 6.11 states that there is a subspace `E subset L_1[0,1]` isomorphic to `ell_1`, hence with the RNP, such that `L_1[0,1]/E` fails the Daugavet property.

## Local partial history

Before the later full counterexample was identified, this run produced a positive structured subcase:

```text
included_partial_history/
  0210287_partition_ell1_rnp_quotient_daugavet/
```

That subpacket proves that if `(A_n)` is a countable measurable partition of a nonatomic probability space and

```text
X = closed span { 1_{A_n} / lambda(A_n) : n in N } subset L_1,
```

then `X` is isometric to `ell_1`, hence has the Schur property and the RNP, and `L_1/X` has the Daugavet property.

This positive partition case is now recorded only as history inside the full literature-status packet. It is subsumed as a subcase/contrast by arXiv:0806.1815: some copies of `ell_1` in `L_1` have Daugavet quotients, but another copy of `ell_1` gives a quotient that fails the Daugavet property.

## Scope

This fully answers the source's second final question negatively. It does not answer the separate source question asking whether there is a rich subspace of `L_1` with the Schur property.

The included partition subcase remains mathematically valid, but it should not be counted as a separate durable packet for the original question. The single canonical status for the RNP quotient question is this later negative literature answer.

## Files

- `source_paper.pdf`: arXiv:math/0210287.
- `supporting_paper_0806.1815.pdf`: the later negative answer paper.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
- `included_partial_history/0210287_partition_ell1_rnp_quotient_daugavet/`: the earlier local partial packet, retained as provenance and contrast.

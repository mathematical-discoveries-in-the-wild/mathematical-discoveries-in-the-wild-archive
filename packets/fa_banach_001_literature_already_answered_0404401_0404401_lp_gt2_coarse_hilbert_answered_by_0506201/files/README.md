# Literature status: `L_p`, `p > 2`, coarse embedding into Hilbert

status: literature_already_answered

source_arxiv: 0404401

supporting_arxiv: 0506201

source_problem: Nowak final remark (A), asking whether the Aharoni--Maurey--Mityagin non-embedding theorem for `L_p`, `p > 2`, has a coarse-uniform counterpart

packet_verdict: negative answer already in later literature

## Summary

In final remark (A), Nowak asks whether `L_p(mu)` admits a coarse uniform embedding into a Hilbert space for `p > 2`.

Mendel--Naor, arXiv:0506201, explicitly discuss the same coarse-embedding question for `L_p` and Hilbert space. They state that Johnson--Randrianarivony resolved it negatively for `p > 2`, and then prove the stronger metric-cotype classification: for `p,q > 0`, `L_p` embeds coarsely into `L_q` if and only if `p <= q` or `q <= p <= 2`. Taking `q=2` gives no coarse embedding `L_p -> L_2` for `p > 2`; a fortiori there is no stronger coarse uniform embedding.

## Evidence

- `source_paper.pdf`: Nowak, arXiv:0404401.
- `supporting_paper_0506201.pdf`: Mendel--Naor, arXiv:0506201.
- Source TeX location: `data/parsed/arxiv_sources/0404401/source.tex`, final remarks, lines around 528--535.
- Supporting TeX locations: `data/parsed/arxiv_sources/0506201/source.tex`, Theorem `thm:coarse` around lines 636--641 and the corollary/proof around lines 2888--2918.

## Scope

This records the standard infinite-dimensional `L_p` answer, including `L_p[0,1]` and `ell_p`. If one reads Nowak's `L_p(mu)` literally to include finite-dimensional measure spaces, those finite-dimensional spaces embed into Hilbert space after changing constants, so they are a trivial exception outside the intended coarse Banach-space phenomenon.

The supporting paper does not need a new argument from this run: it gives a stronger known classification. This packet is for duplicate avoidance and target clearing, not for counting new mathematical progress.

## Verification Notes

- Cheap-index search found no exact prior packet for arXiv:0404401 or the `L_p`, `p>2`, Hilbert coarse-embedding question.
- Local corpus search found repeated later citations to Johnson--Randrianarivony and the decisive Mendel--Naor metric-cotype classification.
- No external novelty search was needed for a new proof claim, because this is explicitly a literature-status packet.

Human-review recommendation: accept as a lightweight literature-already-answered packet, with the finite-dimensional caveat preserved.


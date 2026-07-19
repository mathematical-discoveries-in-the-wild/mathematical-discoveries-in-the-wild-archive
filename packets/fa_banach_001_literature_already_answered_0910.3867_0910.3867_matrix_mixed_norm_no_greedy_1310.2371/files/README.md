# 0910.3867 mixed-norm matrix greedy-basis problem

Status: `literature_already_answered`.

Source paper: S. J. Dilworth, D. Freeman, E. Odell, and Th. Schlumprecht,
*Greedy bases for Besov spaces*, arXiv:0910.3867.

Source question: after Theorem 2a in the introduction, the paper asks whether,
for `1 < p != q < infinity`, the mixed-norm matrix space
`ell_q(ell_p) = (oplus ell_p)_{ell_q}` has a greedy basis.

Supporting answer: Gideon Schechtman, *No greedy bases for matrix spaces with
mixed ell_p and ell_q norms*, arXiv:1310.2371.

Schechtman's introduction explicitly cites the Dilworth--Freeman--Odell--
Schlumprecht question and states that the spaces
`(oplus_{n=1}^\infty ell_p)_{ell_q}` have no greedy basis for
`1 <= p != q < infinity`. Theorem 1 proves the stronger structural statement
that every normalized unconditional basis contains both an `ell_p` subsequence
and an `ell_q` subsequence; by Konyagin--Temlyakov, this prevents democracy
and hence prevents greediness when `p != q`.

Scope: this fully answers the source problem negatively in its stated
reflexive range `1 < p != q < infinity`. The supporting paper also treats
additional non-reflexive mixed `c_0` endpoint variants, which are beyond the
source question recorded here.

Packet contents:

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:0910.3867.
- `supporting_paper_1310.2371.pdf`: arXiv:1310.2371.

Ledger:
`runs/fa_banach_001/ledger/results/0910.3867_matrix_mixed_norm_no_greedy_1310.2371.json`.

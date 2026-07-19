# Literature-implied partial answer: upward LPR exponent implication

Status: `literature_implied_answer (partial direction)`.

Source question: T. P. Hytönen, J. L. Torrea, and D. V. Yakubovich,
*The Littlewood--Paley--Rubio de Francia property of a Banach space for the
case of equal intervals*, arXiv:0807.2981.  In the introduction, after
recording that `LPR_p` implies UMD and type 2, the paper says that it is not
known whether there is an implication between `LPR_p` and `LPR_q` for two
different exponents `p,q in [2,infty)`.

Supporting paper: Denis Potapov, Fedor Sukochev, and Quanhua Xu,
*On the vector-valued Littlewood-Paley-Rubio de Francia inequality*,
arXiv:1104.2671.

Identification: Potapov--Sukochev--Xu explicitly revisit the vector-valued
`LPR_p` property, cite the Hytönen--Torrea--Yakubovich necessary condition,
and state that `p`-independence is unknown.  Their Theorem 3.1 proves one
direction: if a Banach space `X` has `LPR_q` for some `2 <= q < infinity`,
then `X` has `LPR_p` for every `q <= p < infinity`.  Thus the source's
two-exponent question has a positive upward implication.

Scope: this is not a full solution of the source's broad exponent-independence
problem.  The downward implication from `LPR_p` to smaller exponents remains
unsettled in this packet, and so does the larger converse problem asking
whether UMD plus type 2 implies arbitrary-interval `LPR_p`.  An existing run
attempt, `attempts/1104.2671_lpr_umd_type2_bootstrap_barrier.md`, records a
failed direct push on the equal-interval-to-arbitrary-interval bootstrap.

Files:

- `source_paper.pdf`: arXiv:0807.2981.
- `supporting_paper_1104.2671.pdf`: arXiv:1104.2671.
- `solution_packet.pdf`: compact status note.

# Partial solution packet: topologically principal twisted `RD_p` implies ordinary `RD_p`

Status: partial result, likely valid.

Source/open-problem paper: Are Austad, Eduard Ortega, and Mathias Palmstrom,
*Polynomial growth and property `RD_p` for etale groupoids with applications to
`K`-theory*, arXiv:2304.14458.

Source question addressed: Appendix A asks whether `sigma`-twisted property
`RD_p`, for a continuous 2-cocycle `sigma` not cohomologous to the trivial
cocycle, implies ordinary property `RD_p`.

Result: yes for two important families. If `1 < p < infinity` and either

1. the groupoid is principal with continuous length, or
2. the groupoid is sigma-compact and topologically principal with continuous
   proper length,

then `sigma`-twisted `RD_p` with respect to `l` forces polynomial growth with
respect to `l`; by the source paper's polynomial-growth theorem it therefore
has ordinary `RD_p`. For `p=1`, ordinary `RD_1` is automatic for every etale
groupoid.

Main input: Weygandt, *Rapid Decay for Principal Etale Groupoids*,
arXiv:2304.12262, proves the analogous twisted `C^*`/`p=2` obstruction. The
packet adapts the finite-ball obstruction to `ell^p`: the test vector
`|F|^{-1/p} chi_F` still gives twisted operator norm at least `|F|`, while the
weighted `I^p` norm of the constructed test function is at most
`|F|^{1/p}(1+O(R))^k`.

Full-result barrier: for arbitrary groupoids the question contains Chatterji's
2006 open group question as the one-unit groupoid case: can a finitely generated
group fail ordinary RD but have `sigma`-twisted RD for some multiplier? No
answer to that group question was found in the bounded search.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2304.14458.
- `supporting_paper_2304.12262.pdf`: arXiv:2304.12262.
- `supporting_paper_math0606790.pdf`: Mathai with Chatterji appendix,
  arXiv:math/0606790.

Limitations: this does not answer the source question for arbitrary
non-topologically-principal etale groupoids, and in particular does not solve
the one-unit group case. It also does not address whether twisted `RD_p` alone
makes the twisted Schwartz space a Frechet algebra without ordinary `RD_p`; in
the covered cases the result supplies ordinary `RD_p`, so the source's existing
arguments apply.

Review recommendation: human review should check the local-bisection
construction and the `I^p` source/range fiber count, but the proof is a direct
`L^p` adaptation of Weygandt's Lemma 3.1 and Theorem 3.3.

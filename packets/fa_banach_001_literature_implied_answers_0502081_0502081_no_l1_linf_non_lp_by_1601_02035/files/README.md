# Literature-Implied Answer: No-`ell_1` `L_\infty` Space Not `LP`

- Source paper: J. M. F. Castillo, Y. Moreno, J. Suarez, *On Lindenstrauss-Pelczynski spaces*, arXiv:math/0502081.
- Supporting paper: J. M. F. Castillo and P. L. Papini, *On isomorphically polyhedral `L_\infty`-spaces*, arXiv:1601.02035.
- Status: `literature_implied_answer (negative answer to the no-ell_1 L_infty/non-LP subquestion)`.
- Packet path: `runs/fa_banach_001/solutions/literature_implied_answers/0502081_no_l1_linf_non_lp_by_1601_02035/`.

## Identification

In Section 4 of arXiv:math/0502081, after producing `LP` spaces not containing
`ell_1`, the authors write that they do not know whether there exist
`L_\infty` spaces not containing `ell_1` which are not `LP` spaces.

The later paper arXiv:1601.02035 proves that there is an isomorphically
polyhedral `L_\infty` space which is not a Lindenstrauss-Pelczynski (`LP`)
space. In the proof, the space is obtained in an exact sequence

```text
0 -> C(omega^omega) -> Omega_H -> c_0 -> 0.
```

Both `C(omega^omega)` and `c_0` contain no copy of `ell_1`, and the property of
containing no `ell_1` is a three-space property. Hence `Omega_H` contains no
`ell_1`. This gives a negative answer to the no-`ell_1` `L_\infty`/non-`LP`
subquestion from arXiv:math/0502081.

## Scope

This packet does not answer the source paper's later Section 5 quotient
questions: whether quotients of two `LP` spaces are `LP`, whether
`ell_\infty/C[0,1]` is `LP`, or whether operators from subspaces of
`c_0(Gamma)` into `LP` spaces extend to `c_0(Gamma)`.

The implication appears to be agent-identified: arXiv:1601.02035 cites the
source paper and constructs the required example, but does not explicitly say
that it is answering the exact no-`ell_1` sentence in arXiv:math/0502081.

## Files

- `source_paper.pdf`: original source paper, arXiv:math/0502081.
- `supporting_paper_1601.02035.pdf`: supporting paper, arXiv:1601.02035.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered compact status note.


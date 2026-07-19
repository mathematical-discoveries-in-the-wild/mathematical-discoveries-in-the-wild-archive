# Literature status: dual ASQ spaces are not all UASQ

Status: `literature_already_answered`

Source paper: Luis Garcia-Lirola and Abraham Rueda Zoca,
*Unconditional almost squareness and applications to spaces of Lipschitz
functions*, arXiv:1605.04699.

## Source Question

In Section 6, Question 6.1 (`UASQASQequivalent` in the arXiv source), the
authors ask:

> Are UASQ and ASQ equivalent, at least, for dual Banach spaces?

The same paper proves that no dual Banach space is UASQ. Therefore the source
question is equivalent to asking whether dual ASQ Banach spaces exist.

## Supporting Answer

Supporting paper: Trond A. Abrahamsen, Petr Hajek, and Stanimir Troyanski,
*Almost square dual Banach spaces*, arXiv:1912.12519.

The supporting paper explicitly discusses this question. In its introduction it
says that `1605.04699` asks whether ASQ spaces can be dual, and later states
that Question 6.1 from the ASQ/UASQ literature asked whether dual ASQ spaces
are UASQ; the authors write that their construction of a dual ASQ space answers
this in the negative. The decisive theorem is Theorem 3.7
(`dual-c0-asq-renorming` in the source): a dual Banach space admits a dual ASQ
norm if and only if it contains an isomorphic copy of `c_0`.

Combined with Theorem 2.5 of `1605.04699` ("no dual UASQ Banach space"), this
gives a negative answer to the source question: dual ASQ and UASQ are not
equivalent.

## Scope

This packet records only the first open question from `1605.04699`, Section 6.
It does not classify the paper's later questions about uniformly discrete
metric spaces `M` with `Lip(M)` ASQ, or about whether `S(M,X)` can be
isomorphic to a dual space.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: local render of arXiv:1605.04699 from source TeX.
- `supporting_paper_1912.12519.pdf`: supporting answer paper.

Ledger record:
`runs/fa_banach_001/ledger/results/1605.04699_dual_asq_not_uasq_1912.12519.json`

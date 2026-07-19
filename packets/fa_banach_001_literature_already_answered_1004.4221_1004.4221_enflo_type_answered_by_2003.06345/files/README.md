# Enflo type question answered by Ivanisvili--van Handel--Volberg

Status: literature_already_answered.

Source/open-problem paper:
Ohad Giladi and Assaf Naor, *Improved bounds in the scaled Enflo type
inequality for Banach spaces*, arXiv:1004.4221.

Duplicate source occurrence:
Mendel and Naor, *Scaled Enflo type is equivalent to Rademacher type*,
arXiv:0506215, recalls the same Enflo problem and separately asks whether
scaled Enflo type `p` implies Enflo type `p`.

Supporting answer paper:
Paata Ivanisvili, Ramon van Handel, and Alexander Volberg,
*Rademacher type and Enflo type coincide*, arXiv:2003.06345.

## Identification

The source introduction recalls Enflo's open problem: whether, for Banach
spaces, Rademacher type `p` implies Enflo type `p`. The source notes that the
reverse implication is immediate and that the endpoint implication was open
outside known classes such as UMD spaces.

The supporting paper explicitly settles this question. Its abstract says that
Rademacher type and Enflo type coincide, and Theorem 1.1 gives the quantitative
comparison

```text
T_p^R(X) <= T_p^E(X) <= (pi/sqrt(2)) T_p^R(X)
```

for every Banach space `X` and every `p in [1,2]`.

This also answers the Enflo-problem occurrence in arXiv:0506215. It does not
answer the separate metric-space question in arXiv:0506215 asking whether
scaled Enflo type `p` implies Enflo type `p` outside the Banach-space
endpoint consequence.

## Scope

This is a full literature answer to the open-problem signal in arXiv:1004.4221:
the endpoint Enflo/Rademacher type equivalence for Banach spaces. It also
covers the same classical Enflo-problem signal in arXiv:0506215. It does not
claim a new proof by this run, and it does not address unrelated optimization
questions about the smallest scale `m` in scaled Enflo type inequalities or
the general metric implication from scaled Enflo type to Enflo type.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1004.4221.
- `supporting_paper_2003.06345.pdf`: arXiv:2003.06345.

Ledger record:
`runs/fa_banach_001/ledger/results/1004.4221_enflo_type_answered_by_2003.06345.json`.

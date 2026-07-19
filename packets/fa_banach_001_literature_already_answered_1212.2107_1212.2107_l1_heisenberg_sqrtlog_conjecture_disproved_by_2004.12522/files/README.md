# Literature status: 3D Heisenberg \(L_1\) distortion conjecture

Status: `literature_already_answered`

Source/open-problem paper: Vincent Lafforgue and Assaf Naor,
*Vertical versus horizontal Poincaré inequalities on the Heisenberg group*,
arXiv:1212.2107.

Supporting answer paper: Assaf Naor and Robert Young,
*Foliated corona decompositions*, arXiv:2004.12522.

## Question Identified

Section 4 of arXiv:1212.2107 asks whether an endpoint \(p=1\)
vertical-versus-horizontal inequality holds for real-valued functions on the
3-dimensional Heisenberg group. It reformulates this as an isoperimetric
question and then states Conjecture 4.4:

```tex
c_1(B_n,d_W) \asymp \sqrt{\log n}
```

for word balls \(B_n\) in the discrete 3-dimensional Heisenberg group.

## Answer Located

Naor--Young, arXiv:2004.12522, explicitly says that earlier references,
including Lafforgue--Naor, conjectured
\(c_{\ell_1}(\mathcal B_n)\asymp \sqrt{\log n}\). Its Theorem 1.6 proves the
sharp asymptotic

```tex
c_{\ell_1}(\mathcal B_n) \asymp \sqrt[4]{\log n}
```

for every integer \(n\ge 2\) in the discrete 3-dimensional Heisenberg group.
This disproves Conjecture 4.4 as stated and rules out the chain of implications
from the endpoint/isoperimetric questions to \(\sqrt{\log n}\) distortion.

## Scope Notes

This packet concerns the 3-dimensional Heisenberg group of arXiv:1212.2107.
Naor--Young emphasize that the 5-dimensional Heisenberg group has different
\(L_1\) distortion behavior of order \(\sqrt{\log n}\); that contrast is part
of the supporting paper's conclusion and does not rescue the 3-dimensional
conjecture.

Local files:

- `source_paper.pdf`: arXiv:1212.2107.
- `supporting_paper_2004.12522.pdf`: arXiv:2004.12522.
- `main.tex` / `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/1212.2107_l1_heisenberg_sqrtlog_conjecture_disproved_by_2004.12522.json`.

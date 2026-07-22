# Literature-implied answer: BFU is not a three-space property

Status: `literature_implied_answer` (full negative answer).

## Source question

Boris Burshteyn, *Uniform λ-Adjustment and μ-Approximation in Banach
Spaces*, arXiv:0804.2832, Section 6, “Open Problems” (p. 89), asks whether
being a BFU-space is a three-space property. Here BFU means that every
norm-bounded subset of the dual is Fréchet--Urysohn in the weak-star
topology; this is the standard property of having weak-star angelic dual.

## Later theorem implying a negative answer

Gonzalo Martínez-Cervantes, *Banach spaces with weak*-sequential dual
ball*, arXiv:1612.05948, supplies the Johnson--Lindenstrauss space `JL_2`.
Theorem 4 states that its weak-star dual ball has sequential order exactly
2, and the proof records

\[
  JL_2/c_0 \cong \ell_2(\Gamma),
  \qquad JL_2\text{ does not have weak-star angelic dual.}
\]

Thus in the exact sequence

\[
  0\longrightarrow c_0\longrightarrow JL_2
   \longrightarrow \ell_2(\Gamma)\longrightarrow 0,
\]

the subspace `c_0` is BFU because it is separable, and the quotient is BFU
because it is reflexive, while the middle space is not BFU. Therefore BFU
is not a three-space property.

The supporting paper does not cite or identify Burshteyn's open problem,
so this belongs in `literature_implied_answers`, not
`literature_already_answered`. No new mathematical result is claimed.

## Files

- `main.tex`, `solution_packet.pdf`: compact implication note.
- `source_paper.pdf`: arXiv:0804.2832.
- `supporting_paper_1612.05948.pdf`: the supporting paper.
- Ledger: `runs/fa_banach_001/ledger/results/0804.2832_bfu_not_three_space_via_jl2_1612.05948.json`.


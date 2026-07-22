# Literature-implied answer: the Continuous Kraus Conjecture

status: literature_implied_answer (full, with the arbitrary-measure formulation obtained by the same POVM proof)

source: K. Mahesh Krishna, *Continuous Deutsch Uncertainty Principle and
Continuous Kraus Conjecture*, arXiv:2310.01450, Conjecture 2.5 on PDF page 4.

decisive supporting theorem: Michel Rumin, *An entropic uncertainty principle
for positive operator valued measures*, arXiv:1109.5889, Theorem 1.1 on PDF
page 2.

independent finite-measure confirmation: K. Mahesh Krishna, *Continuous
Krishna-Parthasarathy Entropic Uncertainty Principle*, arXiv:2405.08003,
Theorem 2.4 on PDF page 3.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/2310.01450_continuous_kraus_via_povm_entropy/`

ledger: `runs/fa_banach_001/ledger/results/2310.01450_continuous_kraus_via_povm_entropy.json`

## Identification

For a continuous Parseval frame, integration of the rank-one operators
`|tau_alpha><tau_alpha|` gives a positive operator-valued measure (POVM). For
two frames, the associated Liouville density is
`|<tau_alpha,omega_beta>|^2`. If `c` is the supremum of the cross-frame
overlaps, this density is bounded by `c^2` times the product reference
measure. Scaling each reference measure by `c` makes Rumin's POVM theorem
apply to the pure state determined by `h`; its two relative entropies are
exactly `S_tau(h)+log(c)` and `S_omega(h)+log(c)`. Since a pure state's von
Neumann entropy is zero, Rumin's inequality becomes

`S_tau(h)+S_omega(h) >= -2 log(c)`,

which is Conjecture 2.5 verbatim.

Rumin states his theorem for sigma-finite product reference measures. The
compact note in `main.tex` records the corresponding rank-one POVM proof for
the source paper's unrestricted measure-space wording. It uses only the two
explicit density functions and iterated positive integrals, so the
sigma-finiteness step used by Rumin to obtain Radon-Nikodym densities is not
needed here.

## Literature status

This is not a new core uncertainty theorem. Rumin's 2011 theorem predates the
2023 conjecture and implies it after the rank-one POVM identification above.
The supporting author therefore could not have known he was answering the
later conjecture. Krishna's 2024 Theorem 2.4 gives an independent direct
Riesz-Thorin proof for finite measure spaces, but that paper does not cite or
explicitly identify Conjecture 2.5. The relation is therefore
agent-identified and belongs in `literature_implied_answers`, not
`literature_already_answered` or `solutions/full`.

## Scope

The entropy inequality in the Continuous Kraus Conjecture is fully resolved.
The separate equality-characterization Question 2.4 in arXiv:2310.01450 is
not answered here.

## Files

- `main.tex`: compact identification and specialization proof.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2310.01450.
- `supporting_paper_1109.5889.pdf`: Rumin's decisive POVM theorem.
- `supporting_paper_2405.08003.pdf`: independent finite-measure confirmation.


# Junge-Ruan answers the finite-p Lp Schauder-basis subcase

Status: `literature_implied_answer (finite-p noncommutative Lp subcase)`.

Source/open-problem signal: arXiv:2103.04368, Tao Mei, Eric Ricard, and
Quanhua Xu, *A Hormander-Mikhlin multiplier theory for free groups and
amalgamated free products of von Neumann algebras*.

## Identification

The source introduction says that better non-radial multiplier understanding is
needed for fundamental open questions, including construction of Schauder bases
for free group reduced C*-algebras and the corresponding noncommutative
`L_p`-spaces.

The finite-`p` noncommutative `L_p` part is already answered after a direct
identification with Junge-Ruan's theorem:

M. Junge and Z.-J. Ruan, *Approximation properties for noncommutative
`L_p`-spaces associated with discrete groups*, Duke Math. J. 117 (2003),
313-341.

Their abstract/theorem states that if `G` is a countable discrete group with the
Haagerup-Kraus approximation property and `VN(G)` has QWEP, then
`L_p(VN(G))`, `1<p<infty`, is a `COL_p` space and has a completely bounded
Schauder basis.  Free groups are countable and have the approximation property;
they are residually finite, hence hyperlinear, and the source itself records
the equivalence between hyperlinearity of `Gamma` and QWEP of `VN(Gamma)`.
Thus `L_p(VN(F_n))` and `L_p(VN(F_infty))` have completely bounded Schauder
bases for every `1<p<infty`.

## Scope

This is not a new proof and not a full answer to the source footnote.  It does
not answer:

- the reduced C*-algebra basis problem;
- the endpoint/von Neumann algebra case `p=infty`;
- whether the canonical group elements, or a basis produced by the source's
  non-radial multipliers, form a Schauder basis;
- sharper unconditional, metric, or multiplier-compatible basis questions.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: local build of arXiv:2103.04368 from parsed source.
- `figures/open_problem_crop.png`: crop of the source footnote/open signal.
- `supporting_paper_junge_ruan_2003_metadata.md`: supporting bibliographic
  metadata and source links; no open local supporting PDF was available in the
  workspace.

## Search Evidence

Cheap run indexes were searched for `2103.04368`, the paper title,
`Schauder basis`, `free group reduced C*`, `noncommutative L_p`, `QWEP`,
`Junge Ruan`, and `completely bounded Schauder basis`; no exact prior packet
was found.  Web searches on 2026-07-18 found public metadata/abstract pages for
Junge-Ruan's Duke Math. J. paper and references listing the exact publication
data.

Human review should confirm the QWEP/free-group implication if this packet is
used beyond duplicate-memory triage.

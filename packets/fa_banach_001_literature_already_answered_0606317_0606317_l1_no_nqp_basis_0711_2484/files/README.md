# Literature Status: ell_1 Has No Semi-normalized NQP Basis

Status: `literature_already_answered (basis subquestion)`

## Source Question

- Source paper: S. J. Dilworth, E. Odell, Th. Schlumprecht, and Andras Zsak,
  "Coefficient Quantization in Banach Spaces", arXiv:math/0606317.
- Location: Section 5, PDF page 21. The arXiv PDF labels the question as
  Problem 5.17.
- Question: Does `ell_1` have an NQP basis, respectively an NQP minimal
  system?

## Supporting Answer

- Supporting paper: P. G. Casazza, S. J. Dilworth, E. Odell,
  Th. Schlumprecht, and A. Zsak, "Coefficient Quantization for Frames in
  Banach Spaces", arXiv:0711.2484.
- Location: Section 5, Corollary 5.15, PDF page 30.
- Answer: No for the semi-normalized basis version. Corollary 5.15 proves
  that no infinite-dimensional Banach space with nontrivial cotype has a
  semi-normalized basis with the NQP, and explicitly adds that this answers
  the `ell_1` question from the 2006 paper. Since `ell_1` has nontrivial
  cotype, it has no semi-normalized NQP basis.

## Scope

This packet records an already-known literature answer, not a new proof from
the run. It covers the `ell_1` semi-normalized basis subquestion. It does not
claim the minimal-system part of the source question, nor does it settle the
broader source problem asking whether every Banach space with an NQP basis
contains `c_0`.

There is a numbering mismatch worth preserving: the source arXiv PDF labels
the `ell_1` question as Problem 5.17, while the supporting paper cites
"Problem 5.18 in [DOSZ]". The wording and citation context identify the same
question.

## Files

- `source_paper.pdf`: arXiv:math/0606317.
- `supporting_paper_0711.2484.pdf`: arXiv:0711.2484.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Search Notes

Cheap run indexes had no previous packet or attempt for arXiv:math/0606317,
the `ell_1` NQP-basis question, or arXiv:0711.2484. A phrase search for
"Net Quantization Property" and "Does ell_1 have an NQP basis" found the
frame follow-up, and the local TeX/PDF source verifies the explicit answer.

Ledger record:
`runs/fa_banach_001/ledger/results/0606317_l1_no_nqp_basis_0711_2484.json`.

## Review Recommendation

Treat the semi-normalized NQP-basis version for `ell_1` as answered
negatively by arXiv:0711.2484. Keep the minimal-system part and the broad
NQP-basis-implies-`c_0` problem open for future work.


# Candidate Full Solution: `ell_1` Copies for Holomorphic-Lipschitz Linearizations

Run: `fa_banach_001`

Source paper: Verónica Dimant, Luis C. García-Lirola, Juan Guerrero-Viu,
Antonín Procházka, "Composition operators for holomorphic Lipschitz
functions", arXiv:2605.21279.

Target: Remark 4.21 on page 25.

Status: candidate full affirmative answer to the question as stated.

## Claim

Remark 4.21 asks whether, if the linearization `\widehat{\phi}` fixes a copy
of `ell_1`, it must fix a complemented copy of `ell_1`.

Yes. In fact, this is not special to holomorphic-Lipschitz linearizations:
every bounded linear operator that fixes a copy of `ell_1` fixes a
complemented copy of `ell_1`. The proof combines the elementary adjoint
lifting from a fixed `ell_1` copy to a fixed `c_0` copy of the adjoint with
Lemma 2.5 of the source paper.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop of Remark 4.21 and the
  question.
- `main.tex`: human-readable proof packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates and rendered page images only.

## Verification Notes

- No computational verification was needed.
- Main verifier focus: check the adjoint step
  `(TA)^*:X^* -> ell_infty` splits by injectivity of `ell_infty`, so `T^*`
  fixes `c_0`.
- Then Lemma 2.5 of arXiv:2605.21279 applies directly and yields a
  complemented `ell_1` copy for `T`.

## Human Review Recommendation

Review as a short general-operator argument. The conclusion appears stronger
than the source-paper question: it answers the exact `\widehat{\phi}` question
without using any special structure of holomorphic-Lipschitz free spaces.

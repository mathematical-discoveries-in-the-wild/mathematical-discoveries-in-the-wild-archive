# Salem spectral-modulus question: scoped later-literature answers

Status: `literature_already_answered (partial subcases; exact log-Hölder bound remains open)`

## Original source

- Boris Bufetov and Boris Solomyak, *On the modulus of continuity for spectral
  measures in substitution dynamics*, arXiv:1305.7373.
- The live boundary appears on page 15 in Section 4 after Theorem 4.1
  (almost-every roof Hölder continuity) and on page 26 in Section 5,
  Remark 5.3 immediately after Theorem 5.1 and equation (5.1)
  (self-similar log-Hölder continuity).

## Separate supporting papers

- Juan Marshall-Maldonado, *Modulus of continuity for spectral measures of
  suspension flows over Salem type substitutions*, arXiv:2009.13607v2,
  Theorems 1.1--1.2 (pages 2--3).  This paper explicitly says that its main objective is the
  Salem question raised by Bufetov--Solomyak and proves pointwise Hölder bounds
  at algebraic spectral parameters.
- Juan Marshall-Maldonado and Boris Solomyak, *Quantitative weak mixing for
  typical Salem substitution suspension flows*, arXiv:2601.15035,
  Theorems 2.3, 2.4 (pages 6--7), and A.2 (page 18).  It proves an almost-every-roof uniform
  sub-Hölder modulus, impossibility of a uniform Hölder rate for every roof,
  and a uniform `exp(-c log*(1/r))` modulus for the self-similar roof.

## Identification

The supporting authors explicitly identify the same Salem boundary and cite
the 2014 source.  These are therefore literature-already-answered subcases,
not new deductions from unrelated theorems.

The exact estimate asked after source Theorem 5.1,

`sigma_a([omega-r,omega+r]) <= C_B (log(1/r))^{-gamma}`

uniformly for `|omega| in [B^{-1},B]`, is stronger than the 2026 log-star
bound and remains open.  The 2026 paper itself says a log-Hölder rate seems
plausible but is not proved.

## Files

- `solution_packet.pdf`: compact theorem-by-theorem status note.
- `source_paper.pdf`: arXiv:1305.7373.
- `supporting_paper_2009.13607.pdf`: algebraic-frequency Hölder result.
- `supporting_paper_2601.15035.pdf`: current uniform Salem rates.
- Attempt record:
  `attempts/1305.7373_salem_log_holder_boundary_attempt.md`.
- Ledger:
  `ledger/results/1305.7373_salem_spectral_modulus_partial_literature_answers.json`.

## Review recommendation

Verify the quantifiers: the 2024 Hölder estimate is pointwise in algebraic
frequency; the 2026 self-similar estimate is uniform but only log-star.  The
packet deliberately does not claim that either settles the original
power-log estimate.

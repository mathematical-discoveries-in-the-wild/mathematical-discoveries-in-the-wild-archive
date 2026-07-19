# Corrected Partial/Audit Packet: Hereditary Failure of UALS

Source paper: S. A. Argyros, A. Georgiou, A.-R. Lagos, and Pavlos Motakis,
*Joint spreading models and uniform approximation of bounded operators*,
arXiv:1712.07638.

Result type: `partial` / audit-corrected reduction

Status: corrected partial result, likely valid, pending human review.

## Source Problem

Problem 2 asks whether there is a Banach space none of whose subspaces satisfies
the UALS property.

## Audit Outcome

The previous active packet claimed that, over complex scalars, any Banach
space with no unconditional basic sequence contains a subspace satisfying UALS,
and therefore that any hereditary non-UALS counterexample must be
unconditionally saturated.

The supplied audit shows this claim is not proved. The gap is the implication

```text
UALS-saturated => UALS
```

The source theorem gives UALS-saturation for scalar-plus-strictly-singular
spaces, but UALS requires a finite-codimensional subspace; saturation only
produces a further infinite-dimensional subspace.

## Corrected Contribution

The active packet now records the rigorous salvage:

- If a complex Banach space contains no unconditional basic sequence, then it
  contains a complex HI subspace all of whose subspaces are UALS-saturated.
- A hypothetical complex space whose every subspace fails UALS has a subspace
  in one of two regimes: a reflexive unconditional-basis regime with hereditary
  UALS failure, or an HI regime with hereditary UALS failure but hereditary
  UALS-saturation.
- UALS failure passes upward from complemented subspaces.
- A complementably minimal non-UALS space would solve Problem 2.
- A uniform complemented bad-pair criterion is sufficient for a full
  counterexample.
- Schlumprecht-type and complete-separation candidate routes are examined, but
  no full counterexample is obtained.

## What Remains Open

Problem 2 remains open. The packet does not prove a full counterexample and
does not prove that hereditary UALS failure forces unconditional saturation.

## History And Evidence

- `history/2026_06_22_pre_audit/`: previous active packet whose advertised
  partial theorem is invalidated by the audit.
- `evidence/2026_06_22_uals_research_note/`: supplied TeX and PDF audit used
  for this update.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: crop of source Problem 2.
- `supporting_paper_math_9502207.pdf`: Ferenczi operator theorem support.
- `supporting_paper_2106.10728.pdf`: modern Gowers dichotomy support.
- `main.tex`: corrected packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Human Review

Recommended checks: the UALS versus UALS-saturation quantifier distinction,
the corrected use of Ferenczi plus Gowers, and the uniform complemented
bad-pair criterion.

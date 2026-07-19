# Stronger partial packet for Kurka's `c0 + X` Borel question

Source: Ondrej Kurka, *The isomorphism class of c0 is not Borel*,
arXiv:1711.03328.

Status: `strong_partial_likely_valid_consolidated`.

This is the single active packet for the arXiv:1711.03328 `c0 + X` Borel
question. It remains a partial result: it does not construct a Borel positive
example and does not prove that no such example exists. It does, however,
strengthen the previous packet and corrects a substantive route error.

## Main Additions

- Verifies the Sobczyk--Kurka reduction: Kurka's question is equivalent to
  asking whether some separable Banach space containing `c0` has a Borel
  isomorphism class.
- Sharpens quotient persistence: if a Borel positive example `Y` exists, then
  for every copy `E ~= c0` in `Y`, the quotient `Y/E` is isomorphic to `Y`.
- Adds restricted automorphy: every isomorphism between two copies of `c0` in
  a Borel positive example extends to an automorphism of the whole space.
- Keeps the unconditional-embedding exclusion: no positive example can embed
  into a space with an unconditional basis.
- Corrects the previous paving route: a space determined by its pavings has
  nontrivial type, hence cannot contain `c0`; pavings are an exclusion, not an
  entry point.
- Refines the CDDK barrier: in the Cuth--Dolezal--Doucha--Kurka codings, a
  positive example must be either the Gurarii Borel problem or a meager Borel
  non-`F_sigma` class.
- Sharpens the Kurka Bourgain--Delbaen absorption obstruction: any Borel
  positive example must absorb a properly coanalytic finite-only parameter
  family, with unbounded Cantor--Bendixson rank below `omega_1`.

## Remaining Open Core

The remaining question is still Kurka's original one in reduced form:

```text
Does there exist a separable Banach space containing c0 whose isomorphism
class is Borel?
```

The packet gives strong necessary conditions for such a space, but no
contradiction and no explicit example.

## Files

- `main.tex`: stronger partial packet source.
- `solution_packet.pdf`: compiled 9-page packet.
- `source_paper.pdf`: local copy of arXiv:1711.03328.
- `figures/open_problem_crop.png`: source-paper screenshot containing the
  `c0 + X` question and Theorem 1.2.
- `evidence/supplied_report_2026_06_18/`: supplied report TeX/PDF from the
  external agent.
- `history/previous_packet_2026_06_18/`: previous active packet, preserved for
  provenance.

## Human Review Recommendation

Review the Sobczyk absorption step, the quotient self-similarity proof, the
automorphism-extension corollary, the use of Johnson--Lindenstrauss--Schechtman
to rule out paving-determined `c0`-containing spaces, and the descriptive-set
theory in the properly coanalytic absorption-excess and rank-unboundedness
arguments.

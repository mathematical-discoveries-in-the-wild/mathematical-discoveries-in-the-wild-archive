# Literature-Already-Answered Packet: absolute no-uncountable-equilateral example

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: later literature gives a ZFC example. This packet records a
literature-status match, not an original proof from the run.

## Original Problem Source

- Piotr Koszmider, *Uncountable equilateral sets in Banach spaces of the form
  C(K)*, arXiv:1503.06356.
- Local PDF: `source_paper.pdf`.

The abstract and introduction ask whether there is an absolute example of a
nonseparable Banach space with no uncountable equilateral set. The paper itself
constructs only consistent `C(K)` examples and notes that under other axioms
all nonseparable `C(K)` spaces have uncountable equilateral sets.

## Supporting Answer Source

- Piotr Koszmider, *Banach spaces in which large subsets of spheres
  concentrate*, arXiv:2104.05335.
- Local PDF: `supporting_paper_2104.05335.pdf`.

## Status Match

The supporting paper proves in ZFC that there is a strictly convex Banach
space of density continuum with no uncountable equilateral set. It derives this
from the stronger sphere-concentration theorem and explicitly contrasts the
result with the earlier consistent `C(K)` examples from arXiv:1503.06356.

This answers the general absolute-example part of the 2015 open discussion.
It does not answer the sharper `C(K)`-absolute question, and it does not
produce a space whose every equivalent renorming lacks uncountable equilateral
sets.

## Verification Notes

- Same-paper check: arXiv:1503.06356 does not give a ZFC example; it gives
  consistent `C(K)` examples and an opposite consistency theorem under
  Martin's axiom plus not-CH.
- Separate-source check: arXiv:2104.05335 is a later, separate paper.
- Exact implication: the supporting paper includes Theorem 2, stating directly
  that there is a strictly convex Banach space of density continuum with no
  uncountable equilateral set. It also explains the standard reduction from an
  arbitrary equilateral set to a unit-sphere `1`-equilateral set.

## Search Bounds

- Searched the run lightweight indexes for `1503.06356`, `uncountable
  equilateral`, `C(K)`, `renorming`, and `Kottman`.
- Inspected arXiv:1503.06356 source around the abstract and introduction.
- Reused the existing run packet for arXiv:1803.11501 / arXiv:2104.05335 as a
  pointer to the later Koszmider theorem, then checked arXiv:2104.05335
  directly for the equilateral consequence and citation of arXiv:1503.06356.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2104.05335.pdf`: later answer source.

## Human Review Recommendation

Verify the scope distinction:

1. arXiv:1503.06356 asks for an absolute nonseparable Banach-space example
   with no uncountable equilateral set.
2. arXiv:2104.05335 proves such an example in ZFC.
3. The remaining `C(K)`-specific absolute and all-renormings variants are not
   claimed solved by this packet.

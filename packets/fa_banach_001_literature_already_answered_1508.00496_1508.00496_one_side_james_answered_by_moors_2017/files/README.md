# Literature-Already-Answered Packet: One-Sided James Theorem

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- B. Cascales, J. Orihuela, and A. Perez,
  *One-sided James' compactness theorem*, arXiv:1508.00496;
  published in *Journal of Mathematical Analysis and Applications* 445(2),
  1267-1283, 2017, DOI: `10.1016/j.jmaa.2016.03.080`.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_question_crop.png`.

The source paper proves the one-sided James compactness theorem under the
additional assumption that `(B_{E^*}, w^*)` is convex block compact. Its final
remarks ask whether Theorems 2 and 10 remain true for arbitrary Banach spaces.

## Supporting Answer Sources

- J. Orihuela, *Conic James' compactness theorem*, arXiv:1610.02763.
  Local PDF: `supporting_paper_1610.02763.pdf`.
- Warren B. Moors, *On a one-sided James' theorem*,
  *Journal of Mathematical Analysis and Applications* 449(1), 528-530,
  2017, DOI: `10.1016/j.jmaa.2016.12.019`.
  Local metadata: `supporting_paper_moors_2017_crossref.json`.

Orihuela's later conic James paper settles the source paper's Theorem 10
direction for arbitrary Banach spaces and records that Theorem 2 remained open
at that stage. Moors's 2017 note then proves the arbitrary-Banach-space
version of the one-sided theorem corresponding to the remaining Theorem 2
question.

## Status

The original partial packet was mathematically useful, but its "not a full
solution" status is outdated. The full arbitrary-space version of the source
paper's Theorem 2 is already answered in the later literature by Moors.

In modern local classification this should be treated as `literature_known`,
not as a new partial result and not as a push target.

## Preserved Partial Work

The previous partial packet is preserved under:

```text
partial_reduction_history/
  README.partial.md
  main.partial.tex
  solution_packet.partial.pdf
```

That older packet contains correct reductions and positive subfamilies:

- a one-set reduction for bounded closed convex `C` with `dist(0,C)>0`;
- an affine-slice subcase;
- a conic-dominated family using Orihuela's conic James theorem;
- frustum and finite-dimensional cylinder families.

These are retained for provenance and as useful explanatory material, but they
should not be ranked as a partial problem to push further.

## Verification Notes

- Same-paper check: arXiv:1508.00496 asks whether the arbitrary-space versions
  of Theorems 2 and 10 hold; it does not itself answer the arbitrary-space
  Theorem 2 question.
- Intermediate source: arXiv:1610.02763 answers the Theorem 10 direction and
  says the Theorem 2 question remained open at that point.
- Decisive later source: Crossref records Warren B. Moors,
  *On a one-sided James' theorem*, DOI `10.1016/j.jmaa.2016.12.019`,
  JMAA 449(1), pages 528-530, 2017. Its reference list cites
  Cascales--Orihuela--Perez, DOI `10.1016/j.jmaa.2016.03.080`, directly.
- Access limitation: the anonymous ScienceDirect request returned only HTML or
  metadata, not a usable local PDF for Moors's paper. The DOI and Crossref
  metadata are stored locally; a human with institutional access can add the
  PDF if desired.

## Files

- `README.md`: this status note.
- `main.tex`: compact literature-status packet source.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: original/source paper PDF.
- `supporting_paper_1610.02763.pdf`: intermediate conic James paper.
- `supporting_paper_moors_2017_crossref.json`: Crossref metadata for Moors's
  decisive later paper.
- `figures/open_question_crop.png`: crop from the source final remarks.
- `partial_reduction_history/`: preserved old partial packet.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat the arbitrary-space Theorem 2 question as already answered by Moors
2017. Do not spend another model round pushing this partial unless the goal is
expository comparison or a self-contained reproof.

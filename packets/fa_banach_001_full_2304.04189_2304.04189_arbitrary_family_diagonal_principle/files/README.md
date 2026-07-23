# Arbitrary-family diagonal principle for nets

Status: `candidate full solution, likely valid pending expert review`

Source: Youssef Azouzi, *A diagonal principle for nets*, arXiv:2304.04189.
The open direction is stated on PDF page 7, at the start of Section 4.

## Result

In ZFC, Azouzi's countable diagonal principle holds for a family of
properties indexed by an arbitrary set.  If each property is preserved under
eventual subnets and every subnet of the original net has a further subnet
satisfying each individual property, then one subnet satisfies all the
properties simultaneously.

The proof first passes to a universal subnet.  Every subnet of a universal net
has the same eventuality ultrafilter.  An arbitrary family of nets with one
common eventuality ultrafilter has a simultaneous refinement: index over
finite sets of tail constraints and choose a point in the intersection of the
corresponding tail ranges.  A distinguished net is refined on the whole index
set, and every other net is refined on a tail.

This immediately gives the arbitrary-product form of Tychonoff's theorem and
the nonseparable form of Banach--Alaoglu by taking one convergence property
per coordinate or per evaluation vector.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the question on page 7.
- `verification_report.md`: proof audit and review focus.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Scope and choice

The result is a full affirmative answer in ordinary ZFC.  The proof is
deliberately nonconstructive: it uses an ultrafilter extending the tail filter
and set-indexed choices.  It does not claim the same theorem in ZF without a
choice principle.

## Novelty check

The run's registry, solution, attempt, and proof-gap indexes were searched for
the arXiv id, exact title, diagonal principles for nets, universal nets, and
common subnets; no duplicate was found.  Bounded web searches on July 22,
2026 used the exact title and phrases from the question, the author name, and
close variants involving universal nets and common ultrafilters.  They found
the source paper and standard diagonal-net material, but no later paper
stating this arbitrary-family theorem or resolving the source question.

The mechanism uses classical universal-net/ultrafilter technology, so novelty
confidence is moderate rather than high: the exact resolution may be folklore
even though no explicit answer was located.

## Human review focus

Please check the common-refinement lemma, especially that the final maps from
the relevant tails are cofinal under the source paper's subnet convention.
Also confirm that the intended open direction permits the standard ZFC choice
principles explicitly anticipated by the source.

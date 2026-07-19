# Laugwitz's Complete-Norm Question: an Aleph-Omega Obstruction

Result type: `full`

Status: candidate full solution, likely valid pending human review.

## Source

- Renan J. S. Isneri, Josias V. Baca, and Lucas M. Fernandes,
  *Norms and Non-Equivalence in Infinite-Dimensional Banach Spaces*,
  arXiv:2508.15686.
- Source question: introduction, page 2.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Exact Target

The source asks whether there is a cardinal `kappa > aleph_0` such that no
real or complex vector space with Hamel basis of cardinality `kappa` can be
endowed with a norm making it a Banach space. The paper says no explicit
example is currently known and attributes the question to Laugwitz.

## Claimed Answer

`kappa = aleph_omega` is such a cardinal in ZFC.

More generally, any singular cardinal of countable cofinality gives the same
obstruction. The packet records the explicit example `aleph_omega` because it
is the canonical first one.

## Proof Summary

Two standard facts are combined.

1. For an infinite-dimensional Banach space `X`, every Hamel basis of `X` has
   cardinality `|X|`.
2. If `dens(X)` is the density character of an infinite-dimensional Banach
   space, then `|X| = dens(X)^{aleph_0}`.

Thus any infinite-dimensional Banach Hamel dimension `kappa` must satisfy
`kappa^{aleph_0} = kappa`, unless it is already below the continuum, which is
impossible by the first fact. Koenig's theorem gives
`aleph_omega^{aleph_0} > aleph_omega`, so no vector space of Hamel dimension
`aleph_omega` admits a complete norm.

## Novelty Check

Cheap run indexes were searched for `2508.15686`, `Laugwitz`, `Hamel bases of
Banach spaces`, and `aleph_omega`; no duplicate packet or attempt for this
target was found. Local source search found the source paper's cited
Halbeisen--Hungerbuehler theorem and an independent Banach-space source
mentioning the standard consequence of Koenig's theorem
`aleph_omega^{aleph_0} > aleph_omega`, but no run packet resolving the stated
Laugwitz question. A bounded web search for the arXiv id and close Laugwitz /
Hamel-basis phrases found no later explicit answer.

Because all ingredients are classical cardinal facts, human review should
decide whether to keep this under `full/` or reclassify it as a
literature-implied answer. The packet's mathematical claim is the explicit ZFC
answer to the question as stated.

## Files

- `main.tex`: self-contained LaTeX proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/make_crops.py`: script used to generate the crop.
- `tmp/`: disposable LaTeX and rendering intermediates.

## Human Review Notes

The key points to check are:

- the standard theorem of Halbeisen--Hungerbuehler equating Hamel-basis
  cardinality and underlying set cardinality for infinite-dimensional Banach
  spaces;
- the proof of `|X| = dens(X)^{aleph_0}`;
- the case split when the continuum is larger than `aleph_omega`;
- the use of Koenig's theorem for `aleph_omega^{aleph_0} > aleph_omega`.

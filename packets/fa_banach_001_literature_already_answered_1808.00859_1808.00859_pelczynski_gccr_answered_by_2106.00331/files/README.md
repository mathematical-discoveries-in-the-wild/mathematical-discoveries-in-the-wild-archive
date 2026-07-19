# Pelczynski Space And Compact Lipschitz Retracts

Status: `literature_already_answered` (scoped subquestion).

Source/open-problem paper: Luis C. Garcia-Lirola and Antonin Prochazka,
*Pelczynski space is isomorphic to the Lipschitz free space over a compact
set*, arXiv:1808.00859.

Supporting answer paper: Petr Hajek and Ruben Medina, *Compact retractions
and Schauder decompositions in Banach spaces*, arXiv:2106.00331.

## Identification

The source paper proves that Pelczynski space `P` is isomorphic to the
Lipschitz free space over a compact convex subset `K` of `P`. After the proof
it notes that the argument would also be completed if the constructed `K`
were a Lipschitz retract of `P`, says this is unknown, and points to the
broader Godefroy-Ozawa question asking whether every separable Banach space
admits a compact convex generating Lipschitz retract.

The later Hajek-Medina paper explicitly treats that Godefroy-Ozawa compact
retraction question. In the introduction it states that every Banach space
with an FDD admits a generating convex compact Lipschitz retract, and that a
space with a monotone Schauder basis admits one with Lipschitz constant
`1+epsilon`. In Section "Compact Lipschitz retracts" it explicitly says this
construction gives a positive answer to the question asked in `GP19`, namely
whether Pelczynski space has a GCCR.

Since Pelczynski space has a Schauder basis, the later FDD/Schauder-basis
theorem supplies a compact convex generating Lipschitz retract in Pelczynski
space.

## Scope

This packet records only the Pelczynski-space GCCR subquestion identified by
the supporting paper. It does not show that the particular compact set
constructed in arXiv:1808.00859 is a Lipschitz retract. It also does not answer
the broader Godefroy-Ozawa question for all separable Banach spaces, nor the
separate question from arXiv:1808.00859 asking whether every separable
infinite-dimensional Banach space `X` has some compact metric `K` with
`F(X) ~= F(K)`.

## Search Evidence

The lane queue selected arXiv:1808.00859. Cheap run indexes had no exact hit
for `1808.00859`; a nearby Lindenstrauss-Pelczynski row was unrelated to
Lipschitz-free spaces. Local source search found the later arXiv:2106.00331
paper, whose introduction and Section "Compact Lipschitz retracts" explicitly
identify the Pelczynski-space GCCR question from `GP19` and answer it through
the FDD construction. Existing run memory also contains a broader serious
attempt for the general Godefroy-Ozawa problem, so no new full attack on that
global problem is claimed here.

## Files

- `source_paper.pdf`: source paper arXiv:1808.00859.
- `supporting_paper_2106.00331.pdf`: supporting later paper.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.

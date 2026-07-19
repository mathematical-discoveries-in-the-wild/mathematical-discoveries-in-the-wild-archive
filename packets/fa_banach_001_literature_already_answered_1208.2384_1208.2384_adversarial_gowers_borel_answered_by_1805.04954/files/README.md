# Adversarial Gowers games beyond the third Borel level

Status: `literature_already_answered`

Source/open-problem paper: Christian Rosendal, *Determinacy of adversarial
Gowers games*, arXiv:1208.2384; published in *Fundamenta Mathematicae* 227
(2014), 163--178.

Supporting answer paper: Noe de Rancourt, *Ramsey theory without pigeonhole
principle and the adversarial Ramsey principle*, arXiv:1805.04954; published in
*Transactions of the American Mathematical Society* 373 (2020), 5025--5056.

## Identification

Problem 1.2 of arXiv:1208.2384 appears on PDF page 3, immediately after
Theorem 1.1.  Rosendal asks whether Theorem 1.1, proved there for
`F_{sigma delta}` and `G_{delta sigma}` sets of block sequences, holds for all
Borel sets, or even for analytic sets in the presence of large cardinals.

arXiv:1805.04954 explicitly identifies this as Rosendal's question.  On PDF
page 6, it states Question 1.10, "Is every Borel set adversarially Ramsey?",
and Question 1.11, "In the presence of large cardinals, is every analytic set
adversarially Ramsey?"  The same paragraph says that the paper proves the
answer to Question 1.10 is yes, and that the answer to Question 1.11 is yes in
the presence of a measurable cardinal.

## Supporting Answer

The decisive Borel result is Theorem 2.4 of arXiv:1805.04954, on PDF page 9:
every Borel subset of `X^omega` is adversarially Ramsey in the abstract Gowers
space setting.  Immediately after the theorem, de Rancourt states that, for the
Rosendal space, the adversarial Gowers games defined there coincide with those
from the introduction, and hence Theorem 2.4 gives a positive answer to
Question 1.10.

The analytic large-cardinal clause is also addressed.  Corollary 2.6 reduces
adversarial Ramseyness for a suitable pointclass in analytic Gowers spaces to
determinacy for the corresponding subsets of `R^omega`; the paragraph following
the corollary invokes Martin's measurable-cardinal theorem for analytic
determinacy and concludes that every analytic set in an analytic Gowers space is
adversarially Ramsey.  It explicitly says this answers Question 1.11.

## Scope

This packet records an already-known literature answer, not a new proof by this
run.  The Borel part is answered in ZFC using Borel determinacy.  The analytic
part is answered under the measurable-cardinal hypothesis used by de Rancourt;
this matches Rosendal's "in the presence of large cardinals" formulation but is
not a ZFC analytic result.  No unresolved part of Rosendal's Problem 1.2 remains
within that stated scope.

The supporting paper uses its own convention for the game labels in the
introductory reformulation, so this packet follows de Rancourt's named
"adversarially Ramsey" Questions 1.10 and 1.11 rather than comparing the
letters `A` and `B` in isolation.

## Search Evidence

The lane-1 queue selected arXiv:1208.2384.  Cheap run indexes were searched for
`1208.2384`, `Determinacy of adversarial Gowers games`, `adversarial Gowers
games`, `strategic Ramsey`, `block sequences`, and `Banach game`; no duplicate
durable packet was found.  Targeted web search for the exact title and the
phrases `adversarial Gowers games Borel analytic large cardinals` and
`adversarially Ramsey Borel Gowers` identified arXiv:1805.04954.  The local TeX
and PDF text of that paper verify that it cites Rosendal's problem source,
restates Questions 1.10 and 1.11, and explicitly says both are answered as
above.

## Files

- `source_paper.pdf`: arXiv:1208.2384.
- `supporting_paper_1805.04954.pdf`: arXiv:1805.04954.
- `source_1208.2384.tex`: local parsed source TeX used to locate Problem 1.2.
- `supporting_1805.04954.tex`: downloaded source TeX used to locate Questions
  1.10 and 1.11, Theorem 2.4, Corollary 2.6, and the measurable-cardinal
  paragraph.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.

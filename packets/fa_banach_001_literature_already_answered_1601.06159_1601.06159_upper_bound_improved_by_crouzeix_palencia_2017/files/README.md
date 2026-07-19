# Crouzeix numerical-range constant: upper bound improved after arXiv:1601.06159

Status: `literature_already_answered (scoped upper-bound improvement)`

Source/open-problem paper: Michel Crouzeix, *Some constants related to
Numerical Ranges*, arXiv:1601.06159; published in *SIAM Journal on Matrix
Analysis and Applications* 37 (2016), 420--442.

Supporting answer paper: Michel Crouzeix and Cesar Palencia, *The numerical
range is a (1+sqrt(2))-spectral set*, *SIAM Journal on Matrix Analysis and
Applications* 38 (2017), 649--655, DOI `10.1137/17M1116672`.

## Identification

On PDF page 2 of arXiv:1601.06159, after recalling the universal bounds
`2 <= Q <= Q_cb <= 11.08`, Crouzeix lists "Some open problems."  The source says
that proving `Q=2` and `Q_cb=2`, or obtaining the exact values, are difficult
open problems.  It then identifies a more modest challenge: sharply improve the
upper bound `11.08`.  It also asks whether `Q=Q_cb`.

The later Crouzeix--Palencia paper gives exactly such a sharp improvement.  Its
official SIAM abstract states that the numerical range of a Hilbert-space
operator is a complete `(1+sqrt(2))`-spectral set.  In the notation of the
source paper, this gives `Q_cb <= 1+sqrt(2)`, and hence also `Q <= 1+sqrt(2)`.
The supporting paper explicitly cites the source paper in its reference list.

## Scope

This packet records a scoped literature answer to the source's upper-bound
improvement challenge only.  It does not resolve Crouzeix's conjecture
`Q=2`, its complete version `Q_cb=2`, the equality question `Q=Q_cb`, the
finite-dimensional questions about `Q(3)` and `Q_cb(3)`, or the other domain
constants listed in the source paper's final problem list.

The supporting publisher PDF was not locally available through the direct SIAM
PDF endpoint during this run: the request returned an access/challenge HTML
page.  The packet therefore keeps the official DOI/abstract-page citation and
the saved access response under `tmp/pdfs/` rather than mislabeling it as a
supporting PDF.

## Search Evidence

The lane-1 queue selected arXiv:1601.06159.  Cheap run indexes were searched for
`1601.06159`, the source title, `numerical ranges`, `Davis-Wielandt`,
`Crawford`, and `numerical index`.  Existing adjacent numerical-index and
Crawford-number packets were found, but no exact packet for the source paper or
for this upper-bound improvement was present before this packet was created.
Targeted web search for Crouzeix--Palencia and `1+sqrt(2)` located the official
SIAM article page, which states the decisive complete `(1+sqrt(2))` theorem and
gives the bibliographic metadata.

## Files

- `source_paper.pdf`: arXiv:1601.06159.
- `source_1601.06159.tex`: local parsed source TeX used to locate the open
  problem passage.
- `supporting_paper_crouzeix_palencia_2017.url`: stable supporting DOI/URL.
- `tmp/pdfs/supporting_paper_crouzeix_palencia_2017_siam_access_page.html`:
  saved publisher access/challenge response from the attempted PDF download.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.

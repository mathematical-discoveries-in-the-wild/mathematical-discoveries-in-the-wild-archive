# Fisher's inequality excludes two proposed Steiner ETF candidates

Status: **literature-implied answer (complete for the two finite candidates)**.

## Source

Matthew Fickus, Dustin G. Mixon, and Janet C. Tremain,
*Steiner equiangular tight frames*, arXiv:1009.5730.

On page 14, at the end of Section 3, the authors leave open whether
\(23\times276\) and \(46\times736\) real ETFs could arise from their Steiner
construction.  This requires \((2,10,46)\)- and \((2,14,92)\)-Steiner
systems, respectively.

## Identification

Fisher's classical inequality says that a nontrivial
\(2\)-\((v,k,\lambda)\) design has at least \(v\) blocks.  A
\((2,k,v)\)-Steiner system has
\[
b=\frac{v(v-1)}{k(k-1)}
\]
blocks.  The proposed parameters give
\[
b(46,10)=23<46,\qquad b(92,14)=46<92.
\]
Consequently neither Steiner system exists, and neither ETF can arise from
the proposed Steiner construction.

The supporting paper by Daniel Horsley, *Generalising Fisher's inequality to
coverings and packings*, arXiv:1409.0485, states Fisher's inequality in its
abstract and on page 2.  The packet also includes the elementary incidence
matrix proof.

## Scope

This completely answers only the two explicit finite design candidates.  It
does not resolve whether other ETFs can break the restricted-isometry
square-root bottleneck, which remains a major open problem.

Files:

- `main.tex`: compact identification and proof;
- `solution_packet.pdf`: rendered note;
- `source_paper.pdf`: arXiv:1009.5730;
- `supporting_paper_1409.0485.pdf`: supporting Fisher-inequality source.

Ledger:
`ledger/results/1009.5730_fisher_excludes_two_steiner_etf_candidates.json`.

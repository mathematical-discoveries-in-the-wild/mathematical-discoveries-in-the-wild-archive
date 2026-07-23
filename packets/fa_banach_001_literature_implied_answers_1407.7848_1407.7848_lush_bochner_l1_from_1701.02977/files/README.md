# Lushness of vector-valued \(L_1\)

Status: `literature_implied_answer (full)`

## Source question

Y. S. Choi, S. K. Kim, H. J. Lee, and M. Martín, *On Banach
spaces with the approximate hyperplane series property*,
arXiv:`1407.7848`, page 7, immediately after Corollary 2.13:

> Whether \(L_1(\mu,X)\) is lush for every lush space \(X\) is not known
> to the best of our knowledge.

Here \(\mu\) is an arbitrary measure, as in the results immediately
preceding the question.

## Identification

V. Kadets, M. Martín, J. Merí, and A. Pérez, *Spear operators between
Banach spaces*, arXiv:`1701.02977`, Theorem 8.10(b) and Corollary 8.12
(page 92 of the supporting PDF), prove that for every sigma-finite measure
\(\nu\),
\[
X\text{ lush}\quad\Longleftrightarrow\quad L_1(\nu,X)\text{ lush}.
\]

This answers the arbitrary-measure question after a short local reduction.
Given \(f,g\in L_1(\mu,X)\), their joint essential support is sigma-finite:
the sets where \(\|f\|+\|g\|\ge 1/n\) have finite measure.  Thus \(f,g\)
belong to the isometric subspace \(L_1(\mu|_A,X)\), which is lush by the
supporting theorem.  A lush slice witness in this subspace extends by
Hahn--Banach to the whole \(L_1(\mu,X)\).  Since lushness is tested on an
arbitrary pair of unit vectors, the whole space is lush.

## Scope and provenance

The forward implication requested in arXiv:`1407.7848` is settled for every
measure.  The supporting authors explicitly prove and call new the
sigma-finite identity-operator case, but they do not state the arbitrary-
measure support reduction.  The classification is therefore
`literature_implied_answer`, rather than a new proof produced by this run or
an explicit literature answer in precisely the source's full generality.

Packet:
`runs/fa_banach_001/solutions/literature_implied_answers/1407.7848_lush_bochner_L1_from_1701.02977/`

Ledger:
`runs/fa_banach_001/ledger/results/1407.7848_lush_bochner_L1_from_1701.02977.json`


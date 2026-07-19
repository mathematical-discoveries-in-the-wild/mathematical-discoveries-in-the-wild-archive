# Literature-Implied Answer: Infinite-Dimensional Amenable Calkin Algebra

status: `literature_implied_answer (full problem)`

source_problem:
- arXiv: `0909.2628`
- paper: Volker Runde, "(Non-)amenability of `B(E)`"
- location: final section `Questions`, the question labelled `calkin`

supporting_source:
- arXiv: `1407.8073`
- paper: Pavlos Motakis, Daniele Puglisi, Despoina Zisimopoulou, "A hierarchy of Banach spaces with `C(K)` Calkin Algebras"
- location: Theorem B in the introduction, and Theorem 5.1 in the final section

## Identification

Runde asks whether there is a Banach space `E` such that its Calkin algebra `Cal(E)=B(E)/K(E)` is amenable and infinite-dimensional.

Motakis-Puglisi-Zisimopoulou prove that for every countable compact metric space `K` there is a Banach space `X` whose Calkin algebra is isomorphic, as a Banach algebra, to `C(K)`. Take any infinite countable compact metric `K`, for example the convergent sequence `{0} union {1/n : n in N}`. Then `C(K)` is infinite-dimensional. It is also a commutative C*-algebra, hence nuclear and amenable. Therefore `Cal(X)` is amenable and infinite-dimensional.

## Scope

This is a full positive answer to Runde's Calkin-algebra question, but it is a literature-implied answer, not a new construction from this run. The supporting paper does not appear to explicitly cite Runde's question; the relation is obtained by matching the supporting theorem with standard C*-algebra amenability.

## Files

- `source_paper.pdf`: original problem source, arXiv `0909.2628`.
- `supporting_paper_1407.8073.pdf`: supporting construction source.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Verification

Cheap run indexes had no exact prior packet for `0909.2628`. Local source search found `1407.8073`, and web search found the same primary arXiv source. The implication uses only Theorem B/5.1 of `1407.8073`, the standard amenability of commutative C*-algebras, and invariance of amenability under Banach algebra isomorphism.

ledger: `runs/fa_banach_001/ledger/results/0909.2628_amenable_infinite_dimensional_calkin_via_ck.json`

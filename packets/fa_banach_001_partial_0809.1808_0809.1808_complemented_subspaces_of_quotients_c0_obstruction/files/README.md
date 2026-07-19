# Rosenthal-Odell Quotient Problem: Operator Reduction

Status: `stronger_partial_result (strict ell_1-predual quotient problem reduced to subprojectivity; U(X,Z)=K(X,Z), superprojectivity, no reflexive quotients, transverse c0 splitting, extension obstruction, and WU trichotomy recorded)`

Run: `fa_banach_001`  
Source: arXiv:0809.1808, Ioannis Gasparis, "New examples of c_0-saturated Banach spaces"  
Upgrade processed: `2026-06-22`

## Classification

This is a stronger partial/reduction packet, not a full solution.

Gasparis records Rosenthal's question asking whether every quotient of an `ell_1`-predual is `c_0`-saturated, and Odell's special case for quotients of `C(K)` with `K` countable compact. Under the strict/isometric convention for `ell_1`-preduals, no full proof or counterexample is claimed here.

Under the broader isomorphic convention `E^* isomorphic to ell_1`, Argyros--Motakis give a literature counterexample. This is recorded as context only, because it does not settle the strict source problem or Odell's countable compact `C(K)` subproblem.

## Upgraded Durable Claim

Let `E` be a real strict `ell_1`-predual and let `X` be a quotient of `E`. Then for every Banach space `Z`,

`U(X,Z) = K(X,Z)`,

where `U` denotes unconditionally converging operators and `K` denotes compact operators. Equivalently, every noncompact operator from `X` fixes a copy of `c_0`.

Consequences recorded in the packet:

- every complemented infinite-dimensional subspace of `X` contains `c_0`;
- every infinite-dimensional quotient of `X` contains a complemented copy of `c_0`;
- `X` has no infinite-dimensional reflexive quotient;
- `X` is superprojective;
- the remaining strict `c_0`-saturation problem is exactly equivalent to subprojectivity of these quotients.

For quotients of countable compact `C(K)`, the same equivalence says:

`X is c_0-saturated` iff `X is subprojective`.

## What Changed

The previous packet's complemented-subspace theorem remains correct, but it is subsumed by the stronger 2017 theorem of Galego--Gonzalez--Pello. The upgrade also corrects the Krulisova citation from Theorem 4.5 to Theorem 4.2.

New material added from the supplied report:

- compactness of unconditionally converging operators on strict `ell_1`-predual quotients;
- superprojectivity and no infinite-dimensional reflexive quotients;
- exact reduction of the strict problem to subprojectivity;
- a transverse `c_0`-splitting / iterated peeling lemma for any hypothetical strict counterexample;
- a Josefson--Nissenzweig extension obstruction;
- the existing `(WU)` trichotomy retained and integrated with the stronger operator reduction.

## Evidence And History

- `evidence/supplied_report_2026_06_22_rosenthal_odell/`: supplied TeX/PDF report.
- `history/previous_packet_2026_06_22_before_operator_reduction/`: previous active README, TeX, PDF, and ledger snapshot.

The duplicate check found the active 0809.1808 packet and registry row, but those only recorded the older complemented-subspace reduction, `(WU)` trichotomy, and broad isomorphic counterexample. They did not record the Galego--Gonzalez--Pello operator theorem, superprojectivity, or the subprojectivity equivalence, so this upgrade was incorporated.

## Files

- `main.tex`: upgraded proof/reduction packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: Gasparis source paper.
- `supporting_paper_1606.00308.pdf`: Galego--Gonzalez--Pello arXiv source for the operator theorem.
- `supporting_paper_1509.06610.pdf`: Krulisova property `(V)` reference.
- `supporting_paper_1608.01962.pdf`: Argyros--Motakis broad isomorphic counterexample reference.
- `supporting_paper_2412.10263.pdf`: Gonzalez--Pello 2025 subprojectivity/superprojectivity reference.
- `supporting_paper_math_9201219.pdf`: Odell quotient paper.
- `supporting_paper_math_9204215.pdf`: Alspach strict `ell_1`-predual quotient note.
- `supporting_paper_math_9805081.pdf`: Alspach Bourgain--Delbaen dual stress-test context.
- `figures/open_problem_crop.png`: source excerpt containing the Rosenthal/Odell question.

## Human Review Focus

1. Check the scalar convention: the strict operator reduction is stated for real strict `ell_1`-preduals.
2. Verify the use of Galego--Gonzalez--Pello Corollary 3.5 and Proposition 3.6, especially the quotient-stability step for `Sp(U^{-1}K)`.
3. Check the exact equivalence between `c_0`-saturation and subprojectivity; the forward implication uses separability plus Sobczyk.
4. Keep the broad isomorphic `ell_1`-predual counterexample separate from the strict/countable `C(K)` source question.
5. Treat the transverse splitting and extension obstruction as constraints on counterexamples, not as a closure of the problem.

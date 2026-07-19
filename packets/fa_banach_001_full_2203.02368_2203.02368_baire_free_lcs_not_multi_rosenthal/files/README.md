# Full answer to Question 8.7 of arXiv:2203.02368

Status: claimed full solution, likely valid, for human review.

## Result

Question 8.7 of Komisarchik--Megrelishvili asks whether the free locally convex
space `L(N^N)` is multi-Asplund or, at least, multi-Rosenthal.

The answer is negative in the stronger form:

> `L(N^N)` is not multi-Rosenthal. Consequently it is not multi-Asplund.

Here `N^N` is the Baire space, homeomorphic to the space of irrationals used in
the source paper.

## Packet contents

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: Komisarchik--Megrelishvili, arXiv:2203.02368.
- `supporting_paper_2106.13413.pdf`: Leiderman--Uspenskij, arXiv:2106.13413, for the nearby multi-reflexive context and multi-`P` terminology.
- `figures/open_problem_crop.png`: PDF page 33 crop showing Question 8.7.

## Proof summary

If a locally convex space embeds into a product of Rosenthal Banach spaces, then
every continuous linear map from it to a Banach space factors through a
Rosenthal Banach space. This follows because continuity into a Banach space is
controlled by finitely many product coordinates.

If `L(N^N)` were multi-Rosenthal, take a continuous surjection
`s : N^N -> ell_1` and extend it linearly to
`\hat{s}: L(N^N) -> ell_1`. The factorization lemma would make `ell_1` a
quotient of a Rosenthal Banach space. But quotients of Rosenthal Banach spaces
are Rosenthal, while `ell_1` is not. Contradiction.

## Novelty check

Before promotion, the run indexes were searched for `2203.02368`, the title,
`Question 8.7`, `multi-Asplund`, `multi-Rosenthal`, `free locally convex`, and
`L(N^N)`. No existing packet or attempt for this target was found.

Bounded web searches on 2026-06-15 for exact phrases including
`"L(N^N)" "multi-Rosenthal"`, `"multi-Asplund" "free locally convex space"`,
`"multi-Rosenthal" "locally convex"`, and
`"Tameness and Rosenthal type locally convex spaces" "multi-Rosenthal"` found
the source paper and nearby multi-reflexive/nuclear literature, but no prior
answer to Question 8.7.

## Human review recommendation

Review the factorization lemma for continuous linear maps out of a subspace of
a product of Rosenthal Banach spaces, and the quotient permanence argument for
Rosenthal spaces. These are the only nontrivial proof steps.

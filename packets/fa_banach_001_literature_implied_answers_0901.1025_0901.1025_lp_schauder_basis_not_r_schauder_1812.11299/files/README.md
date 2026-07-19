# Literature-implied answer: `L^p[0,1]` has a Schauder basis that is not `R`-Schauder

Status: `literature_implied_answer`

Run: `fa_banach_001`  
Agent: `agent_lane_12`  
Date: 2026-06-20

## Source Question

Christoph Kriegler and Christian Le Merdy, *Tensor extension properties of `C(K)`-representations and applications to unconditionality*, arXiv:0901.1025.

In Remark 5.6(2), page 22, they note that for `1 < p != 2 < infinity`, `L^p([0,1])` has a finite-dimensional Schauder decomposition that is not `R`-Schauder, and ask whether `L^p([0,1])` admits a Schauder basis that is not `R`-Schauder.

## Supporting Literature

Loris Arnold and Christian Le Merdy, *New counterexamples on Ritt operators, sectorial operators and R-boundedness*, arXiv:1812.11299.

On page 7, after Corollary 0.4, Arnold--Le Merdy state that it follows from Fackler and Kalton--Lancien that if a Banach space `X` has an unconditional basis and is not isomorphic to a Hilbert space, then `X` has a Schauder basis which is not `R`-Schauder.

Since `L^p([0,1])` has the Haar unconditional basis for `1 < p < infinity` and is not isomorphic to a Hilbert space when `p != 2`, the source question has an affirmative answer for the whole asked range.

## Scope

This is a literature-implied answer, not a new proof from the run. The supporting paper does not appear to explicitly cite arXiv:0901.1025 or say it is answering Remark 5.6(2); the implication is identified by matching the general theorem to the specific `L^p([0,1])` question.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: local copy of arXiv:0901.1025.
- `supporting_paper_1812.11299.pdf`: local copy of arXiv:1812.11299.

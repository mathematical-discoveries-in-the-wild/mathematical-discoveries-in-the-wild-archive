# Compact-refinement counterexample for approximate unique extension property

Status: `candidate_counterexample_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_06`  
Date: 2026-07-03

## Source Target

Ian Thompson, "An approximate unique extension property for completely positive maps", arXiv:2301.08285v1.

The source asks, after Theorem 3.6, whether the approximate unique extension
property can be refined under separability so that the errors
`pi(t)-u_beta^* psi(t) u_beta` are compact, in analogy with Voiculescu's
Weyl-von Neumann theorem.

## Result

The packet gives a negative answer in general. If a separable unital operator
space has an approximate-UEP representation that is not UEP, then its countable
amplification yields a separable AUEP representation and a UCP extension for
which no unitary can make all pointwise errors compact. Thompson's own Cuntz
algebra example supplies such a representation, so the source question has a
counterexample under the separability hypotheses.

The obstruction is the Calkin quotient: compact pointwise errors for even one
unitary would force the Calkin image of the UCP extension to be a
`*`-homomorphism. The countable amplification of any nonmultiplicative extension
has a noncompact multiplicative defect, contradicting this.

## Packet Files

- `main.tex`: self-contained proof note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: stitched crop of pages 11-12 showing the
  compact-refinement question.

## Novelty Check

Bounded search performed 2026-07-03:

- Cheap indexes searched for `2301.08285`, exact title phrase, approximate
  unique extension property, compact refinement, Calkin, and Voiculescu compact
  language. No existing run packet for this target was found.
- Local source search identified only the source-paper question passage.
- Web search for exact close variants of "approximate unique extension
  property" with "compact", "Calkin", and "Voiculescu" found the source arXiv
  paper but no separate resolution.

Novelty confidence: bounded-local-plus-web; human reviewer should still check
recent operator-algebra literature for this exact compact-refinement variant.

## Human Review Focus

Check the Calkin-quotient obstruction and the use of Thompson's Example 2:
the non-boundary irreducible representation of `O_infty` is AUEP by Theorem
3.6 but not UEP, hence admits a nonmultiplicative UCP extension. The rest is a
countable amplification argument.

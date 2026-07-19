# Product extension of the c0 topological CPCP/SR separation

- source: Gines Lopez-Perez and Ruben Medina, *The equivalence between CPCP and strong regularity under Krein-Milman property*, arXiv:2305.18976.
- target: the paper asks whether, starting from a Banach space failing classical CPCP, one can build a locally convex topology on its unit ball, containing the weak topology, such that the unit ball still fails topological CPCP but satisfies topological strong regularity.
- status: `partial_result_likely_valid`
- result: for every separable Banach space `Y`, the unit ball of `c0 \oplus_infty Y` admits such a topology.

## Contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/broad_question_crop.png`: crop of the motivating question.
- `figures/c0_theorem_crop.png`: crop of source Theorem 3.2.
- `code/render_evidence.py`: regenerates the evidence crops.
- `further_push_notes.md`: follow-up push log explaining why the natural
  finite-`p` and complemented-copy upgrades were not promoted.

## Proof Summary

The source paper constructs a topology `sigma` on `B_c0` where every nonempty open set has diameter `2`, but every open set contains small-diameter convex combinations of relatively open subsets. For `X = c0 ⊕_∞ Y`, take the product topology `sigma × norm` on `B_c0 × B_Y`. The `c0` coordinate forces every nonempty open subset of `B_X` to have diameter `2`, while the norm topology on `Y` lets us make the `Y` coordinate arbitrarily small inside the same convex-combination construction.

## Limitations

This is not a solution for all spaces failing CPCP. It applies to the concrete and natural family of separable `ell_infty`-sums with a `c0` summand. The `ell_infty` norm is used directly in the diameter computation.

## Verification

- `latexmk` compiles the packet.
- The result depends on source Theorem 3.2 from arXiv:2305.18976.
- Web and local index searches did not find a prior packet or later exact statement of this `c0 \oplus_infty Y` product extension.

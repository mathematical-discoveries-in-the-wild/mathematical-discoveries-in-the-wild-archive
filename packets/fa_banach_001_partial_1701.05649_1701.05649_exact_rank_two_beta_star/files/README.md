# Exact Rank Two for the Extended Oscillation Rank

Status: `partial_result_likely_valid`; human verification recommended.

Model: `GPT5.6`.

Source paper: D. H. Leung, H.-W. Ng, and W.-K. Tang, *On ordinal ranks of Baire class functions*, arXiv:1701.05649; Fundamenta Mathematicae 247 (2019), 109-130.

## Source Question

After Proposition 3.6, on page 11, the source asks whether for every uncountable Polish space `(X,tau)`, every countable ordinal `xi >= 2`, and every nonzero countable ordinal `zeta`, there is an `f` in `B_xi(tau)` with `beta^*_xi(f)=zeta`.

## Partial Result

For every uncountable Polish space `(X,tau)` and every countable ordinal `xi >= 2`, there is a characteristic function `f` in `B_xi(tau)` such that

```text
beta^*_xi(f) = 2.
```

Choose a set `A` in `Pi^0_xi(tau) \ Sigma^0_xi(tau)`, which exists by strictness of the Borel hierarchy. The source paper's topology-refinement lemma makes `A` closed in an admissible Polish refinement, so the indicator has oscillation rank at most two. Rank one would make the indicator continuous in an admissible topology, forcing both `A` and its complement to lie in `Sigma^0_xi(tau)`, contrary to the choice of `A`.

Together with the constant-function case and Proposition 3.6 of the source paper, the exact range is therefore known to contain `1`, `2`, and every nonzero countable limit ordinal. The general successor case remains open in this packet.

## Verification and Scope

The proof is noncomputational and uses only strictness of the Borel hierarchy, the standard Baire-class/Borel-preimage characterization, and Lemma 3.1 of the source paper. The formal packet includes an adversarial step check.

Three focused full-upgrade pushes were made. A one-point successor gadget is destroyed by admissible refinements; the difference-hierarchy route currently loses a factor of two; and nested `Pi^0_xi` multilevel constructions give upper bounds without refinement-resistant lower bounds. These routes are recorded in the packet and in the durable attempt note.

A bounded novelty check covered the four local lightweight indexes, arXiv:1701.05649, arXiv:1406.5724, exact-phrase and rank-keyword web searches, and citation metadata for the source article. No explicit prior statement of the exact-rank-two subcase or full later answer was located. This is not an exhaustive literature review, so novelty confidence is moderate.

## Files

- `main.tex`: proof and verification packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page-11 source crop containing the question.
- `code/render_source_crop.py`: reproducible source-crop renderer.


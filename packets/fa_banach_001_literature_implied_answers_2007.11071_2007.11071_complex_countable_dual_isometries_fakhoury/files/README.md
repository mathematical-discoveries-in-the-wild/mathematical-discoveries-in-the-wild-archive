# Complex Countable Dual-Isometry Case

Status: `literature_implied_answer (partial subcase)`

Source paper: C. Brech and C. Piña, "Banach-Stone-like results for combinatorial Banach spaces", arXiv:2007.11071, Ann. Pure Appl. Logic 172 (2021), Paper No. 102989.

Supporting paper: Micheline Fakhoury, "Isometries of p-convexified combinatorial Banach spaces", arXiv:2305.13125, Studia Mathematica (2024).

## Target

Question 6 of Brech--Piña asks whether, for compact hereditary families
`\mathcal F,\mathcal G` on an infinite cardinal `\kappa` such that every
singleton belongs to both `\overline{\mathcal F^{MAX}}` and
`\overline{\mathcal G^{MAX}}`, every isometry
`T:X_\mathcal F^* -> X_\mathcal G^*` is weak-star-to-weak-star continuous,
equivalently the adjoint of an isometry `X_\mathcal G -> X_\mathcal F`.

## Packet Claim

Fakhoury's complex-scalar theorem gives a positive answer to the countable
complex subcase, and in fact under weaker hypotheses: for compact
combinatorial families on `\mathbb N`, every complex-linear isometry between
the dual spaces is a compatible signed permutation of the coordinate
functionals. Such an operator is the adjoint of the corresponding coordinate
signed permutation between the primal spaces, hence is weak-star-to-weak-star
continuous.

This is literature-implied because Fakhoury cites Brech--Piña as background
but does not present the result as a direct answer to Question 6.

## Scope

Settled by literature:

- scalar field `\mathbb C`;
- countable index set `\kappa=\mathbb N`;
- compact hereditary/combinatorial families;
- arbitrary pairs `\mathcal F_1,\mathcal F_2`, not just those satisfying the
  closure-of-maximals hypothesis.

Not settled by this packet:

- the real scalar case under Brech--Piña's closure-of-maximals assumption;
- uncountable index sets;
- a new proof independent of Fakhoury's Kalton--Wood/Hilbert-component method.

## Evidence

- `source_paper.pdf`: arXiv:2007.11071.
- `supporting_paper_2305.13125.pdf`: arXiv:2305.13125.
- `main.tex` / `solution_packet.pdf`: compact status note with the exact
  implication.

## Real-Case Attack Notes

The accompanying attempt note
`runs/fa_banach_001/attempts/2007.11071_real_dual_isometry_closure_push.md`
records the unsuccessful real-case push. The main useful obstruction found is
that known finite real counterexamples arise from low-dimensional block
symmetries such as `\ell_\infty^2 \cong \ell_1^2` or the `K_{2,2}` graph
polytope. Brech--Piña's singleton-closure hypothesis appears designed to
destroy exactly these finite isolated blocks, but this pass did not turn that
intuition into a proof.

## Verification Focus

Check that Fakhoury's Corollary 2.15/Proposition 1.3 applies with
`\mathbf E=\ell_1` over `\mathbb C`, and that compactness of the source
families makes the canonical bases shrinking so that the dual isometry
statement is about the full spaces `X_{\mathcal F_i}^*`. Then the resulting
compatible signed permutation is visibly weak-star continuous as the adjoint
of the primal compatible signed permutation.

# Counterexample packet: LorEA_2 is not convex in general

Status: claimed counterexample, likely valid, needs human review.

Source target: Francesca La Piana and Alexander Mueller-Hermes, *Annihilating and breaking Lorentz cone entanglement*, arXiv:2506.14480.

Question addressed: on page 3, after defining the Lorentzian tensor product and the class `LorEA_2(C_A,C_B)`, the authors write that they do not know whether this set is convex in general, while proving convexity when the output cone is a Lorentz cone.

Result: `LorEA_2(L_2, C_{\ell_1^2})` is not convex. Equivalently, even with Lorentz input, convexity can fail once the output cone is not Lorentz.

Mechanism: the source paper already gives a nonconvexity example for `maxEA_2(C_{\ell_\infty^2}, L_2)` in its appendix. Taking trace adjoints converts max-entanglement annihilating maps from `C` to `D` into max-entanglement annihilating maps from `D^*` to `C^*`. Since `L_2` is self-dual and `L_2 \otimes_L L_2 = L_2 \otimes_max L_2`, the adjoint example becomes a genuine nonconvexity example for `LorEA_2(L_2, C_{\ell_1^2})`.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2506.14480.
- `figures/open_problem_crop.png`: source crop for the question.
- `code/verify_constants.py`: reproduces the scalar inequality in the displayed example.

Novelty check: searched exact phrases around `LorEA_2`, `Lorentz-entanglement annihilating`, `convex`, and the source title on 2026-06-20. No later answer was found beyond the source paper itself.

Review recommendation: check the adjoint-duality lemma and the equality `L_n \otimes_L C = L_n \otimes_max C`; once those two standard identifications are accepted, the counterexample follows immediately from the appendix computation in the source paper.

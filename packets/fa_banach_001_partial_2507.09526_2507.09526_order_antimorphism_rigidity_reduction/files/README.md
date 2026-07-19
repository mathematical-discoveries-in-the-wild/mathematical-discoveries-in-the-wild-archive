# Order-Antimorphism Rigidity Reduction

Status: `partial_result`.

Source target: arXiv:2507.09526, Mark Roelands and Samuel Tiersma, "An order-theoretic characterization of JB-algebras" (current arXiv v3, 2026-03-23).

## Claim

This packet proves a reduction for the residual question on page 5 of the source paper: whether, in infinite dimensions, existence of an order-anti-isomorphism on the open cone already implies existence of a gauge-reversing bijection.

Let `C = V_+^\circ` be the open cone of a complete order unit space. Suppose the order automorphism group of `C` has two rigidity properties:

1. every order automorphism of `C` is positively homogeneous;
2. the center of the order automorphism group consists only of scalar dilations.

Then every order-anti-isomorphism `Phi: C -> C` is automatically homogeneous of degree `-1`. Hence it is gauge-reversing, and the Roelands-Tiersma theorem gives a compatible JB-algebra structure on `V`.

## Scope

This does not solve the full infinite-dimensional Walsh strengthening. It gives an affirmative answer for cones whose interior order automorphisms are already rigid in the above sense. The packet also identifies the obstruction: the hypothesis fails exactly in the kind of scalar-reparametrization behavior visible in one-dimensional factors, such as coordinatewise power maps on orthants.

## Files

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of the source passage posing the infinite-dimensional question.
- `code/lorentz_candidate_check.py`: small deterministic check documenting that the naive non-Hilbert Lorentz-cone inversion formula is not an order-antimorphism.

## Verification

The theorem is formal and does not depend on computation. The included code only records an abandoned counterexample route.

Human review should focus on the group-theoretic reduction, especially the use of the center hypothesis and the monotone multiplicative character argument.

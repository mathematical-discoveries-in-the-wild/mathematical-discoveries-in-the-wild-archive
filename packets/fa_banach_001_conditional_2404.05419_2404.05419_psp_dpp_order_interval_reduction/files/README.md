# Positive Schur to Dunford-Pettis: canonical interval reduction

Status: conditional reduction, likely valid.

Source paper: Jose Rodriguez, "Dunford-Pettis type properties in $L_1$ of a vector measure", arXiv:2404.05419.

Target question: Question 1.2 asks whether $L_1(\nu)$ has the Dunford-Pettis property whenever it has the positive Schur property.

## Result

Let $E=L_1(\nu)$ and let
$j_\nu:L_\infty(\nu)\to L_1(\nu)$ be the canonical inclusion. Put
$K=j_\nu(B_{L_\infty(\nu)})=[-\chi_\Omega,\chi_\Omega]$.

The packet proves:

> If $E$ has the positive Schur property, then $E$ has the Dunford-Pettis property if and only if $K$ is a Dunford-Pettis subset of $E$.

Equivalently, under the positive Schur property, Question 1.2 is reduced to proving that the single canonical weakly compact order interval $[-\chi_\Omega,\chi_\Omega]$ is a Dunford-Pettis set. In operator language this interval condition is equivalent to the adjoint $j_\nu^*:L_1(\nu)^*\to L_\infty(\nu)^*$ being Dunford-Pettis. It is not the same as saying that $j_\nu$ itself is Dunford-Pettis.

## Conditional Dependency

To turn the reduction into a full positive answer to Question 1.2, one must prove the following remaining condition for every vector measure $\nu$:

> If $L_1(\nu)$ has the positive Schur property, then $j_\nu(B_{L_\infty(\nu)})$ is a Dunford-Pettis subset of $L_1(\nu)$.

The packet proves that this condition is both sufficient and necessary for a positive answer, after assuming the positive Schur property.

## Proof Idea

Rodriguez records that the positive Schur property is equivalent to every relatively weakly compact subset of $L_1(\nu)$ being L-weakly compact, and that L-weakly compact subsets of $L_1(\nu)$ are approximately order bounded by scalar multiples of $j_\nu(B_{L_\infty(\nu)})$.

Thus, given weakly null sequences $(f_n)\subset L_1(\nu)$ and $(\varphi_n)\subset L_1(\nu)^*$, approximate the relatively weakly compact set $\{f_n:n\in\mathbb N\}$ within $\epsilon$ by a scalar multiple of the canonical interval. If that interval is a Dunford-Pettis set, then $\varphi_n$ converges uniformly to zero on the approximants, and the $\epsilon$ error is controlled by boundedness of $(\varphi_n)$. This gives $\varphi_n(f_n)\to0$, the sequential Dunford-Pettis criterion.

The converse is standard: in a Dunford-Pettis space every relatively weakly compact set is a Dunford-Pettis set, and Rodriguez notes that $j_\nu(B_{L_\infty(\nu)})$ is weakly compact.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/question_1_2_crop.png`: crop of the source question.

No computational verifier is needed; the result is a functional-analytic reduction.

## Search Notes

Cheap index searches for `2404.05419`, `Dunford-Pettis type properties`, `positive Schur property`, `L_1(\nu)`, and the exact Question 1.2 wording found no existing run packet solving this target. Web searches for the exact question and for the source title returned the source paper and adjacent Banach-lattice material, but no separate resolution of Question 1.2.

Human review should focus on the use of approximate order boundedness from Rodriguez Propositions 2.4 and 2.5 and on the corrected adjoint formulation of the canonical interval condition.

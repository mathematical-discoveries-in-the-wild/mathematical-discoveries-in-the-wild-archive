# Counterexample Packet: Bourgain-root counterexamples in `ell_p`

Status: `candidate_counterexample_likely_valid`

Source paper: arXiv:2512.14949, *Bourgain--uo sequential completeness in vector lattices*, Tomasz Kania and Jaroslaw Swaczyna.

Target: Question 5.2 asks whether Buo-Cauchy sequences converge in `ell_p` for `1 < p < infinity`.

## Result

The answer to the `ell_p`, `1 < p < infinity`, bullet is negative.

Bourgain's 1981 `ell_1` example uses exactly the same subsequence-difference Cauchy test, with convergence given by coordinatewise convergence plus a single `ell_1` dominator. For each `1 < p < infinity`, applying the coordinatewise map

`t -> sign(t) |t|^(1/p)`

to Bourgain's `ell_1` sequence gives a Buo-Cauchy sequence in `ell_p` that does not converge in order and hence does not Buo-converge.

This does not contradict the existing partial packet: every such sequence is still norm convergent in `ell_p`; it fails only the order-bounded domination required for order/Buo convergence.

## Packet contents

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2512.14949.
- `supporting_paper_bourgain_1981.pdf`: Bourgain, *Non-completeness of some convergence on l^1*, Colloq. Math. 44 (1981), 175-178.
- `figures/open_problem_crop.png`: screenshot crop of Question 5.2 from the source paper.
- `figures/bourgain_definition_page.png`: rendered first page of Bourgain's paper, showing the convergence and Cauchy definitions.

## Human review recommendation

Verify the identification of Bourgain's `p`-Cauchy condition with Buo-Cauchy in `ell_1`; it appears verbatim on page 175 of the supporting paper. If accepted, the root-map proof is a short rigorous counterexample for every `1 < p < infinity`.

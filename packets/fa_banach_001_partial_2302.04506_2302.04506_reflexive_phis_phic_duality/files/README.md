# Phi-singular and Phi-cosingular operators: verified reductions and strictness routes

Status: `strong_partial_result_likely_valid`

This packet records a strengthened structural partial result for arXiv
`2302.04506`, "Two classes of operators related to the perturbation classes
problem" by Manuel Gonzalez and Margot Salas-Brown.

It is not a full solution of the global questions `SSing=PhiS` and
`SCos=PhiC`. The prior active packet already contained four likely-valid
structural advances; the supplied report audits those advances, corrects two
details, and adds reductions that make the remaining obstruction more
concrete.

The upgraded packet records:

- reflexive adjoint duality equivalences for `PhiS` and `PhiC`;
- one-sided square characterizations: `PhiS(X,Y)=P Phi_+(X,Y)` when
  `Y x Y` embeds in `Y`, and `PhiC(X,Y)=P Phi_-(X,Y)` when `X` has quotient
  `X x X`;
- subprojective/superprojective barriers showing such operators cannot witness
  strictness of `SSing subset PhiS` or `SCos subset PhiC`;
- extension/lifting obstructions for any remaining perturbation-class
  witness;
- the global equivalence: `PhiS` is an operator ideal iff `PhiS=SSing`, and
  `PhiC` is an operator ideal iff `PhiC=SCos`;
- same-component multiplication reductions: one half is automatic, and
  linearity of the component implies the other half;
- localization of any perturbation-class witness outside `PhiS` to an
  uncomplemented upper semi-Fredholm column range, and dually outside `PhiC`
  to an uncomplemented lower semi-Fredholm row kernel;
- a quotient-algebra route to strict counterexamples: if
  `L(X)/SSing(X) ~= F[epsilon]/(epsilon^n)` for `n>=2`, then
  `PhiS(X) != SSing(X)`, with the dual statement for `SCos` and `PhiC`.

Two corrections from the supplied audit are incorporated: the Gonzalez--Pello
supporting result is Corollary 2.3, not Corollary 2.4, and the adjoint
strictness corollary must keep the hypothesis that the usual
strictly-singular/strictly-cosingular adjoint duality holds for the spaces at
hand.

The global equality questions remain open. The packet should be read as a
strong partial structural reduction and a narrowed construction target for any
future strictness example.

## Files

- `main.tex`: upgraded proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv `2302.04506`.
- `supporting_paper_2412.10263.pdf`: local copy of the Gonzalez--Pello paper
  introducing subprojective/superprojective operators.
- `figures/open_problem_crop.png`: source crop with Questions 1 and 2.
- `figures/phic_open_problem_crop.png`: source crop with Questions 4 and 5.
- `figures/source_duality_proposition_crop.png`: source crop with Proposition
  4.9.
- `code/crop_source_evidence.py`: crop-generation helper.
- `evidence/supplied_phi_singular_exploration_2026_06_23/`: supplied TeX/PDF
  report used for this upgrade.
- `history/previous_partial_2026_06_23/`: previous active README, TeX source,
  and rendered packet.

## Novelty and duplicate check

The upgrade protocol found an existing active packet for arXiv `2302.04506`;
that packet already contained the reflexive duality, one-sided square
characterizations, projective-operator barrier, and extension/lifting
obstruction. The supplied report was therefore incorporated as a stronger
partial result rather than as a new packet.

The supplied report's bounded literature audit, current through 22 June 2026,
found no proof or counterexample settling the global equality questions and no
known construction realizing the quotient-algebra criterion by strictly
singular or strictly cosingular operators. This result remains subject to
human mathematical review.

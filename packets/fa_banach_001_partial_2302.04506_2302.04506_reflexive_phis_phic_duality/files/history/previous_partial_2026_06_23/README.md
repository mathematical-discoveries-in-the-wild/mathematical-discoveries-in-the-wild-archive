# Projectivity, extension, and square-type characterizations for Phi-singular and Phi-cosingular operators

Status: `partial_result_likely_valid`

This packet records a structural partial result for arXiv `2302.04506`,
"Two classes of operators related to the perturbation classes problem" by
Manuel Gonzalez and Margot Salas-Brown.

The source paper proves one-way adjoint implications:

- `K^* in PhiS(Y^*,X^*)` implies `K in PhiC(X,Y)`.
- `K^* in PhiC(Y^*,X^*)` implies `K in PhiS(X,Y)`.

The packet proves four structural advances.

First, when `X` and `Y` are reflexive, the source paper's duality implications
are equivalences. Reflexivity is exactly what makes every operator
`Y^* -> X^*` the adjoint of an operator `X -> Y`, allowing the converse
argument to run through the same semi-Fredholm duality used by the source.

Second, it isolates the one-sided square mechanism already visible inside the
source's combined perturbation-class arguments and turns it into explicit
characterizations of the intermediate classes:

- if `Y x Y` embeds into `Y`, then `PhiS(X,Y)=P Phi_+(X,Y)`;
- if `X` admits a quotient isomorphic to `X x X`, then
  `PhiC(X,Y)=P Phi_-(X,Y)`.

The source's subspace and same-component multiplication-stability questions
therefore have positive answers in these cases. This should be read as an
extracted structural strengthening of the source's square-isomorphism
characterizations, not as a solution of the global equality problem.

The `PhiS` side includes all square-isomorphic codomains noted in the source,
such as `ell_p`, `L_p(mu)`, `c_0`, and `C[0,1]`, and also any codomain merely
containing a closed copy of its square. The `PhiC` side includes every
square-isomorphic domain and more generally every domain with quotient
`X x X`.

Third, using the subprojective/superprojective operator classes of Gonzalez
and Pello (`arXiv:2412.10263`), the packet proves a sharp barrier theorem:

- if `K:X -> Y` is subprojective as an operator, then
  `K in P Phi_+`, `K in PhiS`, and `K in SS` are equivalent;
- if `K:X -> Y` is superprojective as an operator, then
  `K in P Phi_-`, `K in PhiC`, and `K in SC` are equivalent.

Thus any strictness witness for `SS subset PhiS` must be a non-subprojective
operator, and any strictness witness for `SC subset PhiC` must be a
non-superprojective operator. In particular `SS=PhiS` whenever every
operator `X -> Y` is subprojective, for instance when `Y` is subprojective;
dually `SC=PhiC` whenever every operator `X -> Y` is superprojective, for
instance when `X` is superprojective.

Fourth, the final push adds an extension/lifting obstruction:

- if `K in P Phi_+` is not strictly singular, then for every infinite
  dimensional subspace `M` on which `K` is an isomorphism and every
  `A in Phi_+`, the map `A|_M (K|_M)^(-1): K(M) -> Y` cannot extend to an
  operator `Y -> Y`;
- consequently, if the pair `(Y,Y)` has the qualitative linear extension
  property, then `P Phi_+(X,Y)=PhiS(X,Y)=SS(X,Y)`;
- dually, if `K in P Phi_-` is not strictly cosingular, then every quotient
  witness `Q_M K` blocks the lifting of `Q_M B` for all `B in Phi_-`;
- consequently, if `X` has the lifting property, then
  `P Phi_-(X,Y)=PhiC(X,Y)=SC(X,Y)`.

This covers injective-type codomains on the `PhiS` side and
projective-type domains on the `PhiC` side, and gives a concrete failure mode
that any remaining strictness witness must exhibit.

This does not settle the main equality questions `SS=PhiS` or `SC=PhiC`.
It gives a broad duality characterization, sharp positive structural answers
for common square-like domain/codomain classes, and two strong localization
tests for any possible counterexample.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv `2302.04506`.
- `supporting_paper_2412.10263.pdf`: local copy of the Gonzalez--Pello paper
  introducing subprojective/superprojective operators.
- `figures/open_problem_crop.png`: source crop with Questions 1 and 2.
- `figures/phic_open_problem_crop.png`: source crop with Questions 4 and 5.
- `figures/source_duality_proposition_crop.png`: source crop with Proposition 4.9.
- `code/crop_source_evidence.py`: crop-generation helper.

## Novelty check

Cheap run indexes had no prior packet for arXiv `2302.04506`. Web searches for
the exact `PhiS/PhiC` duality and stability vocabulary found only the source
arXiv paper. Targeted searches for `PhiS/PhiC` together with
subprojective/superprojective operators found only `arXiv:2412.10263`, which
introduces those operator classes but does not appear to state the triangular
perturbation consequence in this packet. Final searches combining the
`PhiS/PhiC` vocabulary with extension, lifting, injective, and projective
Banach-space terminology found only the source paper and background
extension-property literature, not the obstruction theorem recorded here. The
result should still be treated as a structural partial answer pending human
review.

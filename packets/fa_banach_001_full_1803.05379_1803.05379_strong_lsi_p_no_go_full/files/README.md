# Full packet: strong DF-LSI_p no-go beyond the p=1 endpoint

Status: likely valid full result for the extracted finite-dimensional nontrivially decohering QMS question; human review recommended.

Source target: arXiv:1803.05379, Ivan Bardet and Cambyse Rouze, "Hypercontractivity and logarithmic Sobolev Inequality for non-primitive quantum Markov semigroups and estimation of decoherence rates".

Open problem context: the conclusion asks for the range of exponents `p` for which one can find a non-primitive semigroup satisfying the strong decoherence-free inequality `LSI_{p,N}(c,0)` with `c>0`. The paper proves the obstruction at `p=2` and notes that the modified `p=1` endpoint behaves differently.

Result in this packet: for every finite `p>1`, the strong inequality `LSI_{p,N}(c,0)` fails for every finite-dimensional nontrivially decohering QMS, i.e. every QMS whose decoherence-free algebra is neither scalar nor all of `B(H)`. Together with the known modified `p=1` examples, this gives the existence range `{1}`.

Upgrade from previous partial packet: the earlier reversible/canonical proof only used reversibility to cancel the fixed-algebra part of the second variation. The full packet replaces that by a fixed-algebra Hamiltonian cancellation: on the decoherence-free algebra, the generator is a derivation, and the singular second-order terms are functions of the same projected state, so their pairing with the derivation vanishes by traciality of `sigma_tr` on `N`.

Novelty/literature check: on 2026-06-23, searches for exact phrases around `LSI_{p,N}(c,0)`, non-primitive QMS, strong log-Sobolev inequalities, and amalgamated `L_p` spaces found the source paper and later modified-LSI/complete-MLSI papers, but no later paper explicitly resolving the stated strong `p`-range question.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1803.05379.
- `supporting_paper_1710.01039.pdf`: source for the modified `p=1` endpoint context.
- `figures/open_problem_crop.png`: crop of the source open-question passage.
- `code/diagonal_decoherence_ratio.py`: small numerical stress check for the two-dimensional diagonal decoherence model.
- `history/partial_reversible_no_go/`: superseded reversible/canonical partial packet preserved for provenance.

Human review focus:

1. Check the fixed-algebra Hamiltonian cancellation lemma in the non-reversible case.
2. Check that the singular second-order terms in the functional-calculus expansion are indeed functions of the projected state after applying `E_N`.
3. Check the endpoint wording: the theorem proves no finite `p>1`, while the cited modified-LSI literature supplies `p=1` examples.

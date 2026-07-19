# Counterexample: an injective ideal without the ell_infty-extension property

Status: `counterexample_likely_valid`

Source paper: Anil Kumar Karn and Deba Prasad Sinha, *Compactness and an approximation property related to an operator ideal*, arXiv:1207.1947.

Open question addressed: page 22 of the source paper asks whether there is an injective operator ideal that fails the `ell_infty`-extension property.

Result: yes. The closed operator ideal `X` of all separable-range operators, equipped with the operator norm, is injective but does not have the `ell_infty`-extension property.

Mechanism: take the canonical Alouglu embedding `i:c0 -> ell_infty(B_{ell_1})`. It is a separable-range operator. If it admitted a separable-range extension `S` to `ell_infty(B_{ell_1})`, then the closure of `S`'s range would be a separable superspace of `i(c0)`. Sobczyk's theorem would complement `i(c0)` inside that separable range, producing a projection from the Alouglu envelope onto `i(c0)`. That would make `c0` injective, contradicting Phillips' theorem that `c0` is not complemented in `ell_infty`.

Packet contents:

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:1207.1947.
- `figures/open_problem_crop.png`: crop of the source paper's open-question passage.

Novelty check: cheap run indexes had no exact `1207.1947` packet. Local source search for the exact extension-property phrase found only the source paper. Web searches on 2026-06-28 for exact variants of `"ell_infty-extension property" "operator ideal"` and `"injective operator ideal" "ell_infty-extension property"` surfaced the source paper but no later answer. A related local paper, arXiv:1106.5088, discusses separable-range operators as classical injective/surjective ideals but does not state this Karn-Sinha counterexample.

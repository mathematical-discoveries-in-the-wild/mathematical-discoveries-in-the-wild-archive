# Full solution: negative answer for the double-arrow ordinal product question

Status: `full_solution_likely_valid`

Source paper: Maciej Korpalski, *Semadeni-Pelczynski derivative and Banach spaces of continuous functions on nonmetrizable cubes*, arXiv:2502.16981.

## Target

Question 1 on PDF page 22 asks whether, for the double arrow space `S`,

```text
C(S) is isomorphic to C(S x [0, alpha])
```

for every ordinal `omega^omega <= alpha < omega_1`.

## Result

No. For every `omega^omega <= alpha < omega_1`,

```text
C(S) is not isomorphic to C(S x [0, alpha]).
```

The source paper's Proposition 6.2 says that if `C(K)` does not embed into `c0(c)`, then `C(S)` is not isomorphic to `C(S x K)`. For `K = [0, alpha]` in the asked range, `C(K)` cannot embed into `c0(c)`: its image would be separable, hence supported on countably many coordinates and embedded into ordinary `c0`, contradicting Brooker's Szlenk-index computation `Sz(C([0, alpha])) > omega`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:2502.16981.
- `figures/question_and_criterion_crop.png`: crop of Question 1 and Proposition 6.2 from the source.

## Search Bounds

Before promotion, the run indexes were searched for `2502.16981`, `double arrow`, `C(S)`, `C(S x [0, alpha])`, `c0(c)`, `Szlenk`, and ordinal variants. Local source searches found no prior packet for this exact consequence. Web searches on 2026-06-29 found Brooker's Szlenk computation and no separate exact resolution of the double-arrow question.

## Human Review Notes

Recommended review focus:

- Confirm that using Proposition 6.2 from the same source is acceptable for the target protocol.
- Check the separable-subspace reduction from `c0(c)` to ordinary `c0`.
- Check the Szlenk-index input for `C([0, alpha])` when `alpha >= omega^omega`.

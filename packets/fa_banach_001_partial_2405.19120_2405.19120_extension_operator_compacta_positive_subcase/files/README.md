# Strong Partial Packet: Convex Reductions and Averaging Obstructions

Status: `strong_partial_result_likely_valid`

Run: `fa_banach_001`

Source paper: Grzegorz Plebanek, Jakub Rondos, Damian Sobota,
*Complemented subspaces of Banach spaces `C(K x L)`*, arXiv:2405.19120.

## Source Problem

Problem 4.1 asks whether `C(beta omega x beta omega)` contains a
complemented isomorphic copy of `C(K)` for every separable compact space
`K`.

The source paper already proves the metric compact case by showing that
`C(beta omega x beta omega)` contains complemented copies of
`C([0,1]^kappa)` for every `1 <= kappa <= c`.

## Upgraded Packet Result

The packet remains partial: it does not solve Problem 4.1 and does not
give a counterexample. It upgrades the earlier extension-operator subcase
to a consolidated structural packet with four durable conclusions.

1. Problem 4.1 is exactly equivalent to its restriction to separable
   Bauer simplices `P(K)` and also to separable weak-star compact dual
   balls `B_{M(K)}`.
2. Every separable almost-Milyutin compactum gives a positive instance;
   in particular every separable Dugundji compactum gives a positive
   instance.
3. A separable dyadic space `K_* = T^N` from Blasco-Ivorra is not
   almost Milyutin, so no proof based only on averaging from Cantor
   cubes can settle the full problem.
4. In the operator model
   `C(beta omega x beta omega) ~= K(ell_1, ell_infty)`, the direct
   projection onto `K(ell_1, C(K))` cannot work unless the evaluation
   copy of `C(K)` is already complemented in `ell_infty`.

The older packet theorem is preserved as a special case via the
averaging/transitivity closure principle.

## What Remains Open

The full Problem 4.1 remains open in this packet. The unresolved part is
the possible existence of noncanonical complemented copies of `C(K)` in
`C(beta omega x beta omega)` for separable compact spaces outside the
known averaging/extension classes.

The supplied report isolates two next targets:

- show that the Blasco-Ivorra test space `K_*` cannot factor
  complementedly through `C(beta omega x beta omega)`, perhaps by
  comparing canonical averaging constants with arbitrary factorization
  constants;
- or build a genuinely twisted, noncanonical factorization for every
  separable Bauer simplex through `K(ell_1, ell_infty)`.

## Files

- `main.tex`: upgraded review packet source.
- `solution_packet.pdf`: compiled upgraded packet.
- `source_paper.pdf`: local copy of arXiv:2405.19120.
- `figures/open_problem_crop.png`: source Problem 4.1 crop.
- `code/make_problem_crop.py`: regenerates the source crop.
- `evidence/supplied_complemented_betaomega_best_2026_06_22/`: supplied
  TeX/PDF report that triggered this upgrade.
- `history/previous_extension_operator_packet_2026_06_22/`: previous
  active packet before this upgrade.

## Verification

Build command:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Index rebuild command:

```sh
conda run --no-capture-output -n sandbox python scripts/build_run_indexes.py runs/fa_banach_001
```

## Human Review

Recommended checks:

- verify the exact-reduction proof, especially separability and weight
  estimates for `P(K)` and `B_{M(K)}`;
- verify the use of Haydon's Milyutin/Dugundji theorem and the
  Blasco-Ivorra obstruction;
- verify that the operator-space no-go lemma only blocks the direct
  `K(ell_1, C(K))` projection route and is not overstated as a
  counterexample.

# Full Solution Packet: ordinal intervals below omega_2

Status: `candidate_full_solution_likely_valid`

Source paper: Piotr Koszmider, *On the existence of overcomplete sets in some
classical nonseparable Banach spaces*, arXiv:2006.00806.

Target question: Question 48 asks whether ZFC proves that `C([0, xi])` admits
an overcomplete set for every ordinal `xi < omega_2`.

Claim proved in this packet: yes. In ZFC, `C([0, xi])` admits an overcomplete
set for every ordinal `xi < omega_2`.

## Proof Mechanism

The previous lane-16 packets covered:

- all `xi < omega_1 * omega`;
- the first countable-block endpoint `C([0, omega_1 * omega])`.

This packet adds the missing top representative `C([0, omega_1^2])`.

The proof splits `[0, omega_1^2]` into the closed skeleton of multiples of
`omega_1`, plus endpoint-vanishing gap functions. A skeleton extension handles
all endpoint masses, while gap perturbations are assigned sparse Taylor
exponent sets indexed by a coherent injection. For a fixed functional, only
countably many gaps matter; after stabilization, analytic coefficient
comparison forces both the skeleton functional and every active gap functional
to vanish.

Classical Kislyakov/Gul'ko-Os'kin classification of ordinal `C(K)` spaces then
reduces all `xi < omega_2` to the finite-multiplicity cases, the countable
representative `omega_1 * omega`, and the top representative `omega_1^2`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2006.00806.
- `figures/open_problem_crop.png`: crop of Question 48 from the source paper.

## Verification

Rendered with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on continuity at limit skeleton points, the
decomposition of `C([0, omega_1^2])`, the active-gap coefficient comparison,
and the exact use of ordinal `C(K)` classification.

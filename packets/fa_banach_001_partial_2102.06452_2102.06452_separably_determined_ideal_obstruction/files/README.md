# Separably Determined Ideal Obstruction for Norm-Attaining Operator Spaces

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Sheldon Dantas, Mingu Jung, Gonzalo Martinez-Cervantes,
  "On the existence of non-norm-attaining operators", arXiv:2102.06452.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Source Problem Context

The source paper quotes Ostrovskii's problem asking whether there exists an
infinite-dimensional Banach space on which every operator attains its norm.
The paper proves Theorem 3.8: if such a space exists, it cannot have the
bounded `A`-approximation property for any norm-closed operator ideal `A` not
containing the identity.

## Claimed Contribution

This packet proves a pair-level ideal version of the compact-operator criterion
from the source paper.

Let `A` be a norm-closed operator ideal that is separably determined in the
domain variable. Let `E` be reflexive and `F` be any Banach space. If the pair
`(E,F)` has the bounded `A`-approximation property and every operator
`E -> F` attains its norm, then

```text
L(E,F) = A(E,F).
```

Equivalently, if `A(E,F)` is proper but `(E,F)` has bounded `A`-approximation,
then `L(E,F)` contains a non-norm-attaining operator.

For `A = K`, this recovers the compact case of the source theorem. The point is
that the same proof works for any domain-separably-determined closed ideal,
using reflexive separable complementation to reduce SOT closure to SOT
sequential closure.

## Novelty Caution

The published PDF of arXiv:2102.06452 does not state this pair-level ideal
theorem. The arXiv source comments do mention the separably determined route in
outline. This packet should therefore be treated as a precise promoted
extension/cleanup of the method, with modest novelty, not as a full solution of
Ostrovskii's problem.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: source crop around Ostrovskii's problem and
  Theorem 3.8.
- `code/crop_open_problem.py`: crop script.
- `tmp/`: build intermediates.

## Human Review Notes

Verifier focus:

- Check the definition of "separably determined" is strong enough for the
  restriction argument.
- Check the passage from SOT non-closure of the ideal unit ball to sequential
  non-closure using a complemented separable subspace of the reflexive domain.
- Check that the bounded `A`-approximation property is stated for the pair
  `(E,F)`, not just for `E`.


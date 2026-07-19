# Literature Answer: Schur Property of the Bourgain-Delbaen Tensor Square

Status: `literature_already_answered`

Source problem paper: M. Gonzalez and J. M. Gutierrez, *The Dunford-Pettis
property on tensor products*, arXiv:math/0004101.

Supporting answer paper: J. Rodriguez, *On weak compactness in projective
tensor products*, arXiv:2206.08651.

## Target

At the end of the source paper, Gonzalez--Gutierrez consider an
infinite-dimensional separable `L_infinity`-space `X` of Bourgain--Delbaen
type with the Schur property and with `X^*` isomorphic to `C[0,1]^*`.

They note that `X^* \hat\otimes_epsilon X^*` fails the Dunford-Pettis
property and that `(X \hat\otimes_pi X)^*` fails the Dunford-Pettis property,
then ask:

- does `X \hat\otimes_pi X` have the Schur property?
- does `X \hat\otimes_pi X` have the Dunford-Pettis property?

## Answer

Yes to both questions.

Rodriguez arXiv:2206.08651 explicitly cites the Schur-preservation problem
for projective tensor products as open, citing Gonzalez--Gutierrez among the
sources, and then proves Theorem `theo:Schur`:

```text
If X and Y have the Schur property, then so does X \hat\otimes_pi Y.
```

Applying this theorem with `Y=X` gives that the Bourgain--Delbaen space in
the source question satisfies that `X \hat\otimes_pi X` has the Schur
property. Since every Banach space with the Schur property has the
Dunford-Pettis property, the tensor square also has the Dunford-Pettis
property.

## Evidence

- `source_paper.pdf`: local copy of arXiv:math/0004101. The question is the
  final displayed `Questions` environment, labelled `qq` in the source.
- `supporting_paper_2206.08651.pdf`: local copy of arXiv:2206.08651. The
  decisive answer is Theorem `theo:Schur`, immediately after the sentence
  saying Schur preservation under projective tensor products seemed open.
- `solution_packet.pdf`: compact human-readable status note built from
  `main.tex`.

## Search Bounds

Before packaging, the run indexes were searched for `0004101`,
`Dunford-Pettis property tensor`, `tensor products Dunford-Pettis`, `DPP
projective tensor`, `Dunford Pettis injective tensor`, and related phrases.
No exact packet for arXiv:math/0004101 was found.

An adjacent conditional packet for arXiv:1504.00520 records that a negative
example to Schur preservation under projective tensor products would imply a
hyper-ideal separation. Rodriguez's theorem gives the opposite general
Schur-preservation result, so this packet should be treated as the relevant
status memory for Schur tensor preservation when the source question is
Gonzalez--Gutierrez's tensor-square question.

## Scope Limitations

This packet is a literature-status identification, not a new proof. It
answers the two final questions in arXiv:math/0004101 for the specified
Bourgain--Delbaen Schur `L_infinity` space. It does not address unrelated
Dunford-Pettis questions for injective tensor products or dual tensor products
except insofar as they appear in the source's setup.

## Human Review Notes

Recommended review focus:

- Confirm that the source's space `X` has the Schur property, as stated in
  the question.
- Confirm that Rodriguez Theorem `theo:Schur` applies to arbitrary Banach
  spaces with the Schur property and not only to spaces with extra FDD
  hypotheses.
- Confirm the standard implication: Schur property implies the
  Dunford-Pettis property.

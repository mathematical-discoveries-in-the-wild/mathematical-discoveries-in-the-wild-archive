# Conditional packet: uniform Ext constants for normalized exact sequences

## Source

- Paper: P. Kochanek, *Stability of vector measures and twisted sums of
  Banach spaces*
- arXiv: `1208.4755`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `conditional`
- Target question: final Problem (6), asking whether the property
  `Ext(mathfrak X, .)=0` is a uniform three-space property, i.e. whether
  `Z(mathfrak X,Z)` is bounded by a function of
  `Z(mathfrak X,X)` and `Z(mathfrak X,Y)` for every exact sequence
  `0 -> Y -> Z -> X -> 0`.
- Packet claim: for an exact sequence with isometric kernel inclusion and a
  homogeneous quotient selector of norm at most `s`, one has

```text
Z(E,Z) <= s Z(E,X) + Z(E,Y) (1 + 2s Z(E,X)).
```

In the canonical metric-quotient normalization this gives, after letting
`s down to 1`,

```text
Z(E,Z) <= Z(E,X) + Z(E,Y) + 2 Z(E,X) Z(E,Y).
```

## Conditional Dependencies

The proof of the displayed estimate is complete under the stated
normalization/selector hypothesis. The dependency for the original problem is
interpretive: if the source question permits arbitrary endpoint
identifications in exact sequences, then the quotient open-map and embedding
distortion constants are not controlled here by `Z(E,X)` and `Z(E,Y)`.

If the problem is read in the standard normalized model where `Y` is a closed
subspace of `Z` and `X=Z/Y` has the quotient norm, the selector hypothesis is
available with every `s>1`, and the packet gives the affirmative bound above.

## Proof Intuition

Given a zero-linear map `F:E->Z`, push it down to `X`, straighten the quotient
map by the assumed constant `Z(E,X)`, and subtract an algebraic linear lift.
The remaining defect has bounded quotient part. A homogeneous selector lifts
that bounded quotient part back into `Z`; subtracting it leaves a zero-linear
map into the kernel `Y`, where the assumed constant `Z(E,Y)` straightens it.
The only bookkeeping is the selector cost, which contributes the
`2s Z(E,X)` term to the zero-linearity constant.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_page37_bottom.png`: first crop of the open question.
- `figures/open_problem_page38_top.png`: continuation crop of the open question.
- `code/crop_evidence.py`: reproduces the evidence crops with PyMuPDF.
- `tmp/`: LaTeX build output.

## Verification Notes

The key verifier focus is the distinction between the normalized quotient
model and a literal arbitrary exact-sequence presentation. The algebraic proof
uses no bounded linear lifting of the quotient approximant; the linear lift is
allowed to be unbounded, as in the zero-linear approximation definition.

Bounded novelty check: the run indexes had no `1208.4755` packet or attempt
before this work. Local source search and short phrase searches for the exact
uniform `Z(E,Z)` estimate did not reveal an existing packet or obvious
literature duplicate. The packet is therefore recorded as a candidate new
conditional/normalized result, not as a claimed full solution of the original
problem under all interpretations.

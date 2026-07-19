# Literature-Implied Answer: A Strictly Singular Non-Weakly-Compact Operator on an L_infty-Space

## Source Question

- Source paper: S. A. Argyros and R. G. Haydon, *A hereditarily indecomposable L_infty-space that solves the scalar-plus-compact problem*, arXiv:0903.3921.
- Location: `ConcRem.tex`, concluding open problems, lines 280--293 in the parsed source.
- Question: if `X` is a `\mathscr L_\infty`-space, must every strictly singular operator on `X` be weakly compact?

## Status

`literature_implied_answer` with negative answer.

The paper A. Aviles, F. Cabello Sanchez, J. M. F. Castillo, M. Gonzalez and Y. Moreno, *On separably injective Banach spaces*, arXiv:1103.6064, records an `\mathcal L_\infty`-space `Omega` in an exact sequence

```text
0 -> C[0,1] -> Omega -> c_0 -> 0
```

whose quotient map is strictly singular. Since `C[0,1]` contains a copy of `c_0`, composing the strictly singular quotient map `q: Omega -> c_0` with an embedding `c_0 -> C[0,1] -> Omega` gives a strictly singular operator `T: Omega -> Omega`. The operator is not weakly compact, because its image of a bounded set contains, up to a fixed scaling, the unit ball of a copy of `c_0`.

## Scope

- This answers only the AH `\mathscr L_\infty` strictly-singular/weakly-compact problem negatively.
- It does not address the separate reflexive scalar-plus-compact problem.
- It does not decide whether AH-style isomorphic preduals of `\ell_1` with scalar-plus-strictly-singular operators must have scalar-plus-compact operators; the counterexample space here is a different `\mathcal L_\infty` space.
- The supporting authors do not appear to identify their construction with the AH question; this is an agent-identified implication from their recorded twisted-sum example.

## Search Evidence

Cheap run indexes were searched for `0903.3921`, `strictly singular weakly compact`, `L_infty strictly singular`, `property (V)`, and `Omega`. Related packets use AH as supporting context, but no existing packet was found for this exact concluding problem. A local search of arXiv:1103.6064 found no citation to arXiv:0903.3921 or to Argyros--Haydon's scalar-plus-compact problem in the supporting passage.

## Files

- `main.tex`: compact status note with the composition proof.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_1103.6064.pdf`: supporting arXiv paper.

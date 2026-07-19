# Order-Retract Monotonicity for SEP Data Hiding

Result type: `partial`

Status: candidate partial result/reduction, likely valid pending human review.

Source paper:

- Ludovico Lami, Carlos Palazuelos, and Andreas Winter,
  "Ultimate data hiding in quantum mechanics and beyond", arXiv:1703.03392.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Source Problem Context

The conclusion of the source paper asks about the small end of separable
measurement data hiding in finite-dimensional GPTs. It notes that if one local
cone is simplicial, then min and max tensor products coincide and
`R(SEP)=1`. It then states the open conjecture that `R(SEP)=1` if and only if
one local cone is simplicial. The same paragraph records the
Namioka-Phelps/gbit case: if one factor is the gbit, then `R(SEP)=1` exactly
when the other cone is simplicial.

## Claimed Contribution

This packet proves a monotonicity principle for the minimal-composite
separable-measurement data hiding ratio.

If `A_0` and `B_0` are local order-retract subtheories of `A` and `B`, then

`R_{A min B}(SEP) >= R_{A_0 min B_0}(SEP)`.

More precisely, every witness tensor in `A_0 tensor B_0` has exactly the same
global base norm and the same `SEP` distinguishability norm after embedding
into `A tensor B`.

Combining this with the source's Namioka-Phelps/gbit case gives:

If a local GPT `B` contains the gbit as a unital positive order retract, then
for every non-simplicial local GPT `A`, the minimal-composite ratio satisfies
`R_{A min B}(SEP)>1`. The symmetric statement also holds.

## Novelty Caution

The source paper already records the exact gbit case. The new ingredient here
is only the order-retract monotonicity and the resulting extension to GPTs
containing a gbit retract. This does not settle the full conjecture for
arbitrary non-simplicial pairs.

Cheap duplicate checks were run against the run registry, solution, attempt,
and proof-gap indexes for arXiv:1703.03392 and the core phrases
`R(SEP)`, `simplicial`, `gbit`, `data hiding`, `Namioka-Phelps`, and
`order retract`. Web checks found the source paper and a later C*-algebraic
Namioka-Phelps/Barker result, but no direct duplicate of this finite GPT
order-retract statement.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: source crop around the cone conjecture.
- `code/crop_open_problem.py`: crop script.
- `tmp/`: build intermediates.

## Human Review Notes

Verifier focus:

- Check the definition of local order-retract subtheory: positive
  unit-preserving maps `i` and `p` with `p i = id`.
- Check that positive unit-preserving maps are base-norm contractions in the
  GPT convention used by the source paper.
- Check the two inequalities proving equality of the `SEP` norm on embedded
  tensors, especially the pullback/pushforward of separable effects.
- Keep the classification as a partial result: this covers only pairs where a
  known positive instance appears as a local order retract.

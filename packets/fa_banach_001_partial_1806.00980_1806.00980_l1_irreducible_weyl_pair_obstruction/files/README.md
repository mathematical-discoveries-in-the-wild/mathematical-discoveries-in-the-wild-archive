# Partial Packet: An L1 Obstruction to Naive Stone-von Neumann Uniqueness

- status: candidate partial obstruction, likely valid
- run: `fa_banach_001`
- source arXiv id: `1806.00980`
- source paper: Jan van Neerven and Pierre Portal, *The Weyl calculus for group generators satisfying the canonical commutation relations*
- target passage: PDF page 36, Open Problem (4)

## Claim

Open Problem (4) asks for an analogue of the Stone-von Neumann uniqueness theorem
for Weyl pairs. The packet proves a basic obstruction to any naive Hilbert-style
analogue:

The standard position/momentum Weyl pair on `L^1(R^d)` is topologically
irreducible under all translations and modulations, but `L^1(R^d)` is
non-reflexive. Therefore this irreducible Banach-space Weyl pair cannot be
similar to a direct sum of Hilbert-space standard pairs.

## Scope

This does not solve Open Problem (4). It narrows what a correct Banach-space
Stone-von Neumann theorem could say: the theorem cannot classify irreducible
Banach Weyl pairs by the Hilbert standard model alone. Any useful analogue must
retain Banach-space geometry, restrict the class of spaces, or use a different
equivalence notion.

## Files

- `main.tex`: full partial-obstruction packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1806.00980
- `figures/open_problem_crop.png`: crop of the source open-problem list
- `code/make_open_problem_crop.py`: script used to regenerate the crop

## Novelty Check

The local run indexes were searched for `1806.00980`, Weyl calculus, Weyl pairs,
group generators, canonical commutation relations, Stone-von Neumann, twisted
convolution, UMD, and functional calculus keywords. No exact prior packet for
this open problem was present.

External searches on June 28, 2026 for combinations of the source title,
`Stone-von Neumann`, `Weyl pairs`, `Banach spaces`, `twisted convolution`, and
`UMD` did not locate a later solution to the source open problems. This packet
is only a partial obstruction, so the novelty claim is correspondingly modest.

## Human Review Recommendation

Check whether the intended Open Problem (4) already excludes non-reflexive
spaces or asks only for a positive theorem in a restricted Banach class. Under
the literal wording "Weyl pairs", the `L^1` standard pair is a simple
irreducible obstruction to a Hilbert-model uniqueness statement.

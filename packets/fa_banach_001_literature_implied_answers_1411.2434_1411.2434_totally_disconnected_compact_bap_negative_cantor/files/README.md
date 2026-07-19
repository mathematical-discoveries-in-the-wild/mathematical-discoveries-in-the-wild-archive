# Literature-implied answer: Cantor metrics give a negative BAP answer

## Status

This packet records a literature-implied answer to the BAP half of a question
asked in Cuth-Doucha, *Lipschitz-free spaces over ultrametric spaces*
(`arXiv:1411.2434`).

The source asks:

> Does the Lipschitz-free space over a totally disconnected compact metric
> space have the BAP? Is it a dual space?

The first clause has a negative answer. Talimdjioski proves for the Cantor set
`K = 2^N`, with `M` the space of compatible metrics on `K`, that the set of
metrics `d` for which `F(K,d)` fails the approximation property is dense and
meager. In particular, there is a compatible Cantor metric `d` such that
`F(K,d)` fails AP, hence fails BAP.

Since the Cantor set is compact, metric, and totally disconnected, this is a
counterexample to the universal BAP assertion in the source question.

## Scope

- Settled here: not every totally disconnected compact metric space has
  Lipschitz-free space with BAP.
- Not settled here: whether every Lipschitz-free space over a totally
  disconnected compact metric space is a dual space.
- Additional context: the same Talimdjioski paper also proves a residual class
  of compatible Cantor metrics for which the free space is a dual of the little
  Lipschitz space and both have MAP. Thus the negative result is existence
  based, not a generic failure statement.

## Files

- `main.tex`: compact status note with the implication.
- `solution_packet.pdf`: compiled version of the note.
- `source_paper.pdf`: Cuth-Doucha source paper (`arXiv:1411.2434`).
- `supporting_paper_2305.07591.pdf`: Talimdjioski supporting paper.

## References

1. M. Cuth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*,
   `arXiv:1411.2434`.
2. F. Talimdjioski, *Lipschitz-free spaces over Cantor sets and approximation
   properties*, `arXiv:2305.07591`.

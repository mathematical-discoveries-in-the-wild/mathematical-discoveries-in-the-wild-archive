# Literature implied answer: property A does not force frequent hypercyclicity

status: literature_implied_answer

source: George Costakis and Ioannis Parissis, *Szemeredi's theorem,
frequent hypercyclicity and multiple recurrence*, arXiv:1008.4017.

supporting answer: Quentin Menet, *Linear chaos and frequent hypercyclicity*,
arXiv:1410.7173.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1008.4017_propertyA_not_fhc_via_menet_1410.7173/`

## Identification

In the final section of the source paper, Costakis--Parissis ask whether every
hypercyclic operator with property `A` must be frequently hypercyclic. They
precede the question by observing that every chaotic operator has property `A`.

Menet later constructed a chaotic operator on `ell_1` which is not
`U`-frequently hypercyclic and hence not frequently hypercyclic. Since a chaotic
operator is hypercyclic and, by the source paper's observation, has property
`A`, Menet's example is a counterexample to the stronger property-`A` question.

## Scope

This packet records a later-literature implication rather than a new
construction from this run. It settles the source's question asking whether

> hypercyclic + property `A` implies frequent hypercyclicity.

It does not settle the next source question asking whether property `A` can
hold without `U`-frequent recurrence.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1008.4017 source paper.
- `supporting_paper_1410.7173.pdf`: Menet's supporting paper.

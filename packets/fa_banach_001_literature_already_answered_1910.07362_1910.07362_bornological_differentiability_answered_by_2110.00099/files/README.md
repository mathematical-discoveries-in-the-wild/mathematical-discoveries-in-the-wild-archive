# Literature-already-answered packet: bornological differentiability

Status: `literature_already_answered (weak-Hadamard case and property-(S) framework)`

This packet records an explicit later-literature answer. It is not claimed as
a new mathematical result of the run.

## Source question

- M. Bachir, G. Flores, and S. Tapia-García, *Compact and Limited
  Operators*, arXiv:1910.07362; Math. Nachr. 294 (2021), 1085-1098.
- Exact location: Open Question 5.7, PDF page 13.
- Local PDF: `source_paper.pdf`.

The question asks first for a weak-Hadamard analogue of the paper's
differentiability characterizations and then for an abstract bornological
framework: find a class of functions whose composition behavior detects when
an operator maps its unit ball into a prescribed bornology.

## Explicit later answer

- M. Bachir and S. Tapia-García, *Non-linear operators and differentiability
  of Lipschitz functions*, arXiv:2110.00099 (2021).
- Local PDF: `supporting_paper_2110.00099.pdf`.
- Exact locations: the explicit statement that the paper answers
  arXiv:1910.07362, Question 5.7 is on PDF page 2; Theorem 1.3 on PDF page 3
  gives the weakly compact/weak-Hadamard characterization; Theorem 4.5 on PDF
  page 11, proved through page 13, gives the abstract property-(S)
  bornological theorem.

Theorem 1.3 states that a bounded linear operator `T:Y->X` is weakly compact
if and only if, for every real-valued Lipschitz function `f` on `X`, the
composition `f o T` is Fréchet differentiable at `y` whenever `f` is
weak-Hadamard differentiable at `Ty`. This exactly settles the first case
highlighted in Open Question 5.7. Theorem 4.5 supplies a common framework for
vector bornologies satisfying property (S), including the Hadamard,
weak-Hadamard, limited, and Fréchet bornologies.

## Scope qualification

The later paper explicitly says it answers Question 5.7, and it completely
answers the highlighted weak-Hadamard case. Its abstract theorem assumes that
the target vector bornology satisfies property (S); it does not assert a
classification for every possible bornology with no structural hypothesis.
Accordingly, the unrestricted literal all-bornologies formulation remains
outside the theorem, while the concrete missing case and the intended broad
framework are answered.

## Files

- `solution_packet.pdf`: compact rendered status note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original paper containing Open Question 5.7.
- `supporting_paper_2110.00099.pdf`: explicit later answer.
- `tmp/`: build and PDF inspection intermediates.

Ledger record:
`runs/fa_banach_001/ledger/results/1910.07362_bornological_differentiability_answered_by_2110.00099.json`.

